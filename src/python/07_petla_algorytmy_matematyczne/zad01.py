r"""
ZAD-01 — Średnia, minimum i maksimum z n liczb

**Poziom:** ★☆☆
**Tagi:** `pętle`, `suma`, `średnia`, `minimum`, `maksimum`

### Treść

Wczytaj liczbę `n`, a następnie w pętli `n` liczb (każdą z osobnej linii). Wypisz ich średnią arytmetyczną, najmniejszą i największą z nich.

Nie zapamiętuj wszystkich liczb — wystarczą trzy zmienne aktualizowane w każdym obrocie pętli (tzw. **akumulatory**): bieżąca suma, bieżące minimum i bieżące maksimum.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 1`)
* kolejne `n` linii: liczby rzeczywiste (całkowite lub z kropką dziesiętną, np. `2.5`; mogą być ujemne)

### Wyjście

Trzy liczby, każda w osobnej linii i z dokładnością do **dwóch miejsc po przecinku**:

1. średnia arytmetyczna,
2. najmniejsza liczba,
3. największa liczba.

### Przykład

**Wejście:**

```
3
4
-1
6
```

**Wyjście:**

```
3.00
-1.00
6.00
```

### Uwagi

* Wczytuj liczby funkcją `float()`, bo mogą mieć część ułamkową.
* Minimum i maksimum najprościej zainicjować pierwszą wczytaną liczbą, a potem w pętli porównywać z nimi kolejne liczby.
* Możesz napisać pomocniczą funkcję, np. `formatuj(x)` zwracającą `f"{x:.2f}"`, ale wczytywanie danych zostaw w programie głównym.

"""


def formatuj(liczba):
    return f"{liczba:.2f}"


if __name__ == "__main__":
    n = int(input())

    pierwsza = float(input())
    suma = pierwsza
    najmniejsza = pierwsza
    najwieksza = pierwsza

    for _ in range(n - 1):
        liczba = float(input())
        suma += liczba
        if liczba < najmniejsza:
            najmniejsza = liczba
        if liczba > najwieksza:
            najwieksza = liczba

    print(formatuj(suma / n))
    print(formatuj(najmniejsza))
    print(formatuj(najwieksza))
