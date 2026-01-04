/*
ZAD-01 — Odwróć napis

**Poziom:** ★☆☆
**Tagi:** `string`, `I/O`

### Treść

Wczytaj napis i wypisz go od tyłu.

### Wejście

* 1. linia: napis

### Wyjście

* 1. linia: odwrócony napis

### Przykład

**Wejście:**

```
barszcz
```

**Wyjście:**

```
zczsrab
```

*/

use std::io;

// Funkcja odwracająca napis
// Złożoność czasowa: O(n), gdzie n to długość napisu
// Złożoność pamięciowa: O(n) - nowy string z odwróconymi znakami
fn odwroc_napis(napis: &str) -> String {
    napis.chars().rev().collect()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let napis = input.trim();

    println!("{}", odwroc_napis(napis));
}
