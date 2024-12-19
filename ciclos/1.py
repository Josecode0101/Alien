# Titulo: Suma de los 100 primeros numeros
# Descripcion: Escribe un programa que sume los primeros 100 números (1 a 100)
# Fecha de creacion: Sabado, 05 de octubre
# Autor: Jose Benito Ondo Ndong

#Usando un bucle:
suma = 0
for numero in range(1,100):
    suma += numero
    print(suma)


#usando la funcion sum:
print(sum(range(1,100)))



