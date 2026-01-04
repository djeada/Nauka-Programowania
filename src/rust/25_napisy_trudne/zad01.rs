/*
ZAD-01 — Podmiana słowa w zdaniu

**Poziom:** ★★☆
**Tagi:** `string`, `replace`, `substring`

### Treść

Masz trzy napisy:

1. Zdanie (tekst do modyfikacji),
2. Słowo A (podnapis do znalezienia),
3. Słowo B (podnapis zastępujący).

Zamień **wszystkie wystąpienia** słowa/podnapisu **A** na **B** w podanym zdaniu.

> Uwaga: A może być częścią innych słów — zamiana dotyczy **każdego wystąpienia podnapisu**.

### Wejście

* 1 linia: zdanie `S`
* 2 linia: napis `A`
* 3 linia: napis `B`

### Wyjście

* 1 linia: zdanie po zamianie

### Przykład

**Wejście:**

```
Lezy jezy na wiezy
zy
rzy
```

**Wyjście:**

```
Lerzy jerzy na wierzy
```

*/

use std::io;

// Funkcja podmieniająca słowo w zdaniu
// Złożoność czasowa: O(n), gdzie n to długość zdania
// Złożoność pamięciowa: O(n)
fn podmien_slowo(zdanie: &str, stary: &str, nowy: &str) -> String {
    zdanie.replace(stary, nowy)
}

fn main() {
    let mut zdanie_str = String::new();
    io::stdin()
        .read_line(&mut zdanie_str)
        .expect("Błąd wczytywania");
    let zdanie = zdanie_str.trim();

    let mut a_str = String::new();
    io::stdin().read_line(&mut a_str).expect("Błąd wczytywania");
    let a = a_str.trim();

    let mut b_str = String::new();
    io::stdin().read_line(&mut b_str).expect("Błąd wczytywania");
    let b = b_str.trim();

    println!("{}", podmien_slowo(zdanie, a, b));
}
