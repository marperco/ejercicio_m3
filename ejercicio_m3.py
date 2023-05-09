# Definimos la lista de nombres
nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

# Definimos una función para separar los nombres en tres grupos
def separar_nombres(nombres):
    magos = []
    cientificos = []
    otros = []
    for nombre in nombres:
        if nombre in ["Harry Houdini", "David Blaine", "Teller"]:
            magos.append(nombre)
        elif nombre in ["Newton", "Hawking", "Einstein"]:
            cientificos.append(nombre)
        else:
            otros.append(nombre)
    return magos, cientificos, otros

# Definimos una función para modificar la lista de magos
def hacer_grandioso(magos):
    for i in range(len(magos)):
        magos[i] = "El gran " + magos[i]

# Definimos una función para imprimir los nombres de una lista
def imprimir_nombres(nombres):
    for nombre in nombres:
        print(nombre)

# Separamos los nombres en tres grupos
magos, cientificos, otros = separar_nombres(nombres)

# Imprimimos la lista completa de nombres
print("Lista completa de nombres:")
imprimir_nombres(nombres)
print()

# Modificamos la lista de magos
hacer_grandioso(magos)

# Imprimimos los nombres de los magos grandiosos
print("Magos grandiosos:")
imprimir_nombres(magos)
print()

# Imprimimos los nombres de los científicos
print("Científicos:")
imprimir_nombres(cientificos)
print()

# Imprimimos los nombres de los otros
print("Otros:")
imprimir_nombres(otros)
