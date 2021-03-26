from tqdm import tqdm
import time
def M_identity(n=None):
    I=[[0 for i in range(n)]for i in range(n)]
    for i in range(n):
        I[i][i]=1
    return I
def M_Interchange(A=None,pre=None,post=None,mode=None):
    m=len(A[0]) #Column
    n=len(A) #Row
    if(mode=='row'):
        for _,i in zip(tqdm (range(m),desc="Interchanging Row {} to {}".format(pre,post),ascii=False, ncols=85),range(m)):
            temp=A[pre][i]
            A[pre][i]=A[post][i]
            A[post][i]=temp
            time.sleep(0.01)
    if(mode=='col'):
        for _,i in zip(tqdm (range(n),desc="Interchanging Col {} to {}".format(pre,post),ascii=False, ncols=85),range(n)):
            temp=A[i][pre]
            A[i][pre]=A[i][post]
            A[i][post]=temp
            time.sleep(0.01)
    return A
def Guas_Jord(A=None):
    n=len(A[0])
    I=M_identity(n)
    for _,p in zip(tqdm (range(n),desc="Inversing...",ascii=False, ncols=75),range(n)):
        if(A[p][p]==0):
            for i in range(p+1,n):   
                if(A[i][p]!=0):
                    M_Interchange(A,p,i,mode='row')
                    M_Interchange(I,p,i,mode='row')
                    break
                #if(A[p][i]!=0):                    #<--Activate When Row Oparation failed and Deactive Col Oparation!!
                #    M_Interchange(A,p,i,mode='col')
                #    M_Interchange(A,p,i,mode='col')
                #    break
        a0=A[p][p]
        for i in range(n):
            A[p][i]=A[p][i]/a0
            I[p][i]=I[p][i]/a0
        for j in range(n):
            a1=A[j][p]
            for k in range(n):
                if(j!=p):
                    A[j][k]=A[j][k]-A[p][k]*a1
                    I[j][k]=I[j][k]-I[p][k]*a1
        
        time.sleep(0.01)
    return I
A= [[8,4,3],[2,1,1],[1,2,1]]   
