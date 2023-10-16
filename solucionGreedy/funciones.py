
# Devuelve el destino no visitado mas cercano
# de una lista de destinos. De encontrarse
# todos los destinos visitados, devuelve el 
# origen y la distancia desde la ciudad en la 
# que se encuentra
def getCiudadMasCercana(destinos: dict, visitadas: list[str], origen: str) -> dict:

    distanciaMinima: int | None = None
    ciudadMasCercana: str | None = None

    # Se recorren los destinos posibles
    for ciudad in destinos:

        # Si la ciudad ya fue visitada se
        # continua con la siguiente 
        if ciudad in visitadas:
            continue

        # Se obtiene la distancia a la que
        # se encuentra la ciudad
        distancia = int(destinos[ciudad])

        # Si aun no hay una distancia minima
        # se asigna una 
        if distanciaMinima is None:
            distanciaMinima = distancia
            ciudadMasCercana = ciudad
            continue

        # Si la distancia a la que se encuentra
        # la ciudad es menor a la minima actual
        # se asigna esta nueva distancia como
        # nuevo minimo y a la ciudad como la 
        # ciudad mas cercana
        if distancia < distanciaMinima:
            distanciaMinima = distancia
            ciudadMasCercana = ciudad

    # Si al haber recorrido todos los destinos
    # no se asigno ninguno, se considera que
    # todos fueron visitados, por lo tanto, se
    # devuelve la ciudad origen y la distancia
    # a la que se encuentra de la ciudad actual
    if ciudadMasCercana is None:

        # Significa que todas las ciudades fueron visitadas
        return {'ciudad': origen, 'distancia': int(destinos[origen])}
    
    return {'ciudad': ciudadMasCercana, 'distancia': distanciaMinima}

