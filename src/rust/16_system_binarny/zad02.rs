/*
ZAD-02A — Wypisz binarnie tylko gdy liczba parzysta

**Poziom:** ★☆☆
**Tagi:** `warunki`, `parzystość`, `binarne`

### Treść

Wczytaj liczbę naturalną `n`. Jeśli `n` jest parzysta — wypisz jej zapis binarny. W przeciwnym razie nie wypisuj nic.

### Wejście

* 1. linia: `n` (liczba naturalna)

### Wyjście

* Jeśli `n % 2 == 0`: jedna linia z zapisem binarnym `n`
* W przeciwnym razie: brak wyjścia

### Przykład

**Wejście:**

```
7
```

**Wyjście:** *(brak)*

ZAD-02B — Wypisz binarnie tylko gdy liczba pierwsza

**Poziom:** ★☆☆
**Tagi:** `pierwszość`, `warunki`, `binarne`

### Treść

Wczytaj liczbę naturalną `n`. Jeśli `n` jest liczbą pierwszą — wypisz jej zapis binarny. W przeciwnym razie nie wypisuj nic.

### Wejście

* 1. linia: `n` (liczba naturalna)

### Wyjście

* Jeśli `n` jest pierwsza: jedna linia z zapisem binarnym `n`
* W przeciwnym razie: brak wyjścia

### Przykład

**Wejście:**

```
7
```

**Wyjście:**

```
111
```

*/

use std::io;

// Funkcja sprawdzająca parzystość
fn czy_parzysta(n: u32) -> bool {
    n % 2 == 0
}

// Funkcja sprawdzająca pierwszość
// Złożoność czasowa: O(sqrt(n))
// Złożoność pamięciowa: O(1)
fn czy_pierwsza(n: u32) -> bool {
    if n < 2 {
        return false;
    }
    if n == 2 {
        return true;
    }
    if n % 2 == 0 {
        return false;
    }

    let mut i = 3;
    while i * i <= n {
        if n % i == 0 {
            return false;
        }
        i += 2;
    }
    true
}

fn main() {
    // ZAD-02A: Wypisz binarnie tylko gdy liczba parzysta
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let n: u32 = input.trim().parse().unwrap_or(0);

    if czy_parzysta(n) {
        println!("{:b}", n);
    }

    // ZAD-02B: Wypisz binarnie tylko gdy liczba pierwsza (opcjonalnie)
    // Odkomentować poniższy kod dla ZAD-02B
    /*
    if czy_pierwsza(n) {
        println!("{:b}", n);
    }
    */
}
