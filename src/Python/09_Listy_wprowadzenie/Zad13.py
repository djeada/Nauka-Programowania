"""
Znajdz brakujacy element w liscie.
Ciag arytmetyczny.
"""

# Wersja 1
def znajdz_brakujacy_element(lista):
    suma_przedzialu = (len(lista) + 1) * (min(lista) + max(lista)) // 2
    return suma_przedzialu - sum(lista)


# Testy poprawnosci
lista = [6, 8, 4, 10, 14, 2]
wynik = 12

assert znajdz_brakujacy_element(lista) == wynik
