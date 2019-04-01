import matplotlib.pyplot as plt
import math as mt
import numpy as np
from matplotlib import animation


#To plot
def Plot(time, theta_caos, theta_lin, x, y):
    plt.figure()

    plt.subplot(211)
    plt.plot(time, theta_caos)
    plt.plot(time, theta_lin)
    plt.xlabel('Time [s]')
    plt.ylabel('Theta [Rad]')
    plt.title('Motion of Pendulum')
    plt.legend(['Non_linear','Linear'], loc = 'lower right')

    plt.subplot(212)
    plt.plot(x, y)
    plt.xlabel('X [m]')
    plt.ylabel('Y [m]')
    plt.title('Positions of Pendulum')
    plt.tight_layout()
    plt.show()

#Parameters
g = 9.81
l = 1.0
ang_f = mt.sqrt(g/l) #Angular frecuency
dif_t = 0.01 #Constant rate of change
T = 3 #20 seconds of motion
count = 0
#Initial Conditions
ang_init = 60*mt.pi/180
ang_vel_init = 0.0
t = 0.0
#Ever changing variables
ang = ang_init
ang_vel = ang_vel_init

#Data to plot theta(time)
theta_caos = [ang_init]
theta_lin = [ang_init]
time = [t]
x = []
y = []

#Loop of our system of first order differentials
while count*dif_t <= T:
    dif_ang_vel = dif_t*(-(ang_f)**2*mt.sin(ang))
    ang_vel += dif_ang_vel # First equation of system
    dif_ang = dif_t * ang_vel
    ang += dif_ang # Second equation of system
    theta_caos.append(ang)
    x1 = l * mt.sin(ang)
    x2 = -l * mt.cos(ang)
    x.append(x1)
    y.append(x2)
    count += 1
    t += dif_t # Ever changing Domain of time
    theta_l= ang_init*mt.sin(ang_f*t + 1.5708) # Linear Armonic Motion
    theta_lin.append(theta_l)
    time.append(t)

#Setting animation figure
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
                     xlim=(-2, 2), ylim=(-2, 2))
ax.grid()
line, = ax.plot([], [], lw=2)
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
#Initialize animation
def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text

def animate(i):
    global t, ang_init, ang_f, dif_t
    t += dif_t # Ever changing Domain of time
    theta_l= ang_init*mt.cos(ang_f*(t-dif_t*i))
    line.set_data(t, theta_l)
    time_text.set_text('time = %.1f' % t)
    return line, time_text

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=100, interval=20, blit=True)
plt.show()
#Plot(time, theta_caos, theta_lin, x, y)
