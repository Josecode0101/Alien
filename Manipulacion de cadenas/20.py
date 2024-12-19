'''Comparar longitud de cadenas: Crea un programa
que tome dos cadenas e indique cuál de las dos tiene
más caracteres, o si ambas tienen la misma longitud.'''
# Titulo: Mayor caracteres
# Descripcion: Comparar longitud de cadenas: Crea un programa
# que tome dos cadenas e indique cuál de las dos tiene
# más caracteres, o si ambas tienen la misma longitud
# Fecha de creacion: Lunes, 30 de septiembre
# Autor: Jose Benito Ondo Ndong

cadena1 = (input("Ingrese una oracion: "))
cadena2 = (input("Ingrese otra oracion: "))
if cadena1 > cadena2:
    print("La primera oracion tiene mas caracteres ")
elif cadena2 > cadena1:
    print("La segunda oracion tiene mas caracteres")
elif cadena1 == cadena2:
    print("Tienen la misma longitud")