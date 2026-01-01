/*
ZAD-06 — Czy średnia elementów znajduje się w liście?

**Poziom:** ★☆☆
**Tagi:** `listy`, `średnia`, `wyszukiwanie`

### Treść

Wczytaj listę liczb całkowitych. Oblicz średnią arytmetyczną elementów i sprawdź, czy ta średnia jest **dokładnie** jednym z elementów listy.

Wypisz:

* `Tak` — jeśli średnia występuje w liście,
* `Nie` — w przeciwnym razie.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite

### Wyjście

Jedno słowo: `Tak` lub `Nie`.

### Przykład

**Wejście:**

```
5
6
2
1
4
27
```

**Wyjście:**

```
Nie
```

### Uwagi

* Średnia może być ułamkiem — wtedy na pewno nie znajduje się w liście liczb całkowitych.

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
    
    let suma: i32 = lista.iter().sum();
    let srednia = suma as f64 / n as f64;
    
    if lista.iter().any(|&x| x as f64 == srednia) {
        println!("Tak");
    } else {
        println!("Nie");
    }
}
