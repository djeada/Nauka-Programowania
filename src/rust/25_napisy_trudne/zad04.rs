/*
ZAD-04 — Wszystkie wystąpienia podnapisu

**Poziom:** ★★☆
**Tagi:** `string`, `substring`, `find`

### Treść

Otrzymujesz napis `S` i napis `W` (wzorzec). Znajdź **wszystkie** pozycje w `S`, od których zaczyna się wystąpienie `W`, i wypisz je w kolejności rosnącej.

Wystąpienia mogą na siebie nachodzić: w napisie `aaaa` wzorzec `aa` zaczyna się na pozycjach `0`, `1` i `2`.

### Wejście

* 1. linia: napis `S`
* 2. linia: wzorzec `W`

### Wyjście

Jedna linia: indeksy początków wszystkich wystąpień `W` w `S`, oddzielone pojedynczymi spacjami.
Jeśli `W` nie występuje w `S`, wypisz `Brak`.

### Ograniczenia

* `1 ≤ |S| ≤ 1000`
* `1 ≤ |W| ≤ 100`

### Przykład

**Wejście:**

```
abrakadabra
abra
```

**Wyjście:**

```
0 7
```

### Uwagi

* Spróbuj nie używać metod `find` ani `count`: dla każdej pozycji `i` od `0` do `len(S) - len(W)` sprawdź, czy od tego miejsca zaczyna się `W` — tak jak sprawdzałeś przedrostek w zadaniu ZAD-03.
* W przeciwieństwie do zadań ZAD-01 i ZAD-02 po znalezieniu wystąpienia **nie przeskakujemy** go — kolejną sprawdzaną pozycją jest `i + 1`.

*/
use std::io;

// Indeksy wszystkich (także nachodzących) wystąpień wzorca w napisie.
// Indeksy liczone po znakach Unicode, tak jak w Pythonie.
// Złożoność czasowa: O(n * m), pamięciowa: O(n + m)
fn wystapienia(napis: &[char], wzorzec: &[char]) -> Vec<usize> {
    if wzorzec.len() > napis.len() {
        return Vec::new();
    }
    (0..=napis.len() - wzorzec.len())
        .filter(|&i| napis[i..i + wzorzec.len()] == *wzorzec)
        .collect()
}

fn wczytaj_linie() -> Vec<char> {
    let mut linia = String::new();
    io::stdin().read_line(&mut linia).expect("Błąd wczytywania");
    // Usuwamy tylko znak końca linii — spacje są częścią napisu.
    linia.trim_end_matches(['\n', '\r']).chars().collect()
}

fn main() {
    let napis = wczytaj_linie();
    let wzorzec = wczytaj_linie();

    let pozycje = wystapienia(&napis, &wzorzec);
    if pozycje.is_empty() {
        println!("Brak");
    } else {
        let teksty: Vec<String> = pozycje.iter().map(|i| i.to_string()).collect();
        println!("{}", teksty.join(" "));
    }
}
