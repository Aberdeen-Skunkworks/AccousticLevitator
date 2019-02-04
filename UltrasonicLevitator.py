#!/usr/bin/python3

from numpy import array as Vector #import the basic vector type
import numpy #Import everything else
import math, cmath

class Transducer(): # Make a new class Transducer    
    def __init__(self, pos, director, phi = 0): 
        #Save the position and director in the new Transducer
        self.pos = pos
        self.director = director
        #Check the director is not [0,0,0]
        length = numpy.linalg.norm(self.director)
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
    def __str__(self):
        return "Transducer{pos="+str(self.pos)+", dir="+str(self.director)+"}"

    #Give the python code required to create this transducer
    def __repr__(self):
        return "Transducer("+repr(self.pos)+", "+repr(self.director)+")"

    def pressure(self, pos, shift = 0):
        #This calculates the pressure this transducer gives to a
        #position in space.  shift allows you to phase shift the
        #transducer (e.g. to make it appear like time is passing)
        rs = pos - self.pos
        mag_rs = numpy.linalg.norm(rs)
        if mag_rs < 0.001: #If within 1mm of the transducer, don't report the pressure, as its flaky if mag_rs->0
            return 0 + 0j
        else:
            theta = math.acos(numpy.dot(rs, self.director) / mag_rs)
            if theta > math.pi/2: #Ignore values behind the transducer
                return 0j;
            
            exponential =  cmath.exp(1j * (self.phi + self.k * mag_rs + shift) ) / mag_rs
            x = (self.k * self.PistonRadius * math.sin(theta))
            if x < 0.000001: #Take care, as when x->0 then sin(x)/x -> 1
                frac = self.p0 * self.PkToPkA
            else:
                frac = self.p0 * self.PkToPkA * math.sin(x) / x
            return exponential * frac

    def dpdx(self, pos, shift = 0):
        #This is an exact expression for calculating nabla p (gradient
        #of the pressure). This is much faster than getting it
        #numerically.
        
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
    #This class represents a single particle
    
    def __init__(self, pos, mass, diameter):
        self.position = pos
        self.mass = mass
        self.diameter = diameter
        self.volume = math.pi * self.diameter**3 / 6.0        # Particle Volume
        self.density = self.mass / self.volume


class ParticleSystem:
    #This class represents a lot of transducers together and allows the calculation of forces etc.
    def __init__(self):
        self.transducers = []
        self.gravity = -9.81
        self.freq = 40000
        
    def appendTransducer(self, *args, **kwargs):
        #Add a transducer to the system
        self.transducers.append(Transducer(*args, **kwargs))

    def pressure(self, pos, shift = 0):
        #Calculate the pressure from all transducers at a given position in space
        p = 0j
        for transducer in self.transducers:
            p += transducer.pressure(pos, shift)
        return p

    def clear(self):
        #clear all transducers from the system
        self.transducers = []
    
    def dpdx(self, pos, shift = 0):
        #Calculate \nabla p (gradient of the pressure) from all
        #transducers at a given position in space
        dpdx = numpy.array([0j,0j,0j])
        for transducer in self.transducers:
            dpdx += transducer.dpdx(pos, shift)
        return dpdx
    
    def Gorkov_potential(self, particle):
        #Calculate the gorkov potential, which is the particle
        #interaction energy with the accoustic field if viscous
        #effects are ignored.
        
        sound_speed_air = 346 # m/s
        sound_speed_particle = 2600 # m/s
        air_density = 1.2 # Density of air kg/m^3
        
        #This potential is calculated using "Acoustofluidics 7: The
        #acoustic radiation force on small particles" available here
        #https://pdfs.semanticscholar.org/f8bb/02d01cde4ec15e9bc53d1cb8ef66d882f40b.pdf

        #Fetch the pressure and pressure gradient
        p = self.pressure(particle.position)
        dpdx = self.dpdx(particle.position)

        #From Eq. 4a and 4b, we can write v_1 in terms of p_1
        omega = 2 * math.pi * self.freq
        v = self.dpdx(particle.position) / (1j * air_density * omega)

        #Note that averages of harmonic fields (like the complex
        #pressure) is given in Eq.8
        avg_vsq = v.dot(numpy.conj(v)).real / 2
        avg_psq = (p * p.conjugate()).real / 2

        #The rest arises from Eq. 27a-d
        k_0 = 1 / (air_density * sound_speed_air**2)
        k_p =  1 / (particle.density * sound_speed_particle**2)
        k_tilde = k_p / k_0
        f_1 = 1 - k_tilde

        rho_tilde = particle.density / air_density
        f_2 = 2 * (rho_tilde - 1) / (2 * rho_tilde + 1)
        
        return particle.volume * (f_1 * 0.5 * k_0 * avg_psq - f_2 * 0.75 * air_density * avg_vsq) - particle.mass * self.gravity * particle.position[2]

    def focus(self, pos):
        #Focus the transducers at a single point in space
        for transducer in self.transducers:
            dmag = numpy.linalg.norm(pos - transducer.pos)
            transducer.phi = (1 - ((dmag / transducer.wavelength) % 1)) * 2 * math.pi
        

            
#Here's the unit tests (small program to check the code above is working correctly!)
#They only run if this file is run, not when this file is imported
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
        part = Particle(Vector([0,0,0]), 7.176591426e-7, 0.0042)
        self.assertAlmostEqual(part.density, 18.5)
        
    def test_Transducer_potential(self):
        sys = ParticleSystem()
        sys.appendTransducer(Vector([0,0,0]), Vector([0,0,1]), 0.5)
        pos = Vector([-0.004545454545454545,-0.004545454545454545,0.19545454545454546])
        self.assertAlmostEqual(abs(sys.pressure(pos)), 33.43931848898868)
        particle = Particle(pos, 7.176591426e-7, 0.0042)
        self.assertAlmostEqual(sys.Gorkov_potential(particle), 1.3760189999640898e-06)
        
#If this file is "run", then we execute the unit tests. If it is imported then we skip them
if __name__ == '__main__':
    print("### Running unit tests!")
    unittest.main()
