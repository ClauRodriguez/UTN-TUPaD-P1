#Funciones
def calcular_promedio(a, b, c):
    return round((a + b + c) / 3, 2)

#Principal
nums = []
for i in range(3):
    nums.append(int(input("Ingrese un numero: ")))

print(f"El promedio de los numeros ingresados es: {calcular_promedio(nums[0],nums[1],nums[-1])}")