
'''Titulo: Un programa que calcula el perimetro de un circulo
Descripcion: Le pide al usuario el radio y la pi viene por defecto y hace la operacion entregando el resultado final
Fecha de creacion: Domingo, 29 de septiembre
Autor: Jose Benito Ondo Ndong'''

pi = 3.141592653589793
radio = int(input("Ingrese el radio:"))
resultado = (radio**2) * pi
redondeado = round(resultado,2)
print("El area del circulo es",redondeado)

