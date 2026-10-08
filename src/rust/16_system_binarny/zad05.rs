/*
ZAD-05A — Minimum bez instrukcji warunkowych

**Poziom:** ★★☆
**Tagi:** `bit-trick`, `min/max`, `bez if`

### Treść

Wczytaj dwie liczby całkowite `a` i `b`. Wypisz mniejszą z nich **bez użycia instrukcji warunkowych** (`if`, wyrażenia `x if warunek else y`) i bez funkcji `min`, `max`, `abs`, `sorted`.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba całkowita: mniejsza z liczb `a` i `b` (gdy są równe — ich wspólna wartość).

### Ograniczenia

* $-10^9 \le a, b \le 10^9$ — w tym zadaniu liczby **mogą być ujemne**

### Przykład

**Wejście:**

```
3
2
```

**Wyjście:**

```
2
```

### Uwagi

* Dopuszczalne są operacje arytmetyczne i bitowe.
* Wskazówka: dla `d = a - b` wyrażenie `d >> 63` daje `-1` (same jedynki w zapisie binarnym), gdy `d < 0`, oraz `0`, gdy `d ≥ 0`. Wtedy `d & (d >> 63)` jest równe `d` albo `0`.
* Tą samą sztuczką otrzymasz maksimum: `a - (d & (d >> 63))`.

ZAD-05B — Wartość bezwzględna bez instrukcji warunkowych

**Poziom:** ★★☆
**Tagi:** `bit-trick`, `maski`, `bez if`

### Treść

Wczytaj liczbę całkowitą `x` i wypisz jej wartość bezwzględną $|x|$ **bez użycia instrukcji warunkowych** (`if`, wyrażenia `x if warunek else y`) i bez funkcji `abs`, `min`, `max`, `sorted`.

### Wejście

* 1. linia: `x`

### Wyjście

Jedna liczba naturalna: $|x|$.

### Ograniczenia

* $-10^9 \le x \le 10^9$ — liczba **może być ujemna**

### Przykład

**Wejście:**

```
-12
```

**Wyjście:**

```
12
```

### Uwagi

* Dopuszczalne są operacje arytmetyczne i bitowe; porównania (`<`, `>`) nie są potrzebne.
* Tak jak w ZAD-05A, **maska znaku** `m = x >> 63` jest równa `-1` (same jedynki), gdy `x < 0`, oraz `0`, gdy `x ≥ 0`.
* XOR z maską `0` nic nie zmienia, a XOR z maską `-1` odwraca wszystkie bity, czyli daje $-x - 1$ (tak liczby ujemne zapisuje kod uzupełnień do dwóch). Wystarczy więc obliczyć `(x ^ m) - m`.

*/
use std::env;
use std::io::{self, Read};

// ZAD-05A: minimum bez instrukcji warunkowych
// Złożoność czasowa: O(1)
// Złożoność pamięciowa: O(1)
fn min_bez_if(a: i64, b: i64) -> i64 {
    let roznica = a - b;
    let maska = roznica >> 63; // -1 jeśli a < b, 0 w przeciwnym razie
    b + (roznica & maska)
}

// ZAD-05B: wartość bezwzględna bez instrukcji warunkowych
// maska = x >> 63 to -1 dla x < 0 i 0 dla x >= 0, więc (x ^ maska) - maska to x albo -x
// Złożoność czasowa: O(1)
// Złożoność pamięciowa: O(1)
fn wartosc_bezwzgledna(x: i64) -> i64 {
    let maska = x >> 63;
    (x ^ maska) - maska
}

fn main() {
    let mut dane = String::new();
    io::stdin()
        .read_to_string(&mut dane)
        .expect("Błąd wczytywania");
    let liczby: Vec<i64> = dane
        .split_whitespace()
        .map(|x| x.parse().expect("Niepoprawna liczba"))
        .collect();

    // Podpunkt wybierany argumentem: zad05 A|B < dane.txt (domyślnie A)
    match env::args().nth(1).as_deref() {
        Some("B") => println!("{}", wartosc_bezwzgledna(liczby[0])),
        _ => println!("{}", min_bez_if(liczby[0], liczby[1])),
    }
}
