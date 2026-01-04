/*
ZAD-05 — Sortowanie listy miast

**Poziom:** ★☆☆
**Tagi:** `class`, `sort`, `obiekty`

### Treść

Masz klasę `Miasto` z polami:

* `nazwa` (napis),
* `liczba_mieszkancow` (liczba naturalna).

Otrzymujesz listę miast.

a) Posortuj miasta alfabetycznie po nazwie.
b) Posortuj miasta rosnąco po liczbie mieszkańców.

Wypisz wyniki w dwóch liniach jako listy w formacie jak w przykładzie.

### Wejście

* 1 linia: liczba naturalna `N`
* następnie `N` linii: `nazwa liczba_mieszkancow` (nazwa bez spacji)

### Wyjście

* 1 linia: lista miast po sortowaniu a)
* 2 linia: lista miast po sortowaniu b)

### Przykład

**Wejście:**

```
3
Paris 2150000
Berlin 3800000
New_York 8400000
```

**Wyjście:**

```
[Miasto("Berlin", 3800000), Miasto("New_York", 8400000), Miasto("Paris", 2150000)]
[Miasto("Paris", 2150000), Miasto("Berlin", 3800000), Miasto("New_York", 8400000)]
```

### Uwagi o formatowaniu

* Wydruk obiektów ma mieć dokładnie format: `Miasto("NAZWA", LICZBA)`.

*/

use std::fmt;
use std::io;

// Struktura reprezentująca miasto
#[derive(Clone, Debug)]
struct Miasto {
    nazwa: String,
    liczba_mieszkancow: u32,
}

impl fmt::Display for Miasto {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Miasto(\"{}\", {})", self.nazwa, self.liczba_mieszkancow)
    }
}

// Funkcja sortująca miasta alfabetycznie po nazwie
// Złożoność czasowa: O(n log n)
// Złożoność pamięciowa: O(n)
fn sortuj_po_nazwie(miasta: &mut Vec<Miasto>) {
    miasta.sort_by(|a, b| a.nazwa.cmp(&b.nazwa));
}

// Funkcja sortująca miasta rosnąco po liczbie mieszkańców
// Złożoność czasowa: O(n log n)
// Złożoność pamięciowa: O(n)
fn sortuj_po_liczbie_mieszkancow(miasta: &mut Vec<Miasto>) {
    miasta.sort_by_key(|m| m.liczba_mieszkancow);
}

fn main() {
    let mut n_str = String::new();
    io::stdin().read_line(&mut n_str).expect("Błąd wczytywania");
    let n: usize = n_str.trim().parse().unwrap_or(0);

    let mut miasta = Vec::new();

    for _ in 0..n {
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Błąd wczytywania");
        let czesci: Vec<&str> = input.trim().split_whitespace().collect();

        if czesci.len() >= 2 {
            let nazwa = czesci[0].to_string();
            let liczba_mieszkancow: u32 = czesci[1].parse().unwrap_or(0);
            miasta.push(Miasto {
                nazwa,
                liczba_mieszkancow,
            });
        }
    }

    // Sortowanie po nazwie
    let mut miasta_a = miasta.clone();
    sortuj_po_nazwie(&mut miasta_a);

    print!("[");
    for (i, miasto) in miasta_a.iter().enumerate() {
        if i > 0 {
            print!(", ");
        }
        print!("{}", miasto);
    }
    println!("]");

    // Sortowanie po liczbie mieszkańców
    let mut miasta_b = miasta.clone();
    sortuj_po_liczbie_mieszkancow(&mut miasta_b);

    print!("[");
    for (i, miasto) in miasta_b.iter().enumerate() {
        if i > 0 {
            print!(", ");
        }
        print!("{}", miasto);
    }
    println!("]");
}
