/*
ZAD-02 — Usuń podnapis

**Poziom:** ★★☆
**Tagi:** `string`, `replace`, `substring`

### Treść

Dostajesz dwa napisy:

1. Napis główny,
2. Podnapis do usunięcia.

Usuń **wszystkie wystąpienia** podnapisu z napisu głównego.

### Wejście

* 1 linia: napis `S`
* 2 linia: napis `T` (do usunięcia)

### Wyjście

* 1 linia: wynikowy napis po usunięciu wszystkich wystąpień

### Przykład

**Wejście:**

```
Lezy jezy na wiezy
zy
```

**Wyjście:**

```
Le je na wie
```

*/

use std::io;

// Funkcja usuwająca podnapis
// Złożoność czasowa: O(n * m), gdzie n to długość napisu, m to długość podnapisu
// Złożoność pamięciowa: O(n)
fn usun_podnapis(napis: &str, podnapis: &str) -> String {
    napis.replace(podnapis, "")
}

fn main() {
    let mut s_str = String::new();
    io::stdin().read_line(&mut s_str).expect("Błąd wczytywania");
    let s = s_str.trim();

    let mut t_str = String::new();
    io::stdin().read_line(&mut t_str).expect("Błąd wczytywania");
    let t = t_str.trim();

    println!("{}", usun_podnapis(s, t));
}
