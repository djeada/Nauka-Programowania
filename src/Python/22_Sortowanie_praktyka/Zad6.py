# Wersja 1
# Zlozonosc czasowa O(n)
# Zlozonosc pamieciowa O(1)
def sortuj_binarna_tablice_v1(tablica):

    zera = tablica.count(0)

    for i in range(zera):
        tablica[i] = 0

    for i in range(zera, len(tablica)):
        tablica[i] = 1

    return tablica


# Testy Poprawnosci
tablica = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]
wynik = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]

assert sortuj_binarna_tablice_v1(tablica) == wynik
