from mylib import mylib 
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

data= pd.read_csv('../DATA/datos_matricula_carrera_2.1718_feb-jul_2018.csv', encoding='latin1')
data =data.iloc[:-1,:-1]
data=data.drop(['Entidad','Periodo'],axis=1)
reporte_calidad = mylib.dqr(data)
 
 #%%
modelo = pd.value_counts(data['Modelo educativo'])
carreras=pd.value_counts(data['Carrera Profesional Tecnico -Bachiller'])
plantel=pd.value_counts(data['Plantel'])

indice = pd.DataFrame(plantel.index.values)
indice = pd.DataFrame(np.array(indice))

#%% modelos educativos
modelo.plot.bar(title = 'Modelos educativos')
plt.ylabel('# carreras')
plt.xlabel('Modelo')

#%% Matriculas por plantel
indice = np.array(indice)
arr = []
data.index= data.Plantel
for k in indice:
    da= data.loc[k]
    arr.append(sum(da.Matricula))
arr = np.array(arr)
matriuclaxplantel = pd.DataFrame(indice)
matxpl= pd.DataFrame(columns= ['Matricula'], index = matriuclaxplantel)
matxpl['Matricula']= arr

matxpl.plot.bar(title = 'Matriculas x plantel')
plt.ylabel('# Matriculas')
plt.xlabel('Plantel')
#%% matricula x carrera
carrera = pd.DataFrame(data['Carrera Profesional Tecnico -Bachiller'].index.values)

carrera = np.array(carrera)
arr = []
data.index= data['Carrera Profesional Tecnico -Bachiller']
for k in carrera:
    da= data.loc[k]
    arr.append(sum(da.Matricula))
arr = np.array(arr)
matriuclaxcarrera = pd.DataFrame(carrera)
matxca= pd.DataFrame(columns= ['Matricula'], index = matriuclaxcarrera)
matxca['Matricula']= arr
unique_values = pd.DataFrame(columns=['Unique_values'])

matxca.drop_duplicates().plot.bar(title = 'Matriculas x carrera')
plt.ylabel('# Matriculas')
plt.xlabel('Carrera')
#%% carrera x plantel

carreras.plot.bar()
plt.ylabel('se imparte en n planteles')
plt.xlabel('Carrera')




    
