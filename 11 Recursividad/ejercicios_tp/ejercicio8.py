#Funciones

def contar_digito(numero, digito):
    if numero == 0:
        return 1 if digito == 0 else 0  #en caso de que digito y numero sean 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

#Main

num = int(input("Ingrese un numero entero positivo: "))
dig = int(input("Ingrese un digito a revisar: "))

print(f"En el numero {num} el digito {dig} se repite {contar_digito(num,dig)} veces")