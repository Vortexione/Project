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
#from Intrigation import Intriga                              #   |rise
#from polynomial import legendre                              #<--|Errors.

def legendre(varriable,num):
    x=varriable;n=num
    
    if n==0:
        return [1 for i in range(len(x))]
    elif n==1 :
        P1=x
        return P1
    else:
        P0=1
        P1=x
        for i in range(1,n,1):
            r=(((2*i+1)*x*P1)-i*P0)/(i+1)
            P0=P1
            P1=r
        return r
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

#Input DashBoard:
n=int(input('Order of 1st Legendre Function: '))
m=int(input('Order of 2nd Legendre Function: '))
xl=float(input('Lower value of x : '))
xh=float(input('Higher value of x : '))

#Genarator:
x=np.linspace(xl,xh,1000)
y0=legendre(x,n)
y1=legendre(x,m)

#Orthogonality Test:


def Simp1_3(upper,lower,order1,order2):
    n=1000
    x=np.linspace(lower,upper,n)
    
    y0=legendre(x,order1)
    y1=legendre(x,order2)
    y3=y0*y1
    h=(upper-lower)/n
    y=0
    for i in range(0,n-2,2):
        y=y+(h/3.0)*(y3[i]+4.0*y3[i+1]+y3[i+2])
    return y

a=Simp1_3(1,-1,n,m)
print('Orthogonality of the legendre polynomials i.e., P%d(x) and P%d(x): '%(n,m),round(a,2))

#Plot:
fig,ax=plt.subplots(ncols=1,nrows=1)
ax.plot(x,y0,'r--',label='Order:{}'.format(n))
ax.plot(x,y1,'b-',label='Order:{}'.format(m))

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Legendre Polynomial Graph')
ax.legend()
plt.show()
