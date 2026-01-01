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
    // Podpunkt a)
    println!("Podaj dlugosc podstawy trojkata: ");
    let mut a = String::new();
    std::io::stdin().read_line(&mut a).expect("Blad odczytu");
    let a: i32 = a.trim().parse().expect("Blad parsowania");
    println!("Podaj wysokosc trojkata: ");
    let mut h = String::new();
    std::io::stdin().read_line(&mut h).expect("Blad odczytu");
    let h: i32 = h.trim().parse().expect("Blad parsowania");
    println!("Pole trojkata wynosi: {}", a * h / 2);

    // Podpunkt b)
    println!("Podaj dlugosc a boku prostokata: ");
    let mut a = String::new();
    std::io::stdin().read_line(&mut a).expect("Blad odczytu");
    let a: i32 = a.trim().parse().expect("Blad parsowania");
    println!("Podaj dlugosc b boku prostokata: ");
    let mut b = String::new();
    std::io::stdin().read_line(&mut b).expect("Blad odczytu");
    let b: i32 = b.trim().parse().expect("Blad parsowania");
    println!("Pole prostokata wynosi: {}", a * b);

    // Podpunkt c)
    println!("Podaj dlugosc przekatnej rombu: ");
    let mut a = String::new();
    std::io::stdin().read_line(&mut a).expect("Blad odczytu");
    let a: f32 = a.trim().parse().expect("Blad parsowania");
    println!("Pole rombu wynosi: {}", a * a / 2.00);

    // Podpunkt d)
    println!("Podaj promien kuli: ");
    let mut r = String::new();
    std::io::stdin().read_line(&mut r).expect("Blad odczytu");
    let r: f32 = r.trim().parse().expect("Blad parsowania");
    println!("Objetosc kuli wynosi: {}", (4.0 / 3.0) * 3.14 * (r * r * r));

    // Podpunkt e)
    println!("Podaj dlugosc podstawy stozka: ");
    let mut a = String::new();
    std::io::stdin().read_line(&mut a).expect("Blad odczytu");
    let a: f32 = a.trim().parse().expect("Blad parsowania");
    println!("Podaj wysokosc stozka: ");
    let mut h = String::new();
    std::io::stdin().read_line(&mut h).expect("Blad odczytu");
    let h: f32 = h.trim().parse().expect("Blad parsowania");
    println!("Objetosc stozka wynosi: {}", 1.00 / 3.00 * 3.14 * a * a * h);

    // Podpunkt f)
    println!("Podaj dlugosc graniastoslupa: ");
    let mut a = String::new();
    std::io::stdin().read_line(&mut a).expect("Blad odczytu");
    let a: i32 = a.trim().parse().expect("Blad parsowania");
    println!("Podaj szerokosc graniastoslupa: ");
    let mut b = String::new();
    std::io::stdin().read_line(&mut b).expect("Blad odczytu");
    let b: i32 = b.trim().parse().expect("Blad parsowania");
    println!("Podaj wysokosc graniastoslupa: ");
    let mut h = String::new();
    std::io::stdin().read_line(&mut h).expect("Blad odczytu");
    let h: i32 = h.trim().parse().expect("Blad parsowania");
    println!("Objetosc graniastoslupa wynosi: {}", a * b * h);
}
