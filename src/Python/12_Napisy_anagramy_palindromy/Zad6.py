"""
Sprawdz czy istnieje permutacja danego slowa bedaca palindromem.
"""

# Wersja 1
def znajdzPermutacje(napis, start, koniec, wynik=[]):

    if start >= koniec:
        if "".join(napis) not in wynik:
            wynik.append("".join(napis))

    else:

        for i in range(start, koniec):
            napis[start], napis[i] = napis[i], napis[start]

            znajdzPermutacje(napis, start + 1, koniec, wynik)

            napis[start], napis[i] = napis[i], napis[start]

        return wynik


def czyPalindrom(slowo):
    for i in range(len(slowo) // 2):
        if slowo[i] != slowo[-i - 1]:
            return False

    return True


def czyIstniejePermutacjaBedacaPalindromemV1(slowo):

    permutacje = znajdzPermutacje(list(slowo), 0, len(slowo))

    wynik = []

    for p in permutacje:
        if czyPalindrom(p):
            wynik.append(p)

    return wynik


# testy poprawnosci
slowo = "adamm"
wynik = ["madam", "amdma"]

assert sorted(czyIstniejePermutacjaBedacaPalindromemV1(slowo)) == sorted(wynik)
