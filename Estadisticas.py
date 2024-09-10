import numpy as np
import csv
from statistics import mean,median,stdev,mode
import pandas as pd 

name=['Data1','Data2','Data3','Data4','Data5']


# Ruta al archivo CSV
Informacion=[]
# Abrir y leer el archivo CSV
for i in range(len(name)):
    ruta_archivo = name[i]
    with open(ruta_archivo+'.csv', mode='r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        archivo=[]
        # Iterar sobre las filas del CSV
        for fila in lector_csv:
            l=[int(i) for i in fila]
            #print(l)
            archivo.append(l)
        Informacion.append(archivo)
Informacion=np.array(Informacion)

real=[]
with open('real.csv', mode='r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        #print(fila)
        real.append(int(fila[0]) )

# voy a ir por cada caso prueba
alpha=np.linspace(0,1,10)
col=[ 'alpha '+'{}'.format(round(i,2)) for i in alpha]
Estadisticas=[]
#print(fila)
for i in range(5):
    # voy a iterara por cada alpha
    case=[]
    for a  in range(len(alpha)):
        #example=[]
        #example.append(alpha[a])
        #print(i,a,len(Informacion))
        count = np.count_nonzero( Informacion[i][a]== real[i])
        case.append(count/50)
        #example.append(mode(Informacion[i][a]))
        #print(example)
        #case.append(example)
    Estadisticas.append(case)

Estadisticas=np.array(Estadisticas)

#frequecia relatica ac(50) , moda, media, mediana, desviacion estandar 
table=[]
table.append(pd.DataFrame(Estadisticas,index=name,columns=col))
print(table[0])

Estadisticas=[]
#print(fila)
for i in range(5):
    # voy a iterara por cada alpha
    case=[]
    for a  in range(len(alpha)):
        #example=[]
        #example.append(alpha[a])
        #print(i,a,len(Informacion))
        #count = np.count_nonzero( Informacion[i][a]== real[i])
        x=mean(Informacion[i][a])
        #print(x)
        case.append(x)
        #example.append(mode(Informacion[i][a]))
        #print(example)
        #case.append(example)
    Estadisticas.append(case)

Estadisticas=np.array(Estadisticas)
table.append(pd.DataFrame(Estadisticas,index=name,columns=col))
print(table[1])

Estadisticas=[]
#print(fila)
for i in range(5):
    # voy a iterara por cada alpha
    case=[]
    for a  in range(len(alpha)):
        #example=[]
        #example.append(alpha[a])
        #print(i,a,len(Informacion))
        #count = np.count_nonzero( Informacion[i][a]== real[i])
        x=mode(Informacion[i][a])
        #print(x)
        case.append(x)
        #example.append(mode(Informacion[i][a]))
        #print(example)
        #case.append(example)
    Estadisticas.append(case)

Estadisticas=np.array(Estadisticas)
table.append(pd.DataFrame(Estadisticas,index=name,columns=col))
print(table[2])

Estadisticas=[]
#print(fila)
for i in range(5):
    # voy a iterara por cada alpha
    case=[]
    for a  in range(len(alpha)):
        #example=[]
        #example.append(alpha[a])
        #print(i,a,len(Informacion))
        #count = np.count_nonzero( Informacion[i][a]== real[i])
        x=np.std(Informacion[i][a])
        print(x)
        case.append(round(x,2))
        #example.append(mode(Informacion[i][a]))
        #print(example)
        #case.append(example)
    Estadisticas.append(case)

Estadisticas=np.array(Estadisticas)
table.append(pd.DataFrame(Estadisticas,index=name,columns=col))
print(table[3])


experimento=[]
with open('Experimentacion Gasp'+'.csv', mode='r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    # Iterar sobre las filas del CSV
    for fila in lector_csv:
        l=[int(i) for i in fila]
        #print(l)
        experimento.append(l)
    
experimento=np.array(experimento)
print(experimento)

medidas=['moda ', 'media', 'desviacion', 'frequencia','valor real']
datos=[]
print(len(experimento))
for i in range(len(experimento)):
    exp=[]
    exp.append(mode(experimento[i]))
    exp.append(median(experimento[i]))
    exp.append(np.std(experimento[i]))
    exp.append((np.count_nonzero(experimento[i]==real[i]))/100 )
    exp.append(real[i])
    datos.append(exp)

datos=pd.DataFrame(datos,index=name,columns=medidas)
print(datos)