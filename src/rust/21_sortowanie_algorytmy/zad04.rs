/*
ZAD-04 — Sortowanie przez scalanie

**Poziom:** ★★☆
**Tagi:** `sorting`, `merge-sort`, `recursion`

### Treść

Wczytaj listę liczb całkowitych i posortuj ją rosnąco algorytmem **sortowania przez scalanie**:

1. Jeśli lista ma mniej niż 2 elementy — jest posortowana.
2. Podziel listę na dwie (w miarę) równe części.
3. Rekurencyjnie posortuj obie części.
4. **Scal** dwie posortowane listy w jedną posortowaną.

### Wejście

* 1 linia: lista liczb całkowitych

### Wyjście

* 1 linia: posortowana lista rosnąco

### Przykład

**Wejście:**

```
[6, 2, 1, 4, 27]
```

**Wyjście:**

```
[1, 2, 4, 6, 27]
```

### Uwagi o algorytmie

* Złożoność czasowa: `O(n log n)`.

*/

use std::io;

// Sortowanie przez scalanie (merge sort)
// Złożoność czasowa: O(n log n)
// Złożoność pamięciowa: O(n) dla bufora
fn sort_v1(lista: &mut [i32]) {
    let srodek = lista.len() / 2;

    if srodek == 0 {
        return;
    }

    sort_v1(&mut lista[..srodek]);
    sort_v1(&mut lista[srodek..]);

    let mut ret = lista.to_vec();
    polacz(&lista[..srodek], &lista[srodek..], &mut ret[..]);
    lista.copy_from_slice(&ret);
}

// Funkcja scalająca dwie posortowane listy
fn polacz(lista_a: &[i32], lista_b: &[i32], ret: &mut [i32]) {
    let mut lewo = 0;
    let mut prawo = 0;
    let mut i = 0;

    while lewo < lista_a.len() && prawo < lista_b.len() {
        if lista_a[lewo] <= lista_b[prawo] {
            ret[i] = lista_a[lewo];
            i += 1;
            lewo += 1;
        } else {
            ret[i] = lista_b[prawo];
            i += 1;
            prawo += 1;
        }
    }

    if lewo < lista_a.len() {
        ret[i..].copy_from_slice(&lista_a[lewo..]);
    }

    if prawo < lista_b.len() {
        ret[i..].copy_from_slice(&lista_b[prawo..]);
    }
}

fn parsuj_liste(input: &str) -> Vec<i32> {
    input
        .trim()
        .trim_start_matches('[')
        .trim_end_matches(']')
        .split(',')
        .filter_map(|s| s.trim().parse().ok())
        .collect()
}

fn test_1() {
    let mut lista = vec![4, 2, 5, 3, 1];
    sort_v1(&mut lista);
    assert_eq!(lista, &[1, 2, 3, 4, 5]);
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");

    let mut lista = parsuj_liste(&input);
    sort_v1(&mut lista);

    print!("[");
    for (i, &val) in lista.iter().enumerate() {
        if i > 0 {
            print!(", ");
        }
        print!("{}", val);
    }
    println!("]");
}
