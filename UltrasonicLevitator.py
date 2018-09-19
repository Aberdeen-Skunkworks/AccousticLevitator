#!/usr/bin/python3

from numpy import array as Vector #import the basic vector type
import numpy #Import everything else
import math, cmath

class Transducer(): # Make a new class Transducer
    #Up front, say that the class has some member variables
    #This is not needed, but is now good practice
    pos: Vector #The position of the transducer
    director: Vector #The unit vector in the direction of the transducer
    phi: float # The phase shift of this transducer
    
    wavelength: float # Wavelength in meters
    PkToPkA: float #Peak to peak amplitude
    p0: float # Amplitude constant (for our board)
    
    #Now we define what happens when you write Transducer(...)
    def __init__(self, pos : Vector, director: Vector, phi: float = 0): 
        #Save the position and director in the new Transducer
        self.pos = pos
        self.director = director
        #Check the director is not [0,0,0]
        length: float = numpy.linalg.norm(self.director)
        if length == 0:
            raise Exception("Cannot use a zero director!")
        self.director = self.director / length
        self.phi = phi
        self.wavelength = 0.00865
        self.PkToPkA = 18.0
        self.p0 = 0.364 # Amplitude constant for our board
        self.k = 2 * math.pi / self.wavelength
        self.PistonRadius = 0.0045

    #Define the string given if someone tries to "print" a Transducer
    def __str__(self) -> str:
        return "Transducer{pos="+str(self.pos)+", dir="+str(self.director)+"}"

    #Give the python code required to create this transducer
    def __repr__(self) -> str:
        return "Transducer("+repr(self.pos)+", "+repr(self.director)+")"

    def pressure(self, pos : Vector, shift: float = 0) -> complex:
        #import numpy as np; import math; import cmath; import constants
        rs = pos - self.pos
        mag_rs = numpy.linalg.norm(rs)
        if mag_rs < 0.001: # Setting calculated dp/dr on top of transducer to zero.
            return 0 + 0j
        else:
            theta = math.acos(numpy.dot(rs, self.director) / mag_rs)
            if theta > math.pi/2:
                return 0j;
            
            exponential =  cmath.exp(1j * (self.phi + self.k * mag_rs + shift) ) / mag_rs
            if theta < 0.0000001: # zero angle causes divistion by zero error -> directionality function aproaches 0
                theta = 0.0000001
            frac = self.p0 * self.PkToPkA * math.sin(self.k * self.PistonRadius * math.sin(theta)) /  (self.k * self.PistonRadius * math.sin(theta))
            return exponential * frac

    def dpdx(self, pos: Vector, shift: float = 0) -> numpy.array:
        rs = pos - self.pos
        mag_rs = numpy.linalg.norm(rs)

        if mag_rs < 0.001: # Setting calculated dp/dr on top of transducer to zero.
            return numpy.array([0j, 0j, 0j])
        else:
            rs_hat = rs / mag_rs
            theta = math.acos((numpy.dot(rs, self.director)) / mag_rs)
            if theta > math.pi/2:
                return numpy.array([0j, 0j, 0j]);
            
            exponent_term =  cmath.exp(1j * (self.phi + shift + self.k * mag_rs ) ) / mag_rs
            if theta < 0.0001: # zero angle causes divistion by zero error -> directionality function aproaches 0
                fraction_term =  (self.p0 * self.PkToPkA)
                d_exponential_term_dr = ((rs_hat * 1j * self.k * cmath.exp(1j * (self.phi +shift + self.k * mag_rs)) ) / (mag_rs))  -  ((cmath.exp(1j*(self.phi + shift + self.k * mag_rs)) * rs_hat) / (mag_rs**2))
                return fraction_term * d_exponential_term_dr
            else:
                fraction_term =  self.p0 * self.PkToPkA * math.sin(self.k * self.PistonRadius * math.sin(theta)) /  (self.k * self.PistonRadius * math.sin(theta))
                d_exponential_term_dr = rs_hat * 1j * self.k * cmath.exp(1j * (self.phi + shift + self.k * mag_rs)) / mag_rs - cmath.exp(1j * (self.phi + shift + self.k * mag_rs)) * rs_hat / mag_rs**2
                numerator = self.p0 * self.PkToPkA * math.sin(self.k * self.PistonRadius * math.sin(theta))
                denominator =  self.k * self.PistonRadius * math.sin(theta)
                d_denominator_dr = self.k * self.PistonRadius * (-numpy.dot(rs_hat, self.director)) / math.sqrt(1 - numpy.dot(rs_hat, self.director)) * (self.director - rs_hat * numpy.dot(self.director, rs_hat)) / mag_rs
                d_numerator_dr = self.p0 * self.PkToPkA * math.cos(self.k * self.PistonRadius * math.sin(theta)) * d_denominator_dr
                d_fraction_dr = (d_numerator_dr * denominator - numerator * d_denominator_dr) / denominator**2
                return (d_fraction_dr * exponent_term) + (fraction_term * d_exponential_term_dr)

