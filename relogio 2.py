from time import sleep
#crie um programa que exiba todos
#os segundos do primeiro minuto
#exiba no formato hh:mm:ss
m = 0
while m < 60:
    s = 0
    while s < 60:
            print(f'00:{m:02}:{s:02}')
            s += 1
            #sleep(1)
    m += 1
