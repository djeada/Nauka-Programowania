/*
ZAD-04 — Sortowanie napisów według długości

**Poziom:** ★☆☆
**Tagi:** `sort`, `string`, `list`

### Treść

Otrzymujesz listę napisów. Posortuj ją rosnąco według długości napisów.

### Wejście

* 1 linia: liczba naturalna `N`
* następnie `N` linii: napis (bez spacji)

### Wyjście

* 1 linia: lista napisów posortowana jak w przykładzie

### Przykład

**Wejście:**

```
4
abcd
ab
a
abc
```

**Wyjście:**

```
['a', 'ab', 'abc', 'abcd']
```

*/

use std::io;

// Funkcja sortująca napisy według długości
// Złożoność czasowa: O(n log n)
// Złożoność pamięciowa: O(n)
fn sortuj_po_dlugosci(napisy: &mut Vec<String>) {
    napisy.sort_by_key(|s| s.len());
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

    sortuj_po_dlugosci(&mut napisy);

    print!("[");
    for (i, napis) in napisy.iter().enumerate() {
        if i > 0 {
            print!(", ");
        }
        print!("'{}'", napis);
    }
    println!("]");
}
