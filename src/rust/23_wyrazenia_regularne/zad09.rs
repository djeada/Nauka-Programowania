/*
ZAD-09 — Usuń fragment napisu od pierwszego wystąpienia słowa klucz

**Poziom:** ★★☆
**Tagi:** `regex`, `string`

### Treść

Otrzymujesz tekst (wiele zdań lub wierszy) oraz słowo klucz. Jeśli słowo klucz wystąpi w tekście, usuń całą część od **pierwszego wystąpienia** tego słowa do końca tekstu. Jeśli słowo klucz nie występuje, wypisz tekst bez zmian.

### Wejście

Dwie części:

1. Tekst (może mieć wiele wierszy)
2. W osobnej linii: `klucz`

### Wyjście

Zmodyfikowany tekst.

### Przykład

*(jak w treści zadania — długi tekst)*

*/

use std::io::{self, BufRead};

// Funkcja usuwająca tekst od pierwszego wystąpienia słowa klucz
// Złożoność czasowa: O(n), gdzie n to długość tekstu
// Złożoność pamięciowa: O(n)
fn usun_od_klucza(tekst: &str, klucz: &str) -> String {
    if let Some(poz) = tekst.find(klucz) {
        tekst[..poz].to_string()
    } else {
        tekst.to_string()
    }
}

fn main() {
    let stdin = io::stdin();
    let wiersze: Vec<String> = stdin.lock().lines()
        .filter_map(|line| line.ok())
        .collect();
    
    if let Some(klucz) = wiersze.last() {
        let tekst = wiersze[..wiersze.len() - 1].join("\n");
        let wynik = usun_od_klucza(&tekst, klucz);
        print!("{}", wynik);
    }
}
