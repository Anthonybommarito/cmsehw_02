import numpy as np
import matplotlib.pyplot as plt

v_0 = 100 #m/s
r = 10 #cm
d = 11.34 #g/cm^3
angle = 40*np.pi/180 #converted degrees to radians for np.sin
g = 9.81 #m/s^2

def fEuler(posx,posy,velx,vely,accelx,accely,dt):
    vx_new = velx + accelx*dt
    vy_new = vely + accely*dt
    posx_new = posx + velx*dt
    posy_new = posy + vely*dt

    return vx_new, vy_new, posx_new, posy_new

def midpoint():
    pass

d_true =  v_0**2*np.sin(2*angle)/g

vx0 = v_0*np.cos(angle)
vy0 = v_0*np.sin(angle)
x0 = 0
y0 = 0

xl=[0]
yl=[0]
tl=[0]
vxl = [vx0]
vyl = [vy0]

t=0
dt=.096

while y0>=0:
    
    vx,vy,x,y = fEuler(x0,y0,vx0,vy0,0,-g,dt)
    
    vx0,vy0,x0,y0 = vx,vy,x,y
    
    t += dt
    
    xl.append(x0)
    yl.append(y0)
    vxl.append(vx0)
    vyl.append(vy0)
    tl.append(t)
    
plt.plot(xl,yl)
yl.index(max(yl))
print(max(xl))
    
#t=0
#dt=.096
#
#for i in range(2000):
#
#    while y[i]>=0:
#    
#        step = fEuler(x[i],y[i],vx[i],vy[i],0,-g,dt)
#    
#        vx.append(step[0])
#        x.append(step[2])
#    
#        vy.append(step[1])
#        y.append(step[3])
#        print(x[i+1],y[i+1])
        


#E = np.abs(d_true - x[-1])/d_true
#
#
#print(E, x[-1], d_true,len(x))
#
#plt.plot(x,y)
