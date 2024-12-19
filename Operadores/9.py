
# Titulo: Panaderia
# Descripcion: Una panadería vende barras de pan a 50 XAF cada una.
# El pan que es del día anterior tiene un descuento del 60%.
# Escribir un programa que comience leyendo el número de
# barras vendidas que son del día anterior.
# Después el programa debe mostrar el precio habitual de
# una barra de pan, el descuento que se le hace por no ser
# fresca y el coste final total.
# Fecha de creacion: Domingo, 29 de septiembre
# Autor: Jose Benito Ondo Ndong

# Los precios normales de los panes 50 xaf.
precios_normal= 50

# precio del descuento 60%= 0.6.
Descuento= 0.6
# precios y descuentos
Panes= int(input("El numero de barras vendidas del dia anterior: "))

# Calcular el precio con descuento.
precio_con_descuento= precios_normal*(1-Descuento)

# Calcular el costo total.
costo_total= Panes*precio_con_descuento

# Mostrar los resultados.
print("El precio habitual de una barra de pan: ", precios_normal)
print("El descuento por no ser fresca: ", Descuento*100,"%")
print("El costo total de los panes vendidos es: ",costo_total, "Xaf")