a = input("Podaj dlugosc 1 boku: ")
b = input("Podaj dlugosc 2 boku: ")
c = input("Podaj dlugosc 3 boku: ")
if (a + b > c)&(b + c > a)&(a + c > b)&(a>0)&(b>0)&(c>0) then
    disp("Mozna zbudowac trojkat")
else
    disp("Nie mozna zbudowac trojkata")
end
