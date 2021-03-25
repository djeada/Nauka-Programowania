def policzUstawioneBity(liczba):
    suma = 0
    while liczba > 0:
        if liczba & 1:
            suma += 1
        liczba >>= 1
    return suma


def przygotujTablice():
    return [policzUstawioneBity(x) for x in range(256)]


# Zlozonosc czasowa O(1)
# Zlozonosc pamieciowa O(1)
def ustawioneBity(tablica, n):
    return (
        tablica[n & 0xFF]
        + tablica[(n >> 8) & 0xFF]
        + tablica[(n >> 16) & 0xFF]
        + tablica[(n >> 24) & 0xFF]
    )


if __name__ == "__main__":

    tablica = przygotujTablice()

    print(ustawioneBity(tablica, -1))
