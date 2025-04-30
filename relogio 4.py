from time import sleep
#crie um programa que exiba todos
#os segundos do primeiro minuto
#exiba no formato hh:mm:ss
h = 0
while h < 24:
    m = 0
    while m < 60:
        s = 0
        while s < 60:
            print(f'{h:02}:{m:02}:{s:02}')
            s += 1
            #sleep(0.1)
        m += 1
    h += 1

        
