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
use std::iter::FromIterator;
use std::iter::Iterator;

fn sort_v1(napis: String) -> String {
    let s_slice: &str = &napis[..];
    let mut chars: Vec<char> = s_slice.chars().collect();
    chars.sort_by(|a, b| a.cmp(b));
    return String::from_iter(chars);
}

fn test_1() {
    let napis: String = "cab".to_owned();
    let wynik = "abc".to_owned();
    assert_eq!(sort_v1(napis), wynik);
}

fn test_2() {
    let napis: String = "eDedCBcbAaa".to_owned();
    let wynik = "ABCDabcdeae".to_owned();
    assert_eq!(sort_v1(napis), wynik);
}

fn main() {
    test_1();
    test_2();
}
