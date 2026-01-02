/*
ZAD-07 — Podziel tekst względem znaków interpunkcyjnych

**Poziom:** ★☆☆
**Tagi:** `regex`, `string`

### Treść

Otrzymujesz napis (jedno lub kilka zdań). Podziel tekst na fragmenty w miejscach występowania znaków interpunkcyjnych (np. `, . ! ? ; :`). Usuń spacje na początku i końcu każdego fragmentu.

### Wejście

Jedna linia:

* `tekst`

### Wyjście

Każdy fragment w osobnej linii.

### Przykład

**Wejście:**

```
Ani nie poszedł do kina, ani nie wybrał się do teatru.
```

**Wyjście:**

```
Ani nie poszedł do kina
ani nie wybrał się do teatru
```

*/

use std::io;

// Funkcja dzieląca tekst względem znaków interpunkcyjnych
// Złożoność czasowa: O(n), gdzie n to długość tekstu
// Złożoność pamięciowa: O(n)
fn podziel_po_interpunkcji(tekst: &str) -> Vec<String> {
    tekst
        .split(|c: char| matches!(c, ',' | '.' | '!' | '?' | ';' | ':'))
        .map(|fragment| fragment.trim().to_string())
        .filter(|fragment| !fragment.is_empty())
        .collect()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let tekst = input.trim();
    
    let fragmenty = podziel_po_interpunkcji(tekst);
    
    for fragment in fragmenty {
        println!("{}", fragment);
    }
}
