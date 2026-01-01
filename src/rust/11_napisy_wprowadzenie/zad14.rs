/*
ZAD-14 — Napis z liczb od 1 do n

**Poziom:** ★☆☆
**Tagi:** `pętle`, `string`

### Treść

Wczytaj `n` i wypisz napis złożony z kolejnych liczb od 1 do `n`, bez separatorów.

### Wejście

* 1. linia: liczba naturalna `n` (n ≥ 1)

### Wyjście

* 1. linia: ciąg `1..n` bez spacji

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
123
```

*/

use std::io;

// Funkcja generująca napis z liczb od 1 do n
// Złożoność czasowa: O(n*log(n)), gdzie log(n) to średnia długość liczby
// Złożoność pamięciowa: O(n*log(n))
fn napis_z_liczb(n: usize) -> String {
    (1..=n).map(|i| i.to_string()).collect()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let n: usize = input.trim().parse().expect("Nieprawidłowa liczba");
    
    println!("{}", napis_z_liczb(n));
}
