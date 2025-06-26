


def crear_agenda():
    contactos = {}
    for i in range(5):
        nombre = input("Ingrese el nombre del contacto: ")
        numero = int(input(" Ingrese su numero telefonico: "))
        contactos[nombre] = numero
    return contactos

def buscar_contacto(nombre, contactos):
    if nombre in contactos:
        return f"Para el contacto {nombre} se encontro el siguiente numero: {contactos[nombre]}"
    else:
        return "No se encontraron contactos con ese nombre"
    

if __name__ == "__main__":
    contactos = crear_agenda()
    nombre = input("Ingrese el nombre del contacto a buscar: ")
    print(buscar_contacto(nombre, contactos))