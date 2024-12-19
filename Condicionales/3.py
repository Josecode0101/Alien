# Titulo: Verifica la contraseña
# Descripcion:Escribe un programa que 
# solicite al usuario ingresar una 
# contraseña dos veces y verifique si 
# ambas coinciden. Si no coinciden, 
# el programa debe mostrar un mensaje de error
# Fecha de creacion: Martes, 01 de octubre
# Autor: Jose Benito Ondo Ndong

contraseña1 = (input("Ingrese una contraseña: "))
contraseña2 = (input("Vuelva a ingresar la contraseña: "))
if contraseña1 == contraseña2:
    print("Contraseña correcta")
else:
    print("ERROR, las contraseñas no coinciden")