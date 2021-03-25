"""
Otrzymujesz roczna stope procentowa, liczbe lat na splacenie kredytu oraz wysokosc
udzielonego kredytu. Oblicz miesieczna rate oraz calkowity koszt kredytu.
"""

if __name__ == "__main__":

    print(
        "podaj stope procentowa, liczbe lat na splacenie kredytu  oraz wysokosc udzielonego kredytu"
    )

    stopa = float(input())
    lata = int(input())
    kredyt = int(input())

    r = stopa / 12 * 0.01
    n = lata * 12

    rata = kredyt * r * (1 + r) ** n / ((1 + r) ** n - 1)

    c_koszt = rata * n

    print("rata mieieczna to {:0.2f}".format(rata))

    print("calkowity koszt to {:0.2f}".format(c_koszt))
