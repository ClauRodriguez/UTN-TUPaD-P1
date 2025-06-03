#Funciones

def es_palindromo(palabra):
    if len(palabra) <= 1: #primero verifico longitud
        return True
    if palabra[0] != palabra[-1]: #luego verifico extremos
        return False
    return es_palindromo(palabra[1:-1]) #llamada recursiva


#Main

palabra = input("Ingrese una palabra o frase sin espacios: ")
print(es_palindromo(palabra))
    