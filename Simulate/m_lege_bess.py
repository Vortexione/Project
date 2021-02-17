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
#from polynomial import legendre,Bessel                       #<--|Errors.

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
def Bessel(varriable,num,term):
    '''
    @Author:Vortex(Suman Mandal)
    
    This typical function oprate Bessel operations.
    Going on three argument :
    1.varriable=x
    2.num=n
    3.term=approxmate terms in series.
    
    '''
    x=varriable;n=num;m=term
    if n==0:
        J0=1
        for i in range(1,m+1,1):
            J0=J0+(((-1)**(i))*((x/2)**(2*i)))/((Fac(i))**2)
        return J0
    if n==1:
        J1=x/2
        for i in range(1,m+1,1):
            J1=J1+(((-1)**(i))*((x/2)**(2*i+1)))/(Fac(i)*Fac(i+1))
        return J1
    else:
        J0=1
        for i in range(1,m+1,1):
            J0=J0+(((-1)**(i))*((x/2)**(2*i)))/((Fac(i))**2)

        J1=x/2
        for i in range(1,m+1,1):
            J1=J1+(((-1)**(i))*((x/2)**(2*i+1)))/(Fac(i)*Fac(i+1))
        
        
        
        for i in range(1,n,1):
            Jn=((2*(i)*J1)/x)-J0
            J0=J1
            J1=Jn
        return Jn
#Factorial Function:
def Fac(num):
    '''
    @Author: Vortex(Suman Mandal)
    
    A common function for factorial operation.
    The Function is controling one argument of
    which is to find the factorial value.
    eg. Fac(4),i.e, 4!=24

    '''
    if num==0:
        return 1
    else:
        f=1
        for i in range(1,num+1,1):
            f=f*i
        return f
#Input:
print('Plotting of Bessel Function Jn(x) ')
n1=int(input('Degree of the Bessel function? '))
m1=int(input('How much Approxmate terms consist in the function J{}(x) '.format(n1)))
xh=float(input('Bessel function will plot for 0<x<? '))
print('Plotting of legendre Function Pn(x) ')
n=int(input('Order of 1st Legendre Function: '))
m=int(input('Order of 2nd Legendre Function: '))

x=np.linspace(0.01,xh,1000)

#Bessel Genarator:
B0=Bessel(x,n1,m1)

#Legendre Genarator:
L0=legendre(x,n)
L1=legendre(x,m)

#Multification of them:
y0=L0*B0
y1=L1*B0

#plot:

fig,ax=plt.subplots(nrows=1,ncols=2,figsize=(10,5))

ax[0].plot(x,L0,'b--',label='P%d(x)'%n)
ax[0].plot(x,L1,'g--',label='P%d(x)'%m)
ax[0].plot(x,B0,'r--',label='J%d(x)'%n1)

ax[1].plot(x,y0,'b--',label='P%d(x)J%d(x)'%(n,n1))
ax[1].plot(x,y1,'g--',label='P%d(x)J%d(x)'%(m,n1))

ax[0].set_xlabel('X')
ax[0].set_ylabel('Y')
ax[0].set_title('Raw Polynomial')

ax[1].set_xlabel('X')
ax[1].set_ylabel('Y')
ax[1].set_title('Multiplicated Graph')

ax[0].set_xlim(0,10)
ax[0].set_ylim(-1,1.3)
ax[1].set_ylim(-2,2.5)

ax[0].legend()
ax[1].legend()
plt.show()

