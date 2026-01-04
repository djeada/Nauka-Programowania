/*
ZAD-08 — Najdłuższy wspólny przedrostek

**Poziom:** ★★★
**Tagi:** `string`, `prefix`, `list`

### Treść

Otrzymujesz listę napisów (w kolejnych liniach). Znajdź najdłuższy przedrostek wspólny dla wszystkich.

### Wejście

* 1 linia: `n` — liczba napisów
* kolejne `n` linii: napisy

### Wyjście

* 1 linia: najdłuższy wspólny przedrostek (może być pusty)

### Przykład

**Wejście:**

```
3
Remolada
Remux
Remmy
```

**Wyjście:**

```
Rem
```

*/

use std::io;

// Funkcja znajdująca najdłuższy wspólny przedrostek
// Złożoność czasowa: O(n * m), gdzie n to liczba napisów, m to długość najkrótszego
// Złożoność pamięciowa: O(m)
fn najdluzszy_wspolny_przedrostek(napisy: &[String]) -> String {
    if napisy.is_empty() {
        return String::new();
    }

    let pierwszy = &napisy[0];
    let mut przedrostek = String::new();

    for (i, c) in pierwszy.chars().enumerate() {
        // Sprawdź czy wszystkie napisy mają ten znak na pozycji i
        if napisy.iter().all(|s| s.chars().nth(i) == Some(c)) {
            przedrostek.push(c);
        } else {
            break;
        }
    }

    przedrostek
}

fn main() {
    let mut n_str = String::new();
    io::stdin().read_line(&mut n_str).expect("Błąd wczytywania");
    let n: usize = n_str.trim().parse().unwrap_or(0);

    let mut napisy = Vec::new();
    for _ in 0..n {
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Błąd wczytywania");
        napisy.push(input.trim().to_string());
    }

    println!("{}", najdluzszy_wspolny_przedrostek(&napisy));
}
