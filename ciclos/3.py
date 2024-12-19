# Titulo: Tabla de multiplicar
# Descripcion: Escribe un programa que 
# solicite al usuario un número y luego
#  imprima la tabla de multiplicar
#  de ese número del 1 al 10
# Fecha de creacion: Sabado, 05 de octubre
# Autor: Jose Benito Ondo Ndong

numero = int(input("Ingresa un numero entero:"))

for i in range(1,10):
    print(f"{numero} x {i} = {numero * i}") 