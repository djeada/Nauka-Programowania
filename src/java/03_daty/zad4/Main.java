/*
ZAD-04 — Dzień tygodnia z numeru

**Poziom:** ★☆☆
**Tagi:** `if-elif-else`, `mapowanie`, `string`

### Treść

Wczytaj liczbę `n`. Jeśli `n` jest w zakresie 1–7, wypisz nazwę dnia tygodnia:

1. Poniedziałek
2. Wtorek
3. Środa
4. Czwartek
5. Piątek
6. Sobota
7. Niedziela

W przeciwnym razie wypisz:
`Niepoprawny numer dnia tygodnia.`

### Wejście

* 1 linia: `n` (liczba całkowita, `n ≥ 0`)

### Wyjście

Jedna linia: nazwa dnia lub komunikat o błędzie.

### Przykład

**Wejście:**

```
8
```

**Wyjście:**

```
Niepoprawny numer dnia tygodnia.
```

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Dla pobranej liczby, wypisz dzien tygodnia odpowiadajacy tej liczbie.

    Scanner s = new Scanner(System.in);
    int n = Integer.parseInt(s.nextLine());

    switch (n) {
      case 1:
        System.out.println("Poniedziałek");
        break;
      case 2:
        System.out.println("Wtorek");
        break;
      case 3:
        System.out.println("Środa");
        break;
      case 4:
        System.out.println("Czwartek");
        break;
      case 5:
        System.out.println("Piątek");
        break;
      case 6:
        System.out.println("Sobota");
        break;
      case 7:
        System.out.println("Niedziela");
        break;
      default:
        System.out.println("Niepoprawny numer dnia tygodnia.");
    }
  }
}

