/*
ZAD-03 — Określanie znaku liczby

**Poziom:** ★☆☆
**Tagi:** `if-elif-else`, `porównania`, `string`

### Treść

Wczytaj liczbę całkowitą `x` i wypisz jeden z komunikatów:

* dla `x < 0`: `Liczba jest ujemna.`
* dla `x > 0`: `Liczba jest dodatnia.`
* dla `x = 0`: `Liczba jest zerem.`

### Wejście

* 1 linia: `x` (liczba całkowita)

### Wyjście

Jedna linia — dokładnie jeden komunikat.

### Przykłady

**Wejście:**

```
-5
```

**Wyjście:**

```
Liczba jest ujemna.
```

**Wejście:**

```
0
```

**Wyjście:**

```
Liczba jest zerem.
```

**Wejście:**

```
2
```

**Wyjście:**

```
Liczba jest dodatnia.
```

*/

use ::std::*;

fn main() {
    let mut liczba = String::new();
    std::io::stdin()
        .read_line(&mut liczba)
        .expect("Blad odczytu");
    let liczba: i32 = liczba.trim().parse().expect("Blad parsowania");

    if liczba < 0 {
        println!("Liczba jest ujemna.");
    } else if liczba > 0 {
        println!("Liczba jest dodatnia.");
    } else {
        println!("Liczba jest zerem.");
    }
}
