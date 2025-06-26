def palabras_unicas(frase):
    frase = set(frase.split())
    return frase

def frecuencia(frase):
    frecuencia = {}
    for palabra in frase.split():
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

    return frecuencia

if __name__ == "__main__":
    frase = input("Ingrese una frase: ")
    frases_unicas = palabras_unicas(frase)
    cant_diccionario = frecuencia(frase)

    print(f"Palabras unicas: {frases_unicas} \n Diccionario: {cant_diccionario}")