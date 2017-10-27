## Differentiation Tester

import math; import cmath; import numpy as np; import constants

def exponential (x, y, z, rt, phi, nt):

    r = (x, y, z)
    rs = np.subtract(r,rt)

    mag_rs = np.linalg.norm(rs)
    k = (2*math.pi)/(float(constants.lamda))   
    
    exponential =  cmath.exp( 1j * (phi + k * mag_rs) ) / mag_rs

    return exponential

def frac (x, y, z, rt, phi, nt):

    r = (x, y, z)
    rs = np.subtract(r,rt)

    mag_rs = np.linalg.norm(rs)
    k = (2*math.pi)/(float(constants.lamda))   
    theta = math.acos((np.dot(rs,nt)) / (mag_rs))

    frac =  (constants.p0*constants.A)*( (math.sin(k*constants.a*math.sin(theta))) /  (k*constants.a*math.sin(theta)) )

    return frac

def sin_theta (x, y, z, rt, phi, nt):

    r = (x, y, z)
    rs = np.subtract(r,rt)

    mag_rs = np.linalg.norm(rs)

    theta = math.acos((np.dot(rs,nt)) / (mag_rs))

    sin_theta = math.sin(theta)
    return sin_theta

def pressure (x, y, z, rt, phi, nt):

    r = (x, y, z)
    rs = np.subtract(r,rt)

    mag_rs = np.linalg.norm(rs)

    theta = math.acos((np.dot(rs,nt)) / (mag_rs))
    exponential =  cmath.exp( 1j * (phi + k * mag_rs) ) / mag_rs
    frac =  (constants.p0*constants.A)*( (math.sin(k*constants.a*math.sin(theta))) /  (k*constants.a*math.sin(theta)) )

    pressure = (exponential*frac)
    return pressure



phi = math.pi   # Phase of the transducer
x= 0.00486648         # Point in space x,y,z
y= 0.486601
z= 0.06541
h = 0.00000000001      # delta x the change to differientate over


r = (x, y, z)
rt = [0.05,0,0.05]
nt = [0,1,0]
rs = np.subtract(r,rt)
mag_rs = np.linalg.norm(rs)
rs_hat = rs / mag_rs
k = (2*math.pi)/(float(constants.lamda))  
theta = math.acos((np.dot(rs,nt)) / (mag_rs))

"""
## Exponential term test: function f=Exponential

df_dr_numercal_x_exponential =  (exponential(x+h,y,z,rt,phi,nt) - exponential(x-h,y,z,rt,phi,nt)) / (2*h)
df_dr_numercal_y_exponential =  (exponential(x,y+h,z,rt,phi,nt) - exponential(x,y-h,z,rt,phi,nt)) / (2*h)
df_dr_numercal_z_exponential =  (exponential(x,y,z+h,rt,phi,nt) - exponential(x,y,z-h,rt,phi,nt)) / (2*h)
df_dr_numercal_exponential = [df_dr_numercal_x_exponential, df_dr_numercal_y_exponential, df_dr_numercal_z_exponential]
# Analytical Terms
df_dr_analytical_exponential = ((rs_hat * 1j * k * cmath.exp(1j*(phi + k * mag_rs)) ) / (mag_rs))  -  ((cmath.exp(1j*(phi + k * mag_rs)) * rs_hat) / (mag_rs**2) )

print("Derivative with respect to x: numerical then analytical")
print (df_dr_numercal_exponential[0])
print(df_dr_analytical_exponential[0])
print("Derivative with respect to y: numerical then analytical")
print (df_dr_numercal_exponential[1])
print(df_dr_analytical_exponential[1])
print("Derivative with respect to z: numerical then analytical")
print (df_dr_numercal_exponential[2])
print(df_dr_analytical_exponential[2])
"""

