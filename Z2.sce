x = input("Podaj liczbe: ")
disp(x)
i=2
is=1
while(i*i<x)
    if(modulo(x,i)==0) then
        disp("Nie jest pierwsza")
        is=0
        break
    end
    i=i+1
end
if(is&x>1) then
    disp("Jest pierwsza")
end
if(x<2) then
    disp("Nie jest pierwsza")
end
