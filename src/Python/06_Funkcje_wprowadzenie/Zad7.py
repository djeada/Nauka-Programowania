"""
Napisz dwie funkcje. Pierwsza powinna prosic uzytkownika o podanie nazwy oraz hasla 
oraz zwracac otrzymane dane. Druga powinna otrzymywac dane od pierwszej i ponownie 
prosic o podanie nazwy oraz hasla. Prosba o podanie danych powinna zostac umieszczona 
w petli. Warunkiem zakonczenia petli jest podanie przez uzytkownika danych identycznych 
z tymi przekazanymi przez pierwsza funkcje.
"""


def inicjalizacja_danych():
    nazwa = input("Podaj nazwe: ")
    haslo = input("Podaj haslo: ")
    return nazwa, haslo


def sprawdzenie_danych(nazwa, haslo):

    nazwa2 = None
    haslo2 = None

    while not (nazwa == nazwa2 and haslo == haslo2):
        nazwa2 = input("Podaj nazwe: ")
        haslo2 = input("Podaj haslo: ")

    print("Dane sa identyczne")


if __name__ == "__main__":

    nazwa, haslo = inicjalizacja_danych()
    sprawdzenie_danych(nazwa, haslo)
