r"""
ZAD-14 — Znajdź błąd: wspólne wiersze

**Poziom:** ★★☆
**Tagi:** `macierze`, `debugowanie`, `listy`

### Treść

Program z sekcji **Kod startowy** miał tworzyć planszę `n×m` wypełnioną zerami, a następnie wpisywać `1` w `k` pól podanych na wejściu. Niestety wypisuje zły wynik. Dla przykładu poniżej zamiast oczekiwanej planszy wypisuje:

```
1 1 0
1 1 0
1 1 0
```

Znajdź błąd i popraw program tak, aby działał zgodnie z opisem.

### Wejście

* 1. linia: `n m` — liczba wierszy i kolumn
* 2. linia: `k` — liczba pól do zaznaczenia
* następnie `k` linii: `r c` — numer wiersza i kolumny pola, **liczone od 0**

### Wyjście

`n` linii po `m` liczb `0` lub `1` oddzielonych spacjami — plansza po zaznaczeniu pól.

### Ograniczenia

* `1 ≤ n, m ≤ 10`
* `0 ≤ k ≤ 20`; to samo pole może zostać podane kilka razy

### Przykład

**Wejście:**

```
3 3
2
0 0
2 1
```

**Wyjście:**

```
1 0 0
0 0 0
0 1 0
```

### Uwagi

* Uruchom program i sprawdź, które pola zmieniają się po zaznaczeniu tylko jednego pola. Przyjrzyj się linii, która tworzy planszę.
* Pomocne może być wypisanie `plansza[0] is plansza[1]` — operator `is` sprawdza, czy dwie nazwy wskazują na **ten sam** obiekt w pamięci.

### Kod startowy

```python
n, m = [int(x) for x in input().split()]
k = int(input())

plansza = [[0] * m] * n

for _ in range(k):
    r, c = [int(x) for x in input().split()]
    plansza[r][c] = 1

for wiersz in plansza:
    print(" ".join(str(x) for x in wiersz))
```

"""


def stworz_plansze(n, m):
    """
    Zwraca planszę n×m wypełnioną zerami.
    Błąd w kodzie startowym: [[0] * m] * n tworzy listę n odwołań do TEGO
    SAMEGO wiersza, więc zmiana jednego pola zmieniała je we wszystkich
    wierszach. Każdy wiersz musi być osobną listą.
    """
    return [[0] * m for _ in range(n)]


if __name__ == "__main__":
    n, m = [int(x) for x in input().split()]
    k = int(input())

    plansza = stworz_plansze(n, m)

    for _ in range(k):
        r, c = [int(x) for x in input().split()]
        plansza[r][c] = 1

    for wiersz in plansza:
        print(" ".join(str(x) for x in wiersz))
