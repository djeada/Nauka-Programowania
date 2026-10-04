r"""
ZAD-01 — Kwadrat

**Poziom:** ★☆☆
**Tagi:** `pętle zagnieżdżone`, `print`, `string`

### Treść

Wczytaj liczbę naturalną `n` i wypisz kwadrat o boku `n` zbudowany z gwiazdek `*`.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 1`)

### Wyjście

`n` linii, w każdej dokładnie `n` znaków `*` (bez spacji).

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
**
**
```

### Uwagi

* Spróbuj użyć dwóch pętli: zewnętrznej dla wierszy i wewnętrznej dla gwiazdek w wierszu (`print("*", end="")`).

"""


def kwadrat(n):
    for _ in range(n):
        for _ in range(n):
            print("*", end="")
        print()


if __name__ == "__main__":
    n = int(input())
    kwadrat(n)
