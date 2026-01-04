/*
ZAD-03 — Pierwsze wystąpienie klucza

**Poziom:** ★☆☆
**Tagi:** `listy`, `wyszukiwanie`, `indeksy`

### Treść

Wczytaj listę liczb całkowitych oraz liczbę `klucz`. Wypisz indeks pierwszego wystąpienia `klucz` w liście.
Jeśli `klucz` nie występuje — wypisz `-1`.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite
* ostatnia linia: `klucz` (liczba całkowita)

### Wyjście

Jedna liczba całkowita — indeks (od `0`) lub `-1`.

### Przykład

**Wejście:**

```
5
2
9
-1
3
8
-1
```

**Wyjście:**

```
2
```

*/
fn main() {
    let mut n = String::new();
    std::io::stdin().read_line(&mut n).unwrap();
    let n: usize = n.trim().parse().unwrap();

    let mut lista = Vec::new();
    for _ in 0..n {
        let mut num = String::new();
        std::io::stdin().read_line(&mut num).unwrap();
        let num: i32 = num.trim().parse().unwrap();
        lista.push(num);
    }

    let mut klucz = String::new();
    std::io::stdin().read_line(&mut klucz).unwrap();
    let klucz: i32 = klucz.trim().parse().unwrap();

    if let Some(pos) = lista.iter().position(|&x| x == klucz) {
        println!("{}", pos);
    } else {
        println!("-1");
    }
}
