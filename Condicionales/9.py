
# Titulo: Determina si es escaleno, equilatero o isosceles
# Descripcion: Escribe un programa que solicite al usuario
# ingresar las longitudes de los tres lados de un
# triangulo y determine si el triangulo es equilatero,
# isosceles o escaleno.
# Fecha de creacion: Martes, 01 de octubre
# Autor: Jose Benito Ondo Ndong

lado1 = int(input("Cuanto mide el primer lado: "))
lado2 = int(input("Cuanto mide el segundo lado: "))
lado3 = int(input("Cuanto mide el tercer lado: "))
if lado1 and lado2 == lado3:
    print("El triangulo es equilatero")
elif lado1 == lado2 != lado3:
    print("El triangulo es isosceles")
elif lado1 != lado2 != lado3:
    print("El triangulo es escaleno")