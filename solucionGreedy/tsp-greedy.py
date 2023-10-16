from get_data import *
from funciones import *

# Se lee el excel con los datos
datos = getDatos('TablaCapitalesEditado.xlsx')

# Se obtienen los nombres de las ciudades utilizando
# los datos leidos del excel 
ciudades = getCiudades(datos)

# Se pasan los datos a un formato mas eficiente
# para su manipulacion  
datosRefinados = refinarDatos(datos)

print('Ciudades disponibles: \n')
print('###################################')
# Se enumeran las ciudades
for  n, ciudad in enumerate(ciudades):
    print(f'{n+1})', '\t', ciudad)
print('###################################\n')

nroCiudad = None

# Se pide que ingrese un numero de ciudad valido
while True:
    try:
        nroCiudad = int(input('Elija una ciudad ingresando el numero (1 - 23): ')) - 1 
        if not 0 <= nroCiudad <= 22:
            raise Exception('Numero no valido')
    except:
        print('\nIngreso de datos no valido, por favor, intente de nuevo.\n')
        continue
    break

# Se obtiene la ciudad de origen correspondiente al
# numero otorgado 
CIUDAD_ORIGEN = ciudades[nroCiudad]

# Se crea la lista de ciudades visitadas y se agrega
# la ciudad de origen a esta 
visitadas = [CIUDAD_ORIGEN]

# Se establece la ciudad de origen como la ciudad actual
ciudadActual = {'ciudad': CIUDAD_ORIGEN, 'distancia': 0}

distanciaRecorrida = 0

print(f'\nCiudad elegida: {CIUDAD_ORIGEN}')

# El ciclo se repetira hasta que se vuelva a la ciudad
# de origen 
while True:

    # Se obtiene la ciudad mas cercana de las que no
    # fueron visitadas y se asigna a la variable
    # ciudadActual  
    ciudadActual = getCiudadMasCercana(datosRefinados[ciudadActual['ciudad']], visitadas, CIUDAD_ORIGEN)

    # Se suma la distancia recorrida para llegar
    # a la ciudad actual 
    distanciaRecorrida += ciudadActual['distancia']

    # Se agrega la ciudad actual a la lista de
    # ciudades visitadas 
    visitadas.append(ciudadActual['ciudad'])

    # Se pregunta si ya se ha vuelto a la ciudad
    # de origen, de ser asi, termina el ciclo, de
    # lo contrario, el viaje continua  
    if ciudadActual['ciudad'] == CIUDAD_ORIGEN:
        break

print('\nRecorrido: \n')
print('###################################')
for ciudad in visitadas:
    print(ciudad)
print('###################################\n')
print(f'\nLa distancia recorrida es {distanciaRecorrida}')
