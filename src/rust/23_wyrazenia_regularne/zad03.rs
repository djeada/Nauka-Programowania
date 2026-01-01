/*
ZAD-03 — Sprawdź, czy napis składa się wyłącznie z cyfr

**Poziom:** ★☆☆
**Tagi:** `regex`, `string`

### Treść

Otrzymujesz napis. Sprawdź, czy składa się wyłącznie z cyfr (`0–9`).

### Wejście

Jedna linia:

* `s`

### Wyjście

Jedna linia:

* `Prawda` — jeśli napis zawiera tylko cyfry
* `Fałsz` — w przeciwnym razie

### Przykład

**Wejście:**

```
1234
```

**Wyjście:**

```
Prawda
```

*/

use std::io;

// Funkcja sprawdzająca czy napis składa się wyłącznie z cyfr
// Złożoność czasowa: O(n), gdzie n to długość napisu
// Złożoność pamięciowa: O(1)
fn czy_tylko_cyfry(napis: &str) -> bool {
    !napis.is_empty() && napis.chars().all(|c| c.is_digit(10))
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let napis = input.trim();
    
    if czy_tylko_cyfry(napis) {
        println!("Prawda");
    } else {
        println!("Fałsz");
    }
}
