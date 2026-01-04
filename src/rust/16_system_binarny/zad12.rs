/*
ZAD-12 — Najdłuższy ciąg zer otoczony jedynkami

**Poziom:** ★★★
**Tagi:** `binarne`, `binary gap`, `pętle`

### Treść

Wczytaj liczbę naturalną `n`. W jej reprezentacji binarnej znajdź długość najdłuższego ciągu kolejnych zer, który jest **z obu stron otoczony jedynkami** (tzw. *binary gap*).

Jeśli nie ma takiego ciągu — wypisz `0`.

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: długość najdłuższego „gapu”.

### Przykład

**Wejście:**

```
14
```

**Wyjście:**

```
0
```

### Uwagi (ważne)

* `14` ma zapis `1110` — zero na końcu **nie jest otoczone jedynkami z prawej**, więc wynik to `0`.
  Dla przykładu `20` (`10100`) najdłuższy gap ma długość `1` (między `1` i `1`).

*/

use std::io;

// Funkcja znajdująca najdłuższy ciąg zer otoczony jedynkami (binary gap)
// Złożoność czasowa: O(log n)
// Złożoność pamięciowa: O(log n)
fn najdluzszy_binary_gap(n: u32) -> usize {
    let binarny = format!("{:b}", n);
    let mut max_gap = 0;
    let mut obecny_gap = 0;
    let mut w_gap = false;

    for c in binarny.chars() {
        if c == '1' {
            if w_gap {
                max_gap = max_gap.max(obecny_gap);
            }
            obecny_gap = 0;
            w_gap = true;
        } else if w_gap {
            obecny_gap += 1;
        }
    }

    max_gap
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let n: u32 = input.trim().parse().unwrap_or(0);

    println!("{}", najdluzszy_binary_gap(n));
}
