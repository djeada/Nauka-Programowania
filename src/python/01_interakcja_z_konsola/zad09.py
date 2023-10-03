"""
Tytul: Kalkulator kredytowy
Tresc: Pobierz roczna stope procentowa, liczbe lat na splacenie kredytu oraz wysokosc udzielonego kredytu. Oblicz miesieczna rate oraz calkowity koszt kredytu.
Dane wejsciowe: Trzy liczby naturalne.
Dane wyjsciowe: Dwie liczby naturalne.
Przyklad:
Dla pobranych liczb: 3.5 (roczna stopa procentowa), 8 (liczba lat) oraz 12000 (wysokosc kredytu), powinny zostac wypisane liczby 143.5 (miesieczna rata) oraz 13776 (calkowity koszt kredytu). Waluta jest umowna.

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
