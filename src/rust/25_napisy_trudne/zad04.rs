/*
ZAD-04 — Usuń powtórzenia znaków

**Poziom:** ★★★
**Tagi:** `string`, `set`, `unique`, `kolejność`

### Treść

Otrzymujesz napis. Usuń wszystkie powtórzenia znaków tak, aby **każdy znak wystąpił tylko raz**, zachowując **kolejność pierwszych wystąpień**.

### Wejście

* 1 linia: napis `S`

### Wyjście

* 1 linia: napis z unikalnymi znakami

### Przykład

**Wejście:**

```
AAAAAAAAAABBBBBBBBA
```

**Wyjście:**

```
AB
```

*/

use std::collections::HashSet;
use std::io;

// Funkcja usuwająca powtórzenia znaków
// Złożoność czasowa: O(n), gdzie n to długość napisu
// Złożoność pamięciowa: O(n)
fn usun_powtorzenia(napis: &str) -> String {
    let mut widziane = HashSet::new();
    napis.chars().filter(|&c| widziane.insert(c)).collect()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let napis = input.trim();

    println!("{}", usun_powtorzenia(napis));
}
