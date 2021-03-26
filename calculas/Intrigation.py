#..Author:: Suman Mandal
import numpy as np



def Intrian(func,t_span,arg=()):
    """

    Returns Intrigation  of a given function.

    Returns Inrigral value of `function` for certain range.

    parameters
    ----------
    func : callable y(t,...)
        function for the intrigation
    t_span : list
        integral range
    arg : tuple
        if there was any extra argument to the function.

    returns
    -------
    output : float   
        The intrigral value of the function.
    """
    n=1001
    x,h=np.linspace(t_span[0],t_span[1],n,retstep=True)
    y=0
    for i in range(0,n-2,2):
        y=y+(h/3.0)*(func(x[i],*arg)+4.0*func(x[i+1],*arg)+func(x[i+2],*arg))
    return y

def eular(Function=None,nsteps=1000,inix=None,iniy=None,finx=None):
    '''
    Return Solution of a Given `Funtion` .

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
        ye=ye+h*func(x[i],ye)
        Y.append(ye)
    return [x,Y,ye]

def modi_eular(Function=None,nsteps=1000,inix=None,iniy=None,finx=None):
    '''
    Return Solution of a Given `Funtion` .

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
        y1=ye+h*func(x[i],ye)
        ye=ye+(h/2)*(func(x[i],ye)+func(x[i+1],y1))
        Y.append(ye)
    return [x,Y,ye]

def runge(Function=None,nsteps=1000,inix=None,iniy=None,finx=None):
    '''
    Return Solution of a Given `Funtion` .

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
        k3=h*func(x[i]+h,ye+k1)
        k4=h*func(x[i]+h,ye+k3)

        k=(k1+4.0*k2+k4)/6
        ye=ye+k
        Y.append(ye)

    return [x,Y,ye]

def runge_kutta(Function=None,nsteps=1000,inix=None,iniy=None,finx=None):
    '''
    Return Solution of a Given `Funtion` .

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

def ODE2(Function_1=None,Function_2=None,nsteps=1000,inix=None,iniy=None,iniz=None,finx=None):
    '''
    Return Solution of a Given `Funtion` .

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

def odeint(func,t_span,y0,mxtep,arg=(),meta=False):
    '''
    Return Solution of a Given `Funtion` .

    parameters
    ----------
    func : callable(y,t,...)
        Computes the derivative of y at t.
    t_span : arraylike
        The initial value point should be the first element of this sequence.
    y0 : arraylike
        Initial values of y.
    mxtep : int
        Use in step determination.
    arg : tuple
        extra data to pass in function.
    meta : optional,False
        return all data used in [x,Z1,Z2]
    Returns
    -------
    Output : arraylike
        Contain solution of the ode.
    '''
    n=mxtep
    x0,xf=t_span
    h=(xf-x0)/n
    x=np.linspace(x0,xf,n+1)
    z10,z20=y0
    z1e=z10
    z2e=z20
    Z1=[z10]
    Z2=[z20]
    for i in range(n):
        k1,l1=func([z1e,z2e],x[i],*arg)
        k1,l1=h*k1,h*l1
        k2,l2=func([(z1e+0.5*k1),(z2e+0.5*l1)],x[i]+0.5*h,*arg)
        k2,l2=h*k2,h*l2
        k3,l3=func([(z1e+0.5*k2),(z2e+0.5*l2)],x[i]+0.5*h,*arg)
        k3,l3=h*k3,h*l3
        k4,l4=func([(z1e+k3),(z2e+l3)],x[i]+h,*arg)
        k4,l4=h*k4,h*l4

        k=(k1+2.0*k2+2.0*k3+k4)/6
        l=(l1+2.0*l2+2.0*l3+l4)/6
        z1e=z1e+k
        Z1.append(z1e)
        z2e=z2e+l
        Z2.append(z2e)
    if meta==False:
        return Z1
    else:
        return [x,Z1,Z2]

#purpose for observing all methods:
if __name__=='__main__':
    pass


