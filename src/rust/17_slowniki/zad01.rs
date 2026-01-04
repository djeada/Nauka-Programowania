/*
ZAD-01 — Słownik: liczby i ich kwadraty

**Poziom:** ★☆☆
**Tagi:** `dict`, `pętla`

### Treść

Wczytaj liczbę `n`. Utwórz słownik, gdzie klucze to liczby od `1` do `n-1`, a wartości to ich kwadraty.

### Wejście

* 1 linia: `n` (n ≥ 1)

### Wyjście

* Słownik w postaci: `{1: 1, 2: 4, ...}`

### Przykład

**Wejście:**

```
5
```

**Wyjście:**

```
{1: 1, 2: 4, 3: 9, 4: 16}
```

*/

use std::collections::HashMap;
use std::io;

// Funkcja tworząca słownik liczb i ich kwadratów
// Złożoność czasowa: O(n)
// Złożoność pamięciowa: O(n)
fn slownik_kwadraty(n: usize) -> HashMap<usize, usize> {
    let mut slownik = HashMap::new();

    for i in 1..n {
        slownik.insert(i, i * i);
    }

    slownik
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let n: usize = input.trim().parse().unwrap_or(1);

    let slownik = slownik_kwadraty(n);

    // Formatowanie jako słownik w stylu Pythona
    print!("{{");
    let mut first = true;
    for i in 1..n {
        if !first {
            print!(", ");
        }
        print!("{}: {}", i, slownik.get(&i).unwrap_or(&0));
        first = false;
    }
    println!("}}");
}
