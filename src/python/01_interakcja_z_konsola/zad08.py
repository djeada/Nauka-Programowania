"""
Tytul: Obliczenie ceny podlogi.
Tresc: Otrzymasz cene pojedynczej plytki, wymiary plytki w postaci kwadratu oraz wymiary podlogi w postaci prostokata. Oblicz, ile kosztowac bedzie podloga o podanych wymiarach.
Jednostki sa umowne.
Dane wejsciowe: Cztery liczby naturalne: cena plytki, dlugosc boku plytki, dlugosc podlogi oraz szerokosc podlogi.
Dane wyjsciowe: Liczba naturalna oznaczajaca cene podlogi.
Przyklad:
Dla pobranych liczb: 2 (cena plytki), 3 (dlugosc boku plytki), 20 (dlugosc podlogi) oraz 40 (szerokosc podlogi), powinna zostac wypisana liczba: 196.

"""

if __name__ == "__main__":

    print("podaj: cene plytki, dlugosc boku plytki i wymiary podlogi")

    cena = int(input())
    bok_plytki = int(input())
    szerokosc_podlogi = int(input())
    dlugosc_podlogi = int(input())

    szerokosc_konieczna = (
        szerokosc_podlogi + bok_plytki - szerokosc_podlogi % bok_plytki
    )
    dlugosc_konieczna = dlugosc_podlogi + bok_plytki - dlugosc_podlogi % bok_plytki

    pole_plytki = bok_plytki ** 2
    pole_podlogi = szerokosc_konieczna * dlugosc_konieczna

    calkowity_koszt = cena * pole_podlogi // pole_plytki

    print(
        "Dla plytki o dlugosci boku ",
        bok_plytki,
        "i ceny ",
        cena,
        " calkowity koszt wylozenia podlogi o wymiarach ",
        szerokosc_podlogi,
        "x",
        dlugosc_podlogi,
        " wynosi ",
        calkowity_koszt,
    )
