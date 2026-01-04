/*
ZAD-08 — Naiwny test pierwszości liczby

**Poziom:** ★★☆
**Tagi:** `pierwszość`, `pętle`, `dzielniki`

### Treść

Napisz funkcję `czy_pierwsza(n)`, która zwraca `True`, jeśli `n` jest liczbą pierwszą, w przeciwnym razie `False`.

### Wejście

Jeden argument funkcji:

* `n` (liczba naturalna, `n ≥ 2`)

### Wyjście

Funkcja zwraca wartość logiczną:

* `True` lub `False`

### Przykład

**Wywołanie funkcji:**

```python
print(czy_pierwsza(7))
print(czy_pierwsza(4))
```

**Wyjście:**

```
True
False
```

### Uwagi

* Dla prostego rozwiązania możesz sprawdzać dzielniki od `2` do `n-1`.
* Dla szybszego rozwiązania możesz sprawdzać dzielniki do `⌊sqrt(n)⌋`.

*/

fn czy_pierwsza(n: i32) -> bool {
    if n < 2 {
        return false;
    }
    if n == 2 {
        return true;
    }
    if n % 2 == 0 {
        return false;
    }

    let mut i = 3;
    while i * i <= n {
        if n % i == 0 {
            return false;
        }
        i += 2;
    }
    true
}

fn main() {
    println!("{}", czy_pierwsza(7));
    println!("{}", czy_pierwsza(4));
}
