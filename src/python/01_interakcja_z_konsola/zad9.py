"""
Tytuł: Wypisywanie na standardowe wyjście.
Treść zadania: Napisz program, który wypisze dowolny ciąg znaków na standardowe wyjście.
Dane wejściowe: Brak.
Dane wyjściowe: Komunikat.
Przykład:
Program może wypisać twoje inicjały lub komunikat "Witaj świecie!".

"""

if __name__ == "__main__":

    print(
        "podaj stope procentowa, liczbe lat na splacenie kredytu  oraz wysokosc udzielonego kredytu"
    )

    stopa = float(input())
    lata = int(input())
    wysokosc_kredytu = int(input())

    r = stopa / 12 * 0.01
    n = lata * 12

    rata = wysokosc_kredytu * r * (1 + r) ** n / ((1 + r) ** n - 1)

    calk_koszt = rata * n

    print("rata mieieczna to {:0.2f}".format(rata))

    print("calkowity koszt to {:0.2f}".format(calk_koszt))
