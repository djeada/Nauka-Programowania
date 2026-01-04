/*
ZAD-06 — Wiersze kończące się określonym napisem

**Poziom:** ★☆☆
**Tagi:** `regex`, `string`, `linijki`

### Treść

Otrzymujesz dwa napisy:

1. tekst wielowierszowy,
2. słowo lub fragment.

Znajdź wszystkie wiersze, które kończą się podanym napisem (wiersz może kończyć się znakiem interpunkcyjnym).

### Wejście

Dwie części:

1. Tekst (wiele wierszy)
2. W osobnej linii: `koncowka`

*(Sposób wczytania tekstu wielowierszowego zależy od platformy — przyjmij, że tekst jest podany w całości jako wejście, a ostatnia linia to `koncowka`.)*

### Wyjście

Wiersze spełniające warunek, każdy w osobnej linii, w kolejności występowania.

### Przykład

**Wejście:**

```
Folgujmy paniom nie sobie, ma rada;
Milujmy wiernie nie jest w nich przysada.
Godności trzeba nie za nic tu cnota,
Miłości pragną nie pragną tu złota.
da
```

**Wyjście:**

```
Folgujmy paniom nie sobie, ma rada;
Milujmy wiernie nie jest w nich przysada.
```

*/

use std::io::{self, BufRead};

// Funkcja znajdująca wiersze kończące się określonym napisem
// Złożoność czasowa: O(n * m), gdzie n to liczba wierszy, m to długość końcówki
// Złożoność pamięciowa: O(n)
fn znajdz_wiersze_z_koncowka(wiersze: &[String], koncowka: &str) -> Vec<String> {
    wiersze
        .iter()
        .filter(|wiersz| {
            // Usuń znaki interpunkcyjne z końca i sprawdź
            let wiersz_bez_inter = wiersz.trim_end_matches(|c: char| !c.is_alphanumeric());
            wiersz_bez_inter.ends_with(koncowka)
        })
        .cloned()
        .collect()
}

fn main() {
    let stdin = io::stdin();
    let wiersze: Vec<String> = stdin.lock().lines().filter_map(|line| line.ok()).collect();

    if let Some(koncowka) = wiersze.last() {
        let tekst_wiersze = &wiersze[..wiersze.len() - 1];
        let wynik = znajdz_wiersze_z_koncowka(tekst_wiersze, koncowka);

        for wiersz in wynik {
            println!("{}", wiersz);
        }
    }
}
