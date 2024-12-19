# Titulo: Contar vocales
# Descripcion:Crea un programa que cuente cuántas 
# vocales (a, e, i, o, u) hay en una cadena proporcionada
# por el usuario.
# Fecha de creacion: Lunes, 30 de septiembre
# Autor: Jose Benito Ondo Ndong

cadena = input("Ingrese un texto: ")
vocales = "aeiouAEIOU"
contador = 0

for elementos in cadena:
    if elementos in vocales:
        contador +=1
print(contador)



