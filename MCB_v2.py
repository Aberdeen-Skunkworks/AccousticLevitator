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
    def __init__(self, pos : Vector, director: Vector, phi: float): 
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

    def pressure(self, pos : Vector) -> complex:
        #import numpy as np; import math; import cmath; import constants
        rs = pos - self.pos
        mag_rs = numpy.linalg.norm(rs)
        if mag_rs < 0.001: # Setting calculated dp/dr on top of transducer to zero.
            return 0 + 0j
        else:
            theta = math.acos(numpy.dot(rs, self.director) / mag_rs)
            exponential =  cmath.exp(1j * (self.phi + self.k * mag_rs) ) / mag_rs
            if theta < 0.0000001: # zero angle causes divistion by zero error -> directionality function aproaches 0
                theta = 0.0000001
            frac = self.p0 * self.PkToPkA * math.sin(self.k * self.PistonRadius * math.sin(theta)) /  (self.k * self.PistonRadius * math.sin(theta))
            return exponential * frac

    def differentiate_pressure(self, pos: Vector) -> numpy.array:
        rs = pos - self.pos
        mag_rs = numpy.linalg.norm(rs)

        if mag_rs < 0.001: # Setting calculated dp/dr on top of transducer to zero.
            return [0, 0, 0] 
        else:
            rs_hat = rs / mag_rs
            theta = math.acos((numpy.dot(rs, self.director)) / mag_rs)
            exponent_term =  cmath.exp(1j * (self.phi + self.k * mag_rs) ) / mag_rs
            if theta < 0.0001: # zero angle causes divistion by zero error -> directionality function aproaches 0
                fraction_term =  (self.p0 * self.PkToPkA)
                d_exponential_term_dr = ((rs_hat * 1j * self.k * cmath.exp(1j * (self.phi + self.k * mag_rs)) ) / (mag_rs))  -  ((cmath.exp(1j*(self.phi + self.k * mag_rs)) * rs_hat) / (mag_rs**2))
                d_p_dr = (fraction_term * d_exponential_term_dr)
            else:
                fraction_term =  self.p0 * self.PkToPkA * math.sin(self.k * self.PistonRadius * math.sin(theta)) /  (self.k * self.PistonRadius * math.sin(theta))
                d_exponential_term_dr = rs_hat * 1j * self.k * cmath.exp(1j * (self.phi + self.k * mag_rs)) / mag_rs - cmath.exp(1j * (self.phi + self.k * mag_rs)) * rs_hat / mag_rs**2
                numerator = self.p0 * self.PkToPkA * math.sin(self.k * self.PistonRadius * math.sin(theta))
                denominator =  self.k * self.PistonRadius * math.sin(theta)
                d_denominator_dr = self.k * self.PistonRadius * (-numpy.dot(rs_hat, self.director)) / math.sqrt(1 - numpy.dot(rs_hat, self.director)) * (self.director - rs_hat * numpy.dot(self.director, rs_hat)) / mag_rs
                d_numerator_dr = self.p0 * self.PkToPkA * math.cos(self.k * self.PistonRadius * math.sin(theta)) * d_denominator_dr
                d_fraction_dr = (d_numerator_dr * denominator - numerator * d_denominator_dr) / denominator**2
                return (d_fraction_dr * exponent_term) + (fraction_term * d_exponential_term_dr)

from typing import List

class ParticleSystem:
    transducers : List[Transducer]
    
    def __init__(self):
        self.transducers = []

    def appendTransducer(self, *args, **kwargs):
        self.transducers.append(Transducer(*args, **kwargs))

    def potential(self, pos: Vector):
        pass
            
#Here's the unit tests (small program to check the code above is working correctly!)
import unittest

class TestAccoustics(unittest.TestCase):
    def test_Transducer_Pressure(self):
        t = Transducer(Vector([-1,2,-3]), Vector([-1,0,0]), 0.5)
        #Verify that the transducer pressure is calculated correctly
        self.assertEqual(t.pressure(Vector([1,2,3])), (0.0006780895717302391+0.013550483821988818j))
        #Verify that the transducer pressure derivative is calculated correctly
        result = numpy.array([-3.11043288+0.1983842j, 0.0+0.0j,-9.33852191+0.45080741j])
        numpy.testing.assert_array_almost_equal(t.differentiate_pressure(Vector([1,2,3])), result)

#If this file is "run", then we execute the unit tests. If it is imported then we skip them
if __name__ == '__main__':
    unittest.main()
