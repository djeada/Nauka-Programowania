/*
ZAD-03 — Znajdź wszystkie ścieżki plików o danej nazwie (rekurencyjnie)

**Poziom:** ★★☆
**Tagi:** `files`, `walk`, `recursive`, `pathlib`

### Treść

Otrzymujesz nazwę pliku (np. `raport.docx`). Przeszukaj cały system plików i znajdź wszystkie pliki o tej nazwie. Wypisz listę pełnych ścieżek do znalezionych plików.

### Wejście

* 1 linia: `filename` (np. `raport.docx`)

### Wyjście

* 1 linia: lista pełnych ścieżek (napisy)

### Przykład

**Wejście:**

```
raport.docx
```

**Wyjście:**

```
[
  'C:\Users\Username\Documents\raport.docx',
  'D:\Projekty\Raporty\raport.docx',
  'E:\Backup\raport.docx'
]
```

### Uwagi

* W środowisku testowym możesz nie mieć uprawnień do wszystkich katalogów — program powinien to bezpiecznie obsłużyć (np. pomijać niedostępne miejsca).

*/

use std::fs;
use std::io;
use std::path::PathBuf;

// Funkcja rekurencyjnie znajdująca pliki o danej nazwie
// Złożoność czasowa: O(n), gdzie n to całkowita liczba plików w systemie
// Złożoność pamięciowa: O(k), gdzie k to liczba pasujących plików
fn znajdz_pliki_rekurencyjnie(start_path: &str, nazwa_pliku: &str) -> Vec<String> {
    let mut wynik = Vec::new();
    znajdz_pliki_helper(start_path, nazwa_pliku, &mut wynik);
    wynik
}

fn znajdz_pliki_helper(sciezka: &str, nazwa_pliku: &str, wynik: &mut Vec<String>) {
    if let Ok(entries) = fs::read_dir(sciezka) {
        for entry in entries.flatten() {
            if let Ok(file_type) = entry.file_type() {
                let path = entry.path();

                if file_type.is_file() {
                    if let Some(nazwa) = path.file_name() {
                        if nazwa == nazwa_pliku {
                            wynik.push(path.to_string_lossy().to_string());
                        }
                    }
                } else if file_type.is_dir() {
                    // Rekurencyjnie przeszukuj podfoldery (z obsługą błędów)
                    if let Some(path_str) = path.to_str() {
                        znajdz_pliki_helper(path_str, nazwa_pliku, wynik);
                    }
                }
            }
        }
    }
    // Ignoruj błędy dostępu (brak uprawnień itp.)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    let nazwa_pliku = input.trim();

    // Szukaj od bieżącego katalogu (w praktyce można użyć "/"  lub "C:\" w systemach Windows)
    let pliki = znajdz_pliki_rekurencyjnie(".", nazwa_pliku);

    println!("[");
    for (i, plik) in pliki.iter().enumerate() {
        if i > 0 {
            println!(",");
        }
        print!("  '{}'", plik);
    }
    println!("\n]");
}
