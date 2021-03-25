"""
Znajdz wszystkie wyjatkowe palindromy jakie mozna utworzyc ze znakow w slowie (bez zmiany kolejnosci).		
Wyjatkowy palindrom spelnia jeden z dwoch warunkow:
1. Wszystkie znaki sa identyczne, np. xxx
2. Wszystkie znaki poza srodkowym znakiem sa identyczne, np. ccdcc.
Pojedynczy znak jest rowniez uznawany za wyjatkowy palindrom.
"""

# Wersja 1
def znajdzWyjatkowePalindromyV1(slowo):
    wynik = []

    for i in range(len(slowo)):
        wynik.append(slowo[i])

        j = i + 1
        while j < len(slowo) and slowo[i] == slowo[j]:
            j += 1

        if j > i + 1:
            wynik.append(slowo[i:j])

        if j + 1 < len(slowo) and slowo[i] == slowo[j + 1]:
            k = j + 1
            while k > i and slowo[i] == slowo[k]:
                k -= 1

            if i + 1 == k:
                wynik.append(slowo[i : i + 2 * (j - i) + 1])

    return wynik


# Testy Poprawnosci
slowo = "xxxx"
wynik = ["x", "xxxx", "x", "xxx", "x", "xx", "x"]
assert sorted(znajdzWyjatkowePalindromyV1(slowo)) == sorted(wynik)

slowo = ""
wynik = []
assert sorted(znajdzWyjatkowePalindromyV1(slowo)) == sorted(wynik)
