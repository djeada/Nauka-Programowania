/*
ZAD-03 — Rok przestępny

**Poziom:** ★☆☆
**Tagi:** `modulo`, `if`, `kalendarz`

### Treść

Wczytaj rok `y` i sprawdź, czy jest przestępny w kalendarzu gregoriańskim.

Wypisz:

* `Rok jest przestępny.`
* `Rok nie jest przestępny.`

### Wejście

* 1 linia: `y` (liczba całkowita, `y ≥ 0`)

### Wyjście

Jedna linia — odpowiedni komunikat.

### Definicja

Rok jest przestępny, gdy:

* jest podzielny przez 400 **lub**
* jest podzielny przez 4 i **nie** jest podzielny przez 100.

### Przykład

**Wejście:**

```
2100
```

**Wyjście:**

```
Rok nie jest przestępny.
```

*/
fn main() {
    let mut y = String::new();
    std::io::stdin().read_line(&mut y).unwrap();
    let y: i32 = y.trim().parse().unwrap();
    
    if (y % 400 == 0) || (y % 4 == 0 && y % 100 != 0) {
        println!("Rok jest przestępny.");
    } else {
        println!("Rok nie jest przestępny.");
    }
}
