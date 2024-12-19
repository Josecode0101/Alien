# Titulo: Frecuencia de letras
# Descripcion: Escribe un programa que solicite
#una cadena y una letra al usuario y determine cuántas 
#veces aparece esa letra en la cadena.
# Fecha de creacion: Lunes, 30 de septiembre
# Autor: Jose Benito Ondo Ndong

texto = (input("Ingrese un texto: "))
letra = (input("Ingrese una letra: "))
conteo = texto.count(letra)
print(letra,"aparece",conteo,"veces en el texto")

