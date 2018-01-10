
def get_angle(rt): 
    
# takes in co-odinates of transducers and outputs the angles between 0 and 2 pi 
# angles are anticlockwise from the x axis for each transducer in turn
    
    import numpy as np; import math;
    
    ntrans = len(rt)
    theta = np.zeros ((ntrans),dtype=float)
    xdir = np.array ((1,0,0)) # Vector pointing down the x axis to take angles from
    
    for transducer in range(0, ntrans):
        
        r = [rt[transducer,0,0], rt[transducer,0,1], rt[transducer,0,2]]
        dmag = np.linalg.norm(r)     # Distance between transducer and origin

        if dmag < (1*10**(-13)):
            theta[transducer] = 0 # setting angle to zero if transducer is ontop of the origin
        else:
            dot = r[0]*xdir[0] + r[1]*xdir[1] + r[2]*xdir[2] # Dot product of the direction of the transducr and the position in space
            theta[transducer] = math.acos(dot/dmag)
            
        if rt[transducer,0,2] < 0: # making angle go from 0 to 2 pi anticlockwise angle from the x axis
            theta[transducer] = math.pi*2 - theta[transducer]
            
        #print(theta[transducer]/(math.pi/180)) # To test uncomment to get angle in degrees 
    
    return (theta)


def pressure (r, rt, phi, nt):
    import numpy as np; import math; import cmath; import constants
    mag_nt = np.linalg.norm(nt)
    nt = np.divide(nt, mag_nt)  # normalising the vector to the unit direction vector
    
    rs = np.subtract(r,rt)
    k = (2*math.pi)/(float(constants.lamda))   
    mag_rs = np.linalg.norm(rs)
    theta = math.acos((np.dot(rs,nt)) / (mag_rs))
    exponential =  cmath.exp( 1j * (phi + k * mag_rs) ) / mag_rs
    frac =  (constants.p0*constants.A)*( (math.sin(k*constants.a*math.sin(theta))) /  (k*constants.a*math.sin(theta)) )

    pressure = (exponential*frac)
    return pressure



def differentiate_pressure(r, rt, phi, nt):
    # Differentiation of pressure with respect to (x,y,z) done analytically
    import math; import cmath; import numpy as np; import constants
    
    mag_nt = np.linalg.norm(nt)
    nt = np.divide(nt, mag_nt)  # normalising the vector to the unit direction vector
    
    rs = np.subtract(r,rt)
    mag_rs = np.linalg.norm(rs)
    rs_hat = rs / mag_rs
    k = (2*math.pi)/(float(constants.lamda))  
    
    theta = math.acos((np.dot(rs,nt)) / (mag_rs))
    exponent_term =  cmath.exp( 1j * (phi + k * mag_rs) ) / mag_rs
    fraction_term =  (constants.p0*constants.A)*( (math.sin(k*constants.a*math.sin(theta))) /  (k*constants.a*math.sin(theta)) )
    
    d_exponential_term_dr = ((rs_hat * 1j * k * cmath.exp(1j*(phi + k * mag_rs)) ) / (mag_rs))  -  ((cmath.exp(1j*(phi + k * mag_rs)) * rs_hat) / (mag_rs**2) )
    
    numerator = constants.p0 * constants.A * math.sin(k*constants.a*math.sin(theta))
    denominator =  k*constants.a*math.sin(theta)
    d_denominator_dr = k*constants.a*(( ((-np.dot(rs,nt))/(mag_rs) ) / ((1 - (np.dot(rs,nt))/(mag_rs) )**0.5) ) * ( (np.dot(nt,mag_rs) - (rs_hat*np.dot(nt,rs)) ) / (mag_rs**2) ) )
    d_numerator_dr = constants.p0 * constants.A * math.cos(k*constants.a*math.sin(theta))*d_denominator_dr
    d_fraction_dr = ((d_numerator_dr*denominator) - (numerator*d_denominator_dr))/(denominator**2)
    
    d_p_dr = (d_fraction_dr * exponent_term) + (fraction_term * d_exponential_term_dr)
    
    return (d_p_dr)


