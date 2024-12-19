# Titulo: Empiezan con la misma letra
# Descripcion: Comprobar si todas las palabras empiezan con la misma
# letra: Solicita una frase al usuario y determina si todas
# las palabras en la frase comienzan con la misma letra.
# Fecha de creacion: Lunes, 30 de septiembre
# Autor: Jose Benito Ondo Ndong

frase = input("Ingrese una frase: ")
frase_minuscula = frase.lower()
frase_separada = frase_minuscula.split()
primera_letra = frase_separada[0][0]
mismas_letras = True

for palabra in frase_separada:
    if palabra[0] != primera_letra:
        mismas_letras = False
        break
print("Si son iguales dara (True) y si no dara (False): ",mismas_letras)
# if mismas_letras:
#     print("Todas las palabras comienzan con la misma letra")
# else:
#     print("Las palabras no comienzan con la misma letra")


