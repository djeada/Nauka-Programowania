/*
ZAD-04 — Obliczanie silni liczby

**Poziom:** ★☆☆
**Tagi:** `pętle`, `silnia`, `mnożenie`

### Treść

Napisz funkcję `silnia(n)`, która zwraca `n!` obliczone przy użyciu pętli.
Przyjmij, że `0! = 1`.

### Wejście

Jeden argument funkcji:

* `n` (liczba naturalna, `n ≥ 0`)

### Wyjście

Funkcja zwraca jedną liczbę naturalną — `n!`.

### Przykład

**Wywołanie funkcji:**

```python
print(silnia(3))
```

**Wyjście:**

```
6
```

*/

fn silnia(n: i32) -> i32 {
    if n == 0 {
        return 1;
    }

    let mut wynik = 1;
    for i in 1..=n {
        wynik *= i;
    }
    wynik
}

fn main() {
    println!("{}", silnia(3));
}
