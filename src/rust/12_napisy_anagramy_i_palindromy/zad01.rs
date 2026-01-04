/*
ZAD-01 — Czy słowo jest palindromem?

**Poziom:** ★☆☆
**Tagi:** `string`, `palindrom`, `I/O`

### Treść

Wczytaj jedno słowo i sprawdź, czy jest palindromem (czytane od lewej do prawej i od prawej do lewej jest takie samo).

### Wejście

* 1. linia: słowo (same litery, bez spacji)

### Wyjście

Jedna linia:

* `Prawda` — jeśli słowo jest palindromem
* `Fałsz` — w przeciwnym razie

### Przykład

**Wejście:**

```
kajak
```

**Wyjście:**

```
Prawda
```

### Uwagi o formatowaniu

* Jeśli chcesz ignorować wielkość liter, porównuj wersje `lower()`.

*/

use std::io;

// Funkcja sprawdzająca czy słowo jest palindromem
// Złożoność czasowa: O(n), gdzie n to długość słowa
// Złożoność pamięciowa: O(n) dla odwróconego słowa
fn czy_palindrom(slowo: &str) -> bool {
    let slowo_lower = slowo.to_lowercase();
    let odwrocone: String = slowo_lower.chars().rev().collect();
    slowo_lower == odwrocone
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let slowo = input.trim();

    if czy_palindrom(slowo) {
        println!("Prawda");
    } else {
        println!("Fałsz");
    }
}
