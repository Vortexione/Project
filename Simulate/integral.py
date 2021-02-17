#Copyright (C) 2020 Noatic Digital LLB.All rights reserved.
#..Author:: Suman Mandal

#Importing :
import numpy as np
import matplotlib.pyplot as plt
#import sys                                                   #<--|Ingnore 
#                                                             #   |Those 
#sys.path.insert(0,'E:\Worm-Whole\Project\Engine\calculas')   #   |lines.
#                                                             #   |It
##Importing unofficial Class/method:                          #   |will
#                                                             #   |rise
#from Intrigation import Intriga                              #<--|Errors.
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

xl=float(input('Give the Lower limit of the function : '))
xu=float(input('Give the Upper limit of the function : '))
z=input('Give the function : ')
#give the function : 1/(x**2+1) [A/Q to your Question]

zf=Intriga(z,xu,xl)
print('Value of the Intrigation : ',zf)