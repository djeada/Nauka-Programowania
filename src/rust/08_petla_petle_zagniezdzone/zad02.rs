/*
ZAD-02 — Trójkąt prostokątny (rosnący)

**Poziom:** ★☆☆
**Tagi:** `pętle`, `print`, `string`

### Treść

Wczytaj `n` (`n ≥ 1`) i wypisz trójkąt o wysokości `n`, gdzie w wierszu `i` jest `i` gwiazdek (`i = 1..n`).

### Wejście

* 1. linia: `n` (`n ≥ 1`)

### Wyjście

`n` linii:

* 1. linia: `*`
* 2. linia: `**`
* …
* `n`-ta linia: `n` gwiazdek

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
*
**
***
```

*/
fn main() {
    let mut n = String::new();
    std::io::stdin().read_line(&mut n).unwrap();
    let n: usize = n.trim().parse().unwrap();

    for i in 1..=n {
        for _ in 0..i {
            print!("*");
        }
        println!();
    }
}
