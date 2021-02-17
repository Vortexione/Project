from tqdm import tqdm
import time
def jacobi(A=None,B=None,tol=1e-10):
    n=len(B)
    X0=[0 for i in range(n)]
    X=[0 for i in range(n)]
    c=0
    epsi=2*tol
    while (epsi>tol):
        for _,i in zip(tqdm (range(n),desc="Itarating({}).....".format(c+1),ascii=False, ncols=75),range(n)):
            s=B[i]
            epsi=0
            for j in range(n):
                if(j!=i):
                    s=s-A[i][j]*X0[j]
            X[i]=s/A[i][i]
            epsi=epsi+(X[i]-X0[i])**2
            X0[i]=X[i]
            time.sleep(0.01)
        c+=1
    return c,X


