function y=trapez()
    a = 0
    b = 0
    c = 0
    while (a <= 0)|(b<=0)|(c<=0)
        a = input("Podaj bok a")
        b = input("Podaj bok b")
        h = input("Podaj bok h")
    end
    y = ((a+b)*h)/2
endfunction
function y=trojkat()
    a = 0
    h = 0
    while (a <= 0)|(h<=0)
        a = input("Podaj bok a")
        h = input("Podaj bok h")
    end
    y = (a*h)/2
endfunction
function y=kwadrat()
    a = 0
    while (a <= 0)
        a = input("Podaj bok a")
    end
    y = a*a
endfunction
disp("Wybierz wpisujac litere")
disp("Opcja 1: Pole powierzchni trapezu")
disp("Opcja 2: Pole powierzchni kwadratu")
disp("Opcja 3: Pole powierzchni trojkata")
w = input("Wybierz opcje:")
switch w
case 1
    trapez()
    break
case 2
    kwadrat()
    break
case 3
    trojkat()
    break
otherwise
    disp("Wybrano niepoprawna opcje")
end
