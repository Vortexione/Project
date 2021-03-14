#Required official PyPI Package Here:
import numpy as np
import matplotlib.pyplot as plt
#Required Local Package/method Here:

def ModifyFormula(formula,vav=None):
    '''
    Modify a `formula` for `python` .

    parameter
    ---------
    formula : str
        Input correct mathematical formula and defected formula in python and numpy.
    vav     : str,optional
        Give the varriable of the of formula. Currently support 1-D.
    return
    ------
    formula : str
        Output correct mathematical formula in python and numpy.
    '''
    #Transformation of Exponential
    formula=formula.replace('^','**')
    formula=formula.replace('exp','np.exp')
    #Transformation of Trigonometric
    formula=formula.replace('tan','np.tan') 
    formula=formula.replace('cos','np.cos')
    formula=formula.replace('sin','np.sin')
    #Transformation of Absoulate value
    formula_list=formula.rsplit('|')
    for i in [i for i in range(1,(len(formula_list)-1)*2) if i%2==1]:
        insertion='np.absolute('if i%4==1 else ')'
        formula_list.insert(i,insertion)
    formula=''.join(formula_list)
    #Tranxformation of independent varriable
    if not vav==None:
        san_vav='r'
        formula=formula.replace(vav,san_vav)
    else:
        pass
    return formula

def DiscontFormula(formula,arg=[0]):
    '''
    Modify a function for zero divition error.

    parameter
    ---------
    formula : str
        base formula
    arg : list
        it contain start end step-size i.e., [start,end,step]
    return
    ------
    out : list
        it contain used independent array of the function array and modified arg.
    '''
    dr=0.00001
    ll,ul,n=arg
    inde=np.linspace(ll,ul,n)
    formularray=np.zeros(n)
    for i in range(n):
        try:
            r=inde[i]
            formularray[i]=eval(formula)
            if np.isinf(formularray[i]):
                raise ZeroDivisionError
        except ZeroDivisionError:
            r=inde[i]
            r=r+dr
            formularray[i]=eval(formula)
            inde[i]=r
            if i==0 :
                arg[0]=r
            elif i==n-1:
                arg[1]=r
    return [inde,formularray,arg]

def GetFirstEnergyGuess(formularray):
    '''
    Energy guess between avg value and minimum value.
    '''
    First_E_guess=formularray.min()+0.000002*(formularray.mean()+formularray.min())
    return First_E_guess

def func1(y,t,a,b):
    z=y
    z=[t*y+a+b] 
    return z

def func_2(func,arg=()):
    sol=func(1,2,*arg)
    return sol
a=1
b=0
print(func_2(func1,arg=(a,b)))