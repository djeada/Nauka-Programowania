/*
ZAD-09 — Kalkulator kredytowy (rata annuitetowa)

**Poziom:** ★★☆
**Tagi:** `finanse`, `float`, `formatowanie`

### Treść

Wczytaj:

* roczną stopę procentową `R` (w %),
* okres spłaty `Y` (w latach),
* kwotę kredytu `P`.

Oblicz miesięczną ratę `M` oraz całkowity koszt `C = M * n`, gdzie `n = 12 * Y`.

Dla `R > 0` użyj wzoru:
[
M = P \cdot \frac{r(1+r)^n}{(1+r)^n-1}
]
gdzie `r = R / (12*100)`.

Dla `R = 0` przyjmij:

* `M = P / n`.

### Wejście

3 liczby (w osobnych liniach):

1. `R` (float, `R ≥ 0`)
2. `Y` (int, `Y > 0`)
3. `P` (float, `P > 0`)

### Wyjście

Dwie linie (do **2 miejsc po przecinku**):

1. miesięczna rata `M`
2. całkowity koszt `C`

### Przykład

**Wejście:**

```
3.5
8
12000
```

**Wyjście:**

```
143.50
13776.00
```

*/
fn main() {
    let mut r_str = String::new();
    std::io::stdin().read_line(&mut r_str).unwrap();
    let r_annual: f64 = r_str.trim().parse().unwrap();

    let mut y_str = String::new();
    std::io::stdin().read_line(&mut y_str).unwrap();
    let y: i32 = y_str.trim().parse().unwrap();

    let mut p_str = String::new();
    std::io::stdin().read_line(&mut p_str).unwrap();
    let p: f64 = p_str.trim().parse().unwrap();

    let n = 12 * y;
    let m: f64;

    if r_annual == 0.0 {
        m = p / (n as f64);
    } else {
        let r = r_annual / (12.0 * 100.0);
        m = p * (r * (1.0 + r).powi(n)) / ((1.0 + r).powi(n) - 1.0);
    }

    let c = m * (n as f64);

    println!("{:.2}", m);
    println!("{:.2}", c);
}
