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




phi = math.pi   # Phase of the transducer
x= 0            # Point in space x,y,z
y= 0.05
z= 0
h = 0.0000000001      # delta x the change to differientate over


r = (x, y, z)
rt = [0.05,0,0.05]
nt = [0,1,0]
rs = np.subtract(r,rt)
mag_rs = np.linalg.norm(rs)
rs_hat = rs / mag_rs
k = (2*math.pi)/(float(constants.lamda))  
theta = math.acos((np.dot(rs,nt)) / (mag_rs))


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







## Fraction term test

df_dr_numercal_x_fraction =  (frac(x+h,y,z,rt,phi,nt) - frac(x-h,y,z,rt,phi,nt)) / (2*h)
df_dr_numercal_y_fraction =  (frac(x,y+h,z,rt,phi,nt) - frac(x,y-h,z,rt,phi,nt)) / (2*h)
df_dr_numercal_z_fraction =  (frac(x,y,z+h,rt,phi,nt) - frac(x,y,z-h,rt,phi,nt)) / (2*h)
df_dr_numercal_fraction = [df_dr_numercal_x_fraction, df_dr_numercal_y_fraction, df_dr_numercal_z_fraction]
# Analytical Terms
numerator = constants.p0 * constants.A * math.sin(k*constants.a*math.sin(theta))
denominator =  k*constants.a*math.sin(theta)
d_denominator_dr = k*constants.a*(( (-np.dot(rs,nt)) / ((1 - (np.dot(rs,nt))/(mag_rs) )**0.5) ) * (nt*( ((1)/(mag_rs)) - ((2*rs_hat)/(mag_rs)) )))
d_numerator_dr = constants.p0 * constants.A * math.cos(k*constants.a*math.sin(theta))*d_denominator_dr

d_fraction_dr_analytical = (d_numerator_dr*denominator - numerator*d_denominator_dr)/(denominator**2)


print("Derivative with respect to x: numerical then analytical")
print (df_dr_numercal_fraction[0])
print(d_fraction_dr_analytical[0])
print("Derivative with respect to y: numerical then analytical")
print (df_dr_numercal_fraction[1])
print(d_fraction_dr_analytical[1])
print("Derivative with respect to z: numerical then analytical")
print (df_dr_numercal_fraction[2])
print(d_fraction_dr_analytical[2])


