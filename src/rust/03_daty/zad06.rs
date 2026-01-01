/*
ZAD-06 — Sprawdzanie poprawności daty

**Poziom:** ★★☆
**Tagi:** `walidacja`, `przestępny`, `if`

### Treść

Wczytaj `d, m, y` i sprawdź, czy jest to poprawna data w kalendarzu gregoriańskim.

Wypisz:

* `Data jest poprawna.`
* `Data jest niepoprawna.`

### Wejście

3 liczby całkowite (w osobnych liniach):

1. `d` — dzień
2. `m` — miesiąc
3. `y` — rok

### Wyjście

Jedna linia — komunikat.

### Ograniczenia / gwarancje

* `y ≥ 0` (lub `y ≥ 1`, jeśli tak chcesz przyjąć — ważne, by było spójnie w całym zbiorze)

### Reguły walidacji

1. `m` musi być w zakresie 1–12
2. Ustal liczbę dni w miesiącu:

   * 31: 1,3,5,7,8,10,12
   * 30: 4,6,9,11
   * luty: 28 lub 29 (zależnie od przestępności roku)
3. `d` musi być w zakresie 1–dni_w_miesiącu

### Przykład

**Wejście:**

```
31
4
2021
```

**Wyjście:**

```
Data jest niepoprawna.
```

*/
fn main() {
    let mut d = String::new();
    std::io::stdin().read_line(&mut d).unwrap();
    let d: i32 = d.trim().parse().unwrap();
    
    let mut m = String::new();
    std::io::stdin().read_line(&mut m).unwrap();
    let m: i32 = m.trim().parse().unwrap();
    
    let mut y = String::new();
    std::io::stdin().read_line(&mut y).unwrap();
    let y: i32 = y.trim().parse().unwrap();
    
    let mut valid = false;
    
    if m >= 1 && m <= 12 && d >= 1 {
        let dni_w_miesiacu = match m {
            1 | 3 | 5 | 7 | 8 | 10 | 12 => 31,
            4 | 6 | 9 | 11 => 30,
            2 => {
                if (y % 400 == 0) || (y % 4 == 0 && y % 100 != 0) {
                    29
                } else {
                    28
                }
            },
            _ => 0,
        };
        
        if d <= dni_w_miesiacu {
            valid = true;
        }
    }
    
    if valid {
        println!("Data jest poprawna.");
    } else {
        println!("Data jest niepoprawna.");
    }
}
