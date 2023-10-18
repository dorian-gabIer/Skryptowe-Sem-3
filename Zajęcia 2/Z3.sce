A=[1 2 3; 5 2 1; 6 4 9]
B=[9 8 7; 2 3 2; 3 9 3]
disp("Macierz A:")
disp(A)
disp("Macierz B:")
disp(B)
disp("Opcja nr 1: Wykonaj operacje mnożenia macierzy A i B")
disp("Opcja nr 2: Wykonaj operacje dodawania macierzy A i B")
disp("Opcja nr 3: Wykonaj operacje mnożenia macierzy A i macierzy odwrotnej do macierzy B")
disp("Opcja nr 4: Wykonaj operacje mnożenia wyznacznika macierzy A i macierzy B")
disp("Opcja nr 5: Wykonaj operacje mnożenia wartości iloczynu elementów z drugiej kolumny macierzy A i drugiego wiersza macierzy B")
disp("Opcja nr 6: Zmiana podanego elementu macierzy A lub B (użytkownik podaje numer wiersza i kolumny i wartość)")
w=input("Wybierz opcje wpisujac cyfre:")
while (w<1)|(w>6)
    w=input("Wybierz opcje wpisujac cyfre:")
end
if w==1 then
    disp(A*B)
elseif w==2 then
    disp(A+B)
elseif w==3 then
    disp(A*inv(B))
elseif w==4 then
    disp(det(A)*B)
elseif w==5 then
    ilo=A(1,2)*A(2,2)*A(3,2)
    disp(ilo*B(2,1))
    disp(ilo*B(2,2))
    disp(ilo*B(2,3))
elseif w==6 then
    m=0
    x=0
    y=0
    z=input("Podaj nowa wartość")
    while (m<>1)&(m<>2)
            m=input("Wybierz macierz wpisujac cyfre 1 dla A oraz cyfre 2 dla B")
        end
    while (x<1)|(x>3)
        x=input("Podaj nr wiersza")
    end
    while (y<1)|(y>3)
        y=input("Podaj nr kolumny")
    end
    if m==1 then
        A(x,y) = z
        disp(A)
    elseif m==2 then
        B(x,y)=z
        disp(B)
    end
end
