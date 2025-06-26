


parcial1 = {1, 2, 3, 5, 7, 8, 10}
parcial2 = {2, 4, 5, 6, 8, 9, 10}

ambos_parciales = parcial1 & parcial2  
print(f"1. Aprobaron AMBOS parciales: {ambos_parciales}")
print(f"   Cantidad: {len(ambos_parciales)} estudiantes")

solo_un_parcial = parcial1 ^ parcial2 
print(f"2. Aprobaron SOLO UNO de los parciales: {solo_un_parcial}")
print(f"   Cantidad: {len(solo_un_parcial)} estudiantes")

al_menos_un_parcial = parcial1 | parcial2  
print(f"3. Aprobaron AL MENOS UN parcial: {al_menos_un_parcial}")
print(f"   Cantidad total: {len(al_menos_un_parcial)} estudiantes")
print("-" * 50)
