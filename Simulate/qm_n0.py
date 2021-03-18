import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.offsetbox import AnnotationBbox,OffsetImage
from matplotlib._png import read_png
#Input Junction[Constant]:
h=1973
m=0.511e+6
e=3.795
a=3
#User Input DashBoard:
 
#How much state in output:
ava=int(input('|!| How much state you want in output?'))
 
#Domain of Wave Function which consist lower value of r(relative distance) and higher value of r.

dom=[1e-10,60]
dom[0]=float(input('|!| lower boundary value of domain : '))
dom[1]=float(input('|!| Upper boundary value of domain : '))
#Step-Size
n=10000
n=int(input('|!| Step size of the calculation : '))
 
r,d=np.linspace(dom[0],dom[1],n,retstep=True)
 
#Formation of Hamiltonian Operator:
 
V=np.zeros((n,n))
K=np.zeros((n,n))
for i in range(n):
    V[i,i]=-((e**2)/r[i])
    K[i,i]=-2
 
for i in range(n-1):
    K[i,i+1]=1
    K[i+1,i]=1
 
H=((-(h**2)/(2*m*d**2))*K)+V

#Eigen Function and Energy Sorting:
E,U=np.linalg.eig(H)

Es=np.sort(E)
for i in range(1,ava+1):
    print('|{}| No  {}s-State Energy : '.format(i-1,i),Es[i],'eV')
Eindex=[]
for i in range(n):
    for j in range(1,ava+1):
        if E[i]==Es[j]:
            Eindex.append(i)
 
style.use('dark_background') 
fig,ax=plt.subplots(ncols=1,nrows=1)
 

for i,j in zip(Eindex,range(ava)):
    ax.plot(r,U[:,i],lw=0.7,label='${}_{}$={}eV'.format('E',j,round(Es[j+1],3)))    
 
#Title label Handle:
ax.set_ylabel('$\Psi$ , Wave Function')
ax.set_xlabel('r in $\AA$ (relative distance)')
ax.set_title('s(l=0)-Wave Solution of ${H}^{1}_{1}$')
ax.yaxis.label.set_color('#3785DF')
ax.xaxis.label.set_color('#3785DF')
ax.title.set_color('#3785DF')

#logo handle:
sloxo=read_png('Slogo.png')
image_box=OffsetImage(sloxo,zoom=0.05)
xy=[1,2]
ab_logo=AnnotationBbox(image_box,xy,xybox=(30.0,-30.0),boxcoords='offset points')
ax.add_artist(ab_logo)
#Grid Handling:
ax.minorticks_on()
ax.axhline(y=0,ls='--',c='#3785DF',lw=0.5)
ax.axvline(x=0,ls='--',c='#3785DF',lw=0.5)
ax.grid(which='major',ls='--',c='#3785DF',lw=0.3)
ax.grid(which='minor',ls=':',c='#3785DF',lw=0.2)
 
#Spin Handling:
 
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
