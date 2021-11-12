"""
Oblicz pola figur i objetosci bryl:

a) Pobierz dlugosci podstawy i wysokosci trojkata i wypisz pole. 
b) Pobierz dlugosci bokow prostokata i wypisz pole. 
c) Pobierz dlugosci przekatnych rombu i wypisz pole. 
d) Pobierz promien kuli i wypisz objetosc.
e) Pobierz promien podstawy i wysokosc stozka i wypisz objetosc.
f) Pobierz dlugosc, szerokosc i wysokosc graniastoslupa i wypisz objetosc.
"""

if __name__ == "__main__":

    print("podaj podstawe i wysokosc trojkata:")
    a = int(input())
    h = int(input())
    print(
        "pole trojkata o podstawie ", a, " i wysokosci ", h, " jest rowne ", a * h / 2
    )

    print("podaj dlogosci bokow prostokata:")
    a = int(input())
    b = int(input())
    print("pole prostokata o bokach ", a, " i ", b, " jest rowne ", a * b)

    print("podaj dlugosc przekatnych rombu:")
    a = int(input())
    b = int(input())
    print("pole rombu o przekatnych ", a, " i ", b, " jest rowne ", a * b / 2)

    print("podaj promien kuli:")
    r = int(input())
    print("objetosc kuli o promieniu ", r, " jest rowna ", 4 / 3 * 3.14 * r ** 3)

    print("podaj promien podstawy i wysokosc stozka:")
    r = int(input())
    h = int(input())
    print(
        "objetosc stozka o podstawie ",
        r,
        " i wysokosci ",
        h,
        " jest rowna ",
        1 / 3 * 3.14 * r ** 2 * h,
    )

    print("podaj dlugosc, szerokosc i wysokosc graniastoslupa:")
    a = int(input())
    b = int(input())
    h = int(input())
    print(
        "objetosc graniastoslupa o dlugosci ",
        a,
        " i szerokosci ",
        b,
        " i wysokosci ",
        h,
        " jest rowna ",
        a * b * h,
    )
