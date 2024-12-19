# Titulo: Verifica el numero mayor
# Descripcion:Escribe un programa que 
# solicite al usuario ingresar tres 
# números, determine cuál es el mayor 
# entre los tres, cuál es el mayor entre
#  los dos restantes y los muestre en orden descendente
# Fecha de creacion: Martes, 01 de octubre
# Autor: Jose Benito Ondo Ndong

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))
if numero1>numero2 and numero1>numero3:
    print(f"El numero {numero1} es mayor")
elif numero2>numero1 and numero2>numero3:
    print("fEl numero {numero2} es mayor")
elif numero3>numero1 and numero3>numero2:
    print(f"El numero {numero3} es mayor")