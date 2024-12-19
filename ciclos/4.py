# Titulo: Factorial de un numero
# Descripcion: Escribe un programa que 
# solicite al usuario un número entero y calcule su factorial
# Fecha de creacion: Sabado, 05 de octubre
# Autor: Jose Benito Ondo Ndong

numero = int(input("Ingrese un numero entero: "))
multiplicador = 1
for i in range(1,numero+1):
    if numero>=0:
        multiplicador = multiplicador * i
    # elif numero == 0:
    #     print("El factorial de 0 es: 1")
print(f"El factorial de {numero} es: {multiplicador}")






