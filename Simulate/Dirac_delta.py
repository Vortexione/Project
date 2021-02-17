import numpy as np
def Intriga(function,upper,lower):
    """

    Returns Intrigation  of a given function.

    Returns Inrigral value of `function` for certain `upper` and `lower`.

    ..Author:: Suman Mandal

    ..Copyright:: (C) Noatic Digital LLB. All rights reserved.

    ..version :: 1.0.0 

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
sigma=[1,0.5,0.25,0.15,0.1,0.05,0.025]
for i in sigma:
    yf=Intriga('np.exp(-(((2-x)/{})**2)/2)*(x+3)/np.sqrt(2*np.pi*({})**2)'.format(i,i),4,0)
    print('|--|The integral value form {} to {} is'.format(0,4),round(yf,6),'|--|')