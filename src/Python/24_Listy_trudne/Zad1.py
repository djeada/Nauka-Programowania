"""
Otrzymujesz tablice skladajaca sie wylacznie z zer i jedynek. Znajdz indeks zera, ktore po zamianie na jedynke daloby najdluzszy nieprzerwany ciag jedynek.
Zachowanie dla otrzymanej tablicy skladajacej sie z samych zer jest nieokreslone.
"""

# Wersja 1
# Zlozonosc czasowa O(n)
# Zlozonosc obliczeniowa O(1)
def znajdzZeroDoPodmianyV1(lista):
    licznikJedynek = 0
    indeksZera = -1

    licznikZer = 0
    poprzedniIndeksZera = -1

    for i in range(len(lista)):

        if lista[i] == 1:
            licznikZer += 1

        else:
            licznikZer = i - poprzedniIndeksZera
            poprzedniIndeksZera = i

        if licznikZer > licznikJedynek:
            licznikJedynek = licznikZer
            indeksZera = poprzedniIndeksZera

    return indeksZera


# Testy Poprawnosci
lista = [0, 0, 1, 0, 1, 1, 1, 0, 1, 1]
wynik = 7

assert znajdzZeroDoPodmianyV1(lista) == wynik

lista = [1, 1, 1, 1, 1, 1, 1, 1]
wynik = -1

assert znajdzZeroDoPodmianyV1(lista) == wynik

lista = [1, 0, 1, 1, 1, 1, 1, 1]
wynik = 1

assert znajdzZeroDoPodmianyV1(lista) == wynik
