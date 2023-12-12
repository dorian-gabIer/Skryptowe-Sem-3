import time
print("Stoper. Kliknij Enter, aby rozpoczac. Po rozpoczeciu kliknij Enter, aby zapisac okrazenie i czas\n")
input()
print("Rozpoczeto\n")
start = time.time()
last = start
c = 1
try:
    while(1):
        input()
        print("Okrazenie: " + str(c) + "\nCzas calkowity: " + str(round(time.time()-start, 2)) + "\nCzas okrazenia: " + str(round(time.time()-last, 2)) + "\n")
        last = time.time()
        c += 1
except KeyboardInterrupt:
    print("Zakonczono program")
