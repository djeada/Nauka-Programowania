/*
ZAD-06 — Maksimum z czterech liczb

**Poziom:** ★☆☆
**Tagi:** `max`, `if`, `porównania`

### Treść

Wczytaj cztery liczby naturalne i wypisz największą z nich.

### Wejście

4 linie: `a`, `b`, `c`, `d` (całkowite, każda `≥ 0`)

### Wyjście

Jedna linia: największa liczba.

### Przykład

**Wejście:**

```
2
5
1
4
```

**Wyjście:**

```
5
```

*/

use ::std::*;

fn main() {
    let mut a = String::new();
    std::io::stdin().read_line(&mut a).expect("Blad odczytu");
    let a: i32 = a.trim().parse().unwrap();
    
    let mut b = String::new();
    std::io::stdin().read_line(&mut b).expect("Blad odczytu");
    let b: i32 = b.trim().parse().unwrap();
    
    let mut c = String::new();
    std::io::stdin().read_line(&mut c).expect("Blad odczytu");
    let c: i32 = c.trim().parse().unwrap();
    
    let mut d = String::new();
    std::io::stdin().read_line(&mut d).expect("Blad odczytu");
    let d: i32 = d.trim().parse().unwrap();

    let mut maks = a;
    if b > maks {
        maks = b;
    }
    if c > maks {
        maks = c;
    }
    if d > maks {
        maks = d;
    }
    
    println!("{}", maks);
}
