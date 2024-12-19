# Titulo: Contar palabras
# Descripcion: Escribe un programa que cuente 
#cuántas palabras tiene una cadena introducida por 
#el usuario. 
# Fecha de creacion: Lunes, 30 de septiembre
# Autor: Jose Benito Ondo Ndong

texto_usuario = (input("Introduce un texto: "))
contar_palabras = len(texto_usuario.split())
print("El texto tiene:",contar_palabras,"palabras.")

