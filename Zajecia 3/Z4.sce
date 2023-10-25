function z = funcy2(x, k, a, y)
    z=(cos(x))^k +sin(a*x)
endfunction
a = input("Podaj wartosc a dla funkcji y=(cos(x))^k +sin(a*x):")
k = input("Podaj wartosc k dla funkcji y=(cos(x))^k +sin(a*x)")
clf()
x=[0:100:50]
y=[0:100:50]
z = funcy2(x', k, a, y)
surf(x, y, z)
