# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 17:24:54 2017

@author: Niall
"""

# -------------------------Import Libaries------------------------------------

import constants; import numpy as np; from calc_pressure_field import calc_pressure_field
from array_grid import array_grid; from direction_vectors import direction_vectors; from vti_writer import vti_writer
from phifind import phifind; from random_transducer_placment import random_transducer_placment


# -------------------------Variables to set------------------------------------

rt = array_grid(0.01,4,4) # (transducer spacing[m], number of xtrans, number of ztrans) rt is the position vector of each transducer
#rt =  random_transducer_placment(15,0.025,0.01) # (number of transducers ,half_grid_size[m], min_allowable_dist[m])

ntrans = len (rt)   # Total number of transducers in grid

nt = direction_vectors(ntrans) # nt is the direction vector of each transducer

phi = phifind(rt,0,0.03,0) # phi is the initial phase of each transducer to focus

# ---------------------- Defining constants ----------------------------------

gsize = constants.gsize; deltaxyz = constants.deltaxyz; x = constants.x; y = constants.y; z = constants.z
npoints = constants.npoints; p0 = constants.p0; A = constants.A; a = constants.a; lamda = constants.lamda   
k1 = constants.k1; k2n = constants.k2n; k2d = constants.k2d; k2 =  constants.k2; gravity = constants.gravity; p_mass = constants.p_mass 

# ----------------------Setting up output arrays-------------------------------

p = np.zeros ((npoints,npoints,npoints,ntrans), dtype=complex)
pcombined = np.zeros ((npoints,npoints,npoints),dtype=complex)
realcombined = np.zeros ((npoints,npoints,npoints),dtype=float)
px = py = pz = np.zeros ((npoints,npoints,npoints), dtype=complex)
ux = uy = uz = np.zeros ((npoints,npoints,npoints), dtype=float)
pabs = pxabs = pyabs = pzabs   = np.zeros ((npoints,npoints,npoints), dtype=float) 
u = np.zeros ((npoints,npoints,npoints), dtype=float)

# ----------------------------------------------------------------------------

p = calc_pressure_field(rt, nt, ntrans, phi) # calculate pressure field

# -----------------Loop to sum pressure of all transducers---------------------

for xloop in range (0,npoints): #Combining the tranducer fields
        for yloop in range (0,npoints):
            for zloop in range (0,npoints):
                for transducers in range (0,ntrans):
                    pcombined[xloop,yloop,zloop] = pcombined[xloop,yloop,zloop] + p[xloop,yloop,zloop, transducers]
                    realcombined[xloop,yloop,zloop] = np.absolute(pcombined[xloop,yloop,zloop]) 
                    
                    
# -----------------Calculating derrivitive of the pressure field---------------


diff_p = np.gradient(pcombined,deltaxyz)
px = diff_p[0]; py = diff_p[1]; pz = diff_p[2]


# ----------------- Calculating the Gork’ov potential-------------------------

# Calculating absuloute values for the pressure field and its derrivitives

for xloop in range (0,(npoints)):
    for yloop in range (0,(npoints)):
        for zloop in range (0,(npoints)): 
            pabs[xloop,yloop,zloop]   = np.absolute(pcombined[xloop,yloop,zloop])  
            pxabs[xloop,yloop,zloop]  = np.absolute(px[xloop,yloop,zloop])  
            pyabs[xloop,yloop,zloop]  = np.absolute(py[xloop,yloop,zloop])  
            pzabs[xloop,yloop,zloop]  = np.absolute(pz[xloop,yloop,zloop])  

# Calculating Gork’ov potential u
for xloop in range (0,npoints):
    for yloop in range (0,npoints):
        for zloop in range (0,npoints):
            u[xloop,yloop,zloop] = (2*k1*pabs[xloop,yloop,zloop]**2) - (2*k2*(pxabs[xloop,yloop,zloop]**2 + pyabs[xloop,yloop,zloop]**2 + pzabs[xloop,yloop,zloop]**2))


# -----------------Calculating derrivitive of Gork’ov potential ---------------


diff_u = np.gradient(u,deltaxyz)
ux = -diff_u[0]; uy = -diff_u[1]; uz = -diff_u[2]

uy = uy + (p_mass*gravity) # including force of gravity 

# -------------------Creating output images and vtk file----------------------

vti_writer (npoints,realcombined,ux,uy,uz)


print("Calculations compleated successfuly")