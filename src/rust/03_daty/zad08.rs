/*
ZAD-08 — Dzień tygodnia dla daty (Zeller)

**Poziom:** ★★☆
**Tagi:** `algorytmy`, `Zeller`, `mapowanie`, `daty`

### Treść

Wczytaj datę `d, m, y` i wyznacz nazwę dnia tygodnia, używając **kongruencji Zellera** dla kalendarza gregoriańskiego.

Kroki:

1. Jeśli `m <= 2`, to:

* `m = m + 12`
* `y = y - 1`

2. Oblicz:

* `K = y % 100`
* `J = y // 100`
* `h = (d + (13*(m+1))//5 + K + K//4 + J//4 + 5*J) % 7`

3. Zmapuj `h` na dzień tygodnia:

* 0 → `Sobota`
* 1 → `Niedziela`
* 2 → `Poniedziałek`
* 3 → `Wtorek`
* 4 → `Środa`
* 5 → `Czwartek`
* 6 → `Piątek`

### Wejście

3 liczby całkowite (w osobnych liniach): `d`, `m`, `y`

### Wyjście

Jedna linia: nazwa dnia tygodnia (dokładnie jedna z: Poniedziałek, Wtorek, Środa, Czwartek, Piątek, Sobota, Niedziela).

### Ograniczenia / gwarancje

* Data wejściowa jest poprawna (zalecane; inaczej dopisz, co robić dla błędnej).
* Kalendarz gregoriański.

### Przykład

**Wejście:**

```
9
10
2020
```

**Wyjście:**

```
Piątek
```

*/
fn main() {
    let mut d = String::new();
    std::io::stdin().read_line(&mut d).unwrap();
    let mut d: i32 = d.trim().parse().unwrap();
    
    let mut m = String::new();
    std::io::stdin().read_line(&mut m).unwrap();
    let mut m: i32 = m.trim().parse().unwrap();
    
    let mut y = String::new();
    std::io::stdin().read_line(&mut y).unwrap();
    let mut y: i32 = y.trim().parse().unwrap();
    
    // Kongruencja Zellera
    if m <= 2 {
        m += 12;
        y -= 1;
    }
    
    let k = y % 100;
    let j = y / 100;
    let h = (d + (13 * (m + 1)) / 5 + k + k / 4 + j / 4 + 5 * j) % 7;
    
    let dzien = match h {
        0 => "Sobota",
        1 => "Niedziela",
        2 => "Poniedziałek",
        3 => "Wtorek",
        4 => "Środa",
        5 => "Czwartek",
        6 => "Piątek",
        _ => "Błąd",
    };
    
    println!("{}", dzien);
}
