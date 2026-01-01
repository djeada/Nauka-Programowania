/*
ZAD-15 — Słowa jako lista

**Poziom:** ★☆☆
**Tagi:** `split`, `list`

### Treść

Wczytaj zdanie i wypisz listę słów w formacie `["Ala", "ma", "kota"]`.

### Wejście

* 1. linia: zdanie

### Wyjście

* 1. linia: lista słów (jak w przykładzie)

### Przykład

**Wejście:**

```
Ala ma kota
```

**Wyjście:**

```
["Ala", "ma", "kota"]
```

*/

use std::io;

// Funkcja formatująca słowa jako lista
// Złożoność czasowa: O(n), gdzie n to długość zdania
// Złożoność pamięciowa: O(m), gdzie m to liczba słów
fn slowa_jako_lista(zdanie: &str) -> String {
    let slowa: Vec<&str> = zdanie.split_whitespace().collect();
    
    let sformatowane: Vec<String> = slowa
        .iter()
        .map(|s| format!("\"{}\"", s))
        .collect();
    
    format!("[{}]", sformatowane.join(", "))
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let zdanie = input.trim();
    
    println!("{}", slowa_jako_lista(zdanie));
}
