#sumar valores n de forma recursiva



def suma_recursiva(num):
    if num == 0:
        return 0
    else:
        return num + suma_recursiva(num - 1)


print(suma_recursiva(9))