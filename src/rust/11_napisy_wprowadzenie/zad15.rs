/*
ZAD-15 — Akronim ze zdania

**Poziom:** ★☆☆
**Tagi:** `napisy`, `słowa`, `upper`

### Treść

**Akronim** to skrót utworzony z pierwszych liter kolejnych słów, np. „Polska Akademia Nauk” → `PAN`.

Wczytaj zdanie i wypisz jego akronim: pierwsze znaki wszystkich słów (zgodnie z konwencją rozdziału — bez interpunkcji), zapisane jeden za drugim **wielkimi** literami.

### Wejście

* 1. linia: zdanie (zawiera co najmniej jedno słowo; może zawierać polskie litery)

### Wyjście

Jedna linia: akronim.

### Przykład

**Wejście:**

```
Polska Akademia Nauk
```

**Wyjście:**

```
PAN
```

### Uwagi

* Słowa mogą być rozdzielone kilkoma spacjami, a zdanie może zaczynać się lub kończyć spacjami — `split()` bez argumentu poradzi sobie z tym.
* Interpunkcja nie należy do słowa: w zdaniu `(Unia Europejska)` słowami są `Unia` i `Europejska`, więc akronim to `UE`. Samotny myślnik `-` nie jest słowem.
* Zamiana na wielką literę dotyczy także polskich liter: `żółta łódź` → `ŻŁ`.

*/
use std::io;

// Akronim: wielkie pierwsze litery kolejnych słów (bez interpunkcji ASCII,
// czyli znaków ze string.punctuation w Pythonie)
fn akronim(zdanie: &str) -> String {
    zdanie
        .split_whitespace()
        .map(|fragment| fragment.trim_matches(|c: char| c.is_ascii_punctuation()))
        .filter_map(|slowo| slowo.chars().next())
        .flat_map(|znak| znak.to_uppercase())
        .collect()
}

fn main() {
    let mut zdanie = String::new();
    io::stdin()
        .read_line(&mut zdanie)
        .expect("Błąd wczytywania");
    println!("{}", akronim(&zdanie));
}
