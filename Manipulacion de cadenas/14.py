# Titulo: Contar consonantes
# Descripcion: Solicita una cadena al usuario 
#y cuenta cuántas consonantes tiene
# Fecha de creacion: Lunes, 30 de septiembre
# Autor: Jose Benito Ondo Ndong

cadena = (input("Ingrese una oracion: "))
contador_consonantes = 0
for caracter in cadena:
    if caracter.lower() in "bcdfghjklmnpqrstvwxyz":
        contador_consonantes +=1
print("Numero de consonantes:",contador_consonantes)