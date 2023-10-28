function trapez()
    a = 0
    b = 0
    c = 0
    while (1)
        a = input("Podaj bok a")
        b = input("Podaj bok b")
        h = input("Podaj bok h")
        if (a>0)&(b>0)&(h>0) then
            break
        end
    end
    disp(((a+b)*h)/2)
endfunction
function trojkat()
    a = 0
    h = 0
    while (1)
        a = input("Podaj bok a")
        h = input("Podaj bok h")
        if (a>0)&(h>0) then
            break
        end
    end
    disp((a*h)/2)
endfunction
function kwadrat()
    a = 0
    while (1)
        a = input("Podaj bok a")
        if (a>0) then
            break
        end
    end
    disp(a*a)
endfunction
while(1)
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
end
