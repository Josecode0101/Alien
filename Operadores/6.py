
'''Titulo: Entero positivo
Descripcion: Escribir un programa que lea un entero positivo, n, introducido 
por el usuario y después muestre en pantalla la suma de todos los 
enteros desde 1 hasta n. La suma de los n primeros enteros positivos 
pueden ser calculada de la siguiente forma:
$$suma=  (n(n+1))/2$$
Fecha de creacion: Domingo, 29 de septiembre
Autor: Jose Benito Ondo Ndong
'''

numero_n = int(input("Ingrese el entero:"))
suma = numero_n * (numero_n + 1) / 2
print(suma)