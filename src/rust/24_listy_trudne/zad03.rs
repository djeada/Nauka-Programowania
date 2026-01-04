/*
ZAD-03 — Minimalny iloczyn trzech liczb

**Poziom:** ★★☆
**Tagi:** `list`, `min`, `math`

### Treść

Otrzymujesz listę liczb całkowitych. Znajdź **najmniejszy możliwy iloczyn trzech liczb** wybranych z tej listy.

Jeśli lista zawiera mniej niż 3 liczby — wypisz iloczyn wszystkich elementów listy.

### Wejście

* 1 linia: lista liczb całkowitych `A`

### Wyjście

* 1 linia: jedna liczba całkowita

### Przykład

**Wejście:**

```
[3, -1, -3, 2, 9, 4]
```

**Wyjście:**

```
-108
```

*/

use std::io;

// Funkcja znajdująca minimalny iloczyn trzech liczb
// Złożoność czasowa: O(n log n) z powodu sortowania
// Złożoność pamięciowa: O(1)
fn minimalny_iloczyn_trzech(lista: &[i32]) -> i64 {
    let n = lista.len();

    if n < 3 {
        // Jeśli mniej niż 3 liczby, zwróć iloczyn wszystkich
        return lista.iter().map(|&x| x as i64).product();
    }

    let mut sorted = lista.to_vec();
    sorted.sort();

    // Minimalny iloczyn to albo:
    // 1. Trzy najmniejsze liczby (jeśli są wszystkie ujemne)
    // 2. Dwie najmniejsze (ujemne) i największa dodatnia
    // 3. Największa ujemna i dwie najmniejsze dodatnie

    let iloczyn1 = (sorted[0] as i64) * (sorted[1] as i64) * (sorted[2] as i64);
    let iloczyn2 = (sorted[0] as i64) * (sorted[1] as i64) * (sorted[n - 1] as i64);
    let iloczyn3 = (sorted[0] as i64) * (sorted[n - 2] as i64) * (sorted[n - 1] as i64);

    iloczyn1.min(iloczyn2).min(iloczyn3)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");

    // Parsuj listę z formatu [3, -1, -3, ...]
    let lista_str = input.trim().trim_start_matches('[').trim_end_matches(']');

    let lista: Vec<i32> = lista_str
        .split(',')
        .filter_map(|s| s.trim().parse().ok())
        .collect();

    println!("{}", minimalny_iloczyn_trzech(&lista));
}
