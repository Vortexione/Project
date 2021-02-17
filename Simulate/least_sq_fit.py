#Copyright (C) 2020 Noatic Digital LLB.All rights reserved.
#..Author:: Suman Mandal
#let introduce us a most common method for finding a equation of linear terms.
#Most commonly known as least square method.
import matplotlib.pyplot as plt
import numpy as np
a1=0.0
b1=0.0
d1=0.0
d2=0.0
#equation of 1st degree curve,i.e. equation of lines.
#y=mx+c -------------------------------------------------------------------(1)
p=[]
q=[]

n=int(input("Sir, enter the pair of the value of the pair"))
print("Caution! 1st parameter is independent and 2nd, dependent varriable")
for i in range(0,n,1):
    x,y=list(map(float,input("enter the data value").split()))

#d1=y1+y2+y3+............
#a1=x1+x2+x3+............
#b1=x1*x1+x2*x2+x3*x3+...
#d2=x1*y1+x2*y2+x3*y3+...

    p.append(x)
    q.append(y)
    a1=a1+x
    d1=d1+y
    d2=d2+x*y
    b1=b1+x*x

#now, eq(1)summetion both side for 0 to n
#d1=m*a1+n*c---------------------------------------------------------------(2)
#now, eq(1) multipy bothside with x and then summetion for 0 to n
#d2=m*b1+c*a1--------------------------------------------------------------(3)

#solution of the eq (2)& (3)
#m=(a1*d1-d2*n)/(a1*a1-b1*n)
#c=(b1*d1-d2*a1)/(n*b1-a1*a1)
    
m=(a1*d1-d2*n)/(a1*a1-b1*n)
c=(b1*d1-d2*a1)/(n*b1-a1*a1)
print("Y=",{m},"X+",{c})
plt.plot(p,q)
x1=np.linspace(0,np.max(x),1000)
y1=m*x1+c
plt.plot(x1,y1)

plt.xlabel("x")
plt.ylabel("Y")
plt.title("linear Least Squared Curve")
plt.show()