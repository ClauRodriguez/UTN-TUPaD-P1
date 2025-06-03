#Funciones

def suma_digitos(n):
    if n < 0:
        return n
    if n < 10:
        return n
    return suma_digitos(n // 10) + (n % 10)



#Main

num = int(input("Ingresa un numero entero positivo: "))
print(f"La suma de sus digitos es: {suma_digitos(num)}")