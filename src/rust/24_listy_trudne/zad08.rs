/*
ZAD-08 — Maksymalny zysk ze sprzedaży sznurka

**Poziom:** ★★★
**Tagi:** `dp`, `rod cutting`, `optymalizacja`

### Treść

Masz sznurek o długości `n` i cennik: ceny kawałków długości od `1` do `n`. Możesz pociąć sznurek na kawałki o całkowitych długościach. Znajdź maksymalny zysk.

### Wejście

* 1 linia: lista `prices` (długości 1..n)
* 2 linia: `n` (liczba naturalna)

### Wyjście

* 1 linia: maksymalny zysk (liczba całkowita)

### Przykład

**Wejście:**

```
[1, 5, 8, 9, 10, 17, 17, 20]
4
```

**Wyjście:**

```
10
```

*/

use std::io;

// Funkcja obliczająca maksymalny zysk ze sprzedaży sznurka (rod cutting problem)
// Złożoność czasowa: O(n^2), gdzie n to długość sznurka
// Złożoność pamięciowa: O(n)
fn maksymalny_zysk_sznurek(ceny: &[i32], n: usize) -> i32 {
    let mut dp = vec![0; n + 1];
    
    for i in 1..=n {
        let mut max_zysk = i32::MIN;
        for j in 1..=i {
            if j <= ceny.len() {
                max_zysk = max_zysk.max(ceny[j - 1] + dp[i - j]);
            }
        }
        dp[i] = max_zysk;
    }
    
    dp[n]
}

fn main() {
    let mut ceny_str = String::new();
    io::stdin().read_line(&mut ceny_str).expect("Błąd wczytywania");
    
    let lista_str = ceny_str.trim()
        .trim_start_matches('[')
        .trim_end_matches(']');
    
    let ceny: Vec<i32> = lista_str
        .split(',')
        .filter_map(|s| s.trim().parse().ok())
        .collect();
    
    let mut n_str = String::new();
    io::stdin().read_line(&mut n_str).expect("Błąd wczytywania");
    let n: usize = n_str.trim().parse().unwrap_or(0);
    
    println!("{}", maksymalny_zysk_sznurek(&ceny, n));
}
