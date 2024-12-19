# Titulo: Encontrar subcadena
# Descripcion: Encontrar subcadena: Solicita una cadena y una 
#subcadena al usuario, y verifica si la subcadena está 
#presente dentro de la cadena principal.
# Fecha de creacion: Lunes, 30 de septiembre
# Autor: Jose Benito Ondo Ndong

cadena1 = (input("Ingrese la primera cadena: "))
cadena2 = (input("Ingrese las segunda cadena: "))
indice = cadena1.find(cadena2)
if indice != -1:
    print("La subcadena se encuentra en la posicion",indice)
else:
    print("No se encontro la subcadena")
