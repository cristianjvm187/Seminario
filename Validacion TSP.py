import itertools
from TSP import greedy_randomized_adaptive_search_procedure
from data import *
#matriz de distancia
import numpy as np

"""
def generar_permutaciones(array):
    return list(itertools.permutations(array))

def fuerza_bruta(tour,d,M):
    permutaciones=generar_permutaciones(tour[1:])
    ans=1e9
    #print(  len(tour[1:]),len(permutaciones))
    for per in permutaciones:
        aux=d[0][per[0]]+d[per[-1]][0]
        for i in range(len(per)-1):
            aux+=d[per[i]][per[i+1]]
        ans=min(ans,aux)
    return ans

#print(d5)
experimento=[]
real=[]
j=0
name=['Data1.csv','Data2.csv','Data3.csv','Data4.csv','Data5.csv']
for d in D:
    real.append(fuerza_bruta([i for i in range(len(d))],d,len(d)))
    alpha=np.linspace(0,1,10)
    lista=[]
    for i in range(len(alpha)):
        aux=[]
        for _ in range(50):
            a= greedy_randomized_adaptive_search_procedure([i for i in range(len(d))],np.array(d),iterations=120,greediness_value=alpha[i])
            aux.append(a[1])
        lista.append(aux)
    np.savetxt(name[j],np.array(lista), delimiter=',', fmt='%d')
    j+=1
    experimento.append(lista)

np.savetxt('real.csv',np.array(real), delimiter=',', fmt='%d')
print(experimento)
#print(generar_permutaciones([ i for i in range(10)]))
"""
tabla=[]
for d in D:
    lista=[]
    for _ in range(100):
        a= greedy_randomized_adaptive_search_procedure([i for i in range(len(d))],np.array(d),iterations=300,greediness_value=0.33)
        lista.append(a[1])
    tabla.append(lista)
tabla=np.array(tabla)
np.savetxt('Experimentacion Gasp.csv',tabla, delimiter=',', fmt='%d')