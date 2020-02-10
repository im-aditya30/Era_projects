import numpy as np

from matplotlib import pyplot as plt

g= np.array([0,-10.0])
h = 0.10

r = np.array([0,0])

x = np.array([])
y = np.array([])
t=0
thet = 0
dt= 0.01
for i in np.arange(0.00, 90.00,0.1) :
    theta = i *np.pi / 180.0
    # print(i)
    # print(abs(50 * np.cos(theta) - 4500))
    ln_x = (50.0 * np.cos(theta)) / abs(50.0 * np.cos(theta) - 45.0)
    y_co = (((25.0* np.sin(theta) + 2)* 4.5) / (25.0*np.cos(theta))) - (0.4 * np.log(ln_x))
    if( y_co >= 0.13 ): 
        h = -y_co
        thet = theta
        break
v = 25*np.array([np.cos(thet),np.sin(thet)])

while r[1] >= h:
    
    x = np.append(x,r[0])
    y= np.append(y,r[1])
    a = np.array([-5*v[0] ,-5*v[1]])
    a_net = np.add(a,g)
    v = np.add(v , a_net*dt)
    r = np.add(r,v*dt)
    t = t + dt
    
plt.plot(x,y)
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()

