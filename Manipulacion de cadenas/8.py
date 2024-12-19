# Titulo: Eliminar espacios
# Descripcion: Solicita una cadena al usuario 
#y elimina todos los espacios en blanco que tenga
# Fecha de creacion: Lunes, 30 de septiembre
# Autor: Jose Benito Ondo Ndong

texto_usuario = (input("Ingrese un texto:"))
texto_sin_espacios = texto_usuario.replace(" ","")
print(texto_sin_espacios)