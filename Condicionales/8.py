# Titulo: Calculo del IMC
# Descripcion: Escribe un programa que 
# solicite al usuario su peso (en kilogramos) 
# y su altura (en metros), y calcule su Índice
#  de Masa Corporal (IMC). Luego, determina su 
# categoría según la siguiente tabla: Bajo peso: IMC<18.5
#Peso normal 18.5<= IMC < 24.9 -- Sobrepeso 25 <= IMC < 29.9 -- Obesidad IMC >= 30
# Fecha de creacion: Martes, 01 de octubre
# Autor: Jose Benito Ondo Ndong

masa = float(input("Cual es tu masa corporal en kg: "))
altura = float(input("Cual es tu altura en metros: "))
imc = (masa // altura **2)
print("Tu indice de masa corporal es: ",imc)
if imc <18.5:
    print("Bajo peso")
elif 18.5 <= imc <24.9:
    print("Peso normal")
elif 25<= imc <29.9:
    print("Sobrepeso")
elif imc>30:
    print("Obesidad, considera ir al gymnasio")
