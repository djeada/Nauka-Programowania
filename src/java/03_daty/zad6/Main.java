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
    // Pierwsza liczba jest dniem, druga miesiacem, trzecia rokiem.

    System.out.print("Podaj dzien, miesiac i rok: \n");

    int dzien;
    int miesiac;
    int rok;

    Scanner s = new Scanner(System.in);

    dzien = Integer.parseInt(s.nextLine());
    miesiac = Integer.parseInt(s.nextLine());
    rok = Integer.parseInt(s.nextLine());

    if (rok >= 1) {
      if (miesiac == 1
          || miesiac == 3
          || miesiac == 5
          || miesiac == 7
          || miesiac == 8
          || miesiac == 10
          || miesiac == 12) {
        if (dzien >= 1 && dzien <= 31) {
          System.out.print("Podana data jest poprawna\n");
        } else {
          System.out.print("Podano niepoprawna date\n");
        }
      } else if (miesiac == 4 || miesiac == 6 || miesiac == 9 || miesiac == 11) {
        if (dzien >= 1 && dzien <= 30) {
          System.out.print("Podana data jest poprawna\n");
        } else {
          System.out.print("Podano niepoprawna date\n");
        }
      } else if (miesiac == 2) {
        if (rok % 4 == 0) {
          if (rok % 100 == 0) {
            if (rok % 400 == 0 && dzien >= 1 && dzien <= 29) {
              System.out.print("Podana data jest poprawna\n");
            } else if (dzien >= 1 && dzien <= 28) {
              System.out.print("Podana data jest poprawna\n");
            } else {
              System.out.print("Podano niepoprawna date\n");
            }
          } else if (dzien >= 1 && dzien <= 29) {
            System.out.print("Podana data jest poprawna\n");
          } else {
            System.out.print("Podano niepoprawna date\n");
          }
        } else if (dzien >= 1 && dzien <= 28) {
          System.out.print("Podana data jest poprawna\n");
        }
      } else {
        System.out.print("Podano niepoprawna date\n");
      }
    } else {
      System.out.print("Podano niepoprawna date\n");
    }
  }
}

