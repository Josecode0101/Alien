# Titulo: Serie Fibonacci
# Descripcion: Escribe un programa que imprima los primeros 15 números de la serie de Fibonacci.
# Fecha de creacion: Sabado, 05 de octubre
# Autor: Jose Benito Ondo


lista = [0,1]

for i in range (0,13):
    lista.append(lista[-1] + lista[-2])
print(f"Los primeros 15 numeros de la serie Fibonacci: {lista}")




