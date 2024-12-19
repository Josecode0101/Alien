# Titulo: Aprobado o suspenso
# Descripcion:Escribe un programa que 
# solicite al usuario ingresar una 
# calificación (1 - 10) y muestre lo 
# correspondiente según la siguiente tabla:
#sobresaliente: 9-10 -- notable: 7-8 -- aprobado: 5-6 -- suspendido: 0-4.9
# Fecha de creacion: Martes, 01 de octubre
# Autor: Jose Benito Ondo Ndong

nota = float(input("Ingrese su nota: "))
if 0<= nota <=4.9:
    print("Supendido")
elif 5<= nota <=6:
    print("Aprobado")
elif 7<= nota <=8:
    print("Notable")
elif 9<= nota <=10:
    print("Sobresaliente")
else:
    print("ERROR,numero fuera de rango, ingresa tu nota del 1 al 10")