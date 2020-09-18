'''
Znajdz brakujacy element w liscie.
Ciag arytmetyczny.
'''

#Wersja 1
def znajdzBrakujacyElement(lista):
    return sum(range(lista[0], lista[-1]+1)) - sum(lista)

#Testy poprawnosci
lista = [2, 4, 8, 10, 14]
wynik = 12

assert(znajdzBrakujacyElement(lista) == wynik)

