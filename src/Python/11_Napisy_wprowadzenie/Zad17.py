"""
Otrzymujesz liste liczb. Zamien liste na napis.
"""


def znamien_na_napis(lista):
    napis = ""
    for liczba in lista:
        napis += str(liczba)
    return napis


def test_znamien_na_napis():
    assert znamien_na_napis([1, 2, 3, 4, 5]) == "12345"


if __name__ == "__main__":

    test_znamien_na_napis()
