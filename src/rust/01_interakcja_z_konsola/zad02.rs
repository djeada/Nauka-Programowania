/*
ZAD-02 — Zamiana kolejności liczb

**Poziom:** ★☆☆
**Tagi:** `I/O`, `zmienne`

### Treść

Wczytaj dwie liczby całkowite i wypisz je w odwrotnej kolejności (każda w osobnej linii).

### Wejście

Dwie liczby całkowite:

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Dwie linie:

* 1. linia: `b`
* 2. linia: `a`

### Ograniczenia / gwarancje

* `a`, `b` mieszczą się w typowym zakresie int (np. 32-bit).

### Przykład

**Wejście:**

```
-7
4
```

**Wyjście:**

```
4
-7
```

*/

use ::std::*;

fn main() {
    let mut a = String::new();
    std::io::stdin().read_line(&mut a).unwrap();
    let a: i32 = a.trim().parse().unwrap();

    let mut b = String::new();
    std::io::stdin().read_line(&mut b).unwrap();
    let b: i32 = b.trim().parse().unwrap();

    println!("{}", b);
    println!("{}", a);
}
