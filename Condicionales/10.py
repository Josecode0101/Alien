

# Titulo: Determina si es vocal o consonante
# Descripcion: Escribe un programa que solicite
#  al usuario ingresar un carácter y determine si 
# es una vocal o una consonante. Ignora los 
# caracteres que no sean letras.
# Fecha de creacion: Martes, 01 de octubre
# Autor: Jose Benito Ondo Ndong

caracter = input("Ingrese un caracter: ")
caracter_minuscula = caracter.lower()
vocales = "aeiou"
consonantes = "qwrtypsdfghjklzxcvbnm"

for i in caracter_minuscula:
    if i in vocales:
        print("Es una vocal")
    elif i in consonantes:
        print("Es una consonante")
    else:
        print("No es una vocal ni consonante")