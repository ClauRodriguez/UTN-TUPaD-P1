def segundos_a_horas(segundos):
    return round(segundos / 3600, 2)

#Principal
segundos = int(input("Ingrese los segundos: "))
print(f"Los {segundos} segundos ingresados equivalen a {segundos_a_horas(segundos)} horas")