def acoustic_potential (r, rt, nt, phi):
    
    # Takes in any number of transducer positions and phases and a postion in space
    # will output the acoustic potential U at that location
    
    import numpy as np; import constants; import algorithms
    ntrans = len(rt)
    pressure = np.zeros((ntrans), dtype=complex)
    differentiate_pressure_x = np.zeros((ntrans), dtype=complex)
    differentiate_pressure_y = np.zeros((ntrans), dtype=complex)
    differentiate_pressure_z = np.zeros((ntrans), dtype=complex)
    
    for transducer in range (0, ntrans):
        nt_trans = [ nt[transducer,0,0], nt[transducer,0,1], nt[transducer,0,2]]
        rt_trans = [ rt[transducer,0,0], rt[transducer,0,1], rt[transducer,0,2] ]
        phi_trans = phi[transducer]
        
        pressure[transducer] = algorithms.pressure(r, rt_trans , phi_trans, nt_trans)
        differentiate_pressure = algorithms.differentiate_pressure(r, rt_trans , phi_trans, nt_trans)
        differentiate_pressure_x[transducer] = differentiate_pressure[0]
        differentiate_pressure_y[transducer] = differentiate_pressure[1]
        differentiate_pressure_z[transducer] = differentiate_pressure[2]
    
    total_pressure = np.sum(pressure)
    total_diff_pressure_x = np.sum(differentiate_pressure_x)
    total_diff_pressure_y = np.sum(differentiate_pressure_y)
    total_diff_pressure_z = np.sum(differentiate_pressure_z)

    p_abs   = np.absolute(total_pressure)  
    px_abs  = np.absolute(total_diff_pressure_x)  
    py_abs  = np.absolute(total_diff_pressure_y)  
    pz_abs  = np.absolute(total_diff_pressure_z)  

    
    u = (2*constants.k1*p_abs**2) - (2*constants.k2*(px_abs**2 + py_abs**2 + pz_abs**2))
    u = u - (constants.p_mass*constants.gravity*(r[1])) 
    # including potential energy (mass*g*height) it is taken away even though gravity is negitive so that when the negitive gradient is takn then the force will be downwards
    return u , p_abs

import transducer_placment; import numpy as np; import constants; import vti_writer; import phase_algorithms
    

r = [0, 0.04, 0]
rt = transducer_placment.array_grid(0.01,6,6)
ntrans = len (rt)
nt = transducer_placment.direction_vectors(ntrans)
#phi = np.zeros(ntrans)
phi_focus = phase_algorithms.phase_find(rt,0,0.04,0) # phi is the initial phase of each transducer to focus on a point
phi = phase_algorithms.add_twin_signature(rt,phi_focus)

test = acoustic_potential (r, rt, nt, phi)

u = np.zeros ((constants.npoints,constants.npoints,constants.npoints), dtype=float)
p_abs = np.zeros ((constants.npoints,constants.npoints,constants.npoints), dtype=float)

x = constants.x; y = constants.y; z = constants.z
gsize = constants.gsize
for xloop in range (0,constants.npoints):
    for yloop in range (0,constants.npoints):
        for zloop in range (0,constants.npoints):
            
            r = [ x  , y , z ]          # Point in space for each itteriation
            u_and_p = acoustic_potential(r, rt, nt, phi)
            u[xloop,yloop,zloop] = u_and_p[0]
            p_abs[xloop,yloop,zloop] = u_and_p[1]            
                        
            z = z + constants.deltaxyz    # Adding delta to x,y and z
        y = y + constants.deltaxyz
        z = -gsize               # Resetting the value of z to start value for next loop
    x = x + constants.deltaxyz
    y = 0                       # Resetting the value of y to start value for next loop
    z = -gsize                   # Resetting the value of z to start value for next loop
x = -gsize # Initial values of x,y and z in (m) Grid volume
y = 0.00
z = -gsize



diff_u = np.gradient(u,constants.deltaxyz)
ux = diff_u[0]; uy = diff_u[1]; uz = diff_u[2]

# -----------------Calculating force on particle ---------------

fx = -ux; fy = - uy; fz = -uz


vti_writer.vti_writer (constants.npoints,p_abs,fx,fy,fz,u)

print("Calculations compleated successfuly")






def circle_co_ords(splits):
    import math; import numpy as np
    x = np.zeros (splits)
    y = np.zeros (splits)
    coordinates = np.zeros((splits,2))
    for point in range(0,splits):
        angle = ((2*math.pi) / splits) * (point+1)
        x[point] = 0.01 * math.cos(angle)
        y[point] = 0.01 * math.sin(angle)
    coordinates = [x,y]
    return coordinates
"""
import matplotlib.pyplot as plt;
test = circle_co_ords(50)
plt.plot(test[0], test[1], 'ro')
plt.show() """


def read_from_excel(): # Reads the transducer locations from excel locations.xlsx
    #import required libraries
    from openpyxl import load_workbook
    import numpy as np
    #read  from excel file
    wb = load_workbook('locations.xlsx')
    sheet_1 = wb.get_sheet_by_name('Sheet1')
    x = np.zeros(88)
    y = np.zeros(88)
    coordinates = np.zeros((88,2))
    for i in range(0,88):
        x[i]=sheet_1.cell(row=i+9, column=10).value
        y[i]=sheet_1.cell(row=i+9, column=11).value
     
    coordinates = [x,y]
    return coordinates
"""
import matplotlib.pyplot as plt;
test = read_from_excel()
plt.plot(test[0], test[1], 'ro')
plt.show()"""


def read_from_excel_phases(): # Reads the phases from phase.xlsx
    #import required libraries
    from openpyxl import load_workbook; import numpy as np
    #read  from excel file
    wb = load_workbook('phase.xlsx')
    sheet_1 = wb.get_sheet_by_name('phase')
    phases = np.zeros((88))
    for i in range(0,88):
        phases[i]=sheet_1.cell(row=i+1, column=14).value        
    return phases



