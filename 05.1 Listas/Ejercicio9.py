#Dada la lista “compras”
"""
a) Agregar "jugo" a la lista del tercer cliente usando append.
b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
c) Eliminar "pan" de la lista del primer cliente.
d) Imprimir la lista resultante por pantalla

"""
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

#a)
compras[2].append("jugo")

#b)
compras[1][1] = "tallarines"

#c)
compras[0].remove("pan")

#d)
print(compras)

