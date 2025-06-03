#Funciones

def decimal_binario_recursivo(num):
    binario = ""
    if num == 0:
        return "0"
    if num == 1:
        return "1"
    return decimal_binario_recursivo(num // 2) + str(num % 2)
    



#Main

num = int(input("Ingresa un numero entero positivo en base 10: "))
binario = decimal_binario_recursivo(num)

print(f"El binario del numero {num} es --> {binario}")
