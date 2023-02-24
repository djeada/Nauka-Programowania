"""
Dla pobranych trzech liczb, sprawdz czy reprezentuja one poprawna date. 
Pierwsza liczba jest dniem, druga miesiacem, trzecia rokiem. 
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
