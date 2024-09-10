import numpy as np
import random 
import os
import copy


# Function: Rank Cities by Distance
def ranking(d, tour ,city = 0 ):
    """
        Funcion que va a darme la distancia mas corta
        desde la ciudad i
    """
    rank = np.zeros((len(tour), 2)) # ['Distance', 'City']
    for i in range(0, rank.shape[0]):
        rank[i,0] = d[city,tour[i]]
        rank[i,1] = tour[i]
    rank = rank[rank[:,0].argsort()]
    #print(rank)
    return rank


# Function: Tour Distance
def distance_calc(city_tour,d):
    distance = 0
    for k in range(0, len(city_tour[0])-1):
        m = k + 1
        #print(city_tour[0][k],city_tour[0][m])
        #print(d[city_tour[0][k], city_tour[0][m]])
        distance = distance + d[city_tour[0][k], city_tour[0][m]]            
    #print(distance)
    return distance

# Function: RCL
# 0 totalemente greedy 1 aleatorio totalmente
def restricted_candidate_list(tour,d,greediness_value = 0.5):
    """
        Funcion que me va a crear una ruta
    """
    seed = [[],float("inf")]
    sequence = []
    sequence.append(0)
    count = 1
    aux=copy.deepcopy(tour)
    #print(tour)
    #print("sasas",len(tour))
    for i in range(0, len(tour)):
        count = 1
        rand =random.random() # otra opcion int.from_bytes(os.urandom(8), byteorder = "big") / ((1 << 64) - 1)
        """
            rand va a conter una variable con un numero aleatorio
            que va a decidir si el siguiente numero lo metemos de manera aleatoria o de manera greedy
            Si rand > greedy value -> sera greedy
            sino -> aleatorio
        """
        if (rand > greediness_value and len(sequence) < len(tour)):
            next_city = int(ranking(d, tour,city = sequence[-1] )[count,1])    
            while next_city in sequence:
                count = np.clip(count+1,1,d.shape[0]-1) 
                """
                    Si el i en el tope ya salio debemos ir aumentado 
                    equivalente
                    count+=1
                    cout=min(count , M)
                """ 
                next_city = int(ranking(d, tour,city = sequence[-1] )[count,1])
            sequence.append(next_city)
            aux.remove(next_city)
        elif (rand <= greediness_value and len(sequence) < len(tour)):
            next_city = random.sample(list(aux), 1)[0]
            #Selecciona aleatoriamente
            while next_city in sequence:
                next_city = int(random.sample(list(aux), 1)[0])
            sequence.append(next_city)
            aux.remove(next_city)
    sequence.append(sequence[0])
    seed[0] = sequence
    #print(seed)
    seed[1] = distance_calc(seed,d)
    #print(seed)
    return seed


def local_search_2_opt(tour,d,city_tour):
    tour = copy.deepcopy(city_tour)
    best_route = copy.deepcopy(tour)
    seed = copy.deepcopy(tour)  
    for i in range(1, len(tour[0]) - 2):
        for j in range(i+1, len(tour[0]) - 1):
            best_route[0][i:j] = list(reversed(best_route[0][i:j]))           
            #best_route[0][-1]  = best_route[0][0]                          
            best_route[1] = distance_calc(best_route,d)           
            if (best_route[1] < tour[1]):
                tour[1] = copy.deepcopy(best_route[1])
                for n in range(0, len(tour[0])): 
                    tour[0][n] = best_route[0][n]          
            best_route = copy.deepcopy(seed) 
    return tour

def greedy_randomized_adaptive_search_procedure( tour,d ,iterations = 50, rcl = 25, greediness_value = 0.5):
    count = 0
    #marcando la solucion inicial (Puede no ser factible)
    best_solution = copy.deepcopy(restricted_candidate_list(tour,d ,greediness_value = greediness_value))
    #iterarcions
    while (count < iterations):
        rcl_list = []
        #Construir soluciones
        for i in range(0, rcl):
            rcl_list.append(restricted_candidate_list(tour,d, greediness_value = greediness_value))
        l_candidate=list(range(0,rcl))
        candidate = int(random.sample(l_candidate,1)[0])        
        #Hacer la busqueda local
        city_tour = local_search_2_opt(tour,d,city_tour = rcl_list[candidate])
        while (city_tour[0] != rcl_list[candidate][0]):
            rcl_list[candidate] = copy.deepcopy(city_tour)
            city_tour = local_search_2_opt(tour,d,city_tour = rcl_list[candidate])
        if (city_tour[1] < best_solution[1]):
            best_solution = copy.deepcopy(city_tour) 
        count = count + 1
    return best_solution
