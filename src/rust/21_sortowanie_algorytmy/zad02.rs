/*
ZAD-02 — Sortowanie przez wybieranie

**Poziom:** ★★☆
**Tagi:** `sorting`, `selection-sort`, `list`

### Treść

Wczytaj listę liczb całkowitych i posortuj ją rosnąco algorytmem **sortowania przez wybieranie**.
Dla każdej pozycji `i` znajdź najmniejszy element w zakresie `i..koniec` i zamień go z elementem na pozycji `i`.

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

* Złożoność czasowa: `O(n^2)`.

*/

use std::io;

// Sortowanie przez wybieranie - wersja 1
// Złożoność czasowa: O(n^2)
// Złożoność pamięciowa: O(1)
fn sort_v1(lista: &mut [i32]) {
    for i in 0..lista.len() {
        let mut min_idx = i;
        for j in (i + 1)..lista.len() {
            if lista[min_idx] > lista[j] {
                min_idx = j;
            }
        }
        lista.swap(i, min_idx);
    }
}

// Sortowanie przez wybieranie - wersja 2 (z iteratorami)
// Złożoność czasowa: O(n^2)
// Złożoność pamięciowa: O(1)
fn sort_v2(lista: &mut [i32]) {
    for x in 0..lista.len() {
        let min = lista[x..]
            .iter()
            .enumerate()
            .min_by_key(|&(_, v)| v)
            .map(|(i, _)| x + i)
            .expect("lista is non-empty");

        if x != min {
            lista.swap(x, min);
        }
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

fn test_2() {
    let mut lista = vec![4, 2, 5, 3, 1];
    sort_v2(&mut lista);
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
