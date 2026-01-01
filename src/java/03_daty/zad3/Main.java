/*
ZAD-03 — Rok przestępny

**Poziom:** ★☆☆
**Tagi:** `modulo`, `if`, `kalendarz`

### Treść

Wczytaj rok `y` i sprawdź, czy jest przestępny w kalendarzu gregoriańskim.

Wypisz:

* `Rok jest przestępny.`
* `Rok nie jest przestępny.`

### Wejście

* 1 linia: `y` (liczba całkowita, `y ≥ 0`)

### Wyjście

Jedna linia — odpowiedni komunikat.

### Definicja

Rok jest przestępny, gdy:

* jest podzielny przez 400 **lub**
* jest podzielny przez 4 i **nie** jest podzielny przez 100.

### Przykład

**Wejście:**

```
2100
```

**Wyjście:**

```
Rok nie jest przestępny.
```

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Czy rok jest przestepny?

    Scanner s = new Scanner(System.in);
    int y = Integer.parseInt(s.nextLine());

    boolean isLeap = (y % 400 == 0) || (y % 4 == 0 && y % 100 != 0);

    if (isLeap) {
      System.out.println("Rok jest przestępny.");
    } else {
      System.out.println("Rok nie jest przestępny.");
    }
  }
}

