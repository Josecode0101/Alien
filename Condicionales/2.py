# Titulo: Par o impar
# Descripcion: Escribe un programa que 
# solicite al usuario ingresar un número
# entero y determine si es par o impar
# Fecha de creacion: Martes, 01 de octubre
# Autor: Jose Benito Ondo Ndong

numero = int(input("Introduce un numero: "))
if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")