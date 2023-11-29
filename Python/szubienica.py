import os
import random
szubi = ["------\n|     |\n|\n|\n|\n|", "------\n|     |\n|     |\n|\n|\n|", "------\n|     |\n|     |\n|     O\n|\n|", "------\n|     |\n|     |\n|     O\n|     -+-\n|", "------\n|     |\n|     |\n|     O\n|    -+-\n|    /\\"]
slownik = ["KLAWIATURA", "MYSZ", "EKRAN", "PROGRAM", "WISI", "LITERA", "GRA"]
wykorzystane=[]
sukces = 0
slowo = random.choice(list(open('slowa.txt')))
temp=""
przegranalvl=0
print(slowo)
for i in slowo:
    temp += "-"
while sukces == 0 and przegranalvl < 5:
    litera=input("Wprowadz literę: ")
    litera=litera.upper()
    if litera in wykorzystane:
        print("Wykorzystales juz ta litere.")
    elif litera in slowo:
        print("Tak! " + litera + " znajduje się w zagadkowym słowie!")
        print(szubi[przegranalvl])
        wykorzystane.append(litera)
        print("Wykorzystales juz nastepujace litery:")
        print(wykorzystane)
        temp = ""
        for i in slowo:
            if i == litera or i in wykorzystane:
                temp += i
            else:
                temp += "-"
        print("Na razie zagadkowe słowo wygląda tak:")
        print(temp)
    else:
        print("Nie. " + litera + " nie znajduje się w zagadkowym słowie.")
        przegranalvl += 1
        print(szubi[przegranalvl])
        if przegranalvl == 4:
            break
        wykorzystane.append(litera)
        print("Wykorzystales juz nastepujace litery:")
        print(wykorzystane)
        print("Na razie zagadkowe słowo wygląda tak:")
        print(temp)
    if "-" not in temp:
        sukces = 1
if sukces == 1:
    print("Odgadłeś! Ilosc pomylek: " + str(przegranalvl))
else:
    print("Przegrałeś")
print("Zagadkowe słowo to " + slowo)
