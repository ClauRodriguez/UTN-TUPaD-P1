"""
4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0."""

num = -1
print("El programa sumara los numeros ingresados hasta que se ingrese un cero\n")
suma = 0
while num != 0:
    num = int(input("Ingrese un numero entero: "))
    suma += num

print(f"La suma de los numeros ingresados es: {suma}")