
# Titulo: Eliminar vocales
# Descripcion: Crea un programa que elimine todas
#las vocales de una cadena proporcionada por el usuario.
# Fecha de creacion: Lunes, 30 de septiembre
# Autor: Jose Benito Ondo Ndong

cadena = (input("Ingrese una oracion:"))
espacio = ""
for caracter in cadena:
    if caracter.lower() not in "aeiou":
        espacio += caracter
print("La frase sin vocales:",espacio )