/*
ZAD-06 — Permutacje słowa, które są palindromami

**Poziom:** ★★☆
**Tagi:** `palindrom`, `permutacje`, `multiset`

### Treść

Wczytaj słowo i wypisz wszystkie **unikalne** palindromy, które są jego permutacjami.

### Wejście

* 1. linia: słowo (litery mogą się powtarzać)

### Wyjście

Każdy unikalny palindrom w osobnej linii. Jeśli nie istnieje żaden — puste wyjście.

### Przykład

**Wejście:**

```
aabb
```

**Wyjście:**

```
abba
baab
```

### Uwagi

* Najpierw sprawdź warunek istnienia palindromu z liter: co najwyżej jeden znak może mieć nieparzystą liczbę wystąpień.
* Generuj palindromy z połówek (bez wypisywania duplikatów).

*/

use std::collections::{HashMap, HashSet};
use std::io;

// Funkcja sprawdzająca czy można utworzyć palindrom z liter
// Złożoność czasowa: O(n), gdzie n to długość słowa
// Złożoność pamięciowa: O(k), gdzie k to liczba unikalnych znaków
fn mozna_utworzyc_palindrom(slowo: &str) -> bool {
    let mut liczniki: HashMap<char, usize> = HashMap::new();

    for c in slowo.chars() {
        *liczniki.entry(c).or_insert(0) += 1;
    }

    let nieparzystych = liczniki.values().filter(|&&v| v % 2 == 1).count();
    nieparzystych <= 1
}

// Funkcja generująca unikalne palindromy będące permutacjami słowa
// Złożoność czasowa: O(n! / (n1! * n2! * ...)), gdzie n1, n2 to liczby powtórzeń liter
// Złożoność pamięciowa: O(liczba_unikalnych_palindromów * n)
fn generuj_palindromy(slowo: &str) -> Vec<String> {
    if !mozna_utworzyc_palindrom(slowo) {
        return Vec::new();
    }

    let mut liczniki: HashMap<char, usize> = HashMap::new();
    for c in slowo.chars() {
        *liczniki.entry(c).or_insert(0) += 1;
    }

    let mut polowa = Vec::new();
    let mut srodek = None;

    for (c, count) in liczniki.iter() {
        if count % 2 == 1 {
            srodek = Some(*c);
        }
        for _ in 0..(count / 2) {
            polowa.push(*c);
        }
    }

    let mut wynik = HashSet::new();
    let mut temp = Vec::new();
    generuj_permutacje_palindromow(&mut polowa, 0, &mut temp, srodek, &mut wynik);

    wynik.into_iter().collect()
}

// Funkcja pomocnicza generująca permutacje połówek palindromu
fn generuj_permutacje_palindromow(
    chars: &mut Vec<char>,
    index: usize,
    temp: &mut Vec<char>,
    srodek: Option<char>,
    wynik: &mut HashSet<String>,
) {
    if index == chars.len() {
        let mut palindrom: Vec<char> = temp.clone();
        if let Some(c) = srodek {
            palindrom.push(c);
        }
        palindrom.extend(temp.iter().rev());
        wynik.insert(palindrom.iter().collect());
        return;
    }

    let mut uzyte = HashSet::new();
    for i in index..chars.len() {
        if uzyte.contains(&chars[i]) {
            continue;
        }
        uzyte.insert(chars[i]);

        chars.swap(index, i);
        temp.push(chars[index]);
        generuj_permutacje_palindromow(chars, index + 1, temp, srodek, wynik);
        temp.pop();
        chars.swap(index, i);
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let slowo = input.trim();

    let palindromy = generuj_palindromy(slowo);
    for palindrom in palindromy {
        println!("{}", palindrom);
    }
}
