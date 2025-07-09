# 6. Simular el comportamiento de un reloj digital, imprimiendo la hora, minutos y segundos de un dÍa desde las 00:00:00 horas hasta las 23:59:59 horas.
for h in range(24):  #Se establecen las 24 horas 
    for m in range(60):  #Se establecen los minutos
        for s in range(60): #Se establecen los segundos
            print(f"{h:02}:{m:02}:{s:02}") #Se imprime acorde al orden del reloj (horas, minutos, segundos) #Se usa el :02 para evitar que los numeros queden con un solo digito (1 = 01)

#Parte desde 00:00:00, pero debido a los limites del terminal solo se puede visualizar por un muy corto periodo de tiempo al iniciar el codigo