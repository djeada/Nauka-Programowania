/*
ZAD-05 — Liczba dni w miesiącu (rok nieprzestępny)

**Poziom:** ★☆☆
**Tagi:** `if`, `tablice`, `walidacja`

### Treść

Wczytaj numer miesiąca `m`. Zakładając rok **nieprzestępny**, wypisz liczbę dni w tym miesiącu.
Jeśli `m` nie jest w zakresie 1–12, wypisz:
`Niepoprawny numer miesiąca.`

### Wejście

* 1 linia: `m` (liczba całkowita, `m ≥ 0`)

### Wyjście

* liczba dni (jedna linia) **albo**
* komunikat o błędzie (jedna linia)

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
28
```

*/
fn main() {
    let mut m = String::new();
    std::io::stdin().read_line(&mut m).unwrap();
    let m: i32 = m.trim().parse().unwrap();

    match m {
        1 | 3 | 5 | 7 | 8 | 10 | 12 => println!("31"),
        4 | 6 | 9 | 11 => println!("30"),
        2 => println!("28"),
        _ => println!("Niepoprawny numer miesiąca."),
    }
}
