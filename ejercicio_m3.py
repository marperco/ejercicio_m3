# Lista general de nombres
nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]
magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]

# Crear lista de "otros"
otros = list(set(nombres) - set(magos) - set(cientificos))

# Función para modificar la lista de magos, y hacerlos "grandes"
def hacer_grandioso(magos):
    for i in range(len(magos)):
        magos[i] = "El gran " + magos[i]

# Función para imprimir los nombres de una lista
def imprimir_nombres(nombres):
    for nombre in nombres:
        print(nombre)

# Imprimimos la lista completa de nombres
print("Lista completa de nombres:")
imprimir_nombres(nombres)
print()
# input()
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
print()