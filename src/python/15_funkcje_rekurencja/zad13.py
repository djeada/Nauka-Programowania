r"""
ZAD-13 — Ciągi binarne bez sąsiednich jedynek

**Poziom:** ★★☆
**Tagi:** `rekurencja`, `backtracking`, `napisy`

### Treść

Ciąg binarny to napis złożony ze znaków `0` i `1`. Wypisz wszystkie ciągi binarne długości `n`, w których **żadne dwie jedynki nie stoją obok siebie** (np. `1010` jest poprawny, a `0110` nie), w kolejności leksykograficznej (słownikowej), a na końcu ich liczbę.

Napisz rekurencyjną funkcję `generuj(n, ciag)`, która wypisuje wszystkie poprawne ciągi długości `n` zaczynające się od napisu `ciag` i zwraca ich liczbę. Program wywołuje `generuj(n, "")` i wypisuje zwróconą liczbę.

### Wejście

Jedna liczba naturalna `n`.

### Wyjście

Najpierw wszystkie poprawne ciągi, każdy w osobnej linii, w kolejności leksykograficznej. W ostatniej linii — liczba tych ciągów.

### Ograniczenia

* `1 ≤ n ≤ 12`

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
000
001
010
100
101
5
```

Pozostałe ciągi długości 3 (`011`, `110`, `111`) mają dwie sąsiednie jedynki.

### Uwagi

* To przykład **przeszukiwania z nawrotami** (ang. *backtracking*): budujemy ciąg znak po znaku. W każdym kroku najpierw próbujemy dopisać `0` (zawsze wolno), a potem `1` — ale tylko wtedy, gdy `ciag` jest pusty albo kończy się na `0`. Gdy `ciag` ma już długość `n`, wypisujemy go i zwracamy `1`.
* Próbowanie `0` przed `1` sprawia, że ciągi pojawiają się od razu w kolejności leksykograficznej — nie trzeba ich sortować.
* Ciekawostka: liczba takich ciągów to kolejne liczby Fibonacciego ($2, 3, 5, 8, 13, \dots$).

### Kod startowy

```python
def generuj(n, ciag):
    pass


n = int(input())
print(generuj(n, ""))
```

"""


def generuj(n, ciag):
    """Wypisuje wszystkie ciągi binarne długości n bez sąsiednich jedynek,
    zaczynające się od ciag (w kolejności leksykograficznej), i zwraca ich liczbę."""
    if len(ciag) == n:
        print(ciag)
        return 1
    liczba = generuj(n, ciag + "0")
    if ciag == "" or ciag[-1] == "0":
        liczba += generuj(n, ciag + "1")
    return liczba


if __name__ == "__main__":
    n = int(input())
    print(generuj(n, ""))
