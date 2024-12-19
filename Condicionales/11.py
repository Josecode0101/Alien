# Titulo: Multiplo de un numero
# Descripcion: Escribe un programa que solicite
#  al usuario ingresar dos números enteres y determine
#  si el primero es múltiplo del segundo.
# Fecha de creacion: Martes, 01 de octubre
# Autor: Jose Benito Ondo Ndong

numero1 = int(input("Ingrese un numero entero: "))
numero2 = int(input("Ingrese otro numero entero: "))


if numero1 % numero2 == 0:
    print(f"{numero1} es multiplo de {numero2}")
else:
    print(f"{numero1} no es multiplo de {numero2}")