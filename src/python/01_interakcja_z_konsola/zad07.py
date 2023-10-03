"""
Tytul: Pole powierzchni i objetosc figur geometrycznych.
Tresc zadania: Napisz program, ktory bedzie obliczal pola powierzchni i objetosci figur geometrycznych zgodnie z nastepujacymi instrukcjami:
a) Pobierz dlugosci podstawy i wysokosci trojkata i wypisz jego pole.
b) Pobierz dlugosci bokow prostokata i wypisz jego pole.
c) Pobierz dlugosci przekatnych rombu i wypisz jego pole.
d) Pobierz promien kuli i wypisz jej objetosc.
e) Pobierz promien podstawy i wysokosc stozka i wypisz jego objetosc.
f) Pobierz dlugosc, szerokosc i wysokosc graniastoslupa i wypisz jego objetosc.
Jednostki sa dowolne.
Dane wejsciowe:
* Dwie liczby naturalne dla podpunktow a, b i c.
* Liczba naturalna dla podpunktu d.
* Dwie liczby naturalne dla podpunktu e.
* Trzy liczby naturalne dla podpunktu f.
Dane wyjsciowe: Liczba naturalna dla wszystkich podpunktow.
Przyklad:
a) Dla pobranych liczb: 5 i 2, powinna zostac wypisana liczba: 5.
b) Dla pobranych liczb: 3 i 3, powinna zostac wypisana liczba: 4.
c) Dla pobranych liczb: 2 i 4, powinna zostac wypisana liczba: 1.
d) Dla pobranej liczby: 2, powinna zostac wypisana liczba: 33.493.
e) Dla pobranych liczb: 3 i 2, powinna zostac wypisana liczba: 18.84.
f) Dla pobranych liczb: 2, 2 i 2, powinny zostac wypisana liczba: 8.

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
