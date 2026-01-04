/*
ZAD-09 — Usuń duplikaty (z zachowaniem kolejności)

**Poziom:** ★☆☆
**Tagi:** `listy`, `duplikaty`, `set`

### Treść

Wczytaj listę liczb naturalnych i usuń duplikaty tak, aby każda liczba występowała tylko raz — **zachowując kolejność pierwszego wystąpienia**.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby naturalne

### Wyjście

Jedna linia: lista bez duplikatów, elementy oddzielone przecinkami.

### Przykład

**Wejście:**

```
6
3
2
1
3
2
2
```

**Wyjście:**

```
3,2,1
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

    let mut wynik = Vec::new();
    for num in lista {
        if !wynik.contains(&num) {
            wynik.push(num);
        }
    }

    for (i, num) in wynik.iter().enumerate() {
        if i > 0 {
            print!(",");
        }
        print!("{}", num);
    }
    println!();
}
