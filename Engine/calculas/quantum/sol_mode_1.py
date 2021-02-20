import manage
from Intrigation import ODE2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style 
#Input Junction[Constant] :
h=1973         
h=h*h
m=0.511e+6
e=3.795
 
#User Input Dashboard:
 
#Domain of Wave Function which consist lower value of r(relative distance) and higher value of r.
dom=[1e-10,20]
 
#Step-Size
n=1000
 
#Intial Boundary of energy for which U, Wave function goes to +inf and -inf.
en1 =-1              
en2 =1
 
#Intialisation of loop :last value of U, Wave function.               
Uf3=1
        
while(abs(Uf3)>= 0.0001):    #condition to repeat with accuracy
    
    r,U,zU,Uf1,zUf1=ODE2('z','-(2*({}/{}))*({}+(({}*{})/x))*y'.format(m,h,en1,e,e),nsteps=n,inix=dom[0],iniy=0,iniz=1,finx=dom[1])
    r,U,zU,Uf2,zUf2=ODE2('z','-(2*({}/{}))*({}+(({}*{})/x))*y'.format(m,h,en2,e,e),nsteps=n,inix=dom[0],iniy=0,iniz=1,finx=dom[1])
    en3 = 0.5*(en1+en2)
    print(en3)
    r,U,zU,Uf3,zUf3=ODE2('z','-(2*({}/{}))*({}+(({}*{})/x))*y'.format(m,h,en3,e,e),nsteps=n,inix=dom[0],iniy=0,iniz=1,finx=dom[1])

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
