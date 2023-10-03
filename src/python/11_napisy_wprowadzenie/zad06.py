"""
Tytul: Zamien litery "a" na znaki zapytania.
Tresc: Otrzymasz napis. Zmien litery "a" na znaki zapytania.
Dane wejsciowe: Napis.
Dane wyjsciowe: Napis.
Przyklad:
Dla otrzymanego napisu: "Latarnik", powinien zostac zwrocony napis: "L?t?rnik".

"""


def zamien_litery_a_na_znaki_zapytania(napis):
    return napis.replace("a", "?")


def test_zamien_litery_a_na_znaki_zapytania():
    assert zamien_litery_a_na_znaki_zapytania("ala ma kota") == "?l? m? kot?"
    assert (
        zamien_litery_a_na_znaki_zapytania("ala ma kota a kot ma ale")
        == "?l? m? kot? ? kot m? ?le"
    )


if __name__ == "__main__":
    test_zamien_litery_a_na_znaki_zapytania()
