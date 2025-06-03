#Funciones

def fibonacci_recursivo(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci_recursivo(pos - 1) + fibonacci_recursivo(pos - 2)
    

def serie_fibonacci_hastaN(pos):
    print(f"Serie completa hasta la posicion {pos}")
    for i in range(1, pos + 1):
        print(f"Valor de fibonacci en la posicion {i} ---> {fibonacci_recursivo(i)}")



#Main
pos = int(input("Ingrese una posicion a buscar: "))
serie_fibonacci_hastaN(pos)