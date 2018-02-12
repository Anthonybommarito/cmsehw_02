import numpy as np
import matplotlib.pyplot as plt

v_0 = 100 #m/s
r = 0.10 #m
d = 11.34 #g/cm^3
angle = np.deg2rad(40) #converted degrees to radians for np.sin
g = 9.81 #m/s^2
vx0 = v_0*np.cos(angle)
vy0 = v_0*np.sin(angle)
x0 = 0
y0 = 0

def fEuler(f, t, x, dt):

    return x + dt*f(t, x)
    
def midpoint(f, t, y, dt):
    
    yp = fEuler(f,t+dt/2,y,dt/2)
    
    return y + dt*f(t+dt/2,yp)
    
    
def fgrav(t, z):
    '''
    function while taking gravity into account, no air resistance
    '''
    
    dzdt = np.zeros_like(z)
    
    dzdt[0] = z[2]
    dzdt[1] = z[3]
    dzdt[2] = 0
    dzdt[3] = -g

    return dzdt
    
t = 0
dt = .098

val = np.array([x0,y0,vx0,vy0])
val_list = [[t],[x0],[y0],[vx0],[vy0]] #t,x,y,vx,vy

while val[1]>=0:
    
    fzt = lambda val, t: fEuler(fgrav, t, val, dt)
    val = fzt(val,t)
    
    # Record time, then push it forward
    val_list[0].append( t )
    t += dt
    
    # Record components for later use
    for i in range(4):
        val_list[i+1].append( val[i] )

#print(max(val_list[1]))
#plt.plot(val_list[1],val_list[2])


t = 0
dt = .4

val2 = np.array([x0,y0,vx0,vy0])
val_list2 = [[t],[x0],[y0],[vx0],[vy0]] #t,x,y,vx,vy

while val2[1]>=0:
    
    fzt = lambda val2, t: midpoint(fgrav, t, val2, dt)
    val2 = fzt(val2,t)
    
    # Record time, then push it forward
    val_list2[0].append( t )
    t += dt
    
    # Record components for later use
    for i in range(4):
        val_list2[i+1].append( val2[i] )

#print(max(val_list2[1]))
#plt.plot(val_list2[1],val_list2[2])

def fair(t, z):
    
    C = .47
    p = 1.2 #density of air, kg/m^3
    A = np.pi*r**2
    m = 475
    dzdt = np.zeros_like(z)
    
    dzdt[0] = z[2]
    dzdt[1] = z[3]
    dzdt[2] = -1/2*C*p*A*z[2]**2*(z[2]/np.abs(z[2]))/m
    dzdt[3] = -g + -1/2*C*p*A*z[3]**2*(z[3]/np.abs(z[3]))/m

    return dzdt
    
t = 0
dt = .1

val3 = np.array([x0,y0,vx0,vy0])
val_list3 = [[t],[x0],[y0],[vx0],[vy0]] #t,x,y,vx,vy

while val3[1]>=0:
    
    fzt = lambda val3, t: fEuler(fair, t, val3, dt)
    val3 = fzt(val3,t)
    
    # Record time, then push it forward
    val_list3[0].append( t )
    t += dt
    
    # Record components for later use
    for i in range(4):
        val_list3[i+1].append( val3[i] )

#print(max(val_list3[1]))
#plt.plot(val_list3[1],val_list3[2])

t = 0
dt = .4

val4 = np.array([x0,y0,vx0,vy0])
val_list4 = [[t],[x0],[y0],[vx0],[vy0]] #t,x,y,vx,vy

while val4[1]>=0:
    
    fzt = lambda val4, t: midpoint(fair, t, val4, dt)
    val4 = fzt(val4,t)
    
    # Record time, then push it forward
    val_list4[0].append( t )
    t += dt
    
    # Record components for later use
    for i in range(4):
        val_list4[i+1].append( val4[i] )

print(max(val_list4[1]))
plt.plot(val_list4[1],val_list4[2])