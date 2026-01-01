/*
ZAD-04 — Tabliczka mnożenia N × N

**Poziom:** ★★☆
**Tagi:** `pętle zagnieżdżone`, `formatowanie`, `arytmetyka`

### Treść

Wczytaj liczbę naturalną `N` (`N ≥ 1`) i wypisz tabliczkę mnożenia `N × N`.

W wierszu `i` i kolumnie `j` (licząc od 1) ma znaleźć się wartość `i*j`.
Liczby w jednym wierszu oddzielaj pojedynczą spacją.

### Wejście

* 1. linia: `N` (`N ≥ 1`)

### Wyjście

`N` linii, w każdej `N` liczb.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
1 2 3
2 4 6
3 6 9
```

### Uwagi o formatowaniu

* Nie dodawaj spacji na końcu wiersza.

*/
fn main() {
    let mut n = String::new();
    std::io::stdin().read_line(&mut n).unwrap();
    let n: usize = n.trim().parse().unwrap();
    
    for i in 1..=n {
        for j in 1..=n {
            if j > 1 {
                print!(" ");
            }
            print!("{}", i * j);
        }
        println!();
    }
}
