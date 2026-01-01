/*
ZAD-11 — Średnia długość słów

**Poziom:** ★☆☆
**Tagi:** `string`, `arytmetyka`

### Treść

Wczytaj zdanie i oblicz średnią długość słów. Wynik ma być liczbą całkowitą.

### Wejście

* 1. linia: zdanie

### Wyjście

* 1. linia: średnia długość słów (liczba całkowita)

### Przykład

**Wejście:**

```
Zepsuty rower.
```

**Wyjście:**

```
6
```

### Uwagi

* Licz jako: `suma_dlugosci // liczba_slow` (dzielenie całkowite).

*/

use std::io;

// Funkcja obliczająca średnią długość słów
// Złożoność czasowa: O(n), gdzie n to długość zdania
// Złożoność pamięciowa: O(m), gdzie m to liczba słów
fn srednia_dlugosc_slow(zdanie: &str) -> usize {
    let slowa: Vec<String> = zdanie
        .split_whitespace()
        .map(|s| s.trim_matches(|c: char| !c.is_alphanumeric()).to_string())
        .filter(|s| !s.is_empty())
        .collect();
    
    if slowa.is_empty() {
        return 0;
    }
    
    let suma: usize = slowa.iter().map(|s| s.chars().count()).sum();
    suma / slowa.len()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let zdanie = input.trim();
    
    println!("{}", srednia_dlugosc_slow(zdanie));
}
