
# Write data to vti files to be viewed in Paraview

def vti_writer (npoints,realcombined,fx,fy,fz,u):
    
    import vtk; import numpy as  np
    
    
    # creating vti image file with combined pressure magnitude data
    filename = "writeImageData.vti"
    
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
    
    
    # ----------------------------------------------------------------------------
    
    # creating vti image file with combined pressure magnitude data
    filename2 = "gorkov.vti"
    
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
    """
    file2 = open('output'+str(npoints)+'x'+str(npoints)+'x'+str(npoints)+'.raw', 'wb')
    minu = np.min(u)
    maxu = np.max(u)
    for z in range(dims[2]):
        for y in range(dims[1]):
            for x in range(dims[0]):
                    val = int(255 * ((u[x,y,z]-minu) / (maxu-minu)))                    
                    file2.write(val.to_bytes(1, byteorder='little', signed=False))
    file2.close()
    """
    for z in range(dims[2]):
        for y in range(dims[1]):
            for x in range(dims[0]):
                imageData.SetScalarComponentFromDouble(x, y, z, 0, u[x,y,z])
    
    writer = vtk.vtkXMLImageDataWriter()
    writer.SetFileName(filename2)
    if vtk.VTK_MAJOR_VERSION <= 5:
        writer.SetInputConnection(imageData.GetProducerPort())
    else:
        writer.SetInputData(imageData)
    writer.Write()
    
    
    # ----------------------------------------------------------------------------
    
    # creating vti image file with negitive gorkov potentials 
    filename3 = "Force.vti"
    
    imageDataForce = vtk.vtkImageData()
    imageDataForce.SetDimensions(npoints, npoints, npoints)
    imageDataForce.SetOrigin( (-npoints+1)/2, 0, (-npoints+1)/2 )
    if vtk.VTK_MAJOR_VERSION <= 5:
        imageDataForce.SetNumberOfScalarComponents(3)
        imageDataForce.SetScalarTypeToDouble()
    else:
        imageDataForce.AllocateScalars(vtk.VTK_DOUBLE, 3)
    
    dims = imageDataForce.GetDimensions()
    
    # Fill every entry of the image data
    for z in range(dims[2]):
        for y in range(dims[1]):
            for x in range(dims[0]):
                imageDataForce.SetScalarComponentFromDouble(x, y, z, 0, fx[x,y,z])
                imageDataForce.SetScalarComponentFromDouble(x, y, z, 1, fy[x,y,z])
                imageDataForce.SetScalarComponentFromDouble(x, y, z, 2, fz[x,y,z])
    
    writer = vtk.vtkXMLImageDataWriter()
    writer.SetFileName(filename3)
    if vtk.VTK_MAJOR_VERSION <= 5:
        writer.SetInputConnection(imageDataForce.GetProducerPort())
    else:
        writer.SetInputData(imageDataForce)
    writer.Write()
