# Titulo: Cuenta de ahorros
# Descripcion: Imagina que acabas de abrir una nueva cuenta de ahorros
# que te ofrece el 4% de interés al año. Estos ahorros debido
# a intereses, que no se cobran hasta finales de año, se te
# añaden al balance final de tu cuenta de ahorros. Escribir
# un programa que comience leyendo la cantidad de dinero
# depositada en la cuenta de ahorros, introducida por el
# usuario. Después el programa debe calcular y mostrar por
# pantalla la cantidad de ahorros tras el primer, segundo
# y tercer años. Redondear cada cantidad a dos decimales.
# Fecha de creacion: Domingo, 29 de septiembre
# Autor: Jose Benito Ondo Ndong

balance = float(input("Cual es el balance de su cuenta:"))
print()
interes0 = 0.04 
interes1 = (balance * interes0 + balance)
interes1_redondeado = round(interes1,2)
print("-Estos son los ahorros del 1er año:",interes1_redondeado,"xaf")
print()
interes2 = (interes1 * interes0 + interes1)
interes2_redondeado = round(interes2,2)
print("-Estos son los ahorros del 2do año:",interes2_redondeado, "xaf")
print()
interes3 = (interes2 * interes0 + interes2)
interes3_redondeado = round(interes3,2)
print("-Estos son los ahorros del 3er año:",interes3_redondeado, "xaf")




