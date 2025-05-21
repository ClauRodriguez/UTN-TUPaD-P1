#Funciones
def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5 ) + 32

#Principal
temp_celsius = float(input("Ingrese una temperatura en grados celsius: "))

print(f"Usted ingreso {temp_celsius}°C \nSu equivalente en Fahrenheit es {celsius_a_fahrenheit(temp_celsius)}°F")