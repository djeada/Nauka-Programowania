/*
ZAD-03 — Trójkąt prostokątny (malejący)

**Poziom:** ★☆☆
**Tagi:** `pętle`, `print`, `string`

### Treść

Wczytaj `n` (`n ≥ 1`) i wypisz odwrócony trójkąt o wysokości `n`, zaczynając od `n` gwiazdek i kończąc na `1`.

### Wejście

* 1. linia: `n` (`n ≥ 1`)

### Wyjście

`n` linii:

* 1. linia: `n` gwiazdek
* 2. linia: `n-1` gwiazdek
* …
* ostatnia linia: `*`

### Przykład

**Wejście:**

```
4
```

**Wyjście:**

```
****
***
**
*
```

*/
fn main() {
    let mut n = String::new();
    std::io::stdin().read_line(&mut n).unwrap();
    let n: usize = n.trim().parse().unwrap();

    for i in (1..=n).rev() {
        for _ in 0..i {
            print!("*");
        }
        println!();
    }
}
