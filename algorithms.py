
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
    return theta


def pressure (r, rt, phi, nt):
    import numpy as np; import math; import cmath; import constants
    mag_nt = np.linalg.norm(nt)
    nt = np.divide(nt, mag_nt)  # normalising the vector to the unit direction vector

    rs = np.subtract(r,rt)
    k = (2*math.pi)/(float(constants.lamda))   
    mag_rs = np.linalg.norm(rs)
    if mag_rs < 0.001: # Setting calculated dp/dr on top of transducer to zero.
        pressure = 0+0j
    else:
        theta = math.acos((np.dot(rs,nt)) / (mag_rs))
        exponential =  cmath.exp( 1j * (phi + k * mag_rs) ) / mag_rs
        if theta < 0.0000001: # zero angle causes divistion by zero error -> directionality function aproaches 0
            theta = 0.0000001
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
    if mag_rs < 0.001: # Setting calculated dp/dr on top of transducer to zero.
        d_p_dr = [ 0, 0, 0] 
    else:
        rs_hat = rs / mag_rs
        k = (2*math.pi)/(float(constants.lamda))  
        theta = math.acos((np.dot(rs,nt)) / (mag_rs))
        exponent_term =  cmath.exp( 1j * (phi + k * mag_rs) ) / mag_rs
        if theta < 0.0001: # zero angle causes divistion by zero error -> directionality function aproaches 0
            fraction_term =  (constants.p0*constants.A)
            d_exponential_term_dr = ((rs_hat * 1j * k * cmath.exp(1j*(phi + k * mag_rs)) ) / (mag_rs))  -  ((cmath.exp(1j*(phi + k * mag_rs)) * rs_hat) / (mag_rs**2) )
            d_p_dr = (fraction_term * d_exponential_term_dr)
        else:
            fraction_term =  (constants.p0*constants.A)*( (math.sin(k*constants.a*math.sin(theta))) /  (k*constants.a*math.sin(theta)) )
            d_exponential_term_dr = ((rs_hat * 1j * k * cmath.exp(1j*(phi + k * mag_rs)) ) / (mag_rs))  -  ((cmath.exp(1j*(phi + k * mag_rs)) * rs_hat) / (mag_rs**2) )
            numerator = constants.p0 * constants.A * math.sin(k*constants.a*math.sin(theta))
            denominator =  k*constants.a*math.sin(theta)
            d_denominator_dr = k*constants.a*(( ((-np.dot(rs,nt))/(mag_rs) ) / ((1 - (np.dot(rs,nt))/(mag_rs) )**0.5) ) * ( (np.dot(nt,mag_rs) - (rs_hat*np.dot(nt,rs)) ) / (mag_rs**2) ) )
            d_numerator_dr = constants.p0 * constants.A * math.cos(k*constants.a*math.sin(theta))*d_denominator_dr
            d_fraction_dr = ((d_numerator_dr*denominator) - (numerator*d_denominator_dr))/(denominator**2)
                
            d_p_dr = (d_fraction_dr * exponent_term) + (fraction_term * d_exponential_term_dr)
    return d_p_dr


def acoustic_potential (r, rt, phi, nt):
    
    # Takes in any number of transducer positions and phases and a postion in space
    # will output the acoustic potential U at that location
    
    import numpy as np; import constants; import algorithms
    ntrans = len(rt)
    pressure = np.zeros((ntrans), dtype=complex)
    differentiate_pressure_x = np.zeros((ntrans), dtype=complex)
    differentiate_pressure_y = np.zeros((ntrans), dtype=complex)
    differentiate_pressure_z = np.zeros((ntrans), dtype=complex)
    
    for transducer in range (0, ntrans):
        nt_trans = [ nt[transducer,0,0], nt[transducer,0,1], nt[transducer,0,2] ]
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

    return u, p_abs


def differentiate_acoustic_potential(h,r,rt,phi,nt):
    x = r[0]; y = r[1]; z = r[2]
    
    du_dr_numercal_x = (acoustic_potential( [x+h, y, z], rt,phi,nt ) - acoustic_potential( [x-h, y, z], rt,phi,nt)) / (2*h)
    du_dr_numercal_y = (acoustic_potential( [x, y+h, z], rt,phi,nt ) - acoustic_potential( [x, y-h, z], rt,phi,nt)) / (2*h)
    du_dr_numercal_z = (acoustic_potential( [x, y, z+h], rt,phi,nt ) - acoustic_potential( [x, y, z-h], rt,phi,nt)) / (2*h)
    du_dr_numercal   = [du_dr_numercal_x, du_dr_numercal_y, du_dr_numercal_z]

    return du_dr_numercal


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
plt.show()
"""



def circle_co_ords(splits, diameter): 
    """Take in number of points and circle diamiter and output coordinates of points in a circle centered at the origin"""
    import math; import numpy as np
    x = np.zeros (splits)
    y = np.zeros (splits)
    coordinates = np.zeros((splits,2))
    for point in range(0,splits):
        angle = ((2*math.pi) / splits) * (point+1)
        x[point] = diameter * math.cos(angle)
        y[point] = diameter * math.sin(angle)
    coordinates = [x,y]
    return coordinates
"""
import matplotlib.pyplot as plt;
test = circle_co_ords(50, 0.01)
plt.plot(test[0], test[1], 'ro')
plt.show()
"""

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