"""
## sin_theta term test

d_sin_theta_dr_numercal_x =  (sin_theta(x+h,y,z,rt,phi,nt) - sin_theta(x-h,y,z,rt,phi,nt)) / (2*h)
d_sin_theta_dr_numercal_y =  (sin_theta(x,y+h,z,rt,phi,nt) - sin_theta(x,y-h,z,rt,phi,nt)) / (2*h)
d_sin_theta_dr_numercal_z =  (sin_theta(x,y,z+h,rt,phi,nt) - sin_theta(x,y,z-h,rt,phi,nt)) / (2*h)
d_sin_theta_dr_numercal = [d_sin_theta_dr_numercal_x, d_sin_theta_dr_numercal_y, d_sin_theta_dr_numercal_z]
# Analytical Terms

d_sin_theta_dr_analytical  = (( ((-np.dot(rs,nt))/(mag_rs) ) / ((1 - (np.dot(rs,nt))/(mag_rs) )**0.5) ) * ( (np.dot(nt,mag_rs) - (rs_hat*np.dot(nt,rs)) ) / (mag_rs**2) ) )


print("Derivative with respect to x: Difference")
print (abs(d_sin_theta_dr_numercal[0]-d_sin_theta_dr_analytical[0]))
print()
print("Derivative with respect to y: Difference")
print (abs(d_sin_theta_dr_numercal[1] - d_sin_theta_dr_analytical[1]))
print()
print("Derivative with respect to z: Difference")
print (abs(d_sin_theta_dr_numercal[2] - d_sin_theta_dr_analytical[2]))
"""

"""
## Fraction term test

df_dr_numercal_x_fraction =  (frac(x+h,y,z,rt,phi,nt) - frac(x-h,y,z,rt,phi,nt)) / (2*h)
df_dr_numercal_y_fraction =  (frac(x,y+h,z,rt,phi,nt) - frac(x,y-h,z,rt,phi,nt)) / (2*h)
df_dr_numercal_z_fraction =  (frac(x,y,z+h,rt,phi,nt) - frac(x,y,z-h,rt,phi,nt)) / (2*h)
df_dr_numercal_fraction = [df_dr_numercal_x_fraction, df_dr_numercal_y_fraction, df_dr_numercal_z_fraction]
# Analytical Terms
numerator = constants.p0 * constants.A * math.sin(k*constants.a*math.sin(theta))
denominator =  k*constants.a*math.sin(theta)
d_denominator_dr = k*constants.a*(( ((-np.dot(rs,nt))/(mag_rs) ) / ((1 - (np.dot(rs,nt))/(mag_rs) )**0.5) ) * ( (np.dot(nt,mag_rs) - (rs_hat*np.dot(nt,rs)) ) / (mag_rs**2) ) )
d_numerator_dr = constants.p0 * constants.A * math.cos(k*constants.a*math.sin(theta))*d_denominator_dr

d_fraction_dr_analytical = ((d_numerator_dr*denominator) - (numerator*d_denominator_dr))/(denominator**2)


print("Derivative with respect to x: numerical then analytical")
print (df_dr_numercal_fraction[0])
print(d_fraction_dr_analytical[0])
print("Derivative with respect to y: numerical then analytical")
print (df_dr_numercal_fraction[1])
print(d_fraction_dr_analytical[1])
print("Derivative with respect to z: numerical then analytical")
print (df_dr_numercal_fraction[2])
print(d_fraction_dr_analytical[2])
"""



## Final Pressure derivation test

dp_dr_numercal_x =  (pressure(x+h,y,z,rt,phi,nt) - pressure(x-h,y,z,rt,phi,nt)) / (2*h)
dp_dr_numercal_y =  (pressure(x,y+h,z,rt,phi,nt) - pressure(x,y-h,z,rt,phi,nt)) / (2*h)
dp_dr_numercal_z =  (pressure(x,y,z+h,rt,phi,nt) - pressure(x,y,z-h,rt,phi,nt)) / (2*h)
dp_dr_numercal = [dp_dr_numercal_x, dp_dr_numercal_y, dp_dr_numercal_z]



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



print("Derivative with respect to x: Difference")
print (abs(dp_dr_numercal[0] - d_p_dr[0]))
print()
print("Derivative with respect to y: Difference")
print (abs(dp_dr_numercal[1] - d_p_dr[1]))
print()
print("Derivative with respect to z: Difference")
print (abs(dp_dr_numercal[2] - d_p_dr[2]))



