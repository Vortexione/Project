from tqdm import tqdm 
import time  
#forward Difference:
def fin_diff(x=None,order=None):
    """
    Returns Finite Difference of a List for specified order.

    Returns forward finite difference of `x` for sepified order=[`order number`,]

    ..version:: 1.0.1

    Parameters
    ----------
    x : list
        It should be a first dimentional list.
    order : list,optional
        The list of specified order of the difference.
        default= `None` (you will get all orders.)
    
    Returns
    -------
        A list consist of the forward finite differences.
    """
    n=len(x)
    

    X=[[] for i in range(n-1)]
    for _,i in zip(tqdm (range (n-1),desc="Sorting.....",ascii=False, ncols=75),range(n-1)):
        for j in range(n-i-1):
            d=x[j+1]-x[j]
            X[i].append(d)
        x=X[i]
        time.sleep(0.01)
    N=[]
    if order==None:
        return X
    else:
        order=[(i-1) for i in order]
        if(len!=1):
            for i in order:
                N.append(X[i])
            return N
        else:
            return X[order[0]]
#factorial Notation of a polynomial:
def factorial_notation(coe=None,utility=1):
    u=utility
    n=len(coe)
    s=1
    for _,j in zip(tqdm (range(n-1,1,-1),desc="Genarating.....",ascii=False, ncols=75),range(n-1,1,-1)):
        for i in range(1,j):
            coe[i]=coe[i]+u*s*coe[i-1]
        s=s+1
        time.sleep(0.01)
    return coe
#forward Interpolation[Main] Function:
def Forward_Interpoln(x=None,y=None,xf=None):
    """
    Returns Forward Interpolation of a List for specified functional data.

    Returns Forward Interpolation of `xf` list for sepified `x` and it function `y` .

    ..version:: 1.0.2

    Parameters
    ----------
    x : list
        It should be a first dimentional independent list.
    y : list
        It should be a first dimentional  dependent list.
    xf : list
        It should be a first dimentional list of unknown x.
    
    Returns
    -------
        A list consist of Intetpoleted value for the xf .
    """
    h=x[1]-x[0]

    T=[]
    for _,i in zip(tqdm(range(len(xf)),desc="Targeting.....",ascii=False, ncols=75),range(len(xf))):
        t=(xf[i]-x[0])/h
        T.append(t)
        time.sleep(0.01)
    
    S=[]
    y_diff=fin_diff(y)
    for _,j in zip(tqdm(range(len(xf)),desc="Finding Value.....",ascii=False, ncols=75),range(len(xf))):
        k=1   
        s=y[0]
        coe=T[j]
        for i in range(len(y_diff)):
            s=s+coe*y_diff[i][0]
            coe=coe*(T[j]-k)/(k+1)
            k=k+1
        S.append(s)
        time.sleep(0.01)
    return S
#Backward Interpolation[Main] Function:
def Backward_Interpoln(x=None,y=None,xf=None):
    """
    Returns Backward Interpolation of a List for specified functional data.

    Returns Backward Interpolation of `xf` list for sepified `x` and it function `y` .

    ..version:: 1.0.2

    Parameters
    ----------
    x : list
        It should be a first dimentional independent list.
    y : list
        It should be a first dimentional  dependent list.
    xf : list
        It should be a first dimentional list of unknown x.
    
    Returns
    -------
        A list consist of Intetpoleted value for the xf .
    """

    h=x[1]-x[0]

    T=[]
    for _,i in zip(tqdm(range(len(xf)),desc="Targeting.....",ascii=False, ncols=75),range(len(xf))):
        t=(xf[i]-x[-1])/h
        T.append(t)
        time.sleep(0.01)
    S=[]
    y_diff=fin_diff(y)
    for _,j in zip(tqdm(range(len(xf)),desc="Finding Value.....",ascii=False, ncols=75),range(len(xf))):
        k=1   
        s=y[-1]
        coe=T[j]
        for i in range(len(y_diff)):
            s=s+coe*y_diff[i][-1]
            coe=coe*(T[j]+k)/(k+1)
            k=k+1
        S.append(s)
        time.sleep(0.01)
    return S
#Centeral Interpolation:
def Centeral_Interpoln(x=None,y=None,xf=None):
    pass
#Lagrance Interpolation:
def lagrance_Interpoln(x=None,y=None,xf=None):
    n=len(x)
    X=[[]for i in range(len(xf))]
    Y=[]
    for _,k in zip(tqdm(range(len(xf)),desc="Coefficent Calculating.....",ascii=False, ncols=84),range(len(xf))):
        for j in range(n):
            l=1
            for i in range(n):
                if(j!=i):
                    l=l*((xf[k]-x[i])/(x[j]-x[i]))
            X[k].append(l)
        time.sleep(0.01)
    
    for _,i in zip(tqdm(range(len(X)),desc="Finding Value.....",ascii=False, ncols=75),range(len(X))):
        yf=0
        for j in range(n):
            yf=yf+y[j]*X[i][j]
        Y.append(yf)
        time.sleep(0.01)
    return Y
#New Sector:   

 