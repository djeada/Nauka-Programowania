"""
ZAD-01 — Wartość wielomianu w punkcie

**Poziom:** ★☆☆
**Tagi:** `wielomiany`, `Horner`, `I/O`

### Treść

Wczytaj współczynniki wielomianu ( a_nx^n + a_{n-1}x^{n-1} + \dots + a_0 ) oraz liczbę ( x ). Oblicz wartość wielomianu w punkcie ( x ).

### Wejście

* 1. linia: `n` — stopień wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb całkowitych: `a_n a_{n-1} ... a_0`
* 3. linia: `x` — liczba całkowita

### Wyjście

Jedna liczba całkowita — wartość wielomianu w punkcie `x`.

### Przykład

**Wejście:**

```
2
3 2 1
1
```

**Wyjście:**

```
6
```

### Uwagi o formatowaniu

* Użyj schematu Hornera (jest najprostszy i najszybszy).

"""


def wartosc_wielomianu_horner(wspolczynniki, x, indeks=0, akumulator=0):
    """
    Oblicza wartość wielomianu w punkcie x używając schematu Hornera (rekurencyjnie).
    Współczynniki w formacie [a_n, ..., a_0].
    
    Złożoność czasowa: O(n), gdzie n to stopień wielomianu
    Złożoność pamięciowa: O(n) ze względu na rekurencję
    """
    if indeks >= len(wspolczynniki):
        return akumulator
    
    # Schemat Hornera: wynik = wynik * x + a_i
    nowy_akumulator = akumulator * x + wspolczynniki[indeks]
    return wartosc_wielomianu_horner(wspolczynniki, x, indeks + 1, nowy_akumulator)


if __name__ == "__main__":
    # Wczytanie stopnia wielomianu
    n = int(input().strip())
    
    # Wczytanie współczynników
    wspolczynniki = list(map(int, input().strip().split()))
    
    # Wczytanie punktu x
    x = int(input().strip())
    
    # Obliczenie wartości wielomianu
    # Złożoność czasowa: O(n)
    # Złożoność pamięciowa: O(n)
    wynik = wartosc_wielomianu_horner(wspolczynniki, x)
    
    # Wypisanie wyniku
    print(wynik)
