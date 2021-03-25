"""
Otrzymujesz liste cen sznurka o dlugosci rownej indeksowi powiekszonemu o 1.
Sprzedajac sznurek pokroiony na trzy czesci mozemy zarobic wiecej niz przy podzieleniu sznurka na pol.
Ile najwiecej mozemy zarobic na sprzedazy sznurka?
"""

# Zlozonosc czasowa: O(n^n)
# Zlozonosc pamieciowa: O(1)
def podzielSznurekV1(ceny, n):

    if n == 0:
        return 0

    maks = 0

    for i in range(n):

        cena = ceny[i] + podzielSznurek(ceny, n - i - 1)

        if cena > maks:
            maks = cena

    return maks


# Zlozonosc czasowa: O(n^2)
# Zlozonosc pamieciowa: O(n)
def podzielSznurekV2(ceny, n):

    T = [0] * (n + 1)

    for i in range(n):
        for j in range(i + 1):
            T[i + 1] = max(T[i + 1], ceny[j] + T[i - j])

    return T[n]


if __name__ == "__main__":

    ceny = [1, 5, 8, 9, 10, 17, 17, 20]

    n = 4

    assert podzielSznurekV1(ceny, n) == 10
    assert podzielSznurekV2(ceny, n) == 10
