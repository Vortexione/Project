import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style 
#Input Junction[Constant] :
h=1973         
h=h*h
m=0.511e+6
e=3.795
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
#User Input Dashboard:
 
#Domain of Wave Function which consist lower value of r(relative distance) and higher value of r.
dom=[1e-10,20]
 
#Step-Size
n=1000
 
#Intial Boundary of energy for which U, Wave function goes to +inf and -inf.
en1 =-12              
en2 =-15
 
#Intialisation of loop :last value of U, Wave function.               
Uf3=1
        
while(abs(Uf3)> 0.01):    #condition to repeat with accuracy
    
    r,U,zU,Uf1,zUf1=ODE2('z','-(2*({}/{}))*({}+(({}*{})/x))*y'.format(m,h,en1,e,e),nsteps=n,inix=dom[0],iniy=0,iniz=1,finx=dom[1])
    r,U,zU,Uf2,zUf2=ODE2('z','-(2*({}/{}))*({}+(({}*{})/x))*y'.format(m,h,en2,e,e),nsteps=n,inix=dom[0],iniy=0,iniz=1,finx=dom[1])
    en3 = 0.5*(en1+en2)
    print(en3)
    r,U,zU,Uf3,zUf3=ODE2('z','-(2*({}/{}))*({}+(({}*{})/x))*y'.format(m,h,en3,e,e),nsteps=n,inix=dom[0],iniy=0,iniz=1,finx=dom[1])
    print(U[-1])
    if (Uf1*Uf3 > 0 ) :
        en1 = en3
    elif(Uf1*Uf3 < 0) :
        en2 = en3
    


style.use('dark_background')   
fig,ax=plt.subplots(ncols=1,nrows=1)  

ax.plot(r,U,c='#36FBB2',lw=0.7,label='E={}eV'.format(round(en3,3)))
#Title label Handle:
ax.set_ylabel('$\Psi$ , Wave Function')
ax.set_xlabel('r in $\AA$ (relative distance)')
ax.set_title('s(l=0)-Wave Solution of ${H}^{1}_{1}$')
ax.yaxis.label.set_color('#3785DF')
ax.xaxis.label.set_color('#3785DF')
ax.title.set_color('#3785DF')
#Grid Handling:
ax.minorticks_on()
ax.axhline(y=0,ls='--',c='#3785DF',lw=0.5)
ax.axvline(x=0,ls='--',c='#3785DF',lw=0.5)
ax.grid(which='major',ls='--',c='#3785DF',lw=0.3)
ax.grid(which='minor',ls=':',c='#3785DF',lw=0.2)

#Spine Handling:

ax.spines['left'].set_color('#3785DF')
ax.spines['right'].set_color('#3785DF')
ax.spines['bottom'].set_color('#3785DF')
ax.spines['top'].set_color('#3785DF')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_linestyle('--')
ax.spines['bottom'].set_linestyle('--')

#ticks Handling:
for label in ax.xaxis.get_ticklabels():
    label.set_color('#3785DF')
for label in ax.yaxis.get_ticklabels():
    label.set_color('#3785DF')
ax.tick_params(axis="x",which='both', direction="out", length=2, width=1, color="#3785DF")
ax.tick_params(axis="y",which='both' ,direction="out", length=2, width=1, color="#3785DF")

#Label Handling:
leg=ax.legend(loc='best',prop={'size':12},edgecolor='#3785DF')
for text in leg.get_texts():
    plt.setp(text, color = '#3785DF')
plt.show()
