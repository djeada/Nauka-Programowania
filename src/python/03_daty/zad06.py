"""
Tytul: Poprawnosc daty.
Tresc: Napisz program, ktory dla pobranych trzech liczb naturalnych sprawdzi, czy reprezentuja one poprawna date. Pierwsza liczba jest dniem, druga miesiacem, trzecia rokiem.
Podpowiedz: Wszystkie liczby nie moga byc mniejsze od 1. Druga liczba nie moze byc wieksza niz 12 itd.
Dane wejsciowe: Trzy liczby naturalne.
Dane wyjsciowe: Komunikat o poprawnosci lub niepoprawnosci daty.
Przyklad:
Dla pobranych liczb 2, 1 i 4, program powinien wypisac informacje o poprawnosci daty.

"""

if __name__ == "__main__":

    print("Podaj trzy liczby:")
    dzien = int(input())
    miesiac = int(input())
    rok = int(input())

    if dzien > 0 and dzien <= 31:
        if miesiac > 0 and miesiac <= 12:
            if rok > 0:
                print("Data jest poprawna.")
            else:
                print("Rok jest niepoprawny.")
        else:
            print("Miesiac jest niepoprawny.")
    else:
        print("Dzien jest niepoprawny.")
