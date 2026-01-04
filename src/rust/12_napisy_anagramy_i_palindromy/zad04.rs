/*
ZAD-04 — Palindromy w zdaniu

**Poziom:** ★★☆
**Tagi:** `string`, `tokenizacja`, `palindrom`

### Treść

Wczytaj zdanie i wypisz wszystkie słowa, które są palindromami.
Ignoruj wielkość liter przy sprawdzaniu.

### Wejście

* 1. linia: zdanie (może zawierać spacje i znaki interpunkcyjne)

### Wyjście

Każdy znaleziony palindrom w osobnej linii, w kolejności występowania w zdaniu.

### Przykład

**Wejście:**

```
Tata zabrał kajak na wycieczkę i uderzył się w oko
```

**Wyjście:**

```
Tata
kajak
i
w
oko
```

### Uwagi o formatowaniu

* Traktuj „słowo” jako ciąg liter/cyfr po usunięciu interpunkcji z brzegów (np. `kara.` → `kara`).
* Porównuj w wersji `lower()`, ale wypisz w oryginalnym brzmieniu z wejścia (tak jak w przykładzie).

*/

use std::io;

// Funkcja sprawdzająca czy słowo jest palindromem (ignorując wielkość liter)
// Złożoność czasowa: O(n), gdzie n to długość słowa
// Złożoność pamięciowa: O(n)
fn czy_palindrom(slowo: &str) -> bool {
    let slowo_lower = slowo.to_lowercase();
    let odwrocone: String = slowo_lower.chars().rev().collect();
    slowo_lower == odwrocone
}

// Funkcja wyodrębniająca palindromy ze zdania
// Złożoność czasowa: O(m * n), gdzie m to liczba słów, n to średnia długość słowa
// Złożoność pamięciowa: O(m * n)
fn znajdz_palindromy(zdanie: &str) -> Vec<String> {
    zdanie
        .split_whitespace()
        .map(|slowo| {
            slowo
                .trim_matches(|c: char| !c.is_alphanumeric())
                .to_string()
        })
        .filter(|slowo| !slowo.is_empty() && czy_palindrom(slowo))
        .collect()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let zdanie = input.trim();

    let palindromy = znajdz_palindromy(zdanie);
    for palindrom in palindromy {
        println!("{}", palindrom);
    }
}
