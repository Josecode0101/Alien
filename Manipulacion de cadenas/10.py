

# Titulo: Sustituir vocales por numeros
# Descripcion: Sustituir vocales por números: Crea un programa 
# que reemplace todas las vocales de una cadena con los siguientes números:
# * a = 1
# * e = 2
# * i = 3
# * o = 4
# * u = 5
# Fecha de creacion: Lunes, 30 de septiembre
# Autor: Jose Benito Ondo Ndong

cadena = "AEIOU"
cadena = cadena.lower()
reemplazo1 = cadena.replace("a","1")
reemplazo2 = reemplazo1.replace("e","2")
reemplazo3 = reemplazo2.replace("i","3")
reemplazo4 = reemplazo3.replace("o","4")
reemplazo5 = reemplazo4.replace("u","5")

print("La frase se quedaria de la siguiente manera: ",reemplazo5)