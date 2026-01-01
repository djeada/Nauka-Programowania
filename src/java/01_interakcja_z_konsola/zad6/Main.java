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

    // Pobierz wielkosc w kilogramach i wypisz ilu gramom odpowiada.

    System.out.print("podaj wielkosc w kilogramach:\n");

    int kilogramy;
    Scanner s = new Scanner(System.in);

    kilogramy = Integer.parseInt(s.nextLine());
    int gramy = kilogramy * 1000;

    System.out.print(kilogramy);
    System.out.print(" kg to ");
    System.out.print(gramy);
    System.out.print(" g.\n");

    // Pobierz wielkosc w calach i wypisz ilu centymetrom odpowiada.

    System.out.print("podaj wielkosc w calach:");
    System.out.print("\n");

    float cal;
    cal = Float.parseFloat(s.nextLine());
    float cm = (float) (cal / 2.54);

    System.out.print(cal);
    System.out.print(" cal to ");
    System.out.print(cm);
    System.out.print(" cm.\n");

    // Pobierz ilosc sekund i przelicz na godziny.

    System.out.print("podaj ilosc sekund:\n");

    float sekundy;
    sekundy = Float.parseFloat(s.nextLine());
    float godziny = sekundy / 3600;

    System.out.print(sekundy);
    System.out.print(" sekund to ");
    System.out.print(godziny);
    System.out.print(" godzin\n");

    // Pobierz liczbe w euro i wypisz ilu zlotowkom odpowiada.

    System.out.print("podaj liczbe w euro:\n");

    float euro;
    euro = Float.parseFloat(s.nextLine());
    float zloty = (float) (euro * 4.40);

    System.out.print(euro);
    System.out.print(" euro to ");
    System.out.print(zloty);
    System.out.print(" zlotych");
    System.out.print("\n");

    // Pobierz miare kata w stopniach i wypisz ilu radianom odpowiada.

    System.out.print("podaj miare kata w stopniach:\n");

    float katStopnie;
    katStopnie = Float.parseFloat(s.nextLine());
    float katRad = (float) (katStopnie * 0.0174532);

    System.out.print(katStopnie);
    System.out.print(" stopni to ");
    System.out.print(katRad);
    System.out.print(" radianow.\n");

    // Pobierz temperature w stopniach Farenheita i wypisz
    // ilu stopniom Celsjusza oraz ilu stopniom Kelwina odpowiada.

    System.out.print("podaj temperature w Farenheitach:\n");

    float tempF;
    tempF = Float.parseFloat(s.nextLine());
    float tempC = (tempF - 32) * 5 / 9;
    float tempK = tempC - 273;

    System.out.print(tempF);
    System.out.print(" F to ");
    System.out.print(tempC);
    System.out.print(" C i ");
    System.out.print(tempK);
    System.out.print(" K\n");
  }
}

