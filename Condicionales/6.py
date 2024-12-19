# Titulo: Calculadora basica
# Descripcion:Escribe un programa que 
# solicite al usuario ingresar dos 
# números y un operador (+, -, \*, /). 
# Luego, realiza la operación correspondiente 
# y muestra el resultado.
# Fecha de creacion: Martes, 01 de octubre
# Autor: Jose Benito Ondo Ndong

numero1 = int(input("Ingresa un numero: "))
numero2 = int(input("Ingresa un numero: "))
operador = input("Ingresa un oprador: ")
suma = (numero1 + numero2)
resta = (numero1 - numero2)
producto = (numero1 * numero2)
division_entera = (numero1 // numero2)
division_decimal = (numero1 / numero2)
if operador == "+":
    print(suma)
elif operador == "-":
    print(resta)
elif operador == "*":
    print(producto)
elif operador == "//":
    print(division_entera)
elif operador == "/":
    print(division_decimal)