# Titulo: Numero aleatorio
# Descripcion: Escribe un programa que genere 
# un número aleatorio entre 1 y 100 y permita 
# al usuario adivinarlo. El programa debe dar 
# pistas indicando si el número es mayor o menor.
# Fecha de creacion: Sabado, 05 de octubre
# Autor: Jose Benito Ondo Ndong

from random import randint

while True:
        try:
                numero_aleatorio = randint(1,100)
                print("Adivina el numero entre 1 y 100")
                while True:
                        numero_usuario = int(input("Ingresa un numero: "))

                        if numero_usuario < numero_aleatorio:
                                print("El numero es mayor")
                        elif numero_usuario > numero_aleatorio:
                                print("El numero es menor")
                        else:
                                print("Felicidades, acertaste!")
                                break
                        respuesta = input("Quieres volver a intentarlo, si o no?").lower()
                        if respuesta != "si":
                                print("Gracias por jugar")
                                break
        except ValueError:
                print("Introduce un numero entero, no se admiten letras ni decimales")
                                                                                            




