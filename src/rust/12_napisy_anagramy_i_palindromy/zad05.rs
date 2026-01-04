/*
ZAD-05 — Anagramy słowa w zdaniu

**Poziom:** ★★☆
**Tagi:** `anagram`, `string`, `zliczanie`

### Treść

Wczytaj zdanie oraz słowo-klucz. Wypisz wszystkie słowa ze zdania, które są anagramami słowa-klucza (ignoruj wielkość liter).

### Wejście

* 1. linia: zdanie
* 2. linia: słowo-klucz `k`

### Wyjście

Każde słowo ze zdania będące anagramem `k` — w osobnej linii (w kolejności występowania).

### Przykład

**Wejście:**

```
Sroga kara.
arak
```

**Wyjście:**

```
kara
```

### Uwagi

* Tak jak wyżej: usuń interpunkcję z brzegów słów.
* Porównuj np. posortowane litery w `lower()`.

*/

use std::io;

// Funkcja sprawdzająca czy dwa słowa są anagramami
// Złożoność czasowa: O(n log n), gdzie n to długość słowa
// Złożoność pamięciowa: O(n)
fn czy_anagramy(s1: &str, s2: &str) -> bool {
    let mut chars1: Vec<char> = s1.to_lowercase().chars().collect();
    let mut chars2: Vec<char> = s2.to_lowercase().chars().collect();

    chars1.sort();
    chars2.sort();

    chars1 == chars2
}

// Funkcja znajdująca anagramy słowa w zdaniu
// Złożoność czasowa: O(m * n log n), gdzie m to liczba słów, n to długość słowa
// Złożoność pamięciowa: O(m * n)
fn znajdz_anagramy(zdanie: &str, klucz: &str) -> Vec<String> {
    zdanie
        .split_whitespace()
        .map(|slowo| {
            slowo
                .trim_matches(|c: char| !c.is_alphanumeric())
                .to_string()
        })
        .filter(|slowo| !slowo.is_empty() && czy_anagramy(slowo, klucz))
        .collect()
}

fn main() {
    let mut zdanie = String::new();
    let mut klucz = String::new();

    io::stdin()
        .read_line(&mut zdanie)
        .expect("Błąd wczytywania");
    io::stdin().read_line(&mut klucz).expect("Błąd wczytywania");

    let zdanie = zdanie.trim();
    let klucz = klucz.trim();

    let anagramy = znajdz_anagramy(zdanie, klucz);
    for anagram in anagramy {
        println!("{}", anagram);
    }
}
