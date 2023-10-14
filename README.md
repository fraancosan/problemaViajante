# Problema Viajante Algoritmos Geneticos

## Consigna
- Hallar la ruta de distancia mínima que logre unir todas las capitales de provincias de la República Argentina, utilizando un método exhaustivo. ¿Puede resolver el problema? Justificar de manera teórica.
- Realizar un programa que cuente con un menú con las siguientes opciones:
  - Permitir ingresar una provincia y hallar la ruta de distancia mínima que logre unir todas las capitales de provincias de la República Argentina partiendo de dicha capital utilizando la siguiente heurística: “Desde cada ciudad ir a la ciudad más cercana no visitada.”  Recordar regresar siempre a la ciudad de partida. Presentar un mapa de la República con el recorrido indicado. Además   indicar la ciudad de partida, el recorrido completo y la longitud del trayecto. El programa deberá permitir seleccionar la capital que el usuario desee ingresar como inicio del recorrido.
  - Encontrar el recorrido mínimo para visitar todas las capitales de las provincias de la República Argentina siguiendo la heurística mencionada en el punto a. Deberá mostrar como salida el recorrido y la longitud del trayecto.
  - Hallar la ruta de distancia mínima que logre unir todas las capitales de provincias de la República Argentina, utilizando un algoritmo genético.

## Recomendaciones para el algoritmo:
N = 50 Número de cromosomas de las poblaciones.
M = 200 Cantidad de ciclos.
Cromosomas: permutaciones de 23 números naturales del 1 al 23 donde cada gen es una ciudad.
Las frecuencias de crossover y de mutación quedan a criterio del grupo.
Se deberá usar crossover cíclico.
