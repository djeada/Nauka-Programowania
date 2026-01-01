/*
ZAD-04 — Maksimum i minimum z dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `max`, `min`, `if`, `formatowanie`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`.
Wypisz je w jednej linii w kolejności: **większa, potem mniejsza**, oddzielone pojedynczą spacją.
Jeśli `a = b`, wypisz `a b` (czyli dwie takie same liczby).

### Wejście

* 1 linia: `a` (całkowita, `a ≥ 0`)
* 2 linia: `b` (całkowita, `b ≥ 0`)

### Wyjście

Jedna linia:
`max(a, b) min(a, b)`

### Przykłady

**Wejście:**

```
1
4
```

**Wyjście:**

```
4 1
```

**Wejście:**

```
5
5
```

**Wyjście:**

```
5 5
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

    if a >= b {
        println!("{} {}", a, b);
    } else {
        println!("{} {}", b, a);
    }
}
