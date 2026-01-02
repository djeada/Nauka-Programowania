/*
ZAD-10 — Podmień napisy z listy A na napisy z listy B

**Poziom:** ★★☆
**Tagi:** `regex`, `string`, `zamiana`

### Treść

Otrzymujesz:

* tekst,
* listę A (napisy do znalezienia),
* listę B (napisy do podmiany), tej samej długości co A.

Zastąp w tekście wszystkie wystąpienia słów z listy A odpowiadającymi im słowami z listy B (ten sam indeks). Zamieniaj tylko **całe słowa**, nie fragmenty innych słów.

### Wejście

1. Tekst (jedna lub wiele linii)
2. Liczba naturalna `n` — długość list
3. `n` wierszy: elementy listy A
4. `n` wierszy: elementy listy B

### Wyjście

Zmodyfikowany tekst.

### Przykład

*(jak w treści — z listami A/B)*

*/

use std::io::{self, BufRead};

// Funkcja podmieniająca słowa z listy A na słowa z listy B
// Złożoność czasowa: O(n * m), gdzie n to długość tekstu, m to liczba zamian
// Złożoność pamięciowa: O(n)
fn podmien_slowa(tekst: &str, lista_a: &[String], lista_b: &[String]) -> String {
    let mut wynik = tekst.to_string();
    
    for (a, b) in lista_a.iter().zip(lista_b.iter()) {
        // Zamieniamy tylko całe słowa
        let slowa: Vec<&str> = wynik.split_whitespace().collect();
        let nowe_slowa: Vec<String> = slowa.iter()
            .map(|&slowo| {
                // Usuń znaki interpunkcyjne z końca
                let (koniec_inter, slowo_czyste) = if let Some(ostatni_idx) = slowo.rfind(|c: char| c.is_alphanumeric()) {
                    let (czyste, inter) = slowo.split_at(ostatni_idx + 1);
                    (inter, czyste)
                } else {
                    ("", slowo)
                };
                
                if slowo_czyste == a.as_str() {
                    format!("{}{}", b, koniec_inter)
                } else {
                    slowo.to_string()
                }
            })
            .collect();
        wynik = nowe_slowa.join(" ");
    }
    
    wynik
}

fn main() {
    let stdin = io::stdin();
    let mut wiersze: Vec<String> = stdin.lock().lines()
        .filter_map(|line| line.ok())
        .collect();
    
    if wiersze.is_empty() {
        return;
    }
    
    // Ostatnia część to liczba n
    let n: usize = wiersze.pop().and_then(|s| s.parse().ok()).unwrap_or(0);
    
    // Bierzemy n elementów z końca jako listę B
    let lista_b: Vec<String> = wiersze.split_off(wiersze.len().saturating_sub(n));
    
    // Kolejne n elementów to lista A
    let lista_a: Vec<String> = wiersze.split_off(wiersze.len().saturating_sub(n));
    
    // Reszta to tekst
    let tekst = wiersze.join("\n");
    
    let wynik = podmien_slowa(&tekst, &lista_a, &lista_b);
    print!("{}", wynik);
}
