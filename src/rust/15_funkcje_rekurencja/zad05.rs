/*
ZAD-05 — k-ta pochodna wielomianu

**Poziom:** ★★☆
**Tagi:** `pochodna`, `wielomiany`, `I/O`

### Treść

Wczytaj wielomian stopnia `n` oraz liczbę `k`. Wypisz współczynniki wielomianu będącego `k`-tą pochodną.

### Wejście

* 1. linia: `n` — stopień wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb: `a_n ... a_0`
* 3. linia: `k` — rząd pochodnej (`k ≥ 1`)

### Wyjście

* Jeśli po zróżniczkowaniu `k` razy zostaje wielomian niezerowy: wypisz jego współczynniki w jednej linii (spacje).
* Jeśli wielomian „znika” (stopień < k): wypisz dokładnie `[]`.

### Przykład

**Wejście:**

```
2
4 -3 2
1
```

**Wyjście:**

```
8 -3
```

### Uwagi o formatowaniu

* Pochodna: jeśli aktualne współczynniki to `[c_d, c_{d-1}, ..., c_0]`, to pochodna ma współczynniki:
  `[d*c_d, (d-1)*c_{d-1}, ..., 1*c_1]`.

*/

use std::io;

// Funkcja obliczająca k-tą pochodną wielomianu
// Złożoność czasowa: O(n * k), gdzie n to stopień wielomianu
// Złożoność pamięciowa: O(n)
fn pochodna_wielomianu(wspolczynniki: &[i32], k: usize) -> Option<Vec<i32>> {
    if k == 0 {
        return Some(wspolczynniki.to_vec());
    }

    if wspolczynniki.is_empty() {
        return None;
    }

    if wspolczynniki.len() <= k {
        return None;
    }

    let mut wynik = wspolczynniki.to_vec();

    for _ in 0..k {
        if wynik.len() <= 1 {
            return None;
        }

        let mut nowa = Vec::new();
        let stopien = wynik.len() - 1;

        for (i, &w) in wynik.iter().enumerate() {
            if i < wynik.len() - 1 {
                nowa.push(w * (stopien - i) as i32);
            }
        }

        wynik = nowa;
    }

    if wynik.is_empty() {
        None
    } else {
        Some(wynik)
    }
}

fn main() {
    let mut n_str = String::new();
    io::stdin().read_line(&mut n_str).expect("Błąd wczytywania");

    let mut wspolczynniki_str = String::new();
    io::stdin()
        .read_line(&mut wspolczynniki_str)
        .expect("Błąd wczytywania");
    let wspolczynniki: Vec<i32> = wspolczynniki_str
        .trim()
        .split_whitespace()
        .map(|s| s.parse().expect("Nieprawidłowa liczba"))
        .collect();

    let mut k_str = String::new();
    io::stdin().read_line(&mut k_str).expect("Błąd wczytywania");
    let k: usize = k_str.trim().parse().expect("Nieprawidłowa liczba");

    match pochodna_wielomianu(&wspolczynniki, k) {
        Some(wynik) => {
            for (i, &w) in wynik.iter().enumerate() {
                if i > 0 {
                    print!(" ");
                }
                print!("{}", w);
            }
            println!();
        }
        None => {
            println!("[]");
        }
    }
}
