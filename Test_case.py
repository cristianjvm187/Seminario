import numpy as np
import random as ra
import csv

ra.seed(42)

def generar(M,N,lim_inf=1, lim_sup=100):
    A=[]
    d=[]
    v=[0 for i in range(M)]
    T=ra.randint(lim_sup/2, lim_sup*2)

    for i in range(1,M):
        v[i]=ra.randint(lim_inf,lim_sup/2)
    
    for i in range(0,M):
        aux=[]
        for j in range(0,M):
            if(i!=j):
                di=ra.randint(lim_inf,lim_sup)
                aux.append(di)
            else:
                aux.append(0)
        d.append(aux)
    for i in range(0,N):
        aux=[]
        for j in range(0,M):
            di=ra.randint(0,lim_sup/4)
            aux.append(di)

        A.append(aux)

    return (A,d,v,T)
