litery = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def szyfruj(tekst, klucz):
    tekst = tekst.upper()
    wynik=""
    for i in tekst:
        wynik += litery[(litery.find(i) + klucz) % len(litery)]
    return wynik
def odszyfruj(tekst, klucz):
    tekst = tekst.upper()
    wynik=""
    for i in tekst:
        wynik += litery[(litery.find(i) - klucz) % len(litery)]
    return wynik

testszyfr = szyfruj("TEST", 422)
print(testszyfr)
print(odszyfruj(testszyfr, 422))
