import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm 
from matplotlib import animation

def ModifyPotential(potential):
    '''
    Manipulate potential in python using numpy.

    parameters:
    -----------
    potential : string
        Input incorrect form of formula.
    
    returns:
    --------
    potential : string
        correct form in python.
    '''
    #replacing exponential & power:
    potential=potential.replace('exp','np.exp')
    potential=potential.replace('^','**')
    
    #replacing mod:
    pot_list=potential.rsplit('|')
    for i in [i for i in range(1,(len(pot_list)-1)*2) if i%2==1]:
        insertion='np.absolute(' if i%4==1 else ')'
        pot_list.insert(i,insertion)
    potential=''.join(pot_list)
    
    #replacing trigonometric :
    potential=potential.replace('cos','np.cos')
    potential=potential.replace('sin','np.sin')
    potential=potential.replace('tan','np.tan')

    return potential

def VerifySyntaxPotential(potential):
    '''
    verify syntax of the potential in origin untils there ia no more syntax error.

    parameters:
    -----------
    
    potential : string
        non-verified potential. 
    
    returns:
    --------
    
    potential : string
        verified potential.
    '''
    i=0
    while i==0:
        try:
            r=0
            eval(potential)
        except:
            potential=input('The potential\'s syntax is incorrect. New Potential : ')
            potential=ModifyPotential(potential)
    return potential

def VerifyLimitsPotential(potential):
    i=1
    while i==1:
        eval_pot=list()
        x=-100
        eval_pot.append(eval(potential))
        x=100
        eval_pot.append(eval(potential))
        eval_pot=np.array(eval_pot)
        x=0
        #if it does not respect the condition ask for a new potential
        if all(eval_pot)>eval(potential):
            Questpotential=input('The potential don\'t seem to be corect.Are you Sure(y/n)?')
            if Questpotential=='n':
                potential=input('New Potential : ')
                potential=ModifyPotential(potential)
                potential=VerifySyntaxPotential(potential)
            elif Questpotential=='y':
                i=0
        else:
            i=0
    return potential

def GetFristEnergyGuess(potentialarray):
    First_E_guess=(1/50000)*(potentialarray.min()+potentialarray.mean())
    return First_E_guess





