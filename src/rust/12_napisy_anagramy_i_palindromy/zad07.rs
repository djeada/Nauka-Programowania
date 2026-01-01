/*
ZAD-07 — Minimalna liczba usunięć, aby uzyskać anagramy

**Poziom:** ★★★
**Tagi:** `anagram`, `zliczanie`, `greedy`

### Treść

Wczytaj dwa słowa. Jeśli mają różne długości, wypisz `-1`.
W przeciwnym razie oblicz minimalną liczbę znaków, które trzeba usunąć (łącznie z obu słów), aby pozostałe napisy były anagramami.

### Wejście

* 1. linia: słowo `s1`
* 2. linia: słowo `s2`

### Wyjście

* jedna liczba całkowita: minimalna liczba usunięć lub `-1`

### Przykład

**Wejście:**

```
grazyna
razynax
```

**Wyjście:**

```
2
```

### Uwagi

* Dla tej samej długości: policz zliczenia liter i zsumuj wartości `abs(c1[lit] - c2[lit])`, a wynik wypisz jako tę sumę. (To jest łączna liczba usunięć.)

*/

use std::io;
use std::collections::HashMap;

// Funkcja obliczająca minimalną liczbę usunięć do uzyskania anagramów
// Złożoność czasowa: O(n), gdzie n to długość słów
// Złożoność pamięciowa: O(k), gdzie k to liczba unikalnych znaków
fn min_usuniec_do_anagramow(s1: &str, s2: &str) -> i32 {
    if s1.len() != s2.len() {
        return -1;
    }
    
    let mut liczniki1: HashMap<char, i32> = HashMap::new();
    let mut liczniki2: HashMap<char, i32> = HashMap::new();
    
    for c in s1.chars() {
        *liczniki1.entry(c).or_insert(0) += 1;
    }
    
    for c in s2.chars() {
        *liczniki2.entry(c).or_insert(0) += 1;
    }
    
    let mut suma = 0;
    
    // Zbierz wszystkie unikalne znaki z obu słów
    let mut wszystkie_znaki: std::collections::HashSet<char> = std::collections::HashSet::new();
    for c in s1.chars() {
        wszystkie_znaki.insert(c);
    }
    for c in s2.chars() {
        wszystkie_znaki.insert(c);
    }
    
    for c in wszystkie_znaki {
        let count1 = *liczniki1.get(&c).unwrap_or(&0);
        let count2 = *liczniki2.get(&c).unwrap_or(&0);
        suma += (count1 - count2).abs();
    }
    
    suma
}

fn main() {
    let mut s1 = String::new();
    let mut s2 = String::new();
    
    io::stdin().read_line(&mut s1).expect("Błąd wczytywania");
    io::stdin().read_line(&mut s2).expect("Błąd wczytywania");
    
    let s1 = s1.trim();
    let s2 = s2.trim();
    
    println!("{}", min_usuniec_do_anagramow(s1, s2));
}
