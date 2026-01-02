/*
ZAD-05 — Wyodrębnij cyfry z tekstu

**Poziom:** ★☆☆
**Tagi:** `regex`, `string`

### Treść

Otrzymujesz napis zawierający różne znaki. Wyodrębnij wszystkie cyfry i wypisz je jako jeden napis (z zachowaniem kolejności).

### Wejście

Jedna linia:

* `tekst`

### Wyjście

Jedna linia:

* napis złożony tylko z cyfr z tekstu wejściowego

### Przykład

**Wejście:**

```
Terminator2001
```

**Wyjście:**

```
2001
```

*/

use std::io;

// Funkcja wyodrębniająca cyfry z tekstu
// Złożoność czasowa: O(n), gdzie n to długość tekstu
// Złożoność pamięciowa: O(n)
fn wyodrebnij_cyfry(tekst: &str) -> String {
    tekst.chars()
        .filter(|c| c.is_digit(10))
        .collect()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let tekst = input.trim();
    
    println!("{}", wyodrebnij_cyfry(tekst));
}
