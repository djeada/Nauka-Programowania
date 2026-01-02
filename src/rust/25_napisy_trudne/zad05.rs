/*
ZAD-05 — Usuń powtórzenia sąsiadujących znaków

**Poziom:** ★★★
**Tagi:** `string`, `compress`, `run-length`

### Treść

Otrzymujesz napis. Usuń powtórzenia znaków występujących **bezpośrednio obok siebie**, pozostawiając jedno wystąpienie z każdej „serii”.

### Wejście

* 1 linia: napis `S`

### Wyjście

* 1 linia: napis po redukcji sąsiadów

### Przykład

**Wejście:**

```
AAAAAAAAAABBBBBBBBA
```

**Wyjście:**

```
ABA
```

*/

use std::io;

// Funkcja usuwająca powtórzenia sąsiadujących znaków
// Złożoność czasowa: O(n), gdzie n to długość napisu
// Złożoność pamięciowa: O(n)
fn usun_sasiadow(napis: &str) -> String {
    let mut wynik = String::new();
    let mut poprzedni: Option<char> = None;
    
    for c in napis.chars() {
        if Some(c) != poprzedni {
            wynik.push(c);
            poprzedni = Some(c);
        }
    }
    
    wynik
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let napis = input.trim();
    
    println!("{}", usun_sasiadow(napis));
}
