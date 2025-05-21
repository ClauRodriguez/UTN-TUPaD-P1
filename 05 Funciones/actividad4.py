#Funciones
def calcular_area_circulo(radio):
    return 3.14 * radio ** 2


def calcular_perimetro_circulo(radio):
    return 2*3.14*radio


#Principal
radio = float(input("Ingrese el radio: "))
print(f"El area del circulo es: {calcular_area_circulo(radio)}")
print(f"El perimetro del circulo es: {calcular_perimetro_circulo(radio)}")