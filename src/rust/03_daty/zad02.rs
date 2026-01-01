/*
ZAD-02 — Pełnoletność (18 lat)

**Poziom:** ★☆☆
**Tagi:** `daty`, `porównywanie`, `if`

### Treść

Wczytaj datę urodzenia oraz datę „dzisiaj” i sprawdź, czy osoba ma **ukończone 18 lat** w dniu daty aktualnej.

Wypisz:

* `Osoba jest pełnoletnia.` — jeśli ma ≥ 18 lat,
* `Osoba nie jest pełnoletnia.` — w przeciwnym razie.

### Wejście

6 liczb całkowitych (każda w osobnej linii):

1. `d1` — dzień urodzenia
2. `m1` — miesiąc urodzenia
3. `y1` — rok urodzenia
4. `d2` — aktualny dzień
5. `m2` — aktualny miesiąc
6. `y2` — aktualny rok

### Wyjście

Jedna linia — jeden z komunikatów.

### Ograniczenia / gwarancje

* Obie daty są poprawne (nie musisz walidować).
* Pełnoletność jest osiągana **dokładnie w dniu 18. urodzin**.

### Uwagi (jak to porównać)

Osoba jest pełnoletnia wtedy, gdy data `y1+18, m1, d1` jest **nie późniejsza** niż data aktualna.

### Przykład

**Wejście:**

```
5
12
1999
20
11
2020
```

**Wyjście:**

```
Osoba jest pełnoletnia.
```

*/
fn main() {
    let mut d1 = String::new();
    std::io::stdin().read_line(&mut d1).unwrap();
    let d1: i32 = d1.trim().parse().unwrap();
    
    let mut m1 = String::new();
    std::io::stdin().read_line(&mut m1).unwrap();
    let m1: i32 = m1.trim().parse().unwrap();
    
    let mut y1 = String::new();
    std::io::stdin().read_line(&mut y1).unwrap();
    let y1: i32 = y1.trim().parse().unwrap();
    
    let mut d2 = String::new();
    std::io::stdin().read_line(&mut d2).unwrap();
    let d2: i32 = d2.trim().parse().unwrap();
    
    let mut m2 = String::new();
    std::io::stdin().read_line(&mut m2).unwrap();
    let m2: i32 = m2.trim().parse().unwrap();
    
    let mut y2 = String::new();
    std::io::stdin().read_line(&mut y2).unwrap();
    let y2: i32 = y2.trim().parse().unwrap();
    
    // Sprawdz czy osoba ma 18 lat
    let mut pelnoletni = false;
    if y2 > y1 + 18 {
        pelnoletni = true;
    } else if y2 == y1 + 18 {
        if m2 > m1 {
            pelnoletni = true;
        } else if m2 == m1 && d2 >= d1 {
            pelnoletni = true;
        }
    }
    
    if pelnoletni {
        println!("Osoba jest pełnoletnia.");
    } else {
        println!("Osoba nie jest pełnoletnia.");
    }
}
