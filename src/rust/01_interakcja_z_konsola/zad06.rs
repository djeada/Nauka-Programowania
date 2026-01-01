/*
ZAD-06A — Kilogramy → gramy

**Poziom:** ★☆☆
**Tagi:** `konwersje`

### Treść

Wczytaj wartość w kilogramach `kg` i przelicz na gramy.

### Wejście

* 1 linia: `kg`

### Wyjście

* 1 linia: `g` jako **liczba całkowita**, gdzie:
  `g = kg * 1000`

### Gwarancje

* `kg` jest liczbą całkowitą **lub** taką, że wynik w gramach jest całkowity.

### Przykład

**Wejście:**

```
2.5
```

**Wyjście:**

```
2500
```

ZAD-06B — Cale → centymetry

**Poziom:** ★☆☆
**Tagi:** `konwersje`, `float`

### Treść

Wczytaj liczbę cali `inch` i przelicz na centymetry.

### Wejście

* 1 linia: `inch`

### Wyjście

* 1 linia: `cm = inch * 2.54` wypisane do **2 miejsc po przecinku**

### Przykład

**Wejście:**

```
10
```

**Wyjście:**

```
25.40
```

ZAD-06C — Sekundy → pełne godziny

**Poziom:** ★☆☆
**Tagi:** `dzielenie całkowite`

### Treść

Wczytaj liczbę sekund `s` i wypisz liczbę **pełnych godzin**.

### Wejście

* 1 linia: `s` (liczba całkowita, `s ≥ 0`)

### Wyjście

* 1 linia: `s // 3600`

### Przykład

**Wejście:**

```
8639
```

**Wyjście:**

```
2
```

ZAD-06D — Euro → złotówki (kurs stały)

**Poziom:** ★☆☆
**Tagi:** `konwersje`, `float`

### Treść

Wczytaj kwotę w euro `eur` i przelicz na złotówki przy stałym kursie.

### Wejście

* 1 linia: `eur`

### Wyjście

* 1 linia: `pln = eur * 4.4` do **2 miejsc po przecinku**

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
13.20
```

ZAD-06E — Stopnie → radiany

**Poziom:** ★☆☆
**Tagi:** `pi`, `float`

### Treść

Wczytaj kąt w stopniach `deg` i przelicz na radiany.

### Wejście

* 1 linia: `deg`

### Wyjście

* 1 linia: `rad = deg * π / 180` do **3 miejsc po przecinku**

### Przykład

**Wejście:**

```
180
```

**Wyjście:**

```
3.142
```

ZAD-06F — Fahrenheit → Celsius i Kelviny

**Poziom:** ★☆☆
**Tagi:** `konwersje`, `float`

### Treść

Wczytaj temperaturę w stopniach Fahrenheita `F`. Oblicz temperaturę w Celsjuszach oraz Kelvinach.

### Wejście

* 1 linia: `F`

### Wyjście

Dwie linie:

1. `C = (5/9) * (F - 32)` do **3 miejsc**
2. `K = C + 273.15` do **3 miejsc**

### Przykład

**Wejście:**

```
32
```

**Wyjście:**

```
0.000
273.150
```

*/

use ::std::*;

fn main() {
    const KELVIN_OFFSET: f64 = 273.15;
    const PI: f64 = std::f64::consts::PI;
    
    // Podpunkt a) kg -> g
    let mut kg = String::new();
    std::io::stdin().read_line(&mut kg).expect("Blad odczytu");
    let kg: f64 = kg.trim().parse().expect("Blad parsowania");
    println!("{}", (kg * 1000.0) as i32);

    // Podpunkt b) cale -> cm
    let mut inch = String::new();
    std::io::stdin().read_line(&mut inch).expect("Blad odczytu");
    let inch: f64 = inch.trim().parse().expect("Blad parsowania");
    println!("{:.2}", inch * 2.54);

    // Podpunkt c) sekundy -> pelne godziny
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).expect("Blad odczytu");
    let s: i32 = s.trim().parse().expect("Blad parsowania");
    println!("{}", s / 3600);

    // Podpunkt d) EUR -> PLN
    let mut eur = String::new();
    std::io::stdin().read_line(&mut eur).expect("Blad odczytu");
    let eur: f64 = eur.trim().parse().expect("Blad parsowania");
    println!("{:.2}", eur * 4.4);

    // Podpunkt e) stopnie -> radiany
    let mut deg = String::new();
    std::io::stdin().read_line(&mut deg).expect("Blad odczytu");
    let deg: f64 = deg.trim().parse().expect("Blad parsowania");
    println!("{:.3}", deg * PI / 180.0);

    // Podpunkt f) Fahrenheit -> Celsius i Kelvin
    let mut f = String::new();
    std::io::stdin().read_line(&mut f).expect("Blad odczytu");
    let f: f64 = f.trim().parse().expect("Blad parsowania");
    let c = (5.0 / 9.0) * (f - 32.0);
    let k = c + KELVIN_OFFSET;
    println!("{:.3}", c);
    println!("{:.3}", k);
}
