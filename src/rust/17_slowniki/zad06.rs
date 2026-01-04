/*
ZAD-06 — Histogram znaków w słowie

**Poziom:** ★☆☆
**Tagi:** `dict`, `string`

### Treść

Wczytaj napis. Zwróć słownik: znak → liczba wystąpień.

### Wejście

* 1 linia: napis

### Wyjście

* Słownik, np. `{'k': 1, 'l': 1, 'a': 2, 's': 1}`

### Przykład

**Wejście:**

```
klasa
```

**Wyjście:**

```
{'k': 1, 'l': 1, 'a': 2, 's': 1}
```

*/

use std::collections::HashMap;
use std::io;

// Funkcja tworząca histogram znaków
// Złożoność czasowa: O(n), gdzie n to długość napisu
// Złożoność pamięciowa: O(k), gdzie k to liczba unikalnych znaków
fn histogram_znakow(napis: &str) -> HashMap<char, usize> {
    let mut histogram = HashMap::new();

    for c in napis.chars() {
        *histogram.entry(c).or_insert(0) += 1;
    }

    histogram
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let napis = input.trim();

    let histogram = histogram_znakow(napis);

    print!("{{");
    let mut first = true;
    for c in napis.chars() {
        if let Some(&count) = histogram.get(&c) {
            if !first {
                print!(", ");
            }
            print!("'{}': {}", c, count);
            first = false;
            // Usuń aby nie wypisywać duplikatów
        }
    }
    println!("}}");
}
