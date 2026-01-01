/*
ZAD-02 — Wczytaj, zmodyfikuj i wypisz

**Poziom:** ★☆☆
**Tagi:** `listy`, `indeksy`, `modyfikacja`

### Treść

Wczytaj `N` oraz `N` liczb całkowitych do listy. Następnie:

a) Zwiększ każdy element o `1`.
b) Pomnóż każdy element przez jego indeks (indeksy od `0`).
c) Zastąp wszystkie elementy wartością pierwszego elementu.

Po każdym podpunkcie wypisz wynikową listę w **jednej** linii, elementy oddzielone przecinkami.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite

### Wyjście

Trzy linie:

1. wynik po (a)
2. wynik po (b)
3. wynik po (c)

Elementy w linii oddzielone przecinkami (bez spacji).

### Przykład

**Wejście:**

```
3
3
9
7
```

**Wyjście:**

```
4,10,8
0,9,14
3,3,3
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
    
    // Podpunkt a) zwiększ każdy o 1
    let mut lista_a: Vec<i32> = lista.iter().map(|x| x + 1).collect();
    for (i, num) in lista_a.iter().enumerate() {
        if i > 0 {
            print!(",");
        }
        print!("{}", num);
    }
    println!();
    
    // Podpunkt b) pomnóż każdy przez jego indeks
    let lista_b: Vec<i32> = lista_a.iter().enumerate().map(|(i, x)| x * i as i32).collect();
    for (i, num) in lista_b.iter().enumerate() {
        if i > 0 {
            print!(",");
        }
        print!("{}", num);
    }
    println!();
    
    // Podpunkt c) zastąp wszystkie wartością pierwszego
    if let Some(&first) = lista.first() {
        for i in 0..lista.len() {
            if i > 0 {
                print!(",");
            }
            print!("{}", first);
        }
        println!();
    }
}
