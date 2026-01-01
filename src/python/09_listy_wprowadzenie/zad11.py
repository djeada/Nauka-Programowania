"""
ZAD-11 — Samochody jadące w przeciwnych kierunkach

**Poziom:** ★★☆
**Tagi:** `listy`, `zliczanie`, `string`

### Treść

Wczytaj `N` oraz napis długości `N` złożony z liter `A` i `B`:

* `A` oznacza samochód jadący na wschód,
* `B` oznacza samochód jadący na zachód.

Policz, ile par samochodów minie się, gdy uznamy, że para mija się wtedy, gdy `A` stoi **przed** `B` w ciągu.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* 2. linia: napis długości `N`, tylko `A` i `B` (bez spacji)

### Wyjście

Jedna liczba naturalna — liczba mijających się par.

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

"""


def policz_samchody(lista):
    licznik = 0
    pom = 0
    for samochod in lista:
        if samochod == "A":
            pom += 1
        elif samochod == "B":
            licznik += pom

    return licznik


def test_policz_samochody():
    assert policz_samchody(["A", "B", "A", "B", "B"]) == 5
    assert (
        policz_samchody(["A", "A", "A", "B", "B", "A", "B", "A", "B", "A", "A", "A"])
        == 15
    )


if __name__ == "__main__":

    test_policz_samochody()
