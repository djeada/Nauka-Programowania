/*
ZAD-02 — Wszystkie permutacje słowa

**Poziom:** ★★☆
**Tagi:** `rekurencja`, `permutacje`, `backtracking`

### Treść

Wczytaj słowo z **unikalnych liter** i wypisz wszystkie jego permutacje — każdą w osobnej linii.

### Wejście

* 1. linia: słowo (litery nie powtarzają się)

### Wyjście

Wiele linii — wszystkie permutacje słowa, każda w osobnej linii.

### Przykład

**Wejście:**

```
abc
```

**Wyjście:**

```
abc
acb
bac
bca
cab
cba
```

### Uwagi o formatowaniu

* Kolejność wypisywania permutacji nie musi być dokładnie taka jak w przykładzie, o ile są wszystkie i bez powtórzeń.

*/

use std::io;

// Funkcja generująca wszystkie permutacje słowa
// Złożoność czasowa: O(n!), gdzie n to długość słowa
// Złożoność pamięciowa: O(n! * n) dla przechowania wszystkich permutacji
fn generuj_permutacje(slowo: &str) -> Vec<String> {
    let mut chars: Vec<char> = slowo.chars().collect();
    let mut wynik = Vec::new();
    permutuj(&mut chars, 0, &mut wynik);
    wynik
}

// Funkcja pomocnicza generująca permutacje rekurencyjnie
fn permutuj(chars: &mut Vec<char>, index: usize, wynik: &mut Vec<String>) {
    if index == chars.len() {
        wynik.push(chars.iter().collect());
        return;
    }

    for i in index..chars.len() {
        chars.swap(index, i);
        permutuj(chars, index + 1, wynik);
        chars.swap(index, i); // backtrack
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let slowo = input.trim();

    let permutacje = generuj_permutacje(slowo);
    for perm in permutacje {
        println!("{}", perm);
    }
}
