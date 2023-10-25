function w = isprime(x)
    if (x<0)|(x>500) then
        return
    end
    is=1
    i=2
    while(i*i<=x)
        if(modulo(x,i)==0) then
            is=0
            break
        end
        i=i+1
    end
    if is == 1 then
        w = 1
    else 
        w = 0
    end
endfunction
a = input("Podaj liczbe:")
s = isprime(a)
if s==1 then
    disp("Pierwsza")
elseif s==0 then
    disp("Nie pierwsza")
end
