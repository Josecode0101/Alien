# Titulo: Palabra mas larga
# Descripcion: Escribe un programa que solicite
#una oración al usuario y determine cuál es la palabra
#más larga en la cadena.
# Fecha de creacion: Lunes, 30 de septiembre
# Autor: Jose Benito Ondo Ndong

texto = (input("Ingrese un texto: "))
separar = texto.split()
contar = max(separar)
print("La palabra mas larga en la frase es: ", contar)
