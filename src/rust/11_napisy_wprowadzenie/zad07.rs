/*
ZAD-07 — Zamień znaki na kody ASCII

**Poziom:** ★☆☆
**Tagi:** `ASCII`, `ord`, `string`

### Treść

Wczytaj napis i wypisz kody ASCII wszystkich jego znaków, oddzielone przecinkiem i spacją `", "`.

### Wejście

* 1. linia: napis

### Wyjście

* 1. linia: kody ASCII oddzielone `, `

### Przykład

**Wejście:**

```
Robot
```

**Wyjście:**

```
82, 111, 98, 111, 116
```

*/

use std::io;

// Funkcja zamieniająca znaki na kody ASCII
// Złożoność czasowa: O(n), gdzie n to długość napisu
// Złożoność pamięciowa: O(n)
fn zamien_na_ascii(napis: &str) -> String {
    napis
        .chars()
        .map(|c| (c as u32).to_string())
        .collect::<Vec<String>>()
        .join(", ")
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let napis = input.trim();
    
    println!("{}", zamien_na_ascii(napis));
}
