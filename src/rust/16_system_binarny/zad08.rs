/*
ZAD-08 — Najbliższa potęga dwójki (>= n)

**Poziom:** ★☆☆
**Tagi:** `potęgi 2`, `bitwise`, `pętle`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz najmniejszą potęgę liczby 2, która jest **większa lub równa** `n`.

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: najmniejsze `2^k ≥ n`.

### Przykład

**Wejście:**

```
111
```

**Wyjście:**

```
128
```

### Uwagi

* Dla `n = 0` przyjmij wynik `1`.

*/

use std::io;

// Funkcja znajdująca najmniejszą potęgę dwójki >= n
// Złożoność czasowa: O(log n)
// Złożoność pamięciowa: O(1)
fn najblizsza_potega_dwojki(n: u32) -> u32 {
    if n == 0 {
        return 1;
    }

    if n.is_power_of_two() {
        return n;
    }

    n.next_power_of_two()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let n: u32 = input.trim().parse().unwrap_or(0);

    println!("{}", najblizsza_potega_dwojki(n));
}
