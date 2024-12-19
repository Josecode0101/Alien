# Titulo: Contar caracteres 
# Descripcion: Contar caracteres: Escribe un programa que solicite
# una cadena al usuario y cuente cuántos caracteres tiene,
# excluyendo los espacios
# Fecha de creacion: Lunes, 30 de septiembre
# Autor: Jose Benito Ondo Ndong
#el usuario ingresara una palabra o frase

texto = (input("Escribe una palabra o frase cualquiera: "))
#elimina los espacios
texto_sin_espacios = texto.replace(" ", "")
longitud = len(texto_sin_espacios)
texto_con_comillas = f"'{texto}'"
print ("La palabra o texto:",texto_con_comillas,"tiene",longitud,"caracteres.")
