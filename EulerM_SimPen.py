import matplotlib.pyplot as plt
import math as mt
import numpy as np

#To plot
def Plot(time, theta_caos, theta_lin):
    plt.plot(time, theta_caos, '-o')
    plt.plot(time, theta_lin, '-o')
    plt.xlabel('Time [s]')
    plt.ylabel('Theta [Rad]')
    plt.title('Motion of Pendulum')
    plt.legend(['Non_linear','Linear'], loc = 'lower right')
    plt.show()

#Parameters
g = 9.81
l = 1.0
ang_f = mt.sqrt(g/l) #Angular frecuency
dif_t = 0.1 #Constant rate of change
T = 3 #20 seconds of motion
count = 0
#Initial Conditions
ang_init = 3*mt.pi/180
ang_vel_init = 0.0
t = 0.0
#Ever changing variables
ang = ang_init
ang_vel = ang_vel_init

#Data to plot theta(time)
theta_caos = []
theta_lin = []
time = []
#Loop of our system of first order differentials
while count*dif_t <= T:
    dif_ang_vel = dif_t*(-(ang_f)**2*mt.sin(ang))
    ang_vel += dif_ang_vel # First equation of system
    dif_ang = dif_t * ang_vel
    ang += dif_ang # Second equation of system
    theta_caos.append(abs(ang))
    theta_l= ang*mt.sin(ang_f*t + 1.5708) # Linear Armonic Motion
    theta_lin.append(theta_l)
    t += dif_t # Ever changing Domain of time
    time.append(t)
    count += 1

for k in theta_caos:
    Diff = []
    for i in theta_lin:
        Diff = k / i
#diff = sum(Diff) / float(len(Diff))
diff = np.mean(Diff)
print(diff)

Plot(time, theta_caos, theta_lin)
