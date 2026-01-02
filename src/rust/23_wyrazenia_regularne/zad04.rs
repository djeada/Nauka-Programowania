/*
ZAD-04 — Sprawdź, czy słowo występuje w zdaniu jako osobne słowo

**Poziom:** ★☆☆
**Tagi:** `regex`, `string`

### Treść

Otrzymujesz dwa napisy: zdanie oraz słowo. Sprawdź, czy słowo występuje w zdaniu jako samodzielne słowo (nie jako fragment innego słowa).

### Wejście

Dwie linie:

1. `zdanie`
2. `slowo`

### Wyjście

Jedna linia:

* `Prawda` albo `Fałsz`

### Przykład

**Wejście:**

```
Siała baba mak.
babcia
```

**Wyjście:**

```
Fałsz
```

*/

use std::io;

// Funkcja sprawdzająca czy słowo występuje jako osobne słowo w zdaniu
// Złożoność czasowa: O(n * m), gdzie n to długość zdania, m to długość słowa
// Złożoność pamięciowa: O(n)
fn czy_slowo_w_zdaniu(zdanie: &str, slowo: &str) -> bool {
    // Rozbijamy zdanie na słowa używając separatorów
    let slowa: Vec<&str> = zdanie
        .split(|c: char| !c.is_alphanumeric())
        .filter(|s| !s.is_empty())
        .collect();
    
    // Sprawdzamy czy szukane słowo jest w liście słów
    slowa.iter().any(|&s| s == slowo)
}

fn main() {
    let mut zdanie_str = String::new();
    io::stdin().read_line(&mut zdanie_str).expect("Błąd wczytywania");
    let zdanie = zdanie_str.trim();
    
    let mut slowo_str = String::new();
    io::stdin().read_line(&mut slowo_str).expect("Błąd wczytywania");
    let slowo = slowo_str.trim();
    
    if czy_slowo_w_zdaniu(zdanie, slowo) {
        println!("Prawda");
    } else {
        println!("Fałsz");
    }
}
