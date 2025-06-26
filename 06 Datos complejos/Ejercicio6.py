

alumnos = {}
for i in range(3):
    print(f"=== Alumno {i+1} ===")
    nombre = input("Nombre del alumno: ")

    print("Ingresa las 3 notas:")
    notas_lista = []  
    for j in range(3):
        nota = float(input(f"Nota {j+1}: "))
        notas_lista.append(nota)  
    alumnos[nombre] = tuple(notas_lista)
print("=== PROMEDIOS ===")
print("-" * 30)

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: Promedio -> {promedio:.2f}")
