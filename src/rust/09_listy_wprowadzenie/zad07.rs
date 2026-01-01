/*
ZAD-07 — Średnia dwóch największych liczb

**Poziom:** ★☆☆
**Tagi:** `listy`, `max`, `sortowanie`, `float`

### Treść

Wczytaj `N` liczb naturalnych (`N ≥ 2`). Znajdź największą i drugą największą wartość, a następnie wypisz ich średnią arytmetyczną jako liczbę zmiennoprzecinkową z dokładnością do **jednego** miejsca po przecinku.

### Wejście

* 1. linia: `N` (`N ≥ 2`)
* kolejne `N` linii: liczby naturalne

### Wyjście

Jedna liczba zmiennoprzecinkowa w formacie `%.1f`.

### Przykład

**Wejście:**

```
6
9
2
3
2
1
7
```

**Wyjście:**

```
8.0
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
    
    let mut sorted = lista.clone();
    sorted.sort_by(|a, b| b.cmp(a)); // Sortuj malejąco
    
    let max1 = sorted[0];
    let max2 = sorted[1];
    
    let srednia = (max1 + max2) as f64 / 2.0;
    println!("{:.1}", srednia);
}
