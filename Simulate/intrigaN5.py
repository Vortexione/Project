import numpy as np
import matplotlib.pyplot as plt
#mind it z=dy/dx and dz/dx=f(x,y,z)
#Note     :   Function_1    : z (must be!!)
#         :   Function_2    : 2*z+y
#inital x : 0   , initial y : 1     , initial z : 2
#final  x :10   , final   y : ?     , final   z : ?

#Solution by hand and plot via python numpy matplotlib..
xr=np.linspace(0,10,100)
yr=(3*xr+1)*np.exp(-xr)

#Solution by Runge kutta of order Fourth commonly known as only Runge kutta's method:
def ODE2(Function_1=None,Function_2=None,nsteps=1000,inix=None,iniy=None,iniz=None,finx=None):
    '''
    Return Solution of a Given `Funtion` .

    ..Author:: Suman Mandal

    ..Copyright:: (C) Noatic Digital LLB. All rights reserved.

    ..version :: 1.0.0 

    parameters
    ----------
    Function_1 : string
        the function is followed by string.
    Function_2 : string
        the function is followed by string.
    nsteps : int,optional
        the step number.
    inix : float
        intial value of the independent variable.
    iniy : float
        intial value of the dependent variable i.e., of inix.
    iniz : float
        intial value of slope of the dependent variable.
    finx : float 
        final value of the independent value.

    Returns
    -------
        returns a string contains
                                x : numpy 1darray
                                    contain used x independent values.
                                Y : numpy 1darray
                                    contain correponding values.
                                Z : numpy 1darray
                                    contain correponding values.
                                ye : float
                                    final value of dependent variable to final value.
                                ze : float
                                    final value of slop of the dependent variable. 
    '''
    import numpy as np
    def func1(x,y,z):
        return eval(Function_1)
    def func2(x,y,z):
        return eval(Function_2)
    n=nsteps
    x0=inix
    y0=iniy
    z0=iniz
    xf=finx
    h=(xf-x0)/n
    x=np.linspace(x0,xf,n+1)

    ye=y0
    ze=z0
    Y=[y0]
    Z=[z0]
    for i in range(n):
        k1=h*func1(x[i],ye,ze)
        l1=h*func2(x[i],ye,ze)

        k2=h*func1(x[i]+0.5*h,ye+0.5*k1,ze+0.5*l1)
        l2=h*func2(x[i]+0.5*h,ye+0.5*k1,ze+0.5*l1)

        k3=h*func1(x[i]+0.5*h,ye+0.5*k2,ze+0.5*l2)
        l3=h*func2(x[i]+0.5*h,ye+0.5*k2,ze+0.5*l2)

        k4=h*func1(x[i]+h,ye+k3,ze+l3)
        l4=h*func2(x[i]+h,ye+k3,ze+l3)

        k=(k1+2.0*k2+2.0*k3+k4)/6
        l=(l1+2.0*l2+2.0*l3+l4)/6
        ye=ye+k
        Y.append(ye)
        ze=ze+l
        Z.append(ze)


    return [x,Y,Z,ye,ze]

x,y,z,yf,zf=ODE2('z','(-2*z)-y',nsteps=1000,inix=0,iniy=1,iniz=2,finx=10)
#function must be followed by string.for other detail use : help(runge_kutta)

#ploting:
fig,ax=plt.subplots(nrows=1,ncols=1)

ax.plot(x,y,label='Approx Solution Curve')          #<-solution via runge_kutta
#ax.plot(x,z,label='Approx Solpe-Mag Curve')         #<-extra from upper.
ax.plot(xr,yr,'r--',label='Solution Curve')         #<-solution via hand/paper

#simple ploting style used here:
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Solution')

plt.legend()
plt.show()