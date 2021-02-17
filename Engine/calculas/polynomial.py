#Legendre Function:
def legendre(varriable,num):
    x=varriable;n=num
    
    if n==0:
        return [1 for i in range(len(x))]
    elif n==1 :
        P1=x
        return P1
    else:
        P0=1
        P1=x
        for i in range(1,n,1):
            r=(((2*i+1)*x*P1)-i*P0)/(i+1)
            P0=P1
            P1=r
        return r
#Bessel Function:
def Bessel(varriable,num,term):
    '''
    @Author:Vortex(Suman Mandal)
    
    This typical function oprate Bessel operations.
    Going on three argument :
    1.varriable=x
    2.num=n
    3.term=approxmate terms in series.
    
    '''
    x=varriable;n=num;m=term
    if n==0:
        J0=1
        for i in range(1,m+1,1):
            J0=J0+(((-1)**(i))*((x/2)**(2*i)))/((Fac(i))**2)
        return J0
    if n==1:
        J1=x/2
        for i in range(1,m+1,1):
            J1=J1+(((-1)**(i))*((x/2)**(2*i+1)))/(Fac(i)*Fac(i+1))
        return J1
    else:
        J0=1
        for i in range(1,m+1,1):
            J0=J0+(((-1)**(i))*((x/2)**(2*i)))/((Fac(i))**2)

        J1=x/2
        for i in range(1,m+1,1):
            J1=J1+(((-1)**(i))*((x/2)**(2*i+1)))/(Fac(i)*Fac(i+1))
        
        
        
        for i in range(1,n,1):
            Jn=((2*(i)*J1)/x)-J0
            J0=J1
            J1=Jn
        return Jn
#Factorial Function:
def Fac(num):
    '''
    @Author: Vortex(Suman Mandal)
    
    A common function for factorial operation.
    The Function is controling one argument of
    which is to find the factorial value.
    eg. Fac(4),i.e, 4!=24

    '''
    if num==0:
        return 1
    else:
        f=1
        for i in range(1,num+1,1):
            f=f*i
        return f

def Hermite(x,n):
    H0=1
    H1=2*x
    if(n==0):
        return H0
    if(n==1):
        return H1
    elif(n>=2):
        for i in range(1,n,1):
            Hn=2*x*H1-2*i*H0
            H0=H1
            H1=Hn
        return Hn
def Expo(x,**karg):
    '''
    determine the exponential value of all elements.

    ..version:: 0.0.1

    parameter:
    ---------
    x : float,int,list 
        Input values
    order : int,optional
        Specify the order of the apporximation.
    decimal : int,optional
        Specify the decimal accuracy of the approximation.
    return:
    ------
    out : float,list
        output element-wise exponential of `x`.
    '''
    #param Handling:
    if type(x)==list:
        pass
    else:
        x=[x]
    #Run-time Error:
    try:
        dec=karg['decimal']
    except:
        dec=16
    try:
        n=karg['order']
    except:
        n=19
    #itarator start:
    dn=len(x)
    i=0
    #finding best possible solution:
    while 1/Fac(i)>=0.5*10**(-dec):
        i+=1
    if i>=n:
        i=n
    else:
        pass
    #Solution:
    su=[]
    for k in range(dn):
        mul=1
        s0u=0
        for j in range(i+1):
            s0u=s0u+mul
            mul=mul*x[k]/(j+1)
        su.append(s0u)
    #responses:        
    if len(x)==1:
        return su[0]
    else:
        return su

help(Expo)