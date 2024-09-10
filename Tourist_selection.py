import numpy as np
import random 
import os
import copy

class Tourist():
    def __init__(self, N, k, A: np.ndarray) :
        self.N=N #Numero total del tourist
        self.k=k #Numero de turista a viaje
        self.A=A #Gusto por ciudades
    def feasible(self, cities):
        c=0
        pos=[]
        for tourist in range(0,self.N):
            for city in range(0,len(self.A[0])):
                if(self.A[tourist][city]>0 and city!=0 and city in cities ):
                    c+=1
                    pos.append(tourist)
                    break
        if(c>=self.k):
            return (True,pos)
        return (False,pos)
    def selection(self,cities ):
        v=self.feasible(cities)
        visited=v[1]
        aux=v[0]
        value=0
        selec=[]
        if(aux):
            for t in visited:
                acum=0
                for i in range(len(self.A[0])):
                    if(i in cities):
                        acum+=self.A[t][i] 
                selec.append((acum,t))
            selec=sorted(selec,reverse=True)
            list_Tourist=[]
            for i in range(0,self.k):
                value+=selec[i][0]
                list_Tourist.append(selec[i][1])
            return (value-self.k,list_Tourist)
        else:
            return (0,[])

