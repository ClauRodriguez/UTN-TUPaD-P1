# Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.
dobles = []

for i in range(5, 16, 5):
    dobles.append(i * 2)
print(dobles)