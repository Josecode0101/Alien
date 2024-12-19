import time
hora = int(input("Ingresa la hora (0-23): "))
if hora > 23:
    print("La hora ingresada no es valida. El programa finalizara")
else:
    minuto = int(input("Ingresa los minutos (0-59): "))
    segundo = int(input("Ingresa los segundos (0-59): "))
    
    while True:
        print(f"{hora:02}:{minuto:02}:{segundo:02}",end="\r")
        time.sleep(1)
        segundo += 1

        if segundo == 60:
            segundo = 0
            minuto += 1
        if minuto == 60:
            minuto = 0
            hora += 1
        if hora == 24:
            hora = 0
