'''Titulo: Pago correspondiente
Descripcion: Escribir un programa que pregunte al usuario por 
el número de horas trabajadas y el coste por hora. Después debe
mostrar por pantalla la paga que le corresponde
Fecha de creacion: Domingo, 29 de septiembre
Autor: Jose Benito Ondo Ndong'''

horas = int(input("Cuantas horas trabaja usted al dia:"))
paga_hora = int(input("A cuanto equivale la hora:"))
calculo = (horas*paga_hora)
print("Te corresponde una paga de",calculo,"$")