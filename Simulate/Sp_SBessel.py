#Copyright (C) 2020 Noatic Digital LLB.All rights reserved.
#..Author:: Suman Mandal
import numpy as np
import matplotlib.pyplot as plt


print('---|Sinx Calculation by Bessel Function of order 1/2 of 1st kind of X |---')
n=int(input('Recomendation for n : 50\nNumber of terms in the approximation : '))
xh=float(input('maximum limit of x '))


#Bessel function J1/2(x):
def mod_Bessel(vav,num):
    vav=x;num=n

    
    #gamma function:

    g=np.sqrt(np.pi)
    G=[]
    for i in range(n):
        g=((2*i+1)/2)*g
        G.append(g)   
    
    #Factorial:
    f=1
    F=[1]
    for i in range(1,n):
        f=f*i
        F.append(f)
    #Main Bessel Calculation:
    
    J=0
    for i in range(n):
        J=J+(((-1)**(i))*((x/2)**(2*i)))/(G[i]*F[i])
    P=np.sqrt(x/2)*J
    C=np.sqrt((x*np.pi)/2)*P
    return P,C

x=np.linspace(0,xh,1000)
y1,y2=mod_Bessel(x,n)

#plot:
fig,ax=plt.subplots(nrows=1,ncols=1)
ax.plot(x,y1,'r--',label='J1/2(x)')
ax.plot(x,y2,'m-',label='sin(x) via J1/2(x)')

#simple ploting style used here:
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Fourier Series Graph')
plt.show()

