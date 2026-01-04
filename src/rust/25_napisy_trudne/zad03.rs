/*
ZAD-03 — Czy napis A jest początkiem napisu B?

**Poziom:** ★★☆
**Tagi:** `string`, `prefix`

### Treść

Otrzymujesz dwa napisy:

1. Napis `A` — potencjalny przedrostek,
2. Napis `B` — napis testowany.

Sprawdź, czy `B` **zaczyna się** od `A`.

### Wejście

* 1 linia: `A`
* 2 linia: `B`

### Wyjście

* 1 linia: `Prawda` albo `Fałsz`

### Przykład

**Wejście:**

```
Dino
Dinozaur jest zly
```

**Wyjście:**

```
Prawda
```

*/

use std::io;

// Funkcja sprawdzająca czy napis A jest początkiem napisu B
// Złożoność czasowa: O(n), gdzie n to długość przedrostka
// Złożoność pamięciowa: O(1)
fn czy_przedrostek(a: &str, b: &str) -> bool {
    b.starts_with(a)
}

fn main() {
    let mut a_str = String::new();
    io::stdin().read_line(&mut a_str).expect("Błąd wczytywania");
    let a = a_str.trim();

    let mut b_str = String::new();
    io::stdin().read_line(&mut b_str).expect("Błąd wczytywania");
    let b = b_str.trim();

    if czy_przedrostek(a, b) {
        println!("Prawda");
    } else {
        println!("Fałsz");
    }
}
