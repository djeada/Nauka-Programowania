/*
ZAD-01 — Kwadrat

**Poziom:** ★☆☆
**Tagi:** `pętle zagnieżdżone`, `print`, `string`

### Treść

Wczytaj liczbę naturalną `n` (`n ≥ 1`) i wypisz kwadrat `n × n` zbudowany z gwiazdek `*`.
Każdy wiersz ma zawierać dokładnie `n` gwiazdek (bez spacji).

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 1`)

### Wyjście

`n` linii, w każdej dokładnie `n` znaków `*`.

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
**
**
```

*/
fn main() {
    let mut n = String::new();
    std::io::stdin().read_line(&mut n).unwrap();
    let n: usize = n.trim().parse().unwrap();

    for _ in 0..n {
        for _ in 0..n {
            print!("*");
        }
        println!();
    }
}
