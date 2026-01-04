/*
ZAD-16 — Odległość Hamminga

**Poziom:** ★★☆
**Tagi:** `string`, `porównanie`

### Treść

Wczytaj dwa napisy tej samej długości i policz, na ilu pozycjach różnią się znakami.

### Wejście

* 1. linia: napis `s1`
* 2. linia: napis `s2`  (ta sama długość)

### Wyjście

* 1. linia: odległość Hamminga

### Przykład

**Wejście:**

```
adam
axam
```

**Wyjście:**

```
1
```

*/

use std::io;

// Funkcja obliczająca odległość Hamminga
// Złożoność czasowa: O(n), gdzie n to długość napisów
// Złożoność pamięciowa: O(1)
fn odleglosc_hamminga(s1: &str, s2: &str) -> usize {
    s1.chars()
        .zip(s2.chars())
        .filter(|(c1, c2)| c1 != c2)
        .count()
}

fn main() {
    let mut s1 = String::new();
    let mut s2 = String::new();

    io::stdin().read_line(&mut s1).expect("Błąd wczytywania");
    io::stdin().read_line(&mut s2).expect("Błąd wczytywania");

    let s1 = s1.trim();
    let s2 = s2.trim();

    println!("{}", odleglosc_hamminga(s1, s2));
}
