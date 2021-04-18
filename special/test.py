import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
#|!|User Interface
xi,xf,n=0,15,1000
ti,tf,tn=0,15,500
an=100
Em=1.5
Hm=1.0
W=1
V=1
K=W/V
#|!|Grapfical Mechanics
x=np.linspace(xi,xf,n)
t=np.linspace(ti,tf,tn)


#|!|Graph Plotter

#|!|Section[0]
fig=plt.figure(
    num='Electromagnetic Wave',figsize=(7.0,5.4),
    facecolor='#404141',edgecolor='#D1FEFE'
)
ax=fig.add_subplot(1,1,1, projection='3d',facecolor='#404141')
#|!|
def inti_func():
    pass

def update_plot(j):
    ax.clear()
    ax.axis(False)
    #|1|Electric Vector:
    Ey=Em*np.zeros(n)
    Ez=Em*np.sin(K*x-W*t[j])
    #|!|Magnetic Vector
    Hy=Hm*np.sin(K*x-W*t[j])
    Hz=Hm*np.zeros(n)
    ax.plot(x,Ey,Ez)
    ax.plot(x,Hy,Hz)
    markerline1, stemlines1, baseline1=ax.stem(x[::an],Ey[::an],Ez[::an],linefmt='grey', markerfmt='D')
    plt.setp(baseline1, 'linewidth', 0)
    markerline1.set_markerfacecolor('none')
    markerline2, stemlines2, baseline2=ax.stem(x[::an],Hy[::an],Hz[::an],orientation='y',linefmt='grey', markerfmt='D')
    plt.setp(baseline2, 'linewidth', 0)
    markerline2.set_markerfacecolor('none')


#|!|Section[1]
#ax.plot(x,Ey,Ez)
#ax.plot(x,Hy,Hz)
#markerline1, stemlines1, baseline1=ax.stem(x[::an],Ey[::an],Ez[::an],linefmt='grey', markerfmt='D')
#plt.setp(baseline1, 'linewidth', 0)
#markerline1.set_markerfacecolor('none')
#markerline2, stemlines2, baseline2=ax.stem(x[::an],Hy[::an],Hz[::an],orientation='y',linefmt='grey', markerfmt='D')
#plt.setp(baseline2, 'linewidth', 0)
#markerline2.set_markerfacecolor('none')
#|!|Section[-1]
EmWave=FuncAnimation(fig,update_plot,frames=np.arange(0,tn,1),init_func=inti_func,interval=20)

EmWave.save('EmWave.mp4',dpi=150,fps=10,writer='ffmpeg')
plt.show()