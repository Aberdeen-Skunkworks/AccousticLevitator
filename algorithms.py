
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
    rs = np.subtract(r,rt)
    k = (2*math.pi)/(float(constants.lamda))   
    mag_rs = np.linalg.norm(rs)
    theta = math.acos((np.dot(rs,nt)) / (mag_rs))
    exponential =  cmath.exp( 1j * (phi + k * mag_rs) ) / mag_rs
    frac =  (constants.p0*constants.A)*( (math.sin(k*constants.a*math.sin(theta))) /  (k*constants.a*math.sin(theta)) )

    pressure = (exponential*frac)
    return pressure



def differentiate_pressure(r,rt,nt,phi):
    # Differentiation of pressure with respect to (x,y,z) done analytically
    import math; import cmath; import numpy as np; import constants

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



def read_from_excel():
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


## Testing to see deleted transducers visulised ##
# -------------------------Import Libaries------------------------------------
import numpy as np; import transducer_placment; import matplotlib.pyplot as plt; import phase_algorithms; import math;

trans_to_delete = []  # List of unwanted transducers leave blank to keep all
rt = transducer_placment.big_daddy()    # spcing , x nummber, y number of transducers
rt = transducer_placment.delete_transducers(rt,trans_to_delete)

ntrans = len(rt)
x = np.zeros(ntrans)
y = np.zeros(ntrans)
for transducer in range (0,ntrans): # Writing the coordinates to output rt
    x[transducer]= rt[transducer,0,0]
    y[transducer]= rt[transducer,0,2] 

plt.plot(x, y,'ro')
plt.show()

phase_index = np.zeros((ntrans),dtype=int)
phi_focus = phase_algorithms.phase_find(rt,0,0.05,0)
for transducer in range(0,ntrans):
    phase_index[transducer] = int(2500-phi_focus[transducer]/((2*math.pi)/1250))
    
from connect import Controller 
with Controller() as ctl:
    print ("Connected to controller with", ctl.getOutputs(), "outputs.")

    for i in range(ctl.getOutputs()):
        ctl.disableOutput(i)

    for i in range(ctl.getOutputs()):
        ctl.disableOutput(max(0,i-1))
        ctl.setOffset(i,0)
        ctl.loadOffsets()
        try:
            input("Press enter: triggering "+str(i)+" right now")
        except SyntaxError:
            pass    
    
    
    
    
    
    
    
    