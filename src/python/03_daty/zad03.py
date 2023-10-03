"""
Tytul: Rok przestepny.
Tresc: Napisz program, ktory dla pobranej liczby naturalnej bedzie sprawdzal, czy dany rok jest przestepny.
Podpowiedz: Rok przestepny jest podzielny przez 4, ale nie jest podzielny przez 100, chyba ze jest podzielny przez 400.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Komunikat o tym, czy rok jest przestepny, czy tez nie.
Przyklad:
Dla pobranej liczby 2100, program powinien wypisac informacje, ze rok nie jest przestepny.

"""

if __name__ == "__main__":

    print("Podaj rok: ")
    rok = int(input())

    if rok % 4 == 0 and rok % 100 != 0 or rok % 400 == 0:
        print("Rok jest przestepny.")
    else:
        print("Rok nie jest przestepny.")
