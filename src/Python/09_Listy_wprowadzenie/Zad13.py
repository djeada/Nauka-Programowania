"""
Znajdz brakujacy element w liscie.
Ciag arytmetyczny.
"""

# Wersja 1
def znajdzBrakujacyElement(lista):
    suma_przedzialu = (len(lista) + 1) * (min(lista) + max(lista)) // 2
    return suma_przedzialu - sum(lista)


# Testy poprawnosci
lista = [6, 8, 4, 10, 14, 2]
wynik = 12

assert znajdzBrakujacyElement(lista) == wynik
