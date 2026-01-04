/*
ZAD-08 — Koszt pokrycia podłogi płytkami

**Poziom:** ★★☆
**Tagi:** `ceil`, `arytmetyka`, `formatowanie`, `geometria`

### Treść

Dane są:

* cena jednej płytki `p`,
* bok płytki `t` (płytka kwadratowa),
* długość podłogi `L`,
* szerokość podłogi `W`.

Oblicz liczbę płytek potrzebnych do pokrycia całej podłogi, zakładając układ bez docinania „na styk” (czyli wzdłuż każdego wymiaru zaokrąglasz w górę), a następnie podaj koszt całkowity.

### Wejście

4 liczby (każda w osobnej linii): `p`, `t`, `L`, `W`

### Wyjście

Jedna liczba: całkowity koszt do **2 miejsc po przecinku**.

### Ograniczenia / gwarancje

* `p > 0`, `t > 0`, `L > 0`, `W > 0`
* Liczba płytek:

  * `nL = ceil(L / t)`
  * `nW = ceil(W / t)`
  * `n = nL * nW`
* Koszt: `n * p`

### Przykład

**Wejście:**

```
2
3
20
40
```

**Wyjście:**

```
196.00
```

*/
fn main() {
    let mut p = String::new();
    std::io::stdin().read_line(&mut p).unwrap();
    let p: f64 = p.trim().parse().unwrap();

    let mut t = String::new();
    std::io::stdin().read_line(&mut t).unwrap();
    let t: f64 = t.trim().parse().unwrap();

    let mut l = String::new();
    std::io::stdin().read_line(&mut l).unwrap();
    let l: f64 = l.trim().parse().unwrap();

    let mut w = String::new();
    std::io::stdin().read_line(&mut w).unwrap();
    let w: f64 = w.trim().parse().unwrap();

    let nl = (l / t).ceil();
    let nw = (w / t).ceil();
    let n = nl * nw;
    let cost = n * p;

    println!("{:.2}", cost);
}
