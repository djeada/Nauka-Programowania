/*
ZAD-05 — Sortowanie trzech liczb

**Poziom:** ★★☆
**Tagi:** `sort`, `warunki`, `porządkowanie`

### Treść

Wczytaj trzy liczby naturalne `a`, `b`, `c` i wypisz je w kolejności rosnącej.

### Wejście

* 1 linia: `a` (całkowita, `a ≥ 0`)
* 2 linia: `b` (całkowita, `b ≥ 0`)
* 3 linia: `c` (całkowita, `c ≥ 0`)

### Wyjście

Jedna linia: trzy liczby rosnąco, oddzielone pojedynczymi spacjami.

### Przykład

**Wejście:**

```
2
1
4
```

**Wyjście:**

```
1 2 4
```

### Uwagi

* Możesz użyć wbudowanego sortowania, ale da się też rozwiązać czystymi warunkami.

*/

use ::std::*;

fn main() {
    let mut a = String::new();
    std::io::stdin().read_line(&mut a).unwrap();
    let a: i32 = a.trim().parse().unwrap();
    
    let mut b = String::new();
    std::io::stdin().read_line(&mut b).unwrap();
    let b: i32 = b.trim().parse().unwrap();
    
    let mut c = String::new();
    std::io::stdin().read_line(&mut c).unwrap();
    let c: i32 = c.trim().parse().unwrap();

    // Sortowanie przez porownania
    let mut min = a;
    let mut mid = b;
    let mut max = c;

    if min > mid {
        let temp = min;
        min = mid;
        mid = temp;
    }
    if min > max {
        let temp = min;
        min = max;
        max = temp;
    }
    if mid > max {
        let temp = mid;
        mid = max;
        max = temp;
    }

    println!("{} {} {}", min, mid, max);
}
