"""
Tytul: Haslo.
Tresc: Napisz dwie funkcje:
* Pierwsza funkcja powinna prosic uzytkownika o podanie nazwy uzytkownika i hasla, a nastepnie zwrocic te dane.
* Druga funkcja powinna otrzymac dane od pierwszej funkcji i ponownie prosic uzytkownika o podanie nazwy uzytkownika i hasla. Prosba o podanie danych powinna byc umieszczona w petli. Warunkiem zakonczenia petli jest podanie przez uzytkownika danych identycznych z tymi przekazanymi przez pierwsza funkcje.
Dane wejsciowe: dwie nazwy uzytkownika i hasla (napisy)
Dane wyjsciowe: komunikat

"""


def inicjalizacja_danych():
    """
    Funkcja inicjalizujaca dane.
    """
    nazwa = input("Podaj nazwe: ")
    haslo = input("Podaj haslo: ")
    return nazwa, haslo


def sprawdzenie_danych(nazwa, haslo):
    """
    Funkcja sprawdza czy dane, ktore zostaly podane przez
    uzytkownika sa identyczne z danymi przekazanymi do funkcji.
    """
    nazwa2 = None
    haslo2 = None

    while not (nazwa == nazwa2 and haslo == haslo2):
        nazwa2 = input("Podaj nazwe: ")
        haslo2 = input("Podaj haslo: ")

    print("Dane sa identyczne")


if __name__ == "__main__":

    nazwa, haslo = inicjalizacja_danych()
    sprawdzenie_danych(nazwa, haslo)
