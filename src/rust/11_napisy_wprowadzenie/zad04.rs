/*
ZAD-04 — Zamień wszystkie małe litery na duże

**Poziom:** ★☆☆
**Tagi:** `string`, `upper`

### Treść

Wczytaj napis i zamień wszystkie litery na wielkie.

### Wejście

* 1. linia: napis

### Wyjście

* 1. linia: napis po konwersji

### Przykład

**Wejście:**

```
Rumcajs
```

**Wyjście:**

```
RUMCAJS
```

*/

use std::io;

// Funkcja zamieniająca małe litery na duże
// Złożoność czasowa: O(n), gdzie n to długość napisu
// Złożoność pamięciowa: O(n)
fn zamien_na_wielkie(napis: &str) -> String {
    napis.to_uppercase()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let napis = input.trim();

    println!("{}", zamien_na_wielkie(napis));
}
