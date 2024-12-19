

# Titulo: Calculo del IMC
# Descripcion: Escribir un programa que pida al usuario su peso
# (en kg) y estatura (en metros), calcule el índice
# de masa corporal y lo almacene en una variable,
# y muestre por pantalla la frase Tu índice de masa
# corporal es **imc** donde **imc** es el índice de masa
# corporal calculado redondeado con dos decimales.
# Fecha de creacion: Domingo, 29 de septiembre
# Autor: Jose Benito Ondo Ndong



peso = float(input("Introduzca su peso en kg:"))
estatura = float(input("Introduzca su altura en en metros:"))
#imc = el peso entre la estatura al cuadrado
imc = (peso / estatura**2)
imc_redondeado = round(imc,2)
print ("Tu indice de masa corporal (IMC) es:",imc_redondeado)