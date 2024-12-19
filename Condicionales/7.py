# Titulo: Descuento sobre una cantidad
# Descripcion:Escribe un programa que 
# solicite al usuario el precio de un 
# producto y la cantidad comprada. Si 
# el total de la compra es mayor a 55 000 XAF
# , aplica un descuento del 10%. Muestra el total a pagar
# Fecha de creacion: Martes, 01 de octubre
# Autor: Jose Benito Ondo Ndong

precio_producto = int(input("Ingrese el precio del producto: "))
cantidad_comprada = int(input("Ingrese las unidades compradas: "))
total_sin_descuento = precio_producto * cantidad_comprada
descuento = (total_sin_descuento * 0.10)
total_con_descuento = (total_sin_descuento - descuento)
if total_sin_descuento>55000:
    print("El total a pagar es: ",total_con_descuento)
else:
    print("El total a pagar es: ",total_sin_descuento)