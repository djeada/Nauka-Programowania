/*
ZAD-08 — Wypisz pionowo słowa ze zdania

**Poziom:** ★☆☆
**Tagi:** `split`, `string`

### Treść

Wczytaj zdanie, podziel na słowa i wypisz każde słowo w osobnej linii. Interpunkcja nie jest słowem.

### Wejście

* 1. linia: zdanie

### Wyjście

* wiele linii: słowa w kolejności występowania

### Przykład

**Wejście:**

```
Ala ma kota
```

**Wyjście:**

```
Ala
ma
kota
```

*/

use std::io;

// Funkcja wypisująca słowa pionowo (ignoruje interpunkcję)
// Złożoność czasowa: O(n), gdzie n to długość zdania
// Złożoność pamięciowa: O(m), gdzie m to liczba słów
fn wypisz_slowa_pionowo(zdanie: &str) {
    for slowo in zdanie.split_whitespace() {
        let oczyszczone = slowo.trim_matches(|c: char| !c.is_alphanumeric());
        if !oczyszczone.is_empty() {
            println!("{}", oczyszczone);
        }
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let zdanie = input.trim();

    wypisz_slowa_pionowo(zdanie);
}
