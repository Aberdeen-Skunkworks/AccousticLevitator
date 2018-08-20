# -*- coding: utf-8 -*-

# constants. Config
import math



gsize = 0.02      # Half the length of grid box (m)
deltaxyz = 0.00045    # Distance between points in grid (m)

x = -gsize           # Initial values of x,y and z in (m) Grid volume
y = -gsize
z = -gsize
npoints = int(1 + ((2 * gsize) / deltaxyz)) # Number of points on x y and z axis, plus 1 to index properly


if npoints % 2 == 0:
    print("Number of points is even (No central point exists): ", npoints)
    print("Change the grid size or delta x y z value")
    #exit
else:
    print("Number of points is odd (central point exists): ", npoints)
 

phaseresolution = 1000     # Phase resolution x as in ( 2*pi )/( x ) number of divisions of the phases
p0 = 0.364                  # Amplitude constant 0.364 checked to be correct for our baord
A = 18                 # Peak to peak amplitude
a = 0.0045                  # Piston radius
lamda = 0.00865             # Wavelegnth meters
freq = 40000                # Frequency in Hz
rhoo = 1.2                 # Density of air kg/m^3
rhos = 18.5                 # Density of particle kg/m^3    18.5 Calculated in the lab for white polysterine beads
co = 346                    # Speed of sound in Air m/s
cs = 2600                   # Speed of sound in particle material m/s
particle_diamiter = 0.0042  # Particle diamiter in m


v = (math.pi * particle_diamiter**3)/6.0        # Particle Volume 
p_mass = rhos * v           # particle mass in kg
gravity = -9.81             # m/s^2 negitive as gravity is down \|/

# 4 constants for the Gork’ov potential equation

k1 = ( (1/4) * v * ( ( (1)/((co**2)*(rhoo)) ) - ( (1)/((cs**2)*(rhos)) )))
k2n = (rhoo - rhos)
k2d = (freq**2) * rhoo * (rhoo + 2*rhos)
k2 =  ( (3/4) * v * ( k2n/k2d ) )



#### New constants for gorkov potential

ohmega = freq * math.pi * 2

k = 1 / (rhoo * co**2)
k_p =  1 / (rhos * cs**2)
k_tilda = k_p / k
f_1 = 1 - k_tilda

rho_tilda = rhos / rhoo
f_2 = ( 2* (rho_tilda-1) ) / ( (2*rho_tilda) +1 )

vkpretovel = 1 / (rhoo*ohmega)
vkpre = (1/4) * f_1 *  k
vkvel = (3/8) * f_2 * rhoo
vpvol = v

m1 = vpvol * vkpre
m2 = vpvol * vkvel * (vkpretovel**2)