from typing import List

class Particle:
    position: Vector
    mass: float
    diameter : float  # Particle diamiter in m
    density: float
    volume: float
    
    def __init__(self, pos: Vector, mass: float, diameter: float):
        self.position = pos
        self.mass = mass
        self.diameter = diameter
        self.volume = math.pi * self.diameter**3 / 6.0        # Particle Volume
        self.density = self.mass / self.volume


class ParticleSystem:
    transducers : List[Transducer]
    gravity: float
    
    def __init__(self):
        self.transducers = []
        self.gravity = -9.81
        self.freq = 40000
        
    def appendTransducer(self, *args, **kwargs):
        self.transducers.append(Transducer(*args, **kwargs))

    def pressure(self, pos: Vector, shift:float = 0):
        p = 0j
        for transducer in self.transducers:
            p += transducer.pressure(pos, shift)
        return p

    def clear(self):
        self.transducers = []
    
    def dpdx(self, pos: Vector, shift:float = 0):
        dpdx = numpy.array([0j,0j,0j])
        for transducer in self.transducers:
            dpdx += transducer.dpdx(pos, shift)
        return dpdx
    
    def potential(self, particle: Particle):
        abs_p = abs(self.pressure(particle.position))
        abs_dpdx = numpy.absolute(self.dpdx(particle.position))

        omega = self.freq * math.pi * 2
        sound_speed_air = 346 # m/s
        sound_speed_particle = 2600 # m/s
        air_density = 1.2 # Density of air kg/m^3

        k = 1 / (air_density * sound_speed_air**2)
        k_p =  1 / (particle.density * sound_speed_particle**2)
        k_tilda = k_p / k
        f_1 = 1 - k_tilda
        rho_tilda = particle.density / air_density
        f_2 = ( 2* (rho_tilda-1) ) / ( (2*rho_tilda) +1 )
        
        vkpretovel = 1 / (air_density * omega)
        vkpre = (1.0/4.0) * f_1 *  k
        vkvel = (3.0/8.0) * f_2 * air_density
        vpvol = particle.volume
        
        m1 = vpvol * vkpre
        m2 = vpvol * vkvel * (vkpretovel**2)

        return abs_p**2 * m1 - m2 * abs_dpdx.dot(abs_dpdx) - particle.mass * self.gravity * particle.position[2]

    def focus(self, pos:Vector):
        for transducer in self.transducers:
            dmag = numpy.linalg.norm(pos - transducer.pos)
            transducer.phi = (1 - ((dmag / transducer.wavelength) % 1)) * 2 * math.pi
        

            
#Here's the unit tests (small program to check the code above is working correctly!)
import unittest

class TestAccoustics(unittest.TestCase):
    def test_Transducer_Pressure(self):
        t = Transducer(Vector([-1,2,-3]), Vector([1,0,0]), 0.5)
        #Verify that the transducer pressure is calculated correctly
        self.assertEqual(t.pressure(Vector([1,2,3])), (0.0006780895717302391+0.013550483821988818j))
        #Verify that the transducer pressure derivative is calculated correctly
        result = numpy.array([-3.109593+0.215161j,  0.000000+0.j, -9.338802+0.445215j])
        numpy.testing.assert_array_almost_equal(t.dpdx(Vector([1,2,3])), result)

    def test_Particle_class(self):
        def __init__(self, pos: Vector, mass: float, diameter: float):
            part = Particle(Vector([0,0,0]), 7.176591426e-7, 0.0042)
            self.assertAlmostEqual(part.density, 18.5)
        
    def test_Transducer_potential(self):
        sys = ParticleSystem()
        sys.appendTransducer(Vector([0,0,0]), Vector([0,0,1]), 0.5)
        pos = Vector([-0.004545454545454545,-0.004545454545454545,0.19545454545454546])
        self.assertAlmostEqual(abs(sys.pressure(pos)), 33.43931848898868)
        particle = Particle(pos, 7.176591426e-7, 0.0042)
        self.assertAlmostEqual(sys.potential(particle), 1.3760189999640898e-06)
        
#If this file is "run", then we execute the unit tests. If it is imported then we skip them
if __name__ == '__main__':
    print("### Running unit tests!")
    unittest.main()
