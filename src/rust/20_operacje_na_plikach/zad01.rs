/*
ZAD-01 — Czy ścieżka istnieje?

**Poziom:** ★☆☆
**Tagi:** `files`, `path`, `os`, `pathlib`

### Treść

Otrzymujesz ścieżkę w systemie plików. Sprawdź, czy odnosi się do istniejącego **pliku lub folderu**.

### Wejście

* 1 linia: `path` (napis — ścieżka)

### Wyjście

* 1 linia: `Prawda` jeśli ścieżka istnieje, w przeciwnym razie `Fałsz`

### Przykład

**Wejście:**

```
C:\Users\Username\Documents\plik.txt
```

**Wyjście:**

```
Prawda
```

*/

use std::io;
use std::path::Path;

// Funkcja sprawdzająca czy ścieżka istnieje
// Złożoność czasowa: O(1) - wywołanie systemowe
// Złożoność pamięciowa: O(1)
fn czy_sciezka_istnieje(sciezka: &str) -> bool {
    Path::new(sciezka).exists()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let sciezka = input.trim();

    if czy_sciezka_istnieje(sciezka) {
        println!("Prawda");
    } else {
        println!("Fałsz");
    }
}
