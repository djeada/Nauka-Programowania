/*
ZAD-02 — Pliki o danym rozszerzeniu w folderze (bez podfolderów)

**Poziom:** ★★☆
**Tagi:** `files`, `dir`, `listdir`, `pathlib`

### Treść

Otrzymujesz ścieżkę do folderu i rozszerzenie (np. `.txt`). Znajdź wszystkie pliki o tym rozszerzeniu znajdujące się **bezpośrednio** w tym folderze (bez przeszukiwania podfolderów). Zwróć listę nazw plików.

### Wejście

* 1 linia: `folder_path`
* 2 linia: `ext` (np. `.txt`)

### Wyjście

* 1 linia: lista nazw plików w formacie `['a.txt', 'b.txt']`

### Przykład

**Wejście:**

```
C:\Users\Username\Documents
.txt
```

**Wyjście:**

```
['dokument1.txt', 'notatki.txt', 'lista_zakupów.txt']
```

### Uwagi o formatowaniu

* Porównuj rozszerzenia **bez względu na wielkość liter** (np. `.TXT` też pasuje do `.txt`).

*/

use std::fs;
use std::io;
use std::path::Path;

// Funkcja znajdująca pliki o danym rozszerzeniu w folderze
// Złożoność czasowa: O(n), gdzie n to liczba plików w folderze
// Złożoność pamięciowa: O(k), gdzie k to liczba pasujących plików
fn znajdz_pliki_po_rozszerzeniu(folder: &str, rozszerzenie: &str) -> Vec<String> {
    let mut wynik = Vec::new();

    if let Ok(entries) = fs::read_dir(folder) {
        for entry in entries.flatten() {
            if let Ok(file_type) = entry.file_type() {
                if file_type.is_file() {
                    if let Some(ext) = entry.path().extension() {
                        let ext_str = ext.to_string_lossy().to_lowercase();
                        let rozszerzenie_bez_kropki =
                            rozszerzenie.trim_start_matches('.').to_lowercase();

                        if ext_str == rozszerzenie_bez_kropki {
                            if let Some(nazwa) = entry.file_name().to_str() {
                                wynik.push(nazwa.to_string());
                            }
                        }
                    }
                }
            }
        }
    }

    wynik
}

fn main() {
    let mut folder_input = String::new();
    let mut ext_input = String::new();

    io::stdin()
        .read_line(&mut folder_input)
        .expect("Błąd wczytywania");
    io::stdin()
        .read_line(&mut ext_input)
        .expect("Błąd wczytywania");

    let folder = folder_input.trim();
    let rozszerzenie = ext_input.trim();

    let pliki = znajdz_pliki_po_rozszerzeniu(folder, rozszerzenie);

    print!("[");
    for (i, plik) in pliki.iter().enumerate() {
        if i > 0 {
            print!(", ");
        }
        print!("'{}'", plik);
    }
    println!("]");
}
