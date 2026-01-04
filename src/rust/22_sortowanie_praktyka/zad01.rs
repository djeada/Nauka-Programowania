/*
ZAD-01 — Sortowanie znaków w napisie

**Poziom:** ★☆☆
**Tagi:** `sort`, `string`

### Treść

Otrzymujesz napis. Posortuj alfabetycznie wszystkie jego znaki i wypisz wynikowy napis.

### Wejście

* 1 linia: napis `s`

### Wyjście

* 1 linia: napis `s` po posortowaniu znaków rosnąco (porównanie znaków jak w Pythonie / Unicode)

### Przykład

**Wejście:**

```
Ala ma kota
```

**Wyjście:**

```
 Aaaaklmot
```

### Uwagi o formatowaniu

* Spacje też są znakami i biorą udział w sortowaniu (dlatego w przykładzie wyjście zaczyna się od spacji).

*/

use std::io;
use std::iter::FromIterator;

// Funkcja sortująca znaki w napisie
// Złożoność czasowa: O(n log n), gdzie n to długość napisu
// Złożoność pamięciowa: O(n)
fn sortuj_znaki(napis: String) -> String {
    let mut chars: Vec<char> = napis.chars().collect();
    chars.sort();
    String::from_iter(chars)
}

fn test_1() {
    let napis: String = "cab".to_owned();
    let wynik = "abc".to_owned();
    assert_eq!(sortuj_znaki(napis), wynik);
}

fn test_2() {
    let napis: String = "eDedCBcbAaa".to_owned();
    let wynik = "ABCDaabcdee".to_owned();
    assert_eq!(sortuj_znaki(napis), wynik);
}

fn main() {
    test_1();
    test_2();

    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let napis = input.trim().to_string();

    println!("{}", sortuj_znaki(napis));
}
