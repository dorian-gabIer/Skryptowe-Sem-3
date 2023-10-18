A=[2 1 3; 4 7 6; 5 8 4]
B=[8 2 9; 6 7 1; 4 5 2]
ad = det(A)
bd = det(B)
disp("Wyznacznik macierzy A:")
disp(ad)
disp("Wyznacznik macierzy B:")
disp(bd)
if ad > bd then
    disp("Większy jest wyznacznik macierzy A")
elseif bd > ad then
    disp("Większy jest wyznacznik macierzy B")
else
    disp("Wyznaczniki są równe")
end
