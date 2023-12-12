import time
print("Stoper. Kliknij Enter, aby rozpoczac. Po rozpoczeciu kliknij Enter, aby zapisac okrazenie i czas\n")
input()
print("Rozpoczeto\n")
start = time.time()
last = start
c = 1

try:
    while True:
        input()
        lap_time = round(time.time() - last, 2)
        total_time = round(time.time() - start, 2)
        lap_info = f"Okrazenie: {c}".ljust(20) + f"Czas calkowity: {total_time}".ljust(30) + f"Czas okrazenia: {lap_time}".ljust(25)
        print(lap_info + "\n")

        last = time.time()
        c += 1

except KeyboardInterrupt:
    print("Zakonczono program")
