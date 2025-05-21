#Funciones
def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")

#Principal
num = int(input("Ingrese un numero: "))
print(f"Tabla de multiplicar del {num}")
tabla_multiplicar(num)