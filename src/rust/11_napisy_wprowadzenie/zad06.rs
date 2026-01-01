/*
ZAD-06 — Zamień litery „a” na „?”

**Poziom:** ★☆☆
**Tagi:** `string`, `replace`

### Treść

Wczytaj napis i zamień wszystkie wystąpienia litery `a` na znak `?`.

### Wejście

* 1. linia: napis

### Wyjście

* 1. linia: napis po zamianie

### Przykład

**Wejście:**

```
Latarnik
```

**Wyjście:**

```
L?t?rnik
```

*/

use std::io;

// Funkcja zamieniająca litery 'a' na '?'
// Złożoność czasowa: O(n), gdzie n to długość napisu
// Złożoność pamięciowa: O(n)
fn zamien_a_na_pytajnik(napis: &str) -> String {
    napis.replace('a', "?")
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let napis = input.trim();
    
    println!("{}", zamien_a_na_pytajnik(napis));
}
