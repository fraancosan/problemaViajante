from otros import *
from funciones import *

# Datos iniciales
datosCiudades = getDatos("TablaCapitales.xlsx")
ciudades = datosCiudades[0]

# Menu de opciones
opcion = validarNro(1, 2, 'Elija una opcion (1 - 2): \n1)Elegir ciudad de origen y averiguar mejor ruta por medio de heuristica\n2) Ruta optima por medio de algoritmo genetico\n\n')

# Heuristica
if opcion == 1:
  distanciaRecorrida = 0
  # Se pasan los datos a un formato mas eficiente
  datosRefinados = refinarDatos(datosCiudades)

  print('\nCiudades disponibles:')
  # Se enumeran las ciudades
  for  n, ciudad in enumerate(ciudades):
      print(f'{n+1})', '\t', ciudad)

  # Se pide que ingrese un numero de ciudad valido
  nroCiudad = validarNro(1, 24, 'Elija una ciudad ingresando el numero (1 - 24): ') - 1
  ciudadOrigen = ciudades[nroCiudad]

  # Se crea la lista de ciudades visitadas y se agrega
  # la ciudad de origen a esta 
  visitadas = [ciudadOrigen]

  # Se establece la ciudad de origen como la ciudad actual
  ciudadActual = {'ciudad': ciudadOrigen, 'distancia': 0}

  print(f'\nCiudad elegida: {ciudadOrigen}')

  # El ciclo se repetira hasta que se vuelva a la ciudad de origen 
  while True:
    # Se obtiene la ciudad mas cercana de las que no
    # fueron visitadas y se asigna a la variable
    # ciudadActual  
    ciudadActual = getCiudadMasCercana(datosRefinados[ciudadActual['ciudad']], visitadas, ciudadOrigen)

    # Se suma la distancia recorrida para llegar
    # a la ciudad actual 
    distanciaRecorrida += ciudadActual['distancia']

    # Se agrega la ciudad actual a la lista de
    # ciudades visitadas 
    visitadas.append(ciudadActual['ciudad'])

    # Se pregunta si ya se ha vuelto a la ciudad
    # de origen, de ser asi, termina el ciclo, de
    # lo contrario, el viaje continua  
    if ciudadActual['ciudad'] == ciudadOrigen:
      visitadasNro = getNroVisitadas(visitadas, datosCiudades)
      break

# Algortimo genetico
elif opcion == 2:
  # Datos iniciales
  tamaño = 50
  ciclos = 200
  probMutacion = 0.2
  probCrossover = 0.75

  # Se genera poblacion
  poblacion = generarPoblacion(tamaño, datosCiudades)
  # Se producen todos los ciclos
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

  # Se guarda la distancia recorrida del mejor individuo
  distanciaRecorrida = poblacion[0].objetivo

  # Se guarda el recorrido del mejor individuo
  visitadas = poblacion[0].nombreCiudades
  visitadasNro = poblacion[0].genes


# Se muestra el recorrido
print('\nRecorrido:')
for ciudad in visitadas:
    print(ciudad)
print(f'\nLa distancia recorrida es {distanciaRecorrida} km')
dibujar_mapa(visitadasNro)