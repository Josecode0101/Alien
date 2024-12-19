

# Titulo: Inversion
# Descripcion: Escribir un programa que pregunte al usuario una cantidad 
# a invertir, el interés anual y el número de años, y muestre 
# por pantalla el capital obtenido en la inversión
# Fecha de creacion: Domingo, 29 de septiembre
# Autor: Jose Benito Ondo Ndong

# p : es la inversion inicial
p = int(input("Cuanto desea invertir:"))
#r: es la tasa de inversion anual
r= int(input("Cuanto interes desea ganar en porcentaje:"))
#t : numero de años que dejas la inversion crecer
t = int(input("En cuantos años:"))
resultado = p*(1+r/100)**t
resultado_redondeado = round(resultado,2)
print("El capital obtenido en la inversion es:",resultado_redondeado)

