x = input("Wprowadz liczbe:")
disp("Dzielniki liczby:")
for i=1:x
    if(modulo(x,i)==0) then
        disp(i)
    end
end
