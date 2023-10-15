import openpyxl

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
