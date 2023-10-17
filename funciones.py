import random

############################### Heuristica ###############################

# Devuelve el destino no visitado mas cercano de una lista de destinos. De encontrarse
# todos los destinos visitados, devuelve el origen y la distancia desde la ciudad en la 
# que se encuentra
def getCiudadMasCercana(destinos: dict, visitadas: list[str], origen: str) -> dict:
  distanciaMinima: int | None = None
  ciudadMasCercana: str | None = None

  # Se recorren los destinos posibles
  for ciudad in destinos:
    # Si la ciudad ya fue visitada se continua con la siguiente 
    if ciudad in visitadas:
        continue

    # Se obtiene la distancia a la que se encuentra la ciudad
    distancia = int(destinos[ciudad])

    # Si aun no hay una distancia minima se asigna una 
    if distanciaMinima is None:
        distanciaMinima = distancia
        ciudadMasCercana = ciudad
        continue

    # Si la distancia a la que se encuentra la ciudad es menor a la minima actual
    # se asigna esta nueva distancia como nuevo minimo y a la ciudad como la ciudad mas cercana
    if distancia < distanciaMinima:
        distanciaMinima = distancia
        ciudadMasCercana = ciudad

  # Si al haber recorrido todos los destinos no se asigno ninguno, se considera que
  # todos fueron visitados, por lo tanto, se devuelve la ciudad origen y la distancia
  # a la que se encuentra de la ciudad actual
  if ciudadMasCercana is None:
    # Significa que todas las ciudades fueron visitadas
    return {'ciudad': origen, 'distancia': int(destinos[origen])}
  
  return {'ciudad': ciudadMasCercana, 'distancia': distanciaMinima}

def getNroVisitadas(visitadas, datosCiudades):
  nroVisitadas = []
  for i in visitadas:
    nroVisitadas.append(datosCiudades[0].index(i))
  return nroVisitadas

############################### Algoritmos Geneticos ###############################

def generarPoblacion(tamaño, datosCiudades):
  poblacion = []
  for i in range(tamaño):
    poblacion.append(cromosoma(datosCiudades))
  return poblacion

def fitness(poblacion):
  recorridoTotal = 0
  # Se calcula la distancia total de todos los individuos
  for individuo in poblacion:
    recorridoTotal += individuo.objetivo

  for individuo in poblacion:
    fitness = individuo.objetivo / recorridoTotal
    # Se invierte el fitness para que los individuos con menor distancia tengan mayor fitness
    individuo.fitness = 1 - fitness


def mutacion(individuo, datosCiudades, probMutacion):
  if random.random() <= probMutacion:
    # Selecciona dos genes aleatorios
    i = random.randint(0,len(individuo.genes)-1)
    j = random.randint(0,len(individuo.genes)-1)

    # Intercambia los genes
    individuo.genes[i], individuo.genes[j] = individuo.genes[j], individuo.genes[i]
    individuo.actualizar(datosCiudades)

  return individuo


def crossover(individuo1, individuo2, datosCiudades, probCruce):
  def cruce(genes1, genes2):
    # Genero una lista de genes nuevos, en un inicio esta vacia
    genesNuevos = []
    for i in range(len(genes1)):
      genesNuevos.append(None)
    
    genesNuevos[0] = genes1[0] # El primer gen sera el mismo del primer padre
    posicion = 0 # Posicion en la que se encuentra el gen actual
    while True:
      if genes2[posicion] in genesNuevos:
        break
      posicionNueva = encontrarPosicion(genes1, genes2[posicion])
      genesNuevos[posicionNueva] = genes2[posicion]
      posicion = posicionNueva

    # Se rellenan los genes que quedaron vacios
    for i in range(len(genesNuevos)):
      if genesNuevos[i] == None:
        genesNuevos[i] = genes2[i]
    
    return genesNuevos
    
  def encontrarPosicion(genes, numero):
    # Devuelve la posicion del numero en la lista de genes
    for i in range(len(genes)):
      if genes[i] == numero:
        return i
    
  # Se realiza crossover ciclico
  if random.random() <= probCruce:
    individuo1.genes = cruce(individuo1.genes, individuo2.genes)
    individuo2.genes = cruce(individuo2.genes, individuo1.genes)
    individuo1.actualizar(datosCiudades)
    individuo2.actualizar(datosCiudades)

  return individuo1, individuo2


def torneo(poblacion, tamaño):
  poblacionNueva = []
  for i in range(tamaño):
    # Se eligen dos individuos aleatorios
    j = random.randint(0,tamaño-1)
    k = random.randint(0,tamaño-1)
    seleccion = [poblacion[j], poblacion[k]]

    poblacionNueva.append(max(seleccion, key=lambda x: x.fitness))
  
  return poblacionNueva


class cromosoma():
  def __init__(self, datosCiudades):
    self.genes = self.inicializa()
    self.fitness = 0
    # Se generan todos los datos a partir de los genes
    self.actualizar(datosCiudades)

  
  def inicializa(self):
    def genera(lista):
      # Genera un cromosoma aleatorio dentro de ese rango de numeros
      numero = random.randint(0,23)
      # Si el numero ya esta en la lista, se genera otro
      while numero in lista:
        numero = random.randint(0,23)
      return numero

    lista = []
    for i in range(24):
      lista.append(genera(lista))
    return lista

  def funcionObjetivo(self, datosCiudades):
    # Se calcula la distancia total
    distancia = 0
    # Se itera sobre todas las ciudades, excepto la ultima ya que no hay mas ciudades a las que ir
    for i in range(len(self.genes)-1):
      # Se suma la distancia entre las ciudades
      # Dado que la primer fila de datosCiudades es el nombre de las ciudades, se le suma 1
      distancia += int(datosCiudades[self.genes[i]+1][self.genes[i+1]])

    return distancia
  
  def getNombreCiudades(self, datosCiudades):
    # Se crea una lista con los nombres de las ciudades
    lista = []
    for i in self.genes:
      lista.append(datosCiudades[0][i])
    return lista
  
  def actualizar(self, datosCiudades):
    # Establece los datos del cromosoma en funcion del gen
    self.nombreCiudades = self.getNombreCiudades(datosCiudades)
    self.objetivo = self.funcionObjetivo(datosCiudades)

  def __str__(self):
    return f"Recorrido: {self.nombreCiudades} \nDistancia: {self.objetivo}km"