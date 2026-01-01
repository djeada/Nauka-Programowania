/*
ZAD-04A — Liczba zer w zapisie binarnym

**Poziom:** ★☆☆
**Tagi:** `binarne`, `zliczanie`

### Treść

Wczytaj liczbę naturalną `n`. Policz, ile znaków `0` zawiera jej binarna reprezentacja (bez wiodących zer).

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: liczba zer w zapisie binarnym `n`.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
0
```

### Uwagi

* Dla `n = 0` binarnie to `0`, więc liczba zer wynosi `1`.

ZAD-04B — Liczba jedynek w zapisie binarnym

**Poziom:** ★☆☆
**Tagi:** `popcount`, `binarne`

### Treść

Wczytaj `n`. Policz, ile bitów `1` ma liczba w zapisie binarnym.

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: liczba jedynek w zapisie binarnym `n`.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
2
```

*/

use std::io;

// Funkcja licząca zera w zapisie binarnym
// Złożoność czasowa: O(log n)
// Złożoność pamięciowa: O(1)
fn licz_zera_binarne(n: u32) -> u32 {
    if n == 0 {
        return 1;
    }
    
    let binarny = format!("{:b}", n);
    binarny.chars().filter(|&c| c == '0').count() as u32
}

// Funkcja licząca jedynki w zapisie binarnym (popcount)
// Złożoność czasowa: O(log n)
// Złożoność pamięciowa: O(1)
fn licz_jedynki_binarne(n: u32) -> u32 {
    n.count_ones()
}

fn main() {
    // ZAD-04A: Liczba zer w zapisie binarnym
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let n: u32 = input.trim().parse().unwrap_or(0);
    
    println!("{}", licz_zera_binarne(n));
    
    // ZAD-04B: Liczba jedynek w zapisie binarnym (opcjonalnie)
    // println!("{}", licz_jedynki_binarne(n));
}
