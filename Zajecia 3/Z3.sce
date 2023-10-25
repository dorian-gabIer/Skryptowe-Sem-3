function y = funcy(x)
    y=cos(x)+sin(x)
endfunction
xdata = linspace(0, 50, 100)
plot(xdata, funcy(xdata), "o-")
legend("y=cos(x)+sin(x)")
xtitle("Funkcja cos(x)+sin(x)", "oś X", "oś Y")
