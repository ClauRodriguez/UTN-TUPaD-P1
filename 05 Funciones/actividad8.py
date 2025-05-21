def  calcular_imc(peso, altura):
    imc = peso / altura ** 2
    return round(imc,2)


#Principal
peso = int(input("Ingrese el peso en km: "))
altura = float(input("Ingrese la altura en metros: "))

print(f"Tu IMC es: {calcular_imc(peso, altura)}")