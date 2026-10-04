r"""
ZAD-11 — Samochody jadące w przeciwnych kierunkach

**Poziom:** ★★☆
**Tagi:** `listy`, `zliczanie`, `string`

### Treść

Wczytaj `n` oraz napis długości `n` złożony z liter `A` i `B`, opisujący samochody na drodze:

* `A` oznacza samochód jadący na wschód,
* `B` oznacza samochód jadący na zachód.

Para samochodów minie się, jeśli samochód `A` stoi w napisie **przed** samochodem `B` (niekoniecznie bezpośrednio). Policz wszystkie takie pary.

### Wejście

* 1. linia: liczba samochodów `n`
* 2. linia: napis długości `n` złożony tylko z liter `A` i `B` (bez spacji)

### Wyjście

Jedna liczba naturalna: liczba mijających się par.

### Ograniczenia

* $n \ge 1$

### Przykład

**Wejście:**

```
5
ABABB
```

**Wyjście:**

```
5
```

Pierwszy samochód `A` minie trzy samochody `B`, a drugi `A` — dwa: $3 + 2 = 5$.

"""


def policz_mijajace_sie(samochody):
    licznik = 0
    jadace_na_wschod = 0
    for samochod in samochody:
        if samochod == "A":
            jadace_na_wschod += 1
        else:
            licznik += jadace_na_wschod
    return licznik


if __name__ == "__main__":
    n = int(input())
    samochody = input().strip()
    print(policz_mijajace_sie(samochody))
