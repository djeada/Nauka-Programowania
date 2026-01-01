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
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // ZAD-06A: Pobierz wielkosc w kilogramach i wypisz ilu gramom odpowiada.

    Scanner s = new Scanner(System.in);
    double kg = Double.parseDouble(s.nextLine());
    int g = (int) (kg * 1000);
    System.out.println(g);

    // ZAD-06B: Pobierz wielkosc w calach i wypisz ilu centymetrom odpowiada.

    double inch = Double.parseDouble(s.nextLine());
    double cm = inch * 2.54;
    System.out.printf("%.2f%n", cm);

    // ZAD-06C: Pobierz ilosc sekund i przelicz na pelne godziny.

    int s_val = Integer.parseInt(s.nextLine());
    int hours = s_val / 3600;
    System.out.println(hours);

    // ZAD-06D: Pobierz liczbe w euro i wypisz ilu zlotowkom odpowiada.

    double euro = Double.parseDouble(s.nextLine());
    double pln = euro * 4.4;
    System.out.printf("%.2f%n", pln);

    // ZAD-06E: Pobierz miare kata w stopniach i wypisz ilu radianom odpowiada.

    double deg = Double.parseDouble(s.nextLine());
    double rad = deg * Math.PI / 180;
    System.out.printf("%.3f%n", rad);

    // ZAD-06F: Pobierz temperature w stopniach Farenheita i wypisz
    // ilu stopniom Celsjusza oraz ilu stopniom Kelwina odpowiada.

    double tempF = Double.parseDouble(s.nextLine());
    double tempC = (tempF - 32) * 5 / 9;
    double tempK = tempC + 273.15;
    System.out.printf("%.3f%n", tempC);
    System.out.printf("%.3f%n", tempK);
  }
}

