/*
ZAD-08 — Obliczanie liczby kur i owiec na farmie

**Poziom:** ★★☆
**Tagi:** `układ równań`, `arytmetyka`

### Treść

Na farmie są kury i owce. Wiadomo, że:

* łączna liczba głów wynosi `a`,
* łączna liczba nóg wynosi `b`,
* kura ma 2 nogi, owca ma 4 nogi,
* każda ma dokładnie 1 głowę.

Oblicz liczbę kur oraz liczbę owiec.

### Wejście

Dwie liczby naturalne:

* 1. linia: `a` — liczba głów (`a ≥ 0`)
* 2. linia: `b` — liczba nóg (`b ≥ 0`)

### Ograniczenia / gwarancje

* Istnieje rozwiązanie w liczbach całkowitych nieujemnych.

### Wyjście

Dwie liczby naturalne, każda w oddzielnej linii:

1. liczba kur
2. liczba owiec

### Przykład

**Wejście:**

```
40
100
```

**Wyjście:**

```
30
10
```

### Uwagi o formatowaniu

* Nie wypisuj dodatkowych opisów — tylko liczby.

*/
fn main() {
    let mut a = String::new();
    std::io::stdin().read_line(&mut a).unwrap();
    let a: i32 = a.trim().parse().unwrap();
    
    let mut b = String::new();
    std::io::stdin().read_line(&mut b).unwrap();
    let b: i32 = b.trim().parse().unwrap();
    
    // Uklad rownan:
    // kury + owce = a
    // 2*kury + 4*owce = b
    // Z pierwszego: kury = a - owce
    // Podstawiamy do drugiego: 2*(a - owce) + 4*owce = b
    // 2*a - 2*owce + 4*owce = b
    // 2*a + 2*owce = b
    // 2*owce = b - 2*a
    // owce = (b - 2*a) / 2
    
    let owce = (b - 2 * a) / 2;
    let kury = a - owce;
    
    println!("{}", kury);
    println!("{}", owce);
}
