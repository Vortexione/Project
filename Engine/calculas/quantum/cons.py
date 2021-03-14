import numpy as np
import scipy
from scipy import integrate
from scipy.optimize import newton
import matplotlib.pyplot as plt

def Schrod_deriv(y,r,L,E):
    du2 = y [0]*(( L *( L +1))/( r **2) - 2./ r - E )
    return [y[1],du2]

def shoot1(E,psi_init,x,L):
    sol=integrate.odeint(Schrod_deriv,psi_init,x,args=(L,E))
    return sol[len(sol)-1][0]

def findZeros(rightbound_vals):
    return np.where(np.diff(np.signbit(rightbound_vals)))[0]

def normalize(output_wavefunc):
    normal=max(output_wavefunc)
    return output_wavefunc*(1/(normal))

def RefineEnergy(Ebot,Etop,Nodes,psi0,x,L):
    tolerance = 1e-12
    ET = Etop
    EB = Ebot
    psi = [1]
    while ( abs(EB-ET)>tolerance or abs(psi[-1])>1e-3):
        print(ET,EB)
        initE = (ET+EB)/2.0
        psi = integrate.odeint(Schrod_deriv,psi0,x,args=(L,initE))[:,0]
        nodes_ist = len(findZeros(psi))-1
        print(nodes_ist)
        print(Nodes)
        print(psi[-1])
        if nodes_ist > Nodes+1:
            print('1st')
            ET = initE
            continue
        if nodes_ist < Nodes - 1:
            print('2nd')
            EB = initE
            continue
        if ( nodes_ist % 2 == 0):
            if (( psi [ len ( psi ) -1] <= 0.0)):
                ET = initE
                print('3rd !!')
            else :
                EB = initE
        elif nodes_ist > 0:
            if (( psi [ len ( psi ) -1] <= 0.0)):
                print('4th')
                EB = initE
            else :
                ET = initE
        elif nodes_ist < 0:
            print('5th')
            EB = initE
    return EB,ET

def ShootingHydrogenAtom ( psi_init_hydro , N , L , x_arr_hydro ):
    nodes = N-L-1 # Number of should be nodes
    E_hydro_top = 30.0 # top boundary energy
    E_hydro_bot = -9.0 # bottom boundary energy
    EBref , ETref =RefineEnergy(E_hydro_bot,E_hydro_top,nodes+1,psi_init_hydro,x_arr_hydro , L)
    Enewton = newton(shoot1,EBref,args=(psi_init_hydro,x_arr_hydro,L))
    EBOT = 0
    ETOP = 0
    return EBOT,ETOP,EBref,ETref,Enewton

L = 0. # angular quantum number
N = 1. # principal quantum number
h_ = 1./200.
x_arr_hydro=np.arange(1e-7,35.0+h_,h_)
# Initial conditions as array
psi_init = np.asarray([0.,1.]) # Init cond for hydrogen
nodes = np.arange(1,4,1)
for ii in nodes:
    EB,ET,Bref,Tref,newtonE=ShootingHydrogenAtom(psi_init,ii,0,x_arr_hydro)
    psiB = integrate.odeint( Schrod_deriv,psi_init,x_arr_hydro,args=(L,Tref,))[:,0]
    print(findZeros(psiB))
    plt.plot(x_arr_hydro,normalize(psiB),'-',linewidth=0.9,label ='wavefunction odeint from ebot')
    plt . show ()
    EB, ET,Bref,Tref,newtonE=ShootingHydrogenAtom(psi_init,2,1,x_arr_hydro)

psiB = integrate.odeint(Schrod_deriv,psi_init,x_arr_hydro,args=(1,Tref,))[:,0]
plt.plot(x_arr_hydro,normalize(psiB),'g:',linewidth= 5,label=  'wavefunction odeint from ebot ')
plt . show ()
