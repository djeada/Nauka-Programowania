/*
ZAD-06 — Sumowanie elementów ciągu

**Poziom:** ★☆☆
**Tagi:** `ciągi`, `sumowanie`, `pętle`

### Treść

Wczytaj liczbę naturalną `n` (`n ≥ 1`) i oblicz:

a) ( \sum_{k=1}^{n} (k^2 + k + 1) )

b) ( \sum_{k=1}^{n} (k^2 + 5k) )

c) ( \sum_{k=1}^{n} (k + 2k) )  (czyli ( \sum_{k=1}^{n} 3k ))

Wypisz trzy sumy w kolejności a), b), c).

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 1`)

### Wyjście

Trzy liczby naturalne — każda w oddzielnej linii:

1. suma dla (a)
2. suma dla (b)
3. suma dla (c)

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
10
16
9
```

### Uwagi o formatowaniu

* Wyniki są liczbami całkowitymi — nie stosuj żadnego dodatkowego zaokrąglania.

*/
fn main() {
    let mut n = String::new();
    std::io::stdin().read_line(&mut n).unwrap();
    let n: i32 = n.trim().parse().unwrap();

    // Podpunkt a) suma k^2 + k + 1
    let mut suma_a = 0;
    for k in 1..=n {
        suma_a += k * k + k + 1;
    }
    println!("{}", suma_a);

    // Podpunkt b) suma k^2 + 5k
    let mut suma_b = 0;
    for k in 1..=n {
        suma_b += k * k + 5 * k;
    }
    println!("{}", suma_b);

    // Podpunkt c) suma 3k
    let mut suma_c = 0;
    for k in 1..=n {
        suma_c += 3 * k;
    }
    println!("{}", suma_c);
}
