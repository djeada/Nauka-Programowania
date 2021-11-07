"""
Otrzymujesz napis reprezentujacy sciezke pliku tekstowego. 
Kazdy wiersz pliku reprezentuje adres ip. Posortuj adresy ip 
i zapisz je w liscie.
"""

import pathlib


def wczytaj_plik(sciezka):
    """
    Funkcja wczytujaca plik tekstowy
    """
    return pathlib.Path(sciezka).read_text().splitlines()


def sortuj_adresy_ip(lista):
    """
    Funkcja sortujaca liste adresow ip. Adresy ip dane sa 
    w postaci napisow. Przyklad: '123.4.245.23' 
    """
    lista = [ip.split(".") for ip in lista]
    lista = [[int(i) for i in ip] for ip in lista]
    lista = sorted(lista, key=lambda x: (x[0], x[1], x[2], x[3]))
    lista = [".".join([str(i) for i in ip]) for ip in lista]
    return lista


def test_sortuj_adresy_ip():

    # stworz folder testowy
    pathlib.Path("test").mkdir()

    # utworz plik testowy
    plik = pathlib.Path("test/test.txt")
    plik.write_text(
        "\n".join(
            [
                "123.4.245.23",
                "104.244.253.29",
                "1.198.3.93",
                "32.183.93.40",
                "104.30.244.2",
                "104.244.4.1",
            ]
        )
    )

    print(sortuj_adresy_ip(wczytaj_plik(plik)))
    assert sortuj_adresy_ip(wczytaj_plik(plik)) == [
        "1.198.3.93",
        "32.183.93.40",
        "104.30.244.2",
        "104.244.4.1",
        "104.244.253.29",
        "123.4.245.23",
    ]

    # usun folder testowy
    import shutil

    shutil.rmtree("test")


if __name__ == "__main__":

    test_sortuj_adresy_ip()
