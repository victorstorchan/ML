from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize
import numdifftools as nd
#define the function for the area
#x only contains the interior points
#we added at the end the two extremities
def aux(x,a,b):
    y=np.zeros(len(x))
    k=0
    for i in range(len(x)-1):
        k+=(x[i]-x[i+1])*np.sqrt(a**2-x[i+1]**2)*b/a
    k+=(a-x[0])*np.sqrt(a**2-x[0]**2)*b/a # first extremity
    k+=x[len(x)-1]*b # second extremity
    return k

if __name__ == '__main__':
    
	fun_1_2 = lambda x: aux(x,1,2)
	x_start=[0.75,0.5,0.25] #starting guess, equirepartite points
	bnds_list=[] #the minimizer x_min (vector) has only positive value 
                  #(we work on the positive quarter of the ellipse)
	for i in range(len(x_start)):
        bnds_list.append((0, 1))
	bnds = tuple(bnds_list)
	tuple_x_start=tuple(x_start)
	res = optimize.minimize(fun_1_2, x_start, method='L-BFGS-B', bounds=bnds)

    #hessian_fun_1_2 = nd.Hessian(fun_1_2)
    #h=hessian_fun_1_2([ 0.87571881,  0.70655602,  0.48167682])
    #np.linalg.eigh(h)
