/*
ZAD-12 — Usuń spacje ze zdania

**Poziom:** ★☆☆
**Tagi:** `replace`, `string`

### Treść

Wczytaj zdanie i usuń z niego wszystkie spacje.

### Wejście

* 1. linia: zdanie

### Wyjście

* 1. linia: zdanie bez spacji

### Przykład

**Wejście:**

```
Ala ma kota
```

**Wyjście:**

```
Alamakota
```

*/

use std::io;

// Funkcja usuwająca spacje z napisu
// Złożoność czasowa: O(n), gdzie n to długość napisu
// Złożoność pamięciowa: O(n)
fn usun_spacje(zdanie: &str) -> String {
    zdanie.replace(' ', "")
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let zdanie = input.trim();
    
    println!("{}", usun_spacje(zdanie));
}
