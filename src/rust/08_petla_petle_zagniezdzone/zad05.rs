/*
ZAD-05 — Litera „X”

**Poziom:** ★★☆
**Tagi:** `pętle zagnieżdżone`, `warunki`, `ASCII-art`

### Treść

Wczytaj `n` (`n ≥ 3`) i wypisz literę `X` o wysokości `n`, zbudowaną z `*` na obu przekątnych.

W wierszu `i` i kolumnie `j` (indeksy od 0):

* wypisz `*`, gdy `j == i` **lub** `j == n - 1 - i`,
* w przeciwnym razie wypisz spację.

### Wejście

* 1. linia: `n` (`n ≥ 3`)

### Wyjście

`n` linii po `n` znaków (`*` lub spacja).

### Przykład

**Wejście:**

```
5
```

**Wyjście:**

```
*   *
 * *
  *
 * *
*   *
```

*/
fn main() {
    let mut n = String::new();
    std::io::stdin().read_line(&mut n).unwrap();
    let n: usize = n.trim().parse().unwrap();
    
    for i in 0..n {
        for j in 0..n {
            if j == i || j == n - 1 - i {
                print!("*");
            } else {
                print!(" ");
            }
        }
        println!();
    }
}
