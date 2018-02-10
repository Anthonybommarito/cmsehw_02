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

    return [vx_new, vy_new, posx_new, posy_new]

def midpoint():
    pass

d_true =  v_0**2*np.sin(2*angle)/g

v_0x = v_0*np.cos(angle)
v_0y = v_0*np.sin(angle)

dt = .5

x = [0]
y = [0]
vx = [v_0x]
vy = [v_0y]

t = np.arange(0,1000,dt)
for i in range(len(t)-1):
    if y[i]<0:
        break
    else:
        step = fEuler(x[i],y[i],vx[i],vy[i],0,-g,dt)

        vx.append(step[0])
        x.append(step[2])

        vy.append(step[1])
        y.append(step[3])
        #print(x[i+1],y[i+1])

E = np.abs(d_true - x[-2])/d_true


print(E, x[-2], d_true)

#plt.plot(y,x)
