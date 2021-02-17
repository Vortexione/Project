#Copyright (C) 2020 Noatic Digital LLB.All rights reserved.
#..Author:: Suman Mandal
import numpy as np
import matplotlib.pyplot as plt
x=float(input("Real value of the complex Number : "))
y=float(input("Imaginary value of the complex Number : "))
z=complex(x,y)
t=np.arctan((z.imag)/(z.real))
print('NB: if you want 5th root then give 4. ')
q=int(input("How ?th root of the complex : "))

r=(x**2+y**2)**(1/2)
r=r**(1/(q+1))
p=[]
r1=[]
k=[]
for i in range(q+1):
    a=complex(r*np.cos(((2.0*np.pi*i)+t)/(q+1)),r*np.sin(((2.0*np.pi*i)+t)/(q+1)))
    r1.append(a.real)
    k.append(a.imag)
    p.append(a)
plt.plot(r1,k,'H')
plt.xlabel("Real Axis")
plt.ylabel("Imaginary Axis")
plt.title("Aragand Plane")
plt.grid()
plt.show()
for i in range(q+1):
    print("%sth imaginary root%s= "%(i,z),p[i])

