/*
ZAD-03 — Z ilu słów składa się zdanie?

**Poziom:** ★☆☆
**Tagi:** `string`, `split`

### Treść

Wczytaj zdanie i policz, z ilu słów się składa. Znaki interpunkcyjne nie są słowami.

### Wejście

* 1. linia: zdanie

### Wyjście

* 1. linia: liczba słów

### Przykład

**Wejście:**

```
gram na pianinie.
```

**Wyjście:**

```
3
```

### Uwagi o formatowaniu

* Najprościej: podziel po białych znakach, a z końców słów usuń interpunkcję.

*/

use std::io;

// Funkcja licząca słowa w zdaniu (ignoruje interpunkcję)
// Złożoność czasowa: O(n), gdzie n to długość zdania
// Złożoność pamięciowa: O(m), gdzie m to liczba słów
fn policz_slowa(zdanie: &str) -> usize {
    zdanie
        .split_whitespace()
        .map(|slowo| slowo.trim_matches(|c: char| !c.is_alphanumeric()))
        .filter(|slowo| !slowo.is_empty())
        .count()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let zdanie = input.trim();
    
    println!("{}", policz_slowa(zdanie));
}
