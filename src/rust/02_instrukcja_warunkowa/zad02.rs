/*
ZAD-02 — Porównanie dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `if-else`, `równość`, `string`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`.
Jeśli są równe, wypisz:
`Liczby są identyczne.`
W przeciwnym razie wypisz:
`Liczby są różne.`

### Wejście

* 1 linia: `a` (całkowita, `a ≥ 0`)
* 2 linia: `b` (całkowita, `b ≥ 0`)

### Wyjście

Jedna linia — dokładnie jeden z komunikatów.

### Przykład 1

**Wejście:**

```
7
4
```

**Wyjście:**

```
Liczby są różne.
```

### Przykład 2

**Wejście:**

```
5
5
```

**Wyjście:**

```
Liczby są identyczne.
```

*/

use ::std::*;

fn main() {
    println!("Podaj dwie liczby oddzielone spacjami.");
    let mut wiersz = String::new();
    std::io::stdin().read_line(&mut wiersz).unwrap();
    let liczby: Vec<i32> = wiersz
        .trim()
        .split(' ')
        .map(|x| x.parse::<i32>().unwrap())
        .collect();

    if liczby[0] == liczby[1] {
        println!("Liczby sa identyczne.");
    } else {
        println!("Liczby nie sa identyczne.");
    }
}
