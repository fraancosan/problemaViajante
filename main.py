from excel import *
from funciones import *

# Datos iniciales
datosCiudades = getDatos("TablaCapitales.xlsx")
tamaño = 50
ciclos = 200
probMutacion = 0.2
probCrossover = 0.7


poblacion = generarPoblacion(tamaño, datosCiudades)

print(max(poblacion, key=lambda x: x.objetivo).objetivo)

for nroCiclo in range(1, ciclos+1):
  # Se calcula el fitness de toda la poblacion
  fitness(poblacion)
  # Se realiza seleccion por torneo
  poblacion = torneo(poblacion, tamaño)
  
  # Crossover
  for i in range(0, tamaño, 2):
    poblacion[i], poblacion[i+1] = crossover(poblacion[i], poblacion[i+1], datosCiudades, probCrossover)
  
  # Mutacion
  for i in range(tamaño):
    poblacion[i] = mutacion(poblacion[i], datosCiudades, probMutacion)

# Se ordena la poblacion de menor a mayor
poblacion.sort(key=lambda x: x.objetivo)
#for individuo in poblacion:
#  print(individuo.objetivo)

print(poblacion[0])