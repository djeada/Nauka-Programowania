/*
ZAD-03 — Sortowanie przez wstawianie

**Poziom:** ★★☆
**Tagi:** `sorting`, `insertion-sort`, `list`

### Treść

Wczytaj listę liczb całkowitych i posortuj ją rosnąco algorytmem **sortowania przez wstawianie**.
Buduj posortowany fragment od lewej strony: każdy kolejny element „wstaw” w odpowiednie miejsce, przesuwając większe elementy w prawo.

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

* Działa bardzo dobrze dla danych prawie posortowanych.

*/

use std::io;

// Sortowanie przez wstawianie - wersja 1 (klasyczna)
// Złożoność czasowa: O(n^2) w najgorszym przypadku, O(n) dla posortowanych
// Złożoność pamięciowa: O(1)
fn sort_v1(lista: &mut [i32]) {
    for i in 1..lista.len() {
        let mut j = i;
        while j > 0 && lista[j - 1] > lista[j] {
            lista.swap(j - 1, j);
            j -= 1;
        }
    }
}

// Sortowanie przez wstawianie - wersja 2 (z wyszukiwaniem binarnym)
// Złożoność czasowa: O(n^2) (przesunięcia dominują)
// Złożoność pamięciowa: O(1)
fn sort_v2(lista: &mut [i32]) {
    for x in 1..lista.len() {
        let i = match lista[..x].binary_search(&lista[x]) {
            Ok(i) => i,
            Err(i) => i,
        };
        lista[i..=x].rotate_right(1);
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
