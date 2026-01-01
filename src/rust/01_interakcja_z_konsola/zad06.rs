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
    // Podpunkt a)
    println!("Podaj wielkosc w kilogramach: ");
    let mut wielkosc_w_kg = String::new();
    std::io::stdin()
        .read_line(&mut wielkosc_w_kg)
        .expect("Blad odczytu");
    let wielkosc_w_kg: f32 = wielkosc_w_kg.trim().parse().expect("Blad parsowania");
    println!("{} kg to {} gram", wielkosc_w_kg, wielkosc_w_kg * 1000.0);

    // Podpunkt b)
    println!("Podaj wielkosc w calach: ");
    let mut wielkosc_w_calach = String::new();
    std::io::stdin()
        .read_line(&mut wielkosc_w_calach)
        .expect("Blad odczytu");
    let wielkosc_w_calach: f32 = wielkosc_w_calach.trim().parse().expect("Blad parsowania");
    println!(
        "{} cal to {} cm",
        wielkosc_w_calach,
        wielkosc_w_calach * 2.54
    );

    // Podpunkt c)
    println!("Podaj liczbe sekund: ");
    let mut liczba_sekund = String::new();
    std::io::stdin()
        .read_line(&mut liczba_sekund)
        .expect("Blad odczytu");
    let liczba_sekund: f32 = liczba_sekund.trim().parse().expect("Blad parsowania");
    println!(
        "{} sekund to {} godzin",
        liczba_sekund,
        liczba_sekund / 3600.0
    );

    // Podpunkt d)
    println!("Podaj liczbe w euro: ");
    let mut liczba_w_euro = String::new();
    std::io::stdin()
        .read_line(&mut liczba_w_euro)
        .expect("Blad odczytu");
    let liczba_w_euro: f32 = liczba_w_euro.trim().parse().expect("Blad parsowania");
    println!("{} euro to {} zlotych", liczba_w_euro, liczba_w_euro * 4.2);

    // Podpunkt e)
    println!("Podaj miare kata w stopniach: ");
    let mut miare_kata_w_stopniach = String::new();
    std::io::stdin()
        .read_line(&mut miare_kata_w_stopniach)
        .expect("Blad odczytu");
    let miare_kata_w_stopniach: f32 = miare_kata_w_stopniach
        .trim()
        .parse()
        .expect("Blad parsowania");
    println!(
        "{} stopni to {} radianow",
        miare_kata_w_stopniach,
        miare_kata_w_stopniach * 0.0174533
    );

    // Podpunkt f)
    println!("Podaj temperature w stopniach Fahrenheita: ");
    let mut temperature_w_stopniach_Fahrenheita = String::new();
    std::io::stdin()
        .read_line(&mut temperature_w_stopniach_Fahrenheita)
        .expect("Blad odczytu");
    let temperature_w_stopniach_Fahrenheita: f32 = temperature_w_stopniach_Fahrenheita
        .trim()
        .parse()
        .expect("Blad parsowania");
    println!(
        "{} stopni Fahrenheita to {} stopni Celsjusza",
        temperature_w_stopniach_Fahrenheita,
        (temperature_w_stopniach_Fahrenheita - 32.0) * 5.0 / 9.0
    );
    println!(
        "{} stopni Fahrenheita to {} stopni Kelwina",
        temperature_w_stopniach_Fahrenheita,
        (temperature_w_stopniach_Fahrenheita - 32.0) * 4.0 / 9.0
    );
}
