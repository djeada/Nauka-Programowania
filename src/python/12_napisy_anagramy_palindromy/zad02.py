"""
Tytul: Znalezienie wszystkich permutacji slowa.
Tresc: Napisz program, ktory dla otrzymanego napisu znajdzie jego wszystkie permutacje.
Dane wejsciowe: Napis.
Dane wyjsciowe: Lista napisow.
Przyklad:
Dla otrzymanego napisu: “abc”, powinna zostac zwrocona lista: [“abc”, “bac”, “cab”, “acb”, “bca”, “cba”].

"""


def permutacje(napis):
    """
    Funkcja znajduje wszystkie permutacje dla podanego napisu.
    """
    if len(napis) == 1:
        return [napis]
    else:
        permutacje = []
        for i in range(len(napis)):
            for permutacja in permutacje(napis[:i] + napis[i + 1 :]):
                permutacje.append(napis[i] + permutacja)
        return permutacje


def test_permutacje():
    assert permutacje("abc") == ["abc", "acb", "bac", "bca", "cab", "cba"]
    assert permutacje("abcd") == [
        "abcd",
        "abdc",
        "acbd",
        "acdb",
        "adbc",
        "adcb",
        "bacd",
        "badc",
        "bcad",
        "bcda",
        "bdac",
        "bdca",
        "cabd",
        "cadb",
        "cbad",
        "cbda",
        "cdab",
        "cdba",
        "dabc",
        "dacb",
        "dbac",
        "dbca",
        "dcab",
        "dcba",
    ]


if __name__ == "__main__":
    test_permutacje()
