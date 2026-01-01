/*
ZAD-17 — Konwersja listy na napis

**Poziom:** ★☆☆
**Tagi:** `list`, `string`

### Treść

Otrzymujesz listę liczb naturalnych w zapisie tekstowym (np. `[2, 4, 7]`). Połącz liczby bez separatorów i wypisz jako napis.

### Wejście

* 1. linia: lista w formacie podobnym do Pythona, np. `[2, 4, 7]`

### Wyjście

* 1. linia: napis z połączonych liczb, np. `247`

### Przykład

**Wejście:**

```
[2, 4, 7]
```

**Wyjście:**

```
247
```

### Uwagi

* Najprościej: usuń nawiasy `[` `]`, rozdziel po przecinkach, `strip()`, potem sklej.

*/

use std::io;

// Funkcja konwertująca listę na napis
// Złożoność czasowa: O(n), gdzie n to liczba elementów w liście
// Złożoność pamięciowa: O(n)
fn lista_na_napis(lista_str: &str) -> String {
    // Usuń nawiasy i spacje, podziel po przecinkach
    lista_str
        .trim()
        .trim_start_matches('[')
        .trim_end_matches(']')
        .split(',')
        .map(|s| s.trim())
        .filter(|s| !s.is_empty())
        .collect::<String>()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let lista_str = input.trim();
    
    println!("{}", lista_na_napis(lista_str));
}
