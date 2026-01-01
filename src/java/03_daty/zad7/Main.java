/*
ZAD-07 — Dzień roku (liczba dni od 1 stycznia, włącznie)

**Poziom:** ★★☆
**Tagi:** `sumowanie`, `tablice`, `przestępny`

### Treść

Wczytaj datę `d, m, y` i oblicz numer dnia w roku, tzn. ile dni minęło od 1 stycznia do tej daty **włącznie**.

### Wejście

3 liczby całkowite (w osobnych liniach): `d`, `m`, `y`

### Wyjście

Jedna liczba całkowita: numer dnia w roku.

### Ograniczenia / gwarancje

* Podana data jest poprawna (nie musisz jej sprawdzać), **albo** możesz jawnie napisać: „jeśli data jest niepoprawna, zachowanie nieokreślone”.

  * (Najczyściej: dać gwarancję poprawności.)

### Przykład

**Wejście:**

```
14
2
1482
```

**Wyjście:**

```
45
```

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {
    
    // Oblicz numer dnia w roku

    Scanner s = new Scanner(System.in);
    int d = Integer.parseInt(s.nextLine());
    int m = Integer.parseInt(s.nextLine());
    int y = Integer.parseInt(s.nextLine());

    int[] days = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    
    // Check for leap year
    if ((y % 400 == 0) || (y % 4 == 0 && y % 100 != 0)) {
      days[2] = 29;
    }

    int dayOfYear = d;
    for (int i = 1; i < m; i++) {
      dayOfYear += days[i];
    }

    System.out.println(dayOfYear);
  }
}
