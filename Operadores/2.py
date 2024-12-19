#Un programa que calcula el perimetro de un circulo
'''Titulo: Un programa que calcula el perimetro de un circulo
Descripcion: Le pide al usuario el diametro y la pi viene por defecto y resuelve la operacion
Fecha de creacion: Domingo, 29 de septiembre
Autor: Jose Benito Ondo Ndong'''

pi = 3.141592653589793
diametro = int(input("Introduzca el diametro:"))
resultado = (pi * diametro)
resultado_redondeado = round(resultado,2)
print("El perimetro del circulo es:",resultado_redondeado)

