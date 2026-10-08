/*
ZAD-02 — Operatory bitowe AND, OR i XOR

**Poziom:** ★☆☆
**Tagi:** `bitwise`, `AND`, `OR`, `XOR`

### Treść

Operatory bitowe działają na zapisie binarnym liczb — osobno na każdej pozycji (bicie). Liczby zapisujemy jedna pod drugą, wyrównane do prawej, a brakujące bity z lewej uzupełniamy zerami:

* `a & b` (AND) — bit wyniku jest `1` tylko wtedy, gdy **oba** bity są równe `1`,
* `a | b` (OR) — bit wyniku jest `1`, gdy **co najmniej jeden** z bitów jest równy `1`,
* `a ^ b` (XOR) — bit wyniku jest `1`, gdy bity są **różne**.

Wczytaj dwie liczby naturalne `a` i `b` i wypisz wyniki tych trzech operacji.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Trzy linie — w systemie dziesiętnym:

* 1. linia: `a & b`
* 2. linia: `a | b`
* 3. linia: `a ^ b`

### Ograniczenia

* $0 \le a, b \le 10^9$

### Przykład

**Wejście:**

```
12
10
```

**Wyjście:**

```
8
14
6
```

$12 = 1100_2$ i $10 = 1010_2$. Bit po bicie: AND daje $1000_2 = 8$, OR — $1110_2 = 14$, a XOR — $0110_2 = 6$.

### Uwagi

* Rachunek z przykładu zapisany w słupkach:

  ```
      1100      1100      1100
    & 1010    | 1010    ^ 1010
    ------    ------    ------
      1000      1110      0110
  ```

* Zwróć uwagę na zależności: `a ^ a` to zawsze `0`, `a & 0` to `0`, a `a | 0` i `a ^ 0` to `a`. Zachodzi też równość `(a & b) + (a | b) == a + b` — możesz tak sprawdzić swój wynik.

*/
use std::io::{self, Read};

fn main() {
    let mut dane = String::new();
    io::stdin()
        .read_to_string(&mut dane)
        .expect("Błąd wczytywania");
    let liczby: Vec<u64> = dane
        .split_whitespace()
        .map(|x| x.parse().expect("Niepoprawna liczba"))
        .collect();
    let (a, b) = (liczby[0], liczby[1]);

    println!("{}", a & b);
    println!("{}", a | b);
    println!("{}", a ^ b);
}
