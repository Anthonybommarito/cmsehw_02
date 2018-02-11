import numpy as np
import matplotlib.pyplot as plt

v_0 = 100 #m/s
r = 0.10 #m
d = 11.34 #g/cm^3
angle = np.deg2rad(40) #converted degrees to radians for np.sin
g = 9.81 #m/s^2

def fEuler(posx,posy,velx,vely,accelx,accely,dt):
    vx_new = velx + accelx*dt
    vy_new = vely + accely*dt
    posx_new = posx + velx*dt
    posy_new = posy + vely*dt

    return vx_new, vy_new, posx_new, posy_new

def midpoint(posx,posy,velx,vely,accelx,accely,dt):
    
    vx_new = velx + dt*(accelx) 
    vy_new = vely + dt*((accely))
    posx_new = posx + dt*(velx +(dt/2)*accelx)
    posy_new = posy + dt*(vely +(dt/2)*accely)
    
    return vx_new, vy_new, posx_new, posy_new

d_true =  v_0**2*np.sin(2*angle)/g

# Finding distance using Euler

vx0 = v_0*np.cos(angle)
vy0 = v_0*np.sin(angle)
x0 = 0
y0 = 0

x1=[0]
y1=[0]
t1=[0]
vx1 = [vx0]
vy1 = [vy0]

t=0
dt=.098

while y0>=0:
    
    vx,vy,x,y = fEuler(x0,y0,vx0,vy0,0,-g,dt)
    
    vx0,vy0,x0,y0 = vx,vy,x,y
    
    t += dt
    
    x1.append(x0)
    y1.append(y0)
    vx1.append(vx0)
    vy1.append(vy0)
    t1.append(t)
    
#plt.plot(x1,y1)
y1.index(max(y1))
    
E = np.abs(d_true - x1[-1])/d_true*100

#print('The error is: {0:.2f}%, The calculated distance is: {1:.2f}, The true \
#distance is: {2:.2f}, The number of steps is: {3:}'.format(E,x1[-1],d_true,\
#len(x1)))

#Finding distance using midpoint

vx0 = v_0*np.cos(angle)
vy0 = v_0*np.sin(angle)
x0 = 0
y0 = 0

x2=[0]
y2=[0]
t2=[0]
vx2 = [vx0]
vy2 = [vy0]

t=0
dt=.4

while y0>=0:
    
    vx,vy,x,y = midpoint(x0,y0,vx0,vy0,0,-g,dt)
    
    vx0,vy0,x0,y0 = vx,vy,x,y
    
    t += dt
    
    x2.append(x0)
    y2.append(y0)
    vx2.append(vx0)
    vy2.append(vy0)
    t2.append(t)

#plt.plot(x2,y2)
#y2.index(max(y2))
#print(max(x2))
    
E = np.abs(d_true - x2[-1])/d_true*100

#print('The error is: {0:.2f}%, The calculated distance is: {1:.2f}, The true \
#distance is: {2:.2f}, The number of steps is: {3:}'.format(E,x2[-1],d_true,\
#len(x2)))

#Adding air resistance to Euler

C = .47
p = 1.2 #density of air, kg/m^3
A = np.pi*r**2
m = 475 #kg

vx0 = v_0*np.cos(angle)
vy0 = v_0*np.sin(angle)
ax0 = (-1/2*C*p*A*vx0**2*(vx0/np.abs(vx0)))/m
ay0 = -g+(-1/2*C*p*A*vy0**2*(vy0/np.abs(vy0)))/m
x0 = 0
y0 = 0

x3=[0]
y3=[0]
t3=[0]
vx3 = [vx0]
vy3 = [vy0]
ax3=[ax0]
ay3=[ay0]

t=0
dt=.07

while y0>=0:
    
    vx,vy,x,y = fEuler(x0,y0,vx0,vy0,ax0,ay0,dt)
    
    ax = (-1/2*C*p*A*vx**2*(vx/np.abs(vx)))/m
    ay = -g+(-1/2*C*p*A*vy**2*(vy/np.abs(vy)))/m
    
    ax0,ay0,vx0,vy0,x0,y0 = ax,ay,vx,vy,x,y
    
    t += dt
    
    x3.append(x0)
    y3.append(y0)
    vx3.append(vx0)
    vy3.append(vy0)
    ax3.append(ax0)
    ay3.append(ay0)
    t3.append(t)

plt.plot(x3,y3)
y3.index(max(y3))

print('The calculated distance is: {0:.2f}, The number of steps is: {1:}'\
      .format(x3[-1],len(x3)))