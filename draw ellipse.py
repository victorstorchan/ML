from __future__ import division
import matplotlib.pyplot as plt
import numpy as np

import math

def trace(x,a,b,step_ellipse):
        x0=np.arange(-a,a+step_ellipse,step_ellipse)
        y0=np.zeros(len(x0))
        print(len(x0))
        y=np.zeros(len(x))
        for i in range(len(x0)):
            y0[i]=np.sqrt(a**2-x0[i]**2)*b/a
        y0[len(x0)-1]=0
        
        for i in range(1,len(x)):
            y[i]=np.sqrt(a**2-x[i]**2)*b/a
        y[0]=y[1]
        y[len(x)-1]=y[len(x)-2]
        print(y0)
        plt.figure()
        for i in range(len(x)):
            if i<=len(x)-2:
                if x[i]*x[i+1]>0 and x[i]<0:
                    x_plot=[x[i],x[i]]
                    y_plot=[-y[i+1],y[i+1]]
                    z1_plot=[x[i],x[i+1]]
                    z2_plot=[y[i+1],y[i+1]]
                    z3_plot=[x[i],x[i+1]]
                    z4_plot=[-y[i+1],-y[i+1]]
                    plt.plot(x_plot,y_plot,'r')
                    plt.plot(z1_plot,z2_plot,'r')
                    plt.plot(z3_plot,z4_plot,'r')
                    plt.axis([-1.5, 1.5, -3, 3])
                elif x[i]*x[i+1]<=0:
                    x_plot=[x[i],x[i]]
                    y_plot=[-b,b]
                    z1_plot=[x[i],x[i+1]]
                    z2_plot=[b,b]
                    z3_plot=[x[i+1],x[i+1]]
                    z4_plot=[b,-b]
                    z5_plot=[x[i],x[i+1]]
                    z6_plot=[-b,-b]
                    plt.plot(x_plot,y_plot,'r')
                    plt.plot(z1_plot,z2_plot,'r')
                    plt.plot(z3_plot,z4_plot,'r')
                    plt.plot(z5_plot,z6_plot,'r')
                elif x[i]*x[i+1]>0 and x[i]>0:
                    x_plot=[x[i],x[i]]
                    y_plot=[-y[i],y[i]]
                    z1_plot=[x[i],x[i+1]]
                    z2_plot=[y[i],y[i]]
                    z3_plot=[x[i+1],x[i+1]]
                    z4_plot=[y[i],y[i+1]]
                    z5_plot=[x[i],x[i+1]]
                    z6_plot=[-y[i],-y[i]]
                    z7_plot=[x[i+1],x[i+1]]
                    z8_plot=[-y[i],0]
                    plt.plot(x_plot,y_plot,'r')
                    plt.plot(z1_plot,z2_plot,'r')
                    plt.plot(z3_plot,z4_plot,'r')
                    plt.plot(z5_plot,z6_plot,'r')
                    plt.plot(z7_plot,z8_plot,'r')

            else:
                x_plot=[x[i],x[i]]
                y_plot=[0,y[i]]
                plt.plot(x_plot,y_plot,'r')
        plt.plot(x0,y0,'b')
        plt.plot(x0,-y0,'b')
        #plt.axis([-2, 2, -5, 5])
        plt.show()

if __name__ == '__main__':
    x=np.zeros(9)
    x[0]=-1
    x[1]=-0.75
    x[2]=-0.5
    x[3]=-0.25
    x[4]=0
    x[5]=0.25
    x[6]=0.5
    x[7]=0.75
    x[8]=1
