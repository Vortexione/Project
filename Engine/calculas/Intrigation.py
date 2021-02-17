from tqdm import tqdm 
import time
import numpy as np



def Intriga(function,upper,lower):
    """
    Copyright (C)  2020  Noatic Digital LLB. All rights reserved.

    Returns Intrigation  of a given function.

    Returns Inrigral value of `function` for certain `upper` and `lower`.

    ..version:: 1.0.2

    ..author :: Suman Mandal

    Parameters
    ----------
    function : string 
        Function followed by string i.e, numpy [accessable] 
    Upper : float
        Upper limit of the intrigation
    Lower : float 
        Lower limit of the intrigation
    Returns
    -------
        The intrigral value of the function.
    """
    n=1001
    x=np.linspace(lower,upper,n)
    def g(x):
        return eval(function)
    h=(upper-lower)/n
    y=0
    for i in range(0,n-2,2):
        y=y+(h/3.0)*(g(x[i])+4.0*g(x[i+1])+g(x[i+2]))
    return y

def eular(Function=None,nsteps=1000,inix=None,iniy=None,finx=None):
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
        ye=ye+h*func(x[i],ye)
        Y.append(ye)
    return [x,Y,ye]

def modi_eular(Function=None,nsteps=1000,inix=None,iniy=None,finx=None):
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
        y1=ye+h*func(x[i],ye)
        ye=ye+(h/2)*(func(x[i],ye)+func(x[i+1],y1))
        Y.append(ye)
    return [x,Y,ye]

def runge(Function=None,nsteps=1000,inix=None,iniy=None,finx=None):
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
        k3=h*func(x[i]+h,ye+k1)
        k4=h*func(x[i]+h,ye+k3)

        k=(k1+4.0*k2+k4)/6
        ye=ye+k
        Y.append(ye)

    return [x,Y,ye]

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

#purpose for observing all methods:
if __name__=='__main__':
    pass


