#Funciones


def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia_recursiva(base, exponente - 1)



#Main

base = int(input("Ingrese un numero: "))
exponente = int(input("Ingrese un exponente: "))
potencia = potencia_recursiva(base, exponente)
print(f"La potencia del numero {base} con exponente {exponente} es ---> {potencia}")