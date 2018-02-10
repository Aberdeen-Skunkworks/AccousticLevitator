# -*- coding: utf-8 -*-

# constants. Config
import math


gsize = 0.05         # Half the length of grid box (m)
deltaxyz = 0.0009     # Distance between points in grid (m)

x = -gsize           # Initial values of x,y and z in (m) Grid volume
y = -gsize
z = 0.00
npoints = int(1 + ((2 * gsize) / deltaxyz)) # Number of points on x y and z axis, plus 1 to index properly


phaseresolution = 1250      # Phase resolution x as in ( 2*pi )/( x ) number of divisions of the phases
p0 = 0.17                   # Amplitude constant
A = 17                      # Peak to peak amplitude
a = 0.0045                  # Piston radius
lamda = 0.00865             # Wavelegnth meters
freq = 40000                # Frequency in Hz
rhoo = 1.18                 # Density of air kg/m^3
rhos = 29                   # Density of particle kg/m^3    13.7 Calculated by hand
co = 346                    # Speed of sound in Air m/s
cs = 900                    # Speed of sound in particle material m/s
particle_diamiter = 0.004   # Particle diamiter in m


v = (1/6) * math.pi * particle_diamiter**3          # Particle Volume 
p_mass = rhos * v           # particle mass in kg
gravity = -9.81             # m/s^2 negitive as gravity is down \|/

# 4 constants for the Gork’ov potential equation

k1 = ( (1/4) * v * ( ( (1)/((co**2)*(rhoo)) ) - ( (1)/((cs**2)*(rhos)) )))
k2n = (rhoo - rhos)
k2d = (freq**2) * rhoo * (rhoo + 2*rhos)
k2 =  ( (3/4) * v * ( k2n/k2d ) )

