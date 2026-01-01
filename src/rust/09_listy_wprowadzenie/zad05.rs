/*
ZAD-05 — Zmodyfikuj elementy spełniające warunek

**Poziom:** ★☆☆
**Tagi:** `listy`, `warunki`, `liczby pierwsze`

### Treść

Wczytaj listę liczb całkowitych. Dla każdego podpunktu utwórz **nową listę** na podstawie listy z poprzedniego podpunktu i wypisz ją w jednej linii (przecinki bez spacji):

a) Zwiększ o 1 elementy o **parzystych indeksach** (0,2,4,...).
b) Ustaw na `0` elementy będące **wielokrotnością 3**.
c) Podnieś do kwadratu elementy **mniejsze niż 10**.
d) Oblicz sumę wszystkich elementów listy i wstaw tę sumę na indeksy, które są **liczbami pierwszymi** (2,3,5,7,11,...) — tylko te, które mieszczą się w zakresie listy.
e) Zamień każdy element na **iloczyn wszystkich pozostałych elementów** listy.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite

### Wyjście

Pięć linii (po kolei: a, b, c, d, e), w każdej lista oddzielona przecinkami.

### Przykład

**Wejście:**

```
5
5
7
9
4
2
```

**Wyjście:**

```
6,7,10,4,3
6,7,0,4,3
36,49,0,16,9
36,49,36,36,9
0,0,0,0,0
```

### Uwagi o formatowaniu

* W podpunkcie (d) indeks 0 i 1 nie są pierwsze.
* W podpunkcie (e) jeśli w liście jest `0`, to wiele wyników będzie `0` — to normalne.
* Nie dodawaj przecinków na końcu linii.

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
    
    fn czy_pierwsza(num: usize) -> bool {
        if num < 2 { return false; }
        if num == 2 { return true; }
        if num % 2 == 0 { return false; }
        let mut i = 3;
        while i * i <= num {
            if num % i == 0 { return false; }
            i += 2;
        }
        true
    }
    
    fn wypisz_liste(lista: &[i32]) {
        for (i, num) in lista.iter().enumerate() {
            if i > 0 { print!(","); }
            print!("{}", num);
        }
        println!();
    }
    
    // a) Zwiększ o 1 elementy o parzystych indeksach
    let mut lista_a = lista.clone();
    for i in (0..lista_a.len()).step_by(2) {
        lista_a[i] += 1;
    }
    wypisz_liste(&lista_a);
    
    // b) Ustaw na 0 elementy będące wielokrotnością 3
    let mut lista_b = lista_a.clone();
    for i in 0..lista_b.len() {
        if lista_b[i] % 3 == 0 {
            lista_b[i] = 0;
        }
    }
    wypisz_liste(&lista_b);
    
    // c) Podnieś do kwadratu elementy mniejsze niż 10
    let mut lista_c = lista_b.clone();
    for i in 0..lista_c.len() {
        if lista_c[i] < 10 {
            lista_c[i] = lista_c[i] * lista_c[i];
        }
    }
    wypisz_liste(&lista_c);
    
    // d) Oblicz sumę i wstaw na indeksach pierwszych
    let mut lista_d = lista_c.clone();
    let suma: i32 = lista_d.iter().sum();
    for i in 0..lista_d.len() {
        if czy_pierwsza(i) {
            lista_d[i] = suma;
        }
    }
    wypisz_liste(&lista_d);
    
    // e) Zamień każdy na iloczyn wszystkich pozostałych
    let mut lista_e = vec![0; lista_d.len()];
    for i in 0..lista_d.len() {
        let mut iloczyn = 1;
        for j in 0..lista_d.len() {
            if i != j {
                iloczyn *= lista_d[j];
            }
        }
        lista_e[i] = iloczyn;
    }
    wypisz_liste(&lista_e);
}
