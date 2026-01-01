/*
ZAD-07A — Pole trójkąta

**Poziom:** ★☆☆
**Tagi:** `geometria`, `float`

### Treść

Oblicz pole trójkąta ze wzoru:
( P = \frac{1}{2} a h )

### Wejście

* 1 linia: `a`
* 2 linia: `h`

### Wyjście

* 1 linia: `P` do **3 miejsc po przecinku**

### Przykład

**Wejście:**

```
6
4
```

**Wyjście:**

```
12.000
```

ZAD-07B — Pole prostokąta

**Poziom:** ★☆☆
**Tagi:** `geometria`, `float`

### Treść

Oblicz pole prostokąta:
( P = ab )

### Wejście

* 1 linia: `a`
* 2 linia: `b`

### Wyjście

* 1 linia: `P` do **3 miejsc po przecinku**

### Przykład

**Wejście:**

```
2.5
4
```

**Wyjście:**

```
10.000
```

ZAD-07C — Pole rombu

**Poziom:** ★☆☆
**Tagi:** `geometria`, `float`

### Treść

Oblicz pole rombu z przekątnych:
( P = \frac{1}{2} d_1 d_2 )

### Wejście

* 1 linia: `d1`
* 2 linia: `d2`

### Wyjście

* 1 linia: `P` do **3 miejsc po przecinku**

### Przykład

**Wejście:**

```
10
6
```

**Wyjście:**

```
30.000
```

ZAD-07D — Objętość kuli

**Poziom:** ★★☆
**Tagi:** `geometria`, `pi`, `float`

### Treść

Oblicz objętość kuli:
( V = \frac{4}{3}\pi r^3 )

### Wejście

* 1 linia: `r`

### Wyjście

* 1 linia: `V` do **3 miejsc po przecinku**

### Przykład

**Wejście:**

```
1
```

**Wyjście:**

```
4.189
```

ZAD-07E — Objętość stożka

**Poziom:** ★★☆
**Tagi:** `geometria`, `pi`, `float`

### Treść

Oblicz objętość stożka:
( V = \frac{1}{3}\pi r^2 h )

### Wejście

* 1 linia: `r`
* 2 linia: `h`

### Wyjście

* 1 linia: `V` do **3 miejsc po przecinku**

### Przykład

**Wejście:**

```
2
3
```

**Wyjście:**

```
12.566
```

ZAD-07F — Objętość prostopadłościanu

**Poziom:** ★☆☆
**Tagi:** `geometria`, `float`

### Treść

Oblicz objętość prostopadłościanu:
( V = abc )

### Wejście

* 1 linia: `a`
* 2 linia: `b`
* 3 linia: `c`

### Wyjście

* 1 linia: `V` do **3 miejsc po przecinku**

### Przykład

**Wejście:**

```
2
3
4
```

**Wyjście:**

```
24.000
```

*/

use ::std::*;

fn main() {
    // ZAD-07A: Triangle area
    let mut a = String::new();
    std::io::stdin().read_line(&mut a).expect("Blad odczytu");
    let a: f64 = a.trim().parse().expect("Blad parsowania");
    let mut h = String::new();
    std::io::stdin().read_line(&mut h).expect("Blad odczytu");
    let h: f64 = h.trim().parse().expect("Blad parsowania");
    println!("{:.3}", 0.5 * a * h);

    // ZAD-07B: Rectangle area
    let mut a = String::new();
    std::io::stdin().read_line(&mut a).expect("Blad odczytu");
    let a: f64 = a.trim().parse().expect("Blad parsowania");
    let mut b = String::new();
    std::io::stdin().read_line(&mut b).expect("Blad odczytu");
    let b: f64 = b.trim().parse().expect("Blad parsowania");
    println!("{:.3}", a * b);

    // ZAD-07C: Rhombus area
    let mut d1 = String::new();
    std::io::stdin().read_line(&mut d1).expect("Blad odczytu");
    let d1: f64 = d1.trim().parse().expect("Blad parsowania");
    let mut d2 = String::new();
    std::io::stdin().read_line(&mut d2).expect("Blad odczytu");
    let d2: f64 = d2.trim().parse().expect("Blad parsowania");
    println!("{:.3}", 0.5 * d1 * d2);

    // ZAD-07D: Sphere volume
    let mut r = String::new();
    std::io::stdin().read_line(&mut r).expect("Blad odczytu");
    let r: f64 = r.trim().parse().expect("Blad parsowania");
    let pi = std::f64::consts::PI;
    println!("{:.3}", (4.0 / 3.0) * pi * r.powi(3));

    // ZAD-07E: Cone volume
    let mut r = String::new();
    std::io::stdin().read_line(&mut r).expect("Blad odczytu");
    let r: f64 = r.trim().parse().expect("Blad parsowania");
    let mut h = String::new();
    std::io::stdin().read_line(&mut h).expect("Blad odczytu");
    let h: f64 = h.trim().parse().expect("Blad parsowania");
    let pi = std::f64::consts::PI;
    println!("{:.3}", (1.0 / 3.0) * pi * r.powi(2) * h);

    // ZAD-07F: Cuboid volume
    let mut a = String::new();
    std::io::stdin().read_line(&mut a).expect("Blad odczytu");
    let a: f64 = a.trim().parse().expect("Blad parsowania");
    let mut b = String::new();
    std::io::stdin().read_line(&mut b).expect("Blad odczytu");
    let b: f64 = b.trim().parse().expect("Blad parsowania");
    let mut c = String::new();
    std::io::stdin().read_line(&mut c).expect("Blad odczytu");
    let c: f64 = c.trim().parse().expect("Blad parsowania");
    println!("{:.3}", a * b * c);
}
