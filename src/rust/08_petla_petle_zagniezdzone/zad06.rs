/*
ZAD-06 — Litera „Z”

**Poziom:** ★★☆
**Tagi:** `pętle zagnieżdżone`, `warunki`, `ASCII-art`

### Treść

Wczytaj `n` (`n ≥ 3`) i wypisz literę `Z` o wysokości `n`:

* pierwszy wiersz: `n` gwiazdek,
* ostatni wiersz: `n` gwiazdek,
* w środku: jedna gwiazdka na przekątnej od prawej do lewej.

W wierszu `i` (0..n-1) i kolumnie `j`:

* jeśli `i == 0` lub `i == n-1` → `*`
* else jeśli `j == n-1-i` → `*`
* else → spacja

### Wejście

* 1. linia: `n` (`n ≥ 3`)

### Wyjście

`n` linii po `n` znaków.

### Przykład

**Wejście:**

```
5
```

**Wyjście:**

```
*****
   *
  *
 *
*****
```

*/
fn main() {
    let mut n = String::new();
    std::io::stdin().read_line(&mut n).unwrap();
    let n: usize = n.trim().parse().unwrap();
    
    for i in 0..n {
        for j in 0..n {
            if i == 0 || i == n - 1 || j == n - 1 - i {
                print!("*");
            } else {
                print!(" ");
            }
        }
        println!();
    }
}
