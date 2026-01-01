/*
ZAD-08 — Wyjątkowe palindromy (podciągi bez zmiany kolejności)

**Poziom:** ★★★
**Tagi:** `substring`, `palindrom`, `unikalność`

### Treść

Wczytaj słowo i znajdź wszystkie **unikalne** palindromy, które można z niego utworzyć jako **spójne podciągi** (substringi), bez zmiany kolejności znaków, spełniające warunek „wyjątkowości”:

1. wszystkie znaki są identyczne (np. `aaa`), **albo**
2. wszystkie znaki poza środkowym są identyczne (np. `cbc`).

Pojedynczy znak też jest wyjątkowym palindromem.

### Wejście

* 1. linia: słowo (litery)

### Wyjście

Każdy unikalny wyjątkowy palindrom w osobnej linii.
Jeśli nic poza pojedynczymi znakami nie pasuje, wypisz tylko te unikalne znaki (po jednej linii na znak).

### Przykład

**Wejście:**

```
xxyxx
```

**Wyjście:**

```
x
xx
xxx
xxyxx
y
yxy
```

### Uwagi o formatowaniu

* Usuń duplikaty w wyniku (np. ten sam palindrom znaleziony w kilku miejscach wypisz raz).
* Kolejność wypisywania może być zgodna z pierwszym pojawieniem się w tekście (łatwe i czytelne): wypisuj przy pierwszym znalezieniu danego palindromu.

*/

use std::io;
use std::collections::HashSet;

// Funkcja sprawdzająca czy palindrom jest "wyjątkowy"
// Złożoność czasowa: O(n), gdzie n to długość podciągu
// Złożoność pamięciowa: O(k), gdzie k to liczba unikalnych znaków
fn czy_wyjatkowy_palindrom(s: &str) -> bool {
    let chars: Vec<char> = s.chars().collect();
    let len = chars.len();
    
    // Sprawdź czy jest palindromem
    for i in 0..len / 2 {
        if chars[i] != chars[len - 1 - i] {
            return false;
        }
    }
    
    // Sprawdź warunek wyjątkowości
    if len == 1 {
        return true;
    }
    
    let unikalne: HashSet<char> = chars.iter().cloned().collect();
    
    if unikalne.len() == 1 {
        // Wszystkie znaki identyczne
        return true;
    }
    
    if len % 2 == 1 {
        // Nieparzysta długość - sprawdź czy wszystkie poza środkowym są identyczne
        let srodek = len / 2;
        let pierwszy = chars[0];
        
        for i in 0..len {
            if i != srodek && chars[i] != pierwszy {
                return false;
            }
        }
        return true;
    }
    
    false
}

// Funkcja znajdująca wszystkie unikalne wyjątkowe palindromy
// Złożoność czasowa: O(n^3), gdzie n to długość słowa
// Złożoność pamięciowa: O(n^2) dla przechowania unikalnych palindromów
fn znajdz_wyjatkowe_palindromy(slowo: &str) -> Vec<String> {
    let mut znalezione: HashSet<String> = HashSet::new();
    let len = slowo.len();
    
    for i in 0..len {
        for j in i+1..=len {
            let podciag = &slowo[i..j];
            if czy_wyjatkowy_palindrom(podciag) {
                znalezione.insert(podciag.to_string());
            }
        }
    }
    
    let mut wynik: Vec<String> = znalezione.into_iter().collect();
    wynik.sort_by_key(|s| s.len());
    wynik
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let slowo = input.trim();
    
    let palindromy = znajdz_wyjatkowe_palindromy(slowo);
    for palindrom in palindromy {
        println!("{}", palindrom);
    }
}
