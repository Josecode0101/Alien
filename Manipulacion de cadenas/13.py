# Titulo: Repeticion de caracteres
# Descripcion: Crea un programa que
#duplique cada carácter de una cadena proporcionada
#por el usuario. Ejemplo: "hola" → "hhoollaa
# Fecha de creacion: Lunes, 30 de septiembre
# Autor: Jose Benito Ondo Ndong

cadena = (input("Ingrese un texto: "))
resultado = ""
for caracter in cadena:
    resultado += caracter * 2
print("El resultado es: ",resultado)
