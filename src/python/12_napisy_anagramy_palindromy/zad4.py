"""
Tytul: Wyszukanie wszystkich palindromow w zdaniu.
Tresc: Napisz program, ktory otrzymuje napis reprezentujacy zdanie. Twoim zadaniem jest znalezienie wszystkich palindromow w zdaniu. Roznice miedzy wielkimi i malymi literami powinny byc zignorowane.
Dane wejsciowe: Napis.
Dane wyjsciowe: Lista napisow.
Przyklad:
Dla otrzymanego napisu: “Tata zabral kajak na wycieczke i uderzyl sie w oko”, powinna zostac zwrocona lista: ["kajak", "i", "w", "oko"].

"""
import string


def podziel_zdanie_na_slowa(zdanie):
    """
    Funkcja rozdziela zdanie na slowa.
    """
    return zdanie.translate(str.maketrans("", "", string.punctuation)).split()


def czy_palindrom(slowo):
    """
    Funkcja sprawdza czy podane slowo jest palindromem.
    """
    return slowo == slowo[::-1]


def palindromy_w_zdaniu(zdanie):
    """
    Funkcja zwraca liste palindromow w podanym zdaniu.
    """
    return [slowo for slowo in podziel_zdanie_na_slowa(zdanie) if czy_palindrom(slowo)]


def test_palindromy_w_zdaniu():
    assert sorted(
        palindromy_w_zdaniu("Tata zbaral kajak na wycieczke i uderzyl sie w oko")
    ) == sorted(["kajak", "i", "w", "oko"])


if __name__ == "__main__":
    test_palindromy_w_zdaniu()

