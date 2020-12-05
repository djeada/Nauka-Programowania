'''
Znajdz brakujacy element w liscie.
Ciag arytmetyczny.
'''

#Wersja 1
def znajdzBrakujacyElement(lista):
    return sum(range(lista[0], lista[-1]+1)) - sum(lista)

#Testy poprawnosci
lista = [6, 8, 4, 10, 14, 2]
wynik = 12

assert(znajdzBrakujacyElement(lista) == wynik)

