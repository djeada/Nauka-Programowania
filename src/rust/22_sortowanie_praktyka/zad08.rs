/*
ZAD-08 — Indeks klucza w cyklicznie posortowanej liście

**Poziom:** ★★☆
**Tagi:** `binary search`, `rotacja`, `list`

### Treść

Otrzymujesz cyklicznie posortowaną listę liczb całkowitych (lista była rosnąca, ale została przesunięta) oraz klucz. Znajdź indeks **pierwszego** wystąpienia klucza. Jeśli klucza nie ma — wypisz `-1`.

### Wejście

* 1 linia: liczba naturalna `N`
* 2 linia: `N` liczb całkowitych oddzielonych spacjami
* 3 linia: liczba całkowita `x` (szukany klucz)

### Wyjście

* 1 linia: indeks pierwszego wystąpienia `x` albo `-1`

### Przykład

**Wejście:**

```
6
3 4 5 6 1 2
4
```

**Wyjście:**

```
1
```

### Ograniczenia / gwarancje

* Lista jest wynikiem rotacji listy posortowanej niemalejąco (mogą wystąpić duplikaty).

*/

use std::io;

// Funkcja szukająca klucza w cyklicznie posortowanej liście
// Złożoność czasowa: O(n) - w najgorszym przypadku z duplikatami
// Złożoność pamięciowa: O(1)
fn znajdz_klucz_w_cyklicznej(lista: &[i32], klucz: i32) -> i32 {
    // Szukamy pierwszego wystąpienia klucza
    for (i, &val) in lista.iter().enumerate() {
        if val == klucz {
            return i as i32;
        }
    }
    -1
}

fn main() {
    let mut n_str = String::new();
    io::stdin().read_line(&mut n_str).expect("Błąd wczytywania");
    let _n: usize = n_str.trim().parse().unwrap_or(0);
    
    let mut lista_str = String::new();
    io::stdin().read_line(&mut lista_str).expect("Błąd wczytywania");
    
    let lista: Vec<i32> = lista_str
        .trim()
        .split_whitespace()
        .filter_map(|s| s.parse().ok())
        .collect();
    
    let mut klucz_str = String::new();
    io::stdin().read_line(&mut klucz_str).expect("Błąd wczytywania");
    let klucz: i32 = klucz_str.trim().parse().unwrap_or(0);
    
    let wynik = znajdz_klucz_w_cyklicznej(&lista, klucz);
    println!("{}", wynik);
}
