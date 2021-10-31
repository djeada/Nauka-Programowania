"""
Dla trzech pobranych liczb reprezentujacych date, 
wypisz odpowiadajacy im dzien tygodnia. 
Pierwsza liczba jest dniem, druga miesiacem, trzecia rokiem. 

Wzor Gaussa:
Niech data bedzie dana w formacie DD/MM/CCYY :
    DD - dzien
    MM - miesiac
    CC - stulecie
    YY - rok

    A = CC/4 - 2*CC - 1
    B = 5*YY/4
    C = 26*(MM + 1)/10

    Dzien = (A + B + C + DD) mod 7
"""

if __name__ == "__main__":

    print("Podaj date: ")
    dzien = int(input())
    miesiac = int(input())
    rok = int(input())

    A = rok // 4 - 2 * rok - 1
    B = 5 * rok // 4
    C = 26 * (miesiac + 1) // 10

    dzien_tygodnia = (A + B + C + dzien) % 7

    if dzien_tygodnia == 1:
        print("Poniedzialek")
    elif dzien_tygodnia == 2:
        print("Wtorek")
    elif dzien_tygodnia == 3:
        print("Sroda")
    elif dzien_tygodnia == 4:
        print("Czwartek")
    elif dzien_tygodnia == 5:
        print("Piatek")
    elif dzien_tygodnia == 6:
        print("Sobota")
    elif dzien_tygodnia == 7:
        print("Niedziela")
    else:
        print("Bledne dane.")
