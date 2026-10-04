r"""
ZAD-04 — Usuń pary ze słownika na podstawie wartości

**Poziom:** ★☆☆
**Tagi:** `dict`, `filtrowanie`

### Treść

Wczytaj słownik złożony z `n` par (klucz — słowo, wartość — liczba całkowita) oraz liczbę `k`. Usuń ze słownika wszystkie pary, których wartość jest równa `k`, i wypisz wynikowy słownik.

### Wejście

* 1. linia: `n`
* następnie `n` linii: `klucz wartość` (klucze są różne i składają się z małych liter)
* ostatnia linia: `k`

### Wyjście

Słownik po usunięciu par, w postaci `{'klucz': wartość, …}`, z parami w kolejności z wejścia; jeśli usunięto wszystkie pary — `{}`.

### Ograniczenia

* `1 ≤ n ≤ 50`

### Przykład

**Wejście:**

```
4
aaa 5
abc 1
xxx 5
cba 3
5
```

**Wyjście:**

```
{'abc': 1, 'cba': 3}
```

### Uwagi

* Nie usuwaj elementów ze słownika, po którym właśnie iterujesz — przejdź po kopii kluczy (`list(slownik)`) albo zbuduj nowy słownik.

"""


def usun_pary_o_wartosci(slownik, wartosc):
    """Usuwa ze słownika wszystkie pary, których wartość jest równa podanej."""
    # Iterujemy po kopii kluczy — nie wolno usuwać elementów ze słownika,
    # po którym właśnie przechodzi pętla.
    for klucz in list(slownik):
        if slownik[klucz] == wartosc:
            del slownik[klucz]
    return slownik


if __name__ == "__main__":
    n = int(input())
    slownik = {}
    for _ in range(n):
        klucz, wartosc = input().split()
        slownik[klucz] = int(wartosc)
    k = int(input())

    print(usun_pary_o_wartosci(slownik, k))
