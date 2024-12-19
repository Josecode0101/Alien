# Titulo: Determinar si es palindromo 
# Descripcion: Palíndromo: Escribe un programa que solicite 
# al usuario una palabra o frase y determine si es 
# un palíndromo (se lee igual hacia adelante y hacia atrás).
# Fecha de creacion: Lunes, 30 de septiembre
# Autor: Jose Benito Ondo Ndong
#el usuario ingresara una palabra o frase

texto = (input("Escriba una frase o palabra:"))

texto_invertido = (texto[::-1])

if texto == texto_invertido:
    print("Es un palindromo")
else:
    print("No es un palindromo")



