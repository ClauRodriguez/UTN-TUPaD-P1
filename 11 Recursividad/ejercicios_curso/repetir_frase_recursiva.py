#funcion recursiva que reciba un numero y una frase y que la repita el numero de veces ingresado



def repetir_frase(num, frase):
    if num <= 0:  # Se asegura que no haya ejecuciones innecesarias
        return  
    print(frase)
    repetir_frase(num - 1, frase)

frass = input("Ingrese una frase: ")
num = int(input("Ingrese la cantidad de veces a repetir la frase: "))

repetir_frase(num,frass)