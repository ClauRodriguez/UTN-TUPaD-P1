def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    div = a / b if b != 0 else "Division por cero es indefinida"
    operaciones_cont = [suma, resta, multiplicacion, div]
    op = ["suma", "resta", "multiplicacion", "division"]

    for i in range (len(op)):
        print(f"La {op[i]} = {operaciones_cont[i]}")

#Principal
num1 = int(input("Ingrese un numero entero: "))
num2 = int(input("Ingrese un numero entero: "))
operaciones_basicas(num1,num2)