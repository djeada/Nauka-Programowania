"""
Dla pobranych trzech liczb, sprawdź czy reprezentują one poprawną datę. 
Pierwsza liczba jest dniem, druga miesiącem, trzecia rokiem. 
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
            print("Miesiąc jest niepoprawny.")
    else:
        print("Dzień jest niepoprawny.")

