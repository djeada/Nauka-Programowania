/*
ZAD-07 — Dzień roku (liczba dni od 1 stycznia, włącznie)

**Poziom:** ★★☆
**Tagi:** `sumowanie`, `tablice`, `przestępny`

### Treść

Wczytaj datę `d, m, y` i oblicz numer dnia w roku, tzn. ile dni minęło od 1 stycznia do tej daty **włącznie**.

### Wejście

3 liczby całkowite (w osobnych liniach): `d`, `m`, `y`

### Wyjście

Jedna liczba całkowita: numer dnia w roku.

### Ograniczenia / gwarancje

* Podana data jest poprawna (nie musisz jej sprawdzać), **albo** możesz jawnie napisać: „jeśli data jest niepoprawna, zachowanie nieokreślone”.

  * (Najczyściej: dać gwarancję poprawności.)

### Przykład

**Wejście:**

```
14
2
1482
```

**Wyjście:**

```
45
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
    
    // Liczba dni w każdym miesiącu
    let przestepny = (y % 400 == 0) || (y % 4 == 0 && y % 100 != 0);
    let dni_w_miesiącach = if przestepny {
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    } else {
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    };
    
    let mut dzien_roku = d;
    for i in 0..(m - 1) {
        dzien_roku += dni_w_miesiącach[i as usize];
    }
    
    println!("{}", dzien_roku);
}
