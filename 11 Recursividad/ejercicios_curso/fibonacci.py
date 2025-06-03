#calcular el valor de fibonacci en la posicion dada de forma recursiva


def fibonacci_recursivo(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci_recursivo(pos - 1) + fibonacci_recursivo(pos - 2)
    

print(fibonacci_recursivo(7))