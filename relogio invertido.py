from time import sleep


while True:
    h = 24
    while h > 0:
        m = 60
        while m > 0:
            s = 60
            while s > 0:
                print(f'{h:02}:{m:02}:{s:02}')
                s -= 1
            m -= 1
        h -= 1
                      
