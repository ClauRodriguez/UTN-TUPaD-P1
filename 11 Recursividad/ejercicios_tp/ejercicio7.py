#Funciones

def contar_bloques(n):
    if n == 0:
        return 0
    return contar_bloques(n-1) + n



#Main

n_bloques = int(input("INGRESE LA CANTIDAD DE BLOQUES DEL NIVEL MAS BAJO: "))
print(f"La cantidad de bloques que se necesita para construir toda la piramide es de: {contar_bloques(n_bloques)}")