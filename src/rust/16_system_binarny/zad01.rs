/*
ZAD-01A — Dziesiętny → binarny

**Poziom:** ★☆☆
**Tagi:** `konwersja`, `binarne`, `pętle`

### Treść

Wczytaj liczbę naturalną w systemie dziesiętnym i wypisz jej reprezentację binarną.

### Wejście

* 1. linia: `n` (liczba naturalna)

### Wyjście

Jedna linia: zapis binarny `n`.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
11
```

### Uwagi o formacie

* Dla `n = 0` wypisz `0`.

ZAD-01B — Binarny → dziesiętny

**Poziom:** ★☆☆
**Tagi:** `konwersja`, `string`, `binarne`

### Treść

Wczytaj liczbę naturalną w systemie binarnym (ciąg `0/1`) i wypisz jej wartość w systemie dziesiętnym.

### Wejście

* 1. linia: `b` (ciąg znaków `0` i `1`)

### Wyjście

Jedna linia: liczba w systemie dziesiętnym.

### Przykład

**Wejście:**

```
101
```

**Wyjście:**

```
5
```

*/

use std::io;

// Funkcja konwertująca dziesiętny na binarny
// Złożoność czasowa: O(log n)
// Złożoność pamięciowa: O(log n)
fn dziesietny_na_binarny(n: u32) -> String {
    if n == 0 {
        return "0".to_string();
    }

    format!("{:b}", n)
}

// Funkcja konwertująca binarny na dziesiętny
// Złożoność czasowa: O(n), gdzie n to długość napisu
// Złożoność pamięciowa: O(1)
fn binarny_na_dziesietny(bin: &str) -> u32 {
    u32::from_str_radix(bin, 2).unwrap_or(0)
}

fn main() {
    // ZAD-01A: Dziesiętny → binarny
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let n: u32 = input.trim().parse().unwrap_or(0);

    println!("{}", dziesietny_na_binarny(n));

    // ZAD-01B: Binarny → dziesiętny (opcjonalnie, jeśli jest drugi input)
    // Można odkomentować poniższy kod dla ZAD-01B
    /*
    let mut bin_input = String::new();
    io::stdin().read_line(&mut bin_input).expect("Błąd wczytywania");
    let bin = bin_input.trim();
    println!("{}", binarny_na_dziesietny(bin));
    */
}
