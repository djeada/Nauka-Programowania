"""
Sprawdz czy istnieje permutacja danego slowa bedaca palindromem.
"""

# Wersja 1
def znajdz_permutacje(napis, start, koniec, wynik=[]):

    if start >= koniec:
        if "".join(napis) not in wynik:
            wynik.append("".join(napis))

    else:

        for i in range(start, koniec):
            napis[start], napis[i] = napis[i], napis[start]

            znajdz_permutacje(napis, start + 1, koniec, wynik)

            napis[start], napis[i] = napis[i], napis[start]

        return wynik


def czy_palindrom(slowo):
    for i in range(len(slowo) // 2):
        if slowo[i] != slowo[-i - 1]:
            return False

    return True


def czy_istnieje_permutacja_bedaca_palindromem_v1(slowo):

    permutacje = znajdz_permutacje(list(slowo), 0, len(slowo))

    wynik = []

    for p in permutacje:
        if czy_palindrom(p):
            wynik.append(p)

    return wynik


# testy poprawnosci
slowo = "adamm"
wynik = ["madam", "amdma"]

assert sorted(czy_istnieje_permutacja_bedaca_palindromem_v1(slowo)) == sorted(wynik)
