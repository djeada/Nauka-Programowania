/*
ZAD-07 — Zamiana sąsiadujących bitów

**Poziom:** ★☆☆
**Tagi:** `bitwise`, `maski`, `swap bits`

### Treść

Wczytaj liczbę naturalną `n`. Zamień miejscami każdą parę sąsiadujących bitów w jej zapisie binarnym:

* bit 0 z bitem 1,
* bit 2 z bitem 3,
* bit 4 z bitem 5,
* itd.

Następnie wypisz wynik w systemie dziesiętnym.

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: wynik po zamianie bitów.

### Przykład

**Wejście:**

```
9131
```

**Wyjście:**

```
4951
```

### Uwagi

* Jeśli liczba ma nieparzystą liczbę bitów, najwyższy (samotny) bit pozostaje bez zmian.

*/

use std::io;

// Funkcja zamieniająca sąsiadujące bity
// Złożoność czasowa: O(1)
// Złożoność pamięciowa: O(1)
fn zamien_sasiadujace_bity(n: u32) -> u32 {
    // Wyodrębnij bity parzyste i nieparzyste, następnie zamień
    let parzyste = (n & 0xAAAAAAAA) >> 1; // Bity 1, 3, 5, ... przesunięte w prawo
    let nieparzyste = (n & 0x55555555) << 1; // Bity 0, 2, 4, ... przesunięte w lewo
    parzyste | nieparzyste
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let n: u32 = input.trim().parse().unwrap_or(0);

    println!("{}", zamien_sasiadujace_bity(n));
}
