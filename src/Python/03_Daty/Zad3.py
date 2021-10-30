"""
Dla pobranej liczby reprezentującej rok, sprawdź czy rok jest przestępny.
"""

if __name__ == "__main__":

    print("Podaj rok: ")
    rok = int(input())

    if rok % 4 == 0 and rok % 100 != 0 or rok % 400 == 0:
        print("Rok jest przestępny.")
    else:
        print("Rok nie jest przestępny.")
    