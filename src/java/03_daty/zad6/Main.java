/*
ZAD-06 — Sprawdzanie poprawności daty

**Poziom:** ★★☆
**Tagi:** `walidacja`, `przestępny`, `if`

### Treść

Wczytaj `d, m, y` i sprawdź, czy jest to poprawna data w kalendarzu gregoriańskim.

Wypisz:

* `Data jest poprawna.`
* `Data jest niepoprawna.`

### Wejście

3 liczby całkowite (w osobnych liniach):

1. `d` — dzień
2. `m` — miesiąc
3. `y` — rok

### Wyjście

Jedna linia — komunikat.

### Ograniczenia / gwarancje

* `y ≥ 0` (lub `y ≥ 1`, jeśli tak chcesz przyjąć — ważne, by było spójnie w całym zbiorze)

### Reguły walidacji

1. `m` musi być w zakresie 1–12
2. Ustal liczbę dni w miesiącu:

   * 31: 1,3,5,7,8,10,12
   * 30: 4,6,9,11
   * luty: 28 lub 29 (zależnie od przestępności roku)
3. `d` musi być w zakresie 1–dni_w_miesiącu

### Przykład

**Wejście:**

```
31
4
2021
```

**Wyjście:**

```
Data jest niepoprawna.
```

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Dla pobranych trzech liczb, sprawdz czy reprezentuja one poprawna date.

    Scanner s = new Scanner(System.in);
    int d = Integer.parseInt(s.nextLine());
    int m = Integer.parseInt(s.nextLine());
    int y = Integer.parseInt(s.nextLine());

    boolean valid = false;

    if (y >= 1 && m >= 1 && m <= 12 && d >= 1) {
      int[] days = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
      
      // Check for leap year
      if ((y % 400 == 0) || (y % 4 == 0 && y % 100 != 0)) {
        days[2] = 29;
      }
      
      if (d <= days[m]) {
        valid = true;
      }
    }

    if (valid) {
      System.out.println("Data jest poprawna.");
    } else {
      System.out.println("Data jest niepoprawna.");
    }
  }
}

