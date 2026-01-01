/*
ZAD-10 — Najdłuższe i najkrótsze słowo

**Poziom:** ★☆☆
**Tagi:** `string`, `min/max`, `len`

### Treść

Wczytaj zdanie i znajdź:

a) najdłuższe słowo,
b) najkrótsze słowo.

Jeśli jest remis, wybierz słowo, które występuje wcześniej.

### Wejście

* 1. linia: zdanie

### Wyjście

* 1. linia: najdłuższe słowo
* 2. linia: najkrótsze słowo

### Przykład

**Wejście:**

```
Kaczka lubi wiosnę.
```

**Wyjście:**

```
Kaczka
lubi
```

*/

use std::io;

// Funkcja znajdująca najdłuższe i najkrótsze słowo
// Złożoność czasowa: O(n*m), gdzie n to liczba słów, m to średnia długość słowa
// Złożoność pamięciowa: O(n*m)
fn znajdz_najdluzsze_i_najkrotsze(zdanie: &str) -> (String, String) {
    let slowa: Vec<String> = zdanie
        .split_whitespace()
        .map(|s| s.trim_matches(|c: char| !c.is_alphanumeric()).to_string())
        .filter(|s| !s.is_empty())
        .collect();
    
    if slowa.is_empty() {
        return (String::new(), String::new());
    }
    
    let mut najdluzsze = &slowa[0];
    let mut najkrotsze = &slowa[0];
    
    for slowo in &slowa {
        if slowo.chars().count() > najdluzsze.chars().count() {
            najdluzsze = slowo;
        }
        if slowo.chars().count() < najkrotsze.chars().count() {
            najkrotsze = slowo;
        }
    }
    
    (najdluzsze.clone(), najkrotsze.clone())
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let zdanie = input.trim();
    
    let (najdluzsze, najkrotsze) = znajdz_najdluzsze_i_najkrotsze(zdanie);
    println!("{}", najdluzsze);
    println!("{}", najkrotsze);
}
