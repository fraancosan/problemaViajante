import openpyxl
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

def getDatos(archivo):
  # Abre el archivo Excel
  workbook = openpyxl.load_workbook(archivo)
  # Selecciona una hoja del libro de trabajo
  hoja = workbook['1']

  datos = []
  # Se itera la hoja para obtener todos los datos
  for fila in hoja.iter_rows(values_only=True):
    # Se eliminan los encabezados
    datos.append(fila[1:])
  
  return datos

# Da un formato a los datos de manera que sea mas facil
# trabajar con ellos 
def refinarDatos(datos: list[tuple[int]]) -> dict[dict]:
  datosRefinados: dict[dict] = {}

  # Se obtienen las ciudades
  ciudades = datos[0]

  # A cada ciudad se le asignan las ciudades destino de esta
  for n, ciudad in enumerate(ciudades):
    
    datosCiudad = { ciudades[i]: datos[n+1][i] for i in range(len(ciudades)) }
    # Se crea un diccionario, donde las keys son las ciudades origen
    # y los values son los posibles destinos y sus respectivas distancias al
    # origen  
    datosRefinados.setdefault(ciudad, datosCiudad)
  return datosRefinados


def validarNro(inicial, final, texto):
  while True:
    try:
      nroCiudad = int(input("\n" + texto))
      if not inicial <= nroCiudad <= final:
        raise Exception('Numero no valido')
    except:
      print('\nIngreso de datos no valido, por favor, intente de nuevo.\n')
      continue
    return nroCiudad



def dibujar_mapa(recorrido:list[str]):
  ruta = os.getcwd() + '/mapa.png'
  # Se carga la imagen del mapa
  mapa = mpimg.imread(ruta)

  # Muestra la imagen del mapa
  plt.imshow(mapa)
  # Coordenadas de las capitales (latitud y longitud)
  # Primero Y y luego X
  coordenadas_capitales = [(650,746),(493, 513), (317, 740), (253, 759), (665, 764), (400, 403), (565, 321), (850, 347), (520, 666), (311,852), (1054, 477), (310, 727), (1447, 312), (359, 447), (282, 472), (163, 464), (184, 462), (502, 336), (586, 427), (506, 657), (752, 510), (325, 511), (1599, 340), (941, 554)]
  # Muestra la imagen del mapa
  plt.imshow(mapa)

  # Se agregan las capitales al mapa
  for i in range(len(coordenadas_capitales)):
    x, y = (coordenadas_capitales[i][1], coordenadas_capitales[i][0])
    color = "black"
    if i == recorrido[0]:
      color = "red"
    elif i == recorrido[-1]:
      color = "green"
    plt.scatter(x, y, c=color, marker='o', s=10, zorder=5)

  # Conecta las capitales en el orden del recorrido
  for i in range(len(recorrido) - 1):
    capital1 = recorrido[i]
    capital2 = recorrido[i + 1]

    punto1 = coordenadas_capitales[capital1]
    punto2 = coordenadas_capitales[capital2]

    x1, y1 = punto1[1], punto1[0]
    x2, y2 = punto2[1], punto2[0]

    plt.plot([x1, x2], [y1, y2], 'b-')  # Línea que conecta las capitales

  plt.axis('off')  # Para eliminar los ejes
  return{plt.show()}