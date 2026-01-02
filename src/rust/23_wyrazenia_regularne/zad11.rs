/*
ZAD-11 — Nazwa pliku bez rozszerzenia

**Poziom:** ★★☆
**Tagi:** `regex`, `string`, `ścieżki`

### Treść

Otrzymujesz napis reprezentujący pełną ścieżkę do pliku. Wyodrębnij nazwę pliku (bez katalogów) i usuń rozszerzenie (część po ostatniej kropce). Zwróć samą nazwę bez rozszerzenia.

Ścieżka może zawierać separator `\` lub `/`.

### Wejście

Jedna linia:

* `sciezka`

### Wyjście

Jedna linia:

* `nazwa_pliku_bez_rozszerzenia`

### Przykład

**Wejście:**

```
C:\my-long\path_directory\file.html
```

**Wyjście:**

```
file
```

*/

use std::io;

// Funkcja wyodrębniająca nazwę pliku bez rozszerzenia ze ścieżki
// Złożoność czasowa: O(n), gdzie n to długość ścieżki
// Złożoność pamięciowa: O(n)
fn nazwa_bez_rozszerzenia(sciezka: &str) -> String {
    // Znajdź ostatni separator (\ lub /)
    let nazwa_z_rozszerzeniem = sciezka
        .rsplit(|c| c == '\\' || c == '/')
        .next()
        .unwrap_or(sciezka);
    
    // Usuń rozszerzenie (część po ostatniej kropce)
    if let Some(kropka_idx) = nazwa_z_rozszerzeniem.rfind('.') {
        nazwa_z_rozszerzeniem[..kropka_idx].to_string()
    } else {
        nazwa_z_rozszerzeniem.to_string()
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let sciezka = input.trim();
    
    println!("{}", nazwa_bez_rozszerzenia(sciezka));
}
