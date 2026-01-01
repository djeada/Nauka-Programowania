/*
ZAD-02 — Sortowanie słów w zdaniu

**Poziom:** ★★☆
**Tagi:** `sort`, `string`, `split`

### Treść

Otrzymujesz zdanie. Podziel je na słowa, traktując znaki interpunkcyjne jako separatory, a następnie posortuj słowa alfabetycznie i wypisz listę.

### Wejście

* 1 linia: napis `zdanie`

### Wyjście

* 1 linia: lista słów w formacie jak w przykładzie, np. `['Ala', 'kota', 'ma']`

### Przykład

**Wejście:**

```
Lemur wygina śmiało ciało
```

**Wyjście:**

```
['Lemur', 'ciało', 'wygina', 'śmiało']
```

### Uwagi o formatowaniu

* Ignoruj znaki interpunkcyjne (np. `.,!?;:`) — nie są częścią słów.
* Wielkość liter pozostaje bez zmian (nie zamieniaj na małe/duże), sortujesz to, co w tekście.

*/

use std::io;

// Funkcja sortująca słowa w zdaniu
// Złożoność czasowa: O(n log n), gdzie n to liczba słów
// Złożoność pamięciowa: O(n)
fn sortuj_slowa(zdanie: &str) -> Vec<String> {
    let mut slowa: Vec<String> = zdanie
        .split(|c: char| !c.is_alphanumeric())
        .filter(|s| !s.is_empty())
        .map(|s| s.to_string())
        .collect();
    
    slowa.sort();
    slowa
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let zdanie = input.trim();
    
    let slowa = sortuj_slowa(zdanie);
    
    print!("[");
    for (i, slowo) in slowa.iter().enumerate() {
        if i > 0 {
            print!(", ");
        }
        print!("'{}'", slowo);
    }
    println!("]");
}
