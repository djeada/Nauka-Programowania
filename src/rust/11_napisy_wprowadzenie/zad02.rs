/*
ZAD-02 — Policz wystąpienia znaku

**Poziom:** ★☆☆
**Tagi:** `string`, `count`

### Treść

Wczytaj napis oraz jeden znak. Wypisz, ile razy ten znak występuje w napisie.

### Wejście

* 1. linia: napis
* 2. linia: pojedynczy znak

### Wyjście

* 1. linia: liczba wystąpień

### Przykład

**Wejście:**

```
klamra
a
```

**Wyjście:**

```
2
```

*/

use std::io;

// Funkcja licząca wystąpienia znaku w napisie
// Złożoność czasowa: O(n), gdzie n to długość napisu
// Złożoność pamięciowa: O(1)
fn policz_wystapienia(napis: &str, znak: char) -> usize {
    napis.chars().filter(|&c| c == znak).count()
}

fn main() {
    let mut napis = String::new();
    let mut znak = String::new();

    io::stdin().read_line(&mut napis).expect("Błąd wczytywania");
    io::stdin().read_line(&mut znak).expect("Błąd wczytywania");

    let napis = napis.trim();
    let znak = znak.trim().chars().next().unwrap_or(' ');

    println!("{}", policz_wystapienia(napis, znak));
}
