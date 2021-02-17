import numpy as np
import matplotlib.pyplot as plt

#Note     : Function        :x^2-exp(-x) 
#inital x : 0   , initial y : 0
#final  x : 0   , final   y : ?

#Solution by hand and plot via python numpy matplotlib..
xr=np.linspace(0,10,100)
yr=1-np.exp(-xr)+(xr**3/3)

#Solution by Runge kutta of order Fourth commonly known as only Runge kutta's method:
def runge_kutta(Function=None,nsteps=1000,inix=None,iniy=None,finx=None):
    '''
    Return Solution of a Given `Funtion` .

    ..Author:: Suman Mandal

    ..Copyright:: (C) Noatic Digital LLB. All rights reserved.

    ..version :: 1.0.0 

    parameters
    ----------
    Function : string
        the function is followed string.
    nsteps : int,optional
        the step number.
    inix : float
        intial value of the independent variable.
    iniy : float
        intial value of the dependent variable i.e., of inix.
    finx : float 
        final value of the independent value.

    Returns
    -------
        returns a string contains
                                x : numpy 1darray
                                    contain used x independent values.
                                Y : numpy 1darray
                                    contain correponding values.
                                ye : float
                                    final value of dependent variable to final value. 
    '''
    import numpy as np
    def func(x,y):
        return eval(Function)
    n=nsteps
    x0=inix
    y0=iniy
    xf=finx
    h=(xf-x0)/n
    x=np.linspace(x0,xf,n+1)
    ye=y0
    Y=[y0]
    for i in range(n):
        k1=h*func(x[i],ye)
        k2=h*func(x[i]+0.5*h,ye+0.5*k1)
        k3=h*func(x[i]+0.5*h,ye+0.5*k2)
        k4=h*func(x[i]+h,ye+k3)

        k=(k1+2.0*k2+2.0*k3+k4)/6
        ye=ye+k
        Y.append(ye)

    return [x,Y,ye]

x,y,yf=runge_kutta('x**2-np.exp(-x)',nsteps=1000,inix=0,iniy=0,finx=10)
#function must be followed by string.for other detail use : help(runge_kutta)

#ploting:
fig,ax=plt.subplots(nrows=1,ncols=1)

ax.plot(x,y,label='Approx Solution Curve')          #<-solution via runge_kutta
ax.plot(xr,yr,'r--',label='Solution Curve')         #<-solution via hand/paper

#simple ploting style used here:
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Solution')

plt.legend()
plt.show()