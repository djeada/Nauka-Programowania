"""
Dla pobranej liczby reprezentujacej rok, sprawdz czy rok jest przestepny.
"""

if __name__ == "__main__":

    print("Podaj rok: ")
    rok = int(input())

    if rok % 4 == 0 and rok % 100 != 0 or rok % 400 == 0:
        print("Rok jest przestepny.")
    else:
        print("Rok nie jest przestepny.")
