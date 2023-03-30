"""
Tytuł: Zamiana kolejności liczb.
Treść zadania: Napisz program, który pobierze od użytkownika dwie liczby naturalne i wypisze je w odwróconej kolejności.
Dane wejściowe: Dwie liczby naturalne.
Dane wyjściowe: Dwie liczby naturalne.
Przykład:
Jeśli użytkownik poda liczby -7 oraz 4, program powinien wypisać liczby: 4 i -7.

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
