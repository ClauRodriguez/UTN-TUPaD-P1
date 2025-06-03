def resolver_laberinto(laberinto, x, y, camino):
    #caso base, fuera de los limites
    if x < 0 or y < 0 or x >= len(laberinto) or y >= len(laberinto[0]) or laberinto[x][y] == 1:
        return False

    #agrega la posicion actual al camino
    camino.append((x, y))

    #caso base esquina inferior derecha
    if x == len(laberinto) - 1 and y == len(laberinto[0]) - 1:
        return True
    
    #marcamos el lugar actual para evitar ciclos
    laberinto[x][y] = 1


    #movimiento en las cuatro direcciones
    #izq, der, arriba, abajo
    if (resolver_laberinto(laberinto, x + 1, y, camino) or
        resolver_laberinto(laberinto, x, y + 1, camino) or
        resolver_laberinto(laberinto, x - 1, y, camino) or
        resolver_laberinto(laberinto, x, y - 1, camino)):
        return True
    

    #backtraking si ninguna direccion funciono
    #elimina la posicion actual y desmarca la celda
    camino.pop()
    laberinto[x][y] = 0
    return False


    

laberinto = [
    [0, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0]
]

camino = []


resolver_laberinto(laberinto, 0, 0, camino)

print(camino)



