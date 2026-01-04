/*
ZAD-05 — Liczby z przedziału

**Poziom:** ★☆☆
**Tagi:** `pętle`, `przedziały`, `modulo`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`. Najpierw ustal:

* `lo = min(a, b)`
* `hi = max(a, b)`

Następnie:

a) Wypisz wszystkie liczby naturalne `x` takie, że `lo < x < hi` (każda w osobnej linii).

b) Wypisz wszystkie liczby naturalne `x` takie, że `lo < x < hi` oraz `x` jest podzielne przez `3` (każda w osobnej linii).

### Wejście

Dwie liczby naturalne:

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Najpierw wyniki podpunktu (a), potem wyniki podpunktu (b), każda liczba w osobnej linii.

### Przykład

**Wejście:**

```
9
5
```

**Wyjście:**

```
6
7
8
6
```

### Uwagi o formatowaniu

* Nie wypisuj nagłówków typu „a)” i „b)”.
* Jeśli w którymś podpunkcie nie ma liczb do wypisania, w tej części nie wypisuj nic.
* Nie dodawaj pustej linii między podpunktami.

*/
fn main() {
    let mut a = String::new();
    std::io::stdin().read_line(&mut a).unwrap();
    let a: i32 = a.trim().parse().unwrap();

    let mut b = String::new();
    std::io::stdin().read_line(&mut b).unwrap();
    let b: i32 = b.trim().parse().unwrap();

    let lo = if a < b { a } else { b };
    let hi = if a > b { a } else { b };

    // Podpunkt a) wszystkie liczby miedzy lo i hi
    for x in (lo + 1)..hi {
        println!("{}", x);
    }

    // Podpunkt b) liczby podzielne przez 3
    for x in (lo + 1)..hi {
        if x % 3 == 0 {
            println!("{}", x);
        }
    }
}
