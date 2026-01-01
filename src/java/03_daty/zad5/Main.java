/*
ZAD-05 — Liczba dni w miesiącu (rok nieprzestępny)

**Poziom:** ★☆☆
**Tagi:** `if`, `tablice`, `walidacja`

### Treść

Wczytaj numer miesiąca `m`. Zakładając rok **nieprzestępny**, wypisz liczbę dni w tym miesiącu.
Jeśli `m` nie jest w zakresie 1–12, wypisz:
`Niepoprawny numer miesiąca.`

### Wejście

* 1 linia: `m` (liczba całkowita, `m ≥ 0`)

### Wyjście

* liczba dni (jedna linia) **albo**
* komunikat o błędzie (jedna linia)

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
28
```

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Dla pobranej liczby, wyswietl liczbe dni miesiaca odpowiadajacemu danej liczbie.

    Scanner s = new Scanner(System.in);
    int m = Integer.parseInt(s.nextLine());

    int[] days = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    if (m >= 1 && m <= 12) {
      System.out.println(days[m]);
    } else {
      System.out.println("Niepoprawny numer miesiąca.");
    }
  }
}

