/*
ZAD-18 — Odwróć słowa w zdaniu

**Poziom:** ★★☆
**Tagi:** `split`, `string`, `pętle`

### Treść

Wczytaj zdanie i odwróć litery **w każdym słowie osobno**, zachowując kolejność słów.

### Wejście

* 1. linia: zdanie

### Wyjście

* 1. linia: zdanie z odwróconymi słowami

### Przykład

**Wejście:**

```
Ala ma kota
```

**Wyjście:**

```
alA am atok
```

*/

use std::io;

// Funkcja odwracająca słowa w zdaniu
// Złożoność czasowa: O(n), gdzie n to długość zdania
// Złożoność pamięciowa: O(n)
fn odwroc_slowa(zdanie: &str) -> String {
    zdanie
        .split_whitespace()
        .map(|slowo| slowo.chars().rev().collect::<String>())
        .collect::<Vec<String>>()
        .join(" ")
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let zdanie = input.trim();
    
    println!("{}", odwroc_slowa(zdanie));
}
