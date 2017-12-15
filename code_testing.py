

# Code testing and visulisation


''' Test hex_grid 
import transducer_placment 
import numpy as np
import matplotlib.pyplot as plt
import math


rt = transducer_placment.hex_grid(0.01,6,7)
trans_to_delete = [0,4,5,11,23,30,35,36,37,41]                   # List of unwanted transducers 

trans_to_delete = sorted(trans_to_delete)
ntrans = len (rt)
n_trans_to_delete = len(trans_to_delete)

for loop in range (0, (n_trans_to_delete)):             # Deletes unwanted transducers
    rt = np.delete(rt, trans_to_delete[loop], 0)
    trans_to_delete = np.subtract(trans_to_delete, 1)
    
fig, ax = plt.subplots() 
plt.plot(rt[:,0,0], rt[:,0,2], 'ro')                    # Plots small dots

for trans in range (0, (ntrans - n_trans_to_delete)):   # Plots circles
    circle = plt.Circle((rt[trans,0,0], rt[trans,0,2]), 0.005, color='r')
    ax.add_artist(circle)

plt.xlim(-(math.sqrt(ntrans)*0.0075),(math.sqrt(ntrans)*0.0075)) 
plt.ylim(-(math.sqrt(ntrans)*0.0075),(math.sqrt(ntrans)*0.0075)) '''



### ANIMATION moving images of a circular trap exported into paraview ###

# -------------------------Import Libaries------------------------------------

import constants; import numpy as np; from calc_pressure_field import calc_pressure_field
import transducer_placment; from vti_writer import vti_writer; import phase_algorithms; import algorithms;


# -------------------------Variables to set------------------------------------

coords = algorithms.circle_co_ords(32, 0.01)

trans_to_delete = [0,4,5,11,23,30,35,36,37,41]  # List of unwanted transducers leave blank to keep all
rt = transducer_placment.hex_grid(0.01,6,7)    # spcing , x nummber, y number of transducers
rt = transducer_placment.delete_transducers(rt,trans_to_delete)

ntrans = len (rt)   # Total number of transducers in grid

nt = transducer_placment.direction_vectors(ntrans) # nt is the direction vector of each transducer

for itteration in range (0, 32):
    
    phi_focus = phase_algorithms.phase_find(rt,coords[itteration,0],0.04,coords[itteration,1]) # phi is the initial phase of each transducer to focus on a point
    phi = phase_algorithms.add_twin_signature(rt,phi_focus)
    
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
                        
    
    # -------------------Creating output images and vtk file----------------------
    
    import vtk; 
    
    # creating vti image file with combined pressure magnitude data
    filename = "writeImageData" + str(itteration+1) + ".vti"
    
    imageData = vtk.vtkImageData()
    imageData.SetDimensions(npoints, npoints, npoints )
    imageData.SetOrigin( (-npoints+1)/2, 0, (-npoints+1)/2 )
    if vtk.VTK_MAJOR_VERSION <= 5:
        imageData.SetNumberOfScalarComponents(1)
        imageData.SetScalarTypeToDouble()
    else:
        imageData.AllocateScalars(vtk.VTK_DOUBLE, 1)
    
    dims = imageData.GetDimensions()
    
    # Fill every entry of the image data
    for z in range(dims[2]):
        for y in range(dims[1]):
            for x in range(dims[0]):
                imageData.SetScalarComponentFromDouble(x, y, z, 0, realcombined[x,y,z])
    
    writer = vtk.vtkXMLImageDataWriter()
    writer.SetFileName(filename)
    if vtk.VTK_MAJOR_VERSION <= 5:
        writer.SetInputConnection(imageData.GetProducerPort())
    else:
        writer.SetInputData(imageData)
    writer.Write()
        

print("Calculations compleated successfuly")