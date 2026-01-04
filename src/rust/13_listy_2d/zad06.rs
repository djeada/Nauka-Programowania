/*
ZAD-06 — Scalanie przedziałów

**Poziom:** ★★☆
**Tagi:** `sortowanie`, `przedziały`, `algorytmy`

### Treść

Wczytaj `n` przedziałów `[a_i, b_i]` (a_i ≤ b_i). Scal przedziały nachodzące na siebie i wypisz wynik w kolejności rosnącej po początku.

### Wejście

* 1. linia: `n`
* następnie `n` linii: `a_i b_i`

### Wyjście

* Każdy scalony przedział w osobnej linii: `a b`

### Przykład

**Wejście:**

```
7
23 67
23 53
45 88
77 88
10 22
11 12
42 45
```

**Wyjście:**

```
10 22
23 88
```

### Uwagi

* Przedziały uznajemy za nachodzące, gdy `next_start <= current_end`.

*/

use std::io;

// Struktura reprezentująca przedział
#[derive(Debug, Clone, Copy)]
struct Przedzial {
    poczatek: i32,
    koniec: i32,
}

// Funkcja scalająca przedziały
// Złożoność czasowa: O(n log n) przez sortowanie
// Złożoność pamięciowa: O(n)
fn scal_przedzialy(mut przedzialy: Vec<Przedzial>) -> Vec<Przedzial> {
    if przedzialy.is_empty() {
        return Vec::new();
    }

    // Sortuj według początku przedziałów
    przedzialy.sort_by_key(|p| p.poczatek);

    let mut wynik = Vec::new();
    let mut aktualny = przedzialy[0];

    for i in 1..przedzialy.len() {
        if przedzialy[i].poczatek <= aktualny.koniec {
            // Przedziały nachodzą na siebie - scal
            aktualny.koniec = aktualny.koniec.max(przedzialy[i].koniec);
        } else {
            // Nie nachodzą - dodaj aktualny i zacznij nowy
            wynik.push(aktualny);
            aktualny = przedzialy[i];
        }
    }

    wynik.push(aktualny);
    wynik
}

fn main() {
    let mut n_str = String::new();
    io::stdin().read_line(&mut n_str).expect("Błąd wczytywania");
    let n: usize = n_str.trim().parse().expect("Nieprawidłowa liczba");

    let mut przedzialy = Vec::new();

    for _ in 0..n {
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Błąd wczytywania");
        let liczby: Vec<i32> = input
            .trim()
            .split_whitespace()
            .map(|s| s.parse().expect("Nieprawidłowa liczba"))
            .collect();

        przedzialy.push(Przedzial {
            poczatek: liczby[0],
            koniec: liczby[1],
        });
    }

    let scalone = scal_przedzialy(przedzialy);

    for p in scalone {
        println!("{} {}", p.poczatek, p.koniec);
    }
}
