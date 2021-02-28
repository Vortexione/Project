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
    if vav==None:
        pass
    else:
        san_vav='r'
        formula=formula.replace(vav,san_vav)
    return formula

