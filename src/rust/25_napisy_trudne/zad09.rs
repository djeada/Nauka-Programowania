/*
ZAD-09 — Najdłuższy wspólny podnapis

**Poziom:** ★★★
**Tagi:** `string`, `dp`, `substring`

### Treść

Otrzymujesz dwa napisy. Znajdź **najdłuższy wspólny podnapis** (ciągły fragment), który występuje w obu napisach.

### Wejście

* 1 linia: napis `A`
* 2 linia: napis `B`

### Wyjście

* 1 linia: najdłuższy wspólny podnapis
  (jeśli jest kilka o tej samej długości — wybierz ten, który występuje **najwcześniej w A**; jeśli nadal remis, najwcześniej w B)

### Przykład

**Wejście:**

```
ijkabcdl
xxxxabcd
```

**Wyjście:**

```
abcd
```

*/

use std::io;

// Funkcja znajdująca najdłuższy wspólny podnapis
// Złożoność czasowa: O(n * m), gdzie n i m to długości napisów
// Złożoność pamięciowa: O(n * m)
fn najdluzszy_wspolny_podnapis(a: &str, b: &str) -> String {
    let a_chars: Vec<char> = a.chars().collect();
    let b_chars: Vec<char> = b.chars().collect();
    let n = a_chars.len();
    let m = b_chars.len();

    let mut dp = vec![vec![0; m + 1]; n + 1];
    let mut max_dlugosc = 0;
    let mut koniec_w_a = 0;

    for i in 1..=n {
        for j in 1..=m {
            if a_chars[i - 1] == b_chars[j - 1] {
                dp[i][j] = dp[i - 1][j - 1] + 1;
                if dp[i][j] > max_dlugosc {
                    max_dlugosc = dp[i][j];
                    koniec_w_a = i;
                }
            }
        }
    }

    if max_dlugosc == 0 {
        return String::new();
    }

    a_chars[(koniec_w_a - max_dlugosc)..koniec_w_a]
        .iter()
        .collect()
}

fn main() {
    let mut a_str = String::new();
    io::stdin().read_line(&mut a_str).expect("Błąd wczytywania");
    let a = a_str.trim();

    let mut b_str = String::new();
    io::stdin().read_line(&mut b_str).expect("Błąd wczytywania");
    let b = b_str.trim();

    println!("{}", najdluzszy_wspolny_podnapis(a, b));
}
