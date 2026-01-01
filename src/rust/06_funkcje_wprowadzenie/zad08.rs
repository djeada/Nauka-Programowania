/*
ZAD-08 — Iloraz w dół bez / i %

**Poziom:** ★★☆
**Tagi:** `funkcje`, `pętle`, `odejmowanie`

### Treść

Napisz funkcję `zaokraglij_w_dol(a, b)`, która zwraca wartość `a // b`, ale **nie używa** operatorów `/` ani `%`.

### Wejście

Dwa argumenty:

* `a` (liczba naturalna, `a ≥ 0`)
* `b` (liczba naturalna)

### Ograniczenia / gwarancje

* `b > 0`

### Wyjście

Funkcja zwraca liczbę naturalną — iloraz `a` przez `b` zaokrąglony w dół.

### Przykład

**Wywołanie funkcji:**

```python
print(zaokraglij_w_dol(7, 2))
```

**Wyjście:**

```
3
```

*/

fn zaokraglij_w_dol(mut a: i32, b: i32) -> i32 {
    let mut count = 0;
    while a >= b {
        a -= b;
        count += 1;
    }
    count
}

fn main() {
    println!("{}", zaokraglij_w_dol(7, 2));
}
