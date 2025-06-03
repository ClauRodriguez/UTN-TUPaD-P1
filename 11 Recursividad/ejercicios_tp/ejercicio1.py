#Funciones

def factorial_num(num):
    if num == 1:
        return num
    else:
        return num * factorial_num(num - 1)
    
def n_factorial(cant):
    for i in range(1, cant + 1):
        print(f"El factorial de {i} es: {factorial_num(i)}")



#Main

cant = int(input("Ingrese un numero:  "))
n_factorial(cant)
