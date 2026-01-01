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

Wczytaj temperaturę w stopniach Fahrenheita `F`. Oblicz temperaturę w
Celsjuszach oraz Kelvinach.

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
#include <cmath>
#include <iomanip>
#include <iostream>

int main() {
  // ZAD-06A: kg na g
  double kg;
  std::cin >> kg;
  int g = (int)(kg * 1000);
  std::cout << g << std::endl;

  // ZAD-06B: cale na cm
  double inch;
  std::cin >> inch;
  double cm = inch * 2.54;
  std::cout << std::fixed << std::setprecision(2) << cm << std::endl;

  // ZAD-06C: sekundy na pełne godziny
  int s;
  std::cin >> s;
  int hours = s / 3600;
  std::cout << hours << std::endl;

  // ZAD-06D: euro na pln
  double eur;
  std::cin >> eur;
  double pln = eur * 4.4;
  std::cout << std::fixed << std::setprecision(2) << pln << std::endl;

  // ZAD-06E: stopnie na radiany
  double deg;
  std::cin >> deg;
  double rad = deg * M_PI / 180;
  std::cout << std::fixed << std::setprecision(3) << rad << std::endl;

  // ZAD-06F: Fahrenheit na Celsius i Kelvin
  double F;
  std::cin >> F;
  double C = (5.0 / 9.0) * (F - 32);
  double K = C + 273.15;
  std::cout << std::fixed << std::setprecision(3) << C << std::endl;
  std::cout << std::fixed << std::setprecision(3) << K << std::endl;

  return 0;
}
