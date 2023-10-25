function w = ilop(a, b)
    w = sqrt(a)*sqrt(b)
endfunction
a = 0
b = 0
while (a < 1)|(b < 1)
    a = input("Podaj liczbe a:")
    b = input("Podaj liczbe b:")
end
disp(ilop(a, b))
