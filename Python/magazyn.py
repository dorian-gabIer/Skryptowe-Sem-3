from dataclasses import dataclass
import os.path
@dataclass
class Produkt:
    id: int
    nazwa: str
    cena: float
    sztuki: int
magazyn = []
def dodawanie():
    idexist = 0
    wrongid = 0
    id = int(input("Podaj identyfikator produktu: "))
    if id < 1:
        print("Identyfikator musi byc wiekszy niz 0")
        wrongid = 1
    if wrongid == 0:
        for produkt in magazyn:
            if produkt.id == id:
                print("Produkt o wybranym identyfikatorze juz istnieje")
                idexist=1
                break
    if idexist == 0 and wrongid == 0:
        nazwa = input("Podaj nazwe produktu: ")
        cena = float(input("Podaj cene produktu: "))
        sztuki = int(input("Podaj ilosc dostepnych sztuk produktu: "))
        allok = 1
        if cena < 0:
            print("Cena nie moze byc ujemna")
            allok = 0
        if sztuki < 0:
            print("Ilosc dostepnych sztuk nie moze byc ujemna")
            allok = 0
        if allok == 1:
            magazyn.append(Produkt(id=id, nazwa=nazwa, cena=cena, sztuki=sztuki))

def wyswietlanie():
    for produkt in magazyn:
        print("Identyfikator: " + str(produkt.id) + "\nNazwa: " + produkt.nazwa + "\nCena: " + str(produkt.cena) + "\nIlosc dostepnych sztuk: " + str(produkt.sztuki) + "\n\n")

def usuwanie():
    deleted = 0
    wrongid = 0
    id = int(input("Podaj identyfikator produktu do usuniecia: "))
    if id < 1:
        print("Identyfikator musi byc wiekszy niz 0")
        wrongid = 1
    if wrongid == 0:
        for produkt in magazyn:
            if produkt.id == id:
                magazyn.remove(produkt)
                deleted = 1
                break
    if deleted == 1 and wrongid == 0:
        print("Usunieto produkt o identyfikatorze " + str(id))
    elif deleted == 0 and wrongid == 0:
        print("Nie odnaleziono produktu o identyfikatorze " + str(id))

def aktualizacja_sztuk():
    wrongid = 0
    changed = 0
    id = int(input("Podaj identyfikator produktu: "))
    if id < 1:
        print("Identyfikator musi byc wiekszy niz 0")
        wrongid = 1
    if wrongid == 0:
        sztuki = int(input("Podaj nowa ilosc dostepnych sztuk produktu: "))
    if sztuki < 0:
        print("Ilosc dostepnych sztuk nie moze byc ujemna")
        wrongid = 1
    if wrongid == 0:
        for produkt in magazyn:
            if produkt.id == id:
                produkt.sztuki = sztuki
                changed = 1
                break
    if changed == 1 and wrongid == 0:
        print("Zmieniono ilosc dostepnych sztuk produktu o identyfikatorze " + str(id))
    elif changed == 0 and wrongid == 0:
        print("Nie odnaleziono produktu o identyfikatorze " + str(id))

def sprzedaz():
    wrongid = 0
    sold = 0
    productexist = 0
    id = int(input("Podaj identyfikator produktu: "))
    if id < 1:
        print("Identyfikator musi byc wiekszy niz 0")
        wrongid = 1
    sztuki = int(input("Podaj ilosc sztuk do sprzedazy: "))
    if sztuki < 1:
        print("Ilosc sztuk do sprzedazy musi byc wieksza niz 0")
        wrongid = 1
    if wrongid == 0:
        for produkt in magazyn:
            if(produkt.id == id):
                productexist = 1
                if(produkt.sztuki < sztuki):
                    print("Ilosc sztuk do sprzedazy przekracza ilosc dostepnych")
                else:
                    produkt.sztuki = produkt.sztuki - sztuki
                    sold = 1
                break
    if productexist == 0 and wrongid == 0:
        print("Produkt o podanym identyfikatorze nie istnieje")
    elif sold == 1 and wrongid == 0:
        print("Sprzedano produkt o identyfikatorze " + str(id) + " w " + str(sztuki) + " sztukach za cene rowna " + str(produkt.cena*sztuki))
    else:
        print("Nie sprzedano produktu")

def eksportuj():
    file = open('magazyn.txt', 'w')
    for produkt in magazyn:
        file.write(str(produkt.id)+"\n")
        file.write(produkt.nazwa + "\n")
        file.write(str(produkt.cena) + "\n")
        file.write(str(produkt.sztuki) + "\n")
    file.close()
def zaladuj():
    file_exists = os.path.exists('magazyn.txt')
    if file_exists:
        magazyn = []
        file = open('magazyn.txt', 'r')
        lines = file.readlines()
        id = 0
        nazwa = ""
        cena = 0
        sztuki = 0
        counter = 1
        while(1):
            line = file.readline()
            if not line:
                break
            if counter == 1:
                id = int(line)
            elif counter == 2:
                nazwa = str(line)
            elif counter == 3:
                cena = str(line)
            elif counter == 4:
                sztuki = str(line)
            elif counter == 5:
                magazyn.append(Produkt(id=id, nazwa=nazwa, cena=cena, sztuki=sztuki))
                id = int(line)
                counter = 1
            counter = counter + 1
    else:
        print("Nie istnieje zapisany plik magazynu. Aby zaladowac magazyn musisz go najpierw wyeksportowac")
    if file_exists:
        print("Zaladowano magazyn")

while(1):
    wybor = int(input("Wybierz jedna z opcji wpisujac cyfre: \n1 - Dodawanie produktu\n2 - Wyswietlanie wszystkich produktow\n3 - Usuwanie produktu\n4 - Aktualizacja ilosci produktu\n5 - Sprzedaz produktu\n6 - Wyeksportuj magazyn do pliku\n7 - Zaladuj magazyn z pliku\nWybor: "))
    if wybor == 1:
        dodawanie()
    elif wybor == 2:
        wyswietlanie()
    elif wybor == 3:
        usuwanie()
    elif wybor == 4:
        aktualizacja_sztuk()
    elif wybor == 5:
        sprzedaz()
    elif wybor == 6:
        eksportuj()
    elif wybor == 7:
        zaladuj()
    else:
        print("Niepoprawny wybor")
    print("\n\n")
