/*
ZAD-01 — Wczytaj i wypisz

**Poziom:** ★☆☆
**Tagi:** `listy`, `I/O`, `odwracanie`

### Treść

Wczytaj `N`, następnie `N` liczb całkowitych do listy.

a) Wypisz elementy listy od początku do końca — każdy w osobnej linii.
b) Wypisz elementy listy od końca do początku — w **jednej** linii, oddzielone przecinkami (bez spacji).

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite

### Wyjście

a) `N` linii — elementy w kolejności wczytania.
b) 1 linia — elementy w kolejności odwrotnej, oddzielone przecinkami.

### Przykład

**Wejście:**

```
3
8
12
7
```

**Wyjście:**

```
8
12
7
7,12,8
```

### Uwagi o formatowaniu

* W podpunkcie (b) nie dodawaj przecinka na końcu.

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
    
    // Podpunkt a) wypisz od początku do końca
    for num in &lista {
        println!("{}", num);
    }
    
    // Podpunkt b) wypisz od końca w jednej linii
    for (i, num) in lista.iter().rev().enumerate() {
        if i > 0 {
            print!(",");
        }
        print!("{}", num);
    }
    println!();
}
