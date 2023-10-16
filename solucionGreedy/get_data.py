from openpyxl import *

# Devuelve los datos encontrados en un
# excel en formato de lista  
def getDatos(archivo: str) -> list[tuple[int]]:
  # Abre el archivo Excel
  workbook = load_workbook(archivo)

  # Selecciona una hoja del libro de trabajo
  hoja = workbook['Sheet1']

  datos: list[tuple[int]] = []

  # Se itera la hoja para obtener todos los datos
  for fila in hoja.iter_rows(values_only=True):

    # No se agregan filas que no contengan datos
    if not any(fila[1:24]): continue

    # Se eliminan los encabezados
    datos.append(fila[1:24])
  
  return datos

# Devuelve una lista con los nombres de las ciudades
# encontradas en la lista de datos proveninte del excel 
def getCiudades(datos: list[tuple[int]]) -> list[str]: 

  return list(datos[0])

# Da un formato a los datos de manera que sea mas facil
# trabajar con ellos 
def refinarDatos(datos: list[tuple[int]]) -> dict[dict]:

  datosRefinados: dict[dict] = {}

  # Se obtienen las ciudades
  ciudades = getCiudades(datos)

  # A cada ciudad se le asignan las ciudades destino de esta
  for n, ciudad in enumerate(ciudades):
    
    datosCiudad = { ciudades[i]: datos[n+1][i] for i in range(len(ciudades)) }
    
    # Se crea un diccionario, donde las keys son las ciudades origen
    # y los values son los posibles destinos y sus respectivas distancias al
    # origen  
    datosRefinados.setdefault(ciudad, datosCiudad)

  return datosRefinados