
a = 7
b = 5
c = 3

if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if b < c:
    b, c = c, b

if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    if a*a == b*b + c*c:
        print("TRIANGULO RETANGULO")
    elif a*a > b*b + c*c:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")

    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or a == c or b == c:
        print("TRIANGULO ISOSCELES")