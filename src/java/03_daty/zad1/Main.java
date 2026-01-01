/*
ZAD-01 — Numer dnia tygodnia lub miesiąca

**Poziom:** ★☆☆
**Tagi:** `if`, `zakresy`, `I/O`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz `n` **tylko wtedy**, gdy jest poprawnym numerem:

* dnia tygodnia (1–7) **lub**
* miesiąca (1–12).

W praktyce oznacza to: wypisz `n` tylko wtedy, gdy `1 ≤ n ≤ 12`.

### Wejście

* 1 linia: `n` (liczba całkowita, `n ≥ 0`)

### Wyjście

* Jeśli `1 ≤ n ≤ 12`: wypisz `n` w osobnej linii
* W przeciwnym razie: brak wyjścia

### Przykłady

**Wejście:**

```
5
```

**Wyjście:**

```
5
```

**Wejście:**

```
15
```

**Wyjście:** *(brak)*

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Czy liczba jest numerem tygodnia/miesiaca?

    System.out.print("Podaj liczbe:\n");
    Scanner s = new Scanner(System.in);
    int a = Integer.parseInt(s.nextLine());

    if (a >= 1 && a <= 7) {
      System.out.print("Liczba jest poprawnym numerem tygodnia\n");
    } else {
      System.out.print("Liczba nie jest poprawnym numerem tygodnia\n");
    }

    if (a >= 1 && a <= 12) {
      System.out.print("Liczba jest poprawnym numerem miesiaca\n");
    } else {
      System.out.print("Liczba nie jest poprawnym numerem miesiaca\n");
    }
  }
}

