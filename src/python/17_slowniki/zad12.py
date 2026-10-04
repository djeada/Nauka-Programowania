r"""
ZAD-12 — Porównanie dwóch słowników z listami (kolejność list bez znaczenia)

**Poziom:** ★★☆
**Tagi:** `dict`, `porównanie`, `list`

### Treść

Wczytaj dwa słowniki, w których kluczami są słowa, a wartościami listy liczb całkowitych. Sprawdź, czy słowniki są identyczne, przy czym **kolejność liczb w listach nie ma znaczenia**: oba słowniki muszą mieć ten sam zbiór kluczy, a pod każdym kluczem te same liczby, występujące tyle samo razy.

### Wejście

* 1. linia: `n` — liczba kluczy pierwszego słownika
* następnie `n` linii: `klucz v1 v2 v3 …` (co najmniej jedna liczba)
* następnie linia z `m` — liczbą kluczy drugiego słownika
* następnie `m` linii: `klucz v1 v2 v3 …`

W obrębie jednego słownika klucze są różne.

### Wyjście

Jedno słowo: `Prawda`, jeśli słowniki są identyczne, w przeciwnym razie `Fałsz`.

### Ograniczenia

* `1 ≤ n, m ≤ 20`
* każda lista ma od 1 do 20 liczb

### Przykład

**Wejście:**

```
2
a 1 2 3
b 4 5
2
a 3 2 1
b 5 4
```

**Wyjście:**

```
Prawda
```

### Przykład 2

**Wejście:**

```
1
a 1 2
1
a 2 1 1
```

**Wyjście:**

```
Fałsz
```

Lista `2 1 1` zawiera liczbę `1` dwa razy, a lista `1 2` — tylko raz.

### Uwagi

* Kolejność kluczy na wejściu też nie ma znaczenia.
* Porównanie zbiorów (`set`) nie wystarczy, bo gubi powtórzenia — porównaj posortowane listy.

"""


def wczytaj_slownik():
    """Wczytuje n, a potem n linii 'klucz v1 v2 ...' i zwraca słownik klucz -> lista liczb."""
    n = int(input())
    slownik = {}
    for _ in range(n):
        czesci = input().split()
        slownik[czesci[0]] = [int(x) for x in czesci[1:]]
    return slownik


def czy_identyczne(slownik_a, slownik_b):
    """
    Sprawdza, czy słowniki mają te same klucze, a pod każdym kluczem
    te same liczby (z tymi samymi krotnościami, w dowolnej kolejności).
    """
    if set(slownik_a) != set(slownik_b):
        return False
    for klucz in slownik_a:
        if sorted(slownik_a[klucz]) != sorted(slownik_b[klucz]):
            return False
    return True


if __name__ == "__main__":
    slownik_a = wczytaj_slownik()
    slownik_b = wczytaj_slownik()

    if czy_identyczne(slownik_a, slownik_b):
        print("Prawda")
    else:
        print("Fałsz")
