# Titulo: Imprimir cadena n veces
# Descripcion: Escribe un programa que solicite al
#  usuario una cadena y un número entero, y luego 
# imprima la cadena ese número de veces.
# Fecha de creacion: Sabado, 05 de octubre
# Autor: Jose Benito Ondo Ndong

cadena = input("Esrcibe un texto :")
numero = int(input("Escribe un numero: "))

for i in range(numero):
    print(cadena, end=" ")