/*
ZAD-04 — Wspólny podciąg o największej długości (równe sumy)

**Poziom:** ★★★
**Tagi:** `list`, `prefix`, `hashmap`, `podciąg`

### Treść

Otrzymujesz dwie listy binarne `A` i `B` (zera i jedynki) o tej samej długości. Znajdź **maksymalną długość** podciągu (ciągłych elementów), dla którego suma elementów w podciągu z `A` jest równa sumie elementów w odpowiadającym podciągu z `B` (ten sam zakres indeksów).

### Wejście

* 1 linia: lista binarna `A`
* 2 linia: lista binarna `B` (tej samej długości)

### Wyjście

* 1 linia: maksymalna długość (liczba naturalna)

### Przykład

**Wejście:**

```
[0, 0, 1, 1, 1, 1]
[0, 1, 1, 0, 1, 0]
```

**Wyjście:**

```
5
```

*/

use std::io;
use std::collections::HashMap;

// Funkcja znajdująca maksymalną długość podciągu o równych sumach
// Złożoność czasowa: O(n), gdzie n to długość list
// Złożoność pamięciowa: O(n)
fn max_dlugosc_rownych_sum(a: &[i32], b: &[i32]) -> usize {
    let n = a.len();
    let mut max_dlugosc = 0;
    
    // Obliczamy różnicę sum i szukamy najdłuższego podciągu z różnicą 0
    let mut mapa: HashMap<i32, usize> = HashMap::new();
    mapa.insert(0, 0); // Różnica 0 na pozycji 0
    
    let mut roznica_skumulowana = 0;
    
    for i in 0..n {
        roznica_skumulowana += a[i] - b[i];
        
        if let Some(&poprzednia_poz) = mapa.get(&roznica_skumulowana) {
            max_dlugosc = max_dlugosc.max(i + 1 - poprzednia_poz);
        } else {
            mapa.insert(roznica_skumulowana, i + 1);
        }
    }
    
    max_dlugosc
}

fn main() {
    let mut a_str = String::new();
    io::stdin().read_line(&mut a_str).expect("Błąd wczytywania");
    let lista_a_str = a_str.trim()
        .trim_start_matches('[')
        .trim_end_matches(']');
    let a: Vec<i32> = lista_a_str
        .split(',')
        .filter_map(|s| s.trim().parse().ok())
        .collect();
    
    let mut b_str = String::new();
    io::stdin().read_line(&mut b_str).expect("Błąd wczytywania");
    let lista_b_str = b_str.trim()
        .trim_start_matches('[')
        .trim_end_matches(']');
    let b: Vec<i32> = lista_b_str
        .split(',')
        .filter_map(|s| s.trim().parse().ok())
        .collect();
    
    println!("{}", max_dlugosc_rownych_sum(&a, &b));
}
