/*
ZAD-05A — Funkcja liniowa: y = 3x + 10

**Poziom:** ★★☆
**Tagi:** `arytmetyka`, `float`, `formatowanie`

### Wejście

1 liczba: `x` (może być całkowita lub zmiennoprzecinkowa)

### Wyjście

1 liczba: `y` wypisana z dokładnością do **3 miejsc po przecinku**.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
19.000
```

ZAD-05B — Funkcja liniowa: y = ax + b

**Poziom:** ★★☆
**Tagi:** `arytmetyka`, `float`

### Wejście

3 liczby (każda w osobnej linii): `a`, `b`, `x`

### Wyjście

`y` do 3 miejsc po przecinku.

### Przykład

**Wejście:**

```
1
2
3
```

**Wyjście:**

```
5.000
```

ZAD-05C — Funkcja sześcienna: y = x³ + 2

**Poziom:** ★★☆
**Tagi:** `potęgi`, `float`

### Treść

Oblicz: `y = x^3 + 22 - 20`, czyli równoważnie `y = x^3 + 2`.

### Wejście

1 liczba: `x`

### Wyjście

`y` do 3 miejsc po przecinku.

### Przykład

**Wejście:**

```
5
```

**Wyjście:**

```
127.000
```

ZAD-05D — Wielomian z potęgami: y = a·x^m + b·x^n + c − a

**Poziom:** ★★☆
**Tagi:** `potęgi`, `float`

### Wejście

6 liczb (w osobnych liniach): `a`, `b`, `c`, `m`, `n`, `x`

### Wyjście

`y` do 3 miejsc po przecinku.

### Ograniczenia / gwarancje

* `m` i `n` są liczbami całkowitymi (np. nieujemnymi), aby potęgowanie było jednoznaczne w typowych językach.

### Przykład

**Wejście:**

```
1
1
1
1
1
1
```

**Wyjście:**

```
2.000
```

ZAD-05E — Funkcja z trygonometrią, wykładniczą i logarytmem

**Poziom:** ★★★☆
**Tagi:** `math`, `trygonometria`, `log`, `exp`, `float`

### Treść

Dla `x` (w radianach) oblicz:
[
y=\sin^3(x)\cdot\cos^2(x)+e^{x^2}+\ln(x^3+2x^2-x-3)
]

### Wejście

1 liczba zmiennoprzecinkowa: `x` (w radianach)

### Wyjście

`y` do 3 miejsc po przecinku.

### Ograniczenia / gwarancje

* Dane testowe spełniają warunek dziedziny logarytmu:

  * (x^3+2x^2-x-3 > 0)

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
57.179
```

*/

use ::std::*;

fn main() {
    // Podpunkt a)
    println!("Podaj wspolrzedna x: ");
    let mut x = String::new();
    std::io::stdin().read_line(&mut x).expect("Blad odczytu");
    let x: f64 = x.trim().parse().expect("Blad parsowania");
    println!(
        "Wartosc funkcji y=3x+10 w punkcie {} wynosi: {}",
        x,
        3 * x + 10
    );

    // Podpunkt b)
    println!("Podaj wspolczynnik a: ");
    let mut a = String::new();
    std::io::stdin().read_line(&mut a).expect("Blad odczytu");
    let a: f64 = a.trim().parse().expect("Blad parsowania");
    println!("Podaj wspolczynnik b: ");
    let mut b = String::new();
    std::io::stdin().read_line(&mut b).expect("Blad odczytu");
    let b: f64 = b.trim().parse().expect("Blad parsowania");
    println!("Podaj wspolrzedna x: ");
    let mut x = String::new();
    std::io::stdin().read_line(&mut x).expect("Blad odczytu");
    let x: f64 = x.trim().parse().expect("Blad parsowania");
    println!(
        "Wartosc funkcji y={}x+{} w punkcie {} wynosi: {}",
        a,
        b,
        x,
        a * x + b
    );

    // Podpunkt c)
    println!("Podaj wspolrzedna x: ");
    let mut x = String::new();
    std::io::stdin().read_line(&mut x).expect("Blad odczytu");
    let x: f64 = x.trim().parse().expect("Blad parsowania");
    println!(
        "Wartosc funkcji y=x3+22-20 w punkcie {} wynosi: {}",
        x,
        x * x * x + 22 - 20
    );

    // Podpunkt d)
    println!("Podaj wspolczynnik a: ");
    let mut a = String::new();
    std::io::stdin().read_line(&mut a).expect("Blad odczytu");
    let a: f64 = a.trim().parse().expect("Blad parsowania");
    println!("Podaj wspolczynnik b: ");
    let mut b = String::new();
    std::io::stdin().read_line(&mut b).expect("Blad odczytu");
    let b: f64 = b.trim().parse().expect("Blad parsowania");
    println!("Podaj wspolczynnik c: ");
    let mut c = String::new();
    std::io::stdin().read_line(&mut c).expect("Blad odczytu");
    let c: f64 = c.trim().parse().expect("Blad parsowania");
    println!("Podaj wspolczynnik d: ");
    let mut d = String::new();
    std::io::stdin().read_line(&mut d).expect("Blad odczytu");
    let d: f64 = d.trim().parse().expect("Blad parsowania");
    println!("Podaj wspolczynnik m: ");
    let mut m = String::new();
    std::io::stdin().read_line(&mut m).expect("Blad odczytu");
    let m: f64 = m.trim().parse().expect("Blad parsowania");
    println!("Podaj wspolczynnik n: ");
    let mut n = String::new();
    std::io::stdin().read_line(&mut n).expect("Blad odczytu");
    let n: f64 = n.trim().parse().expect("Blad parsowania");
    println!("Podaj wspolrzedna x: ");
    let mut x = String::new();
    std::io::stdin().read_line(&mut x).expect("Blad odczytu");
    let x: f64 = x.trim().parse().expect("Blad parsowania");
    println!(
        "Wartosc funkcji y={}x{}+{}x{}+{} w punkcie {} wynosi: {}",
        a,
        m,
        b,
        n,
        c,
        x,
        a * x * m + b * x * n + c
    );

    // Podpunkt e)
    println!("Podaj wspolrzedna x: ");
    let mut x = String::new();
    std::io::stdin().read_line(&mut x).expect("Blad odczytu");
    let x: f64 = x.trim().parse().expect("Blad parsowania");
    println!(
        "Wartosc funkcji y=sin3x*cos2x+e^2+log(x3+2x2-x-3) w punkcie {} wynosi: {}",
        x,
        (x * x * x).sin() * (x * x).cos() + x.exp() + x.ln()
    );
}
