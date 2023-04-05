import numpy as np
import random
def score(a,b,x,i,j):
    if i==len(x) or j==len(x[0]):
        return
    else:
        if(b[i-1]==a[j-1]):
            x[i][j]=x[i-1][j-1]+5
            score(a,b,x,i+1,j)
            score(a,b,x,i,j+1)
        else:
            c=max(x[i][j-1],x[i-1][j],x[i-1][j-1])
            if(c==0):
                x[i][j]=0
                score(a,b,x,i+1,j)
                score(a,b,x,i,j+1)
            else:
                x[i][j]=c-4
                score(a,b,x,i+1,j)
                score(a,b,x,i,j+1)

def zero(x,i,j):
    if i==len(x):
        return
    x[0][i]=0
    x[i][0]=0
    zero(x,i+1,j)

x=np.empty((17,17))
l=["A","C","T","G"]
a=[random.choice(l,weights=(25,25,25,25)) for i in range(16)]
b=[random.choice(l,weights=(25,25,25,25)) for i in range(16)]

zero(x,0,0)
score(a,b,x,1,1)