/*
ZAD-10 — Ile bitów trzeba odwrócić (A → B)

**Poziom:** ★★☆
**Tagi:** `XOR`, `popcount`, `bitwise`

### Treść

Wczytaj dwie liczby naturalne `A` i `B`. Oblicz, ile bitów trzeba odwrócić w `A`, aby otrzymać `B`.

### Wejście

* 1. linia: `A`
* 2. linia: `B`

### Wyjście

Jedna liczba naturalna: liczba różniących się bitów.

### Przykład

**Wejście:**

```
34
73
```

**Wyjście:**

```
5
```

*/

use std::io;

// Funkcja obliczająca liczbę różniących się bitów (odległość Hamminga)
// Złożoność czasowa: O(1) lub O(log n)
// Złożoność pamięciowa: O(1)
fn ile_bitow_do_odwrocenia(a: u32, b: u32) -> u32 {
    // XOR daje różnice, następnie liczymy jedynki
    (a ^ b).count_ones()
}

fn main() {
    let mut a_str = String::new();
    let mut b_str = String::new();

    io::stdin().read_line(&mut a_str).expect("Błąd wczytywania");
    io::stdin().read_line(&mut b_str).expect("Błąd wczytywania");

    let a: u32 = a_str.trim().parse().unwrap_or(0);
    let b: u32 = b_str.trim().parse().unwrap_or(0);

    println!("{}", ile_bitow_do_odwrocenia(a, b));
}
