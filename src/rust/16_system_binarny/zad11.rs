/*
ZAD-11 — Palindrom w systemie binarnym

**Poziom:** ★★☆
**Tagi:** `binarne`, `palindrom`, `string`

### Treść

Wczytaj liczbę naturalną `n`. Sprawdź, czy jej reprezentacja binarna (bez wiodących zer) jest palindromem.

Wypisz:

* `Prawda` — jeśli tak,
* `Fałsz` — jeśli nie.

### Wejście

* 1. linia: `n`

### Wyjście

Jedno słowo: `Prawda` lub `Fałsz`.

### Przykład

**Wejście:**

```
26
```

**Wyjście:**

```
Fałsz
```

### Uwagi (ważne)

* `26` ma zapis binarny `11010`, który **nie** jest palindromem.
  (W Twoim wcześniejszym przykładzie było to opisane błędnie — tu trzymamy się definicji palindromu 1:1.)

*/

use std::io;

// Funkcja sprawdzająca czy zapis binarny jest palindromem
// Złożoność czasowa: O(log n)
// Złożoność pamięciowa: O(log n)
fn czy_palindrom_binarny(n: u32) -> bool {
    let binarny = format!("{:b}", n);
    let odwrocony: String = binarny.chars().rev().collect();
    binarny == odwrocony
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let n: u32 = input.trim().parse().unwrap_or(0);
    
    if czy_palindrom_binarny(n) {
        println!("Prawda");
    } else {
        println!("Fałsz");
    }
}
