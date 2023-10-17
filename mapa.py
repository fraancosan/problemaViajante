def dibujar_mapa(recorrido:list[str]):

    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg

    # Se carga la imagen del mapa
    mapa = mpimg.imread('C:/Users/Ignacio/Downloads/problemaViajante-main/mapa.png')

    # Muestra la imagen del mapa
    plt.imshow(mapa)
    recorrido_ordenado = sorted(recorrido)
    # Coordenadas de las capitales (latitud y longitud)
    coordenadas_capitales = [(493, 513), (317, 740), (253, 759), (665, 764), (400, 403), (565, 321), (850, 347), (520, 666), (311,852), (1054, 477), (310, 727), (1447, 312), (359, 447), (282, 472), (163, 464), (184, 462), (502, 336), (586, 427), (506, 657), (752, 510), (325, 511), (1599, 340), (941, 554)]
    # Muestra la imagen del mapa
    plt.imshow(mapa)

    # Se agregan las capitales al mapa
    for punto, nombre in zip(coordenadas_capitales, recorrido_ordenado):
        x, y = (punto[1], punto[0]) 
        plt.scatter(x, y, c='black', marker='o', s=10)

    # Conecta las capitales en el orden del recorrido
    for i in range(len(recorrido) - 1):
        capital1 = recorrido[i]
        capital2 = recorrido[i + 1]

        # Se buscan las coordenadas de las capitales a conectar
        indice_capital1 = recorrido_ordenado.index(capital1)
        indice_capital2 = recorrido_ordenado.index(capital2)

        punto1 = coordenadas_capitales[indice_capital1]
        punto2 = coordenadas_capitales[indice_capital2]

        x1, y1 = punto1[1], punto1[0]
        x2, y2 = punto2[1], punto2[0]

        plt.plot([x1, x2], [y1, y2], 'b-')  # Línea que conecta las capitales

    plt.axis('off')  # Para eliminar los ejes
    return{plt.show()}
    
    