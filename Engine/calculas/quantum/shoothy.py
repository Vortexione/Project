import numpy as np
import matplotlib.pyplot as plt
def insolent(func,t_span,y0,mxtep,arg=()):
    '''
    Return Solution of a Given `Funtion` .


    ..version :: 1.0.0 

    parameters
    ----------
    func : callable(y,t,...)
        Computes the derivative of y at t.
    t_span : arraylike
        The initial value point should be the first element of this sequence.
    y0 : arraylike
        Initial values of y.
    finx : float 
        final value of the independent value.

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
    return [x,Z1,Z2]
def newtson(func,t,arg=()):
    wei=0.00001
    der=(func(t+wei,*arg)-func(t,*arg))/wei
    h=func(t,*arg)/der
    while h>=wei:
        der=(func(t+wei,*arg)-func(t,*arg))/wei
        h=func(t,*arg)/der
        t=t-h
    return t
def Intriga(array,depth):
    h=depth
    n=len(array)
    g=array
    y=0
    for i in range(0,n-2,2):
        y=y+(h/3.0)*(g[i]+4.0*g[i+1]+g[i+2])
    return y
def null_detect(array):
    return np.where(np.diff(np.signbit(array)))[0]


def Hydro_wave(y,t,L,E):
    z1,z2=y
    dydt=[z2,(z1*(-2/t))+(((L*(L+1))/t**2)-E)*z1]
    return dydt

def Optimise(E,L):
    sol=insolent(Hydro_wave,domain,init_psi,step,arg=(L,E))[1][-1]
    return sol
def RefineEnergy(E_top,E_bot,Nodes,L):
    tol=1e-12
    ET=E_top
    EB=E_bot
    psi=[1]
    while (abs(EB-ET)>tol or psi[-1]>1e-3):
        print(ET,EB)
        initE=(ET+EB)/2.0
        psi=insolent(Hydro_wave,domain,init_psi,step,arg=(L,initE))[1]
        nodes_ist=len(null_detect(psi))-1
        if nodes_ist>Nodes+1:
            ET=initE
            continue
        if nodes_ist<Nodes-1:
            EB=initE
            continue
        if (nodes_ist%2==0):
            if(psi[-1]<=0.0):
                ET=initE
            else:
                EB=initE
        elif (nodes_ist>0):
            if(psi[-1]<=0.0):
                EB=initE
            else:
                ET=initE
        elif(nodes_ist<0):
            EB=initE
    return EB,ET
def EmploySolute(n,L):
    nodes=n-L-1
    E_Top=30.0
    E_Bot=-9.0
    new_EB,new_EB=RefineEnergy(E_Top,E_Bot,nodes+1,L)
    newE=newtson(Optimise,new_EB,arg=(L,))
    return newE
domain=[1e-18,30]
init_psi=[0,1]
step=1000

N=1
L=0

nodes=np.arange(1,4,1)
for ii in nodes:
    E_new=EmploySolute(ii,L)
    x,psi=insolent(Hydro_wave,domain,init_psi,step,arg=(L,E_new))[0:2]
    dx=x[1]-x[0]
    psi=np.array(psi)
    prob=psi*psi
    norm=np.sqrt(Intriga(prob,dx))
    psi=(1/norm)*psi
    plt.plot(x,psi)
    plt.show()




