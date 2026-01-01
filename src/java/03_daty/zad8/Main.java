/*
ZAD-08 — Dzień tygodnia dla daty (Zeller)

**Poziom:** ★★☆
**Tagi:** `algorytmy`, `Zeller`, `mapowanie`, `daty`

### Treść

Wczytaj datę `d, m, y` i wyznacz nazwę dnia tygodnia, używając **kongruencji Zellera** dla kalendarza gregoriańskiego.

Kroki:

1. Jeśli `m <= 2`, to:

* `m = m + 12`
* `y = y - 1`

2. Oblicz:

* `K = y % 100`
* `J = y // 100`
* `h = (d + (13*(m+1))//5 + K + K//4 + J//4 + 5*J) % 7`

3. Zmapuj `h` na dzień tygodnia:

* 0 → `Sobota`
* 1 → `Niedziela`
* 2 → `Poniedziałek`
* 3 → `Wtorek`
* 4 → `Środa`
* 5 → `Czwartek`
* 6 → `Piątek`

### Wejście

3 liczby całkowite (w osobnych liniach): `d`, `m`, `y`

### Wyjście

Jedna linia: nazwa dnia tygodnia (dokładnie jedna z: Poniedziałek, Wtorek, Środa, Czwartek, Piątek, Sobota, Niedziela).

### Ograniczenia / gwarancje

* Data wejściowa jest poprawna (zalecane; inaczej dopisz, co robić dla błędnej).
* Kalendarz gregoriański.

### Przykład

**Wejście:**

```
9
10
2020
```

**Wyjście:**

```
Piątek
```

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    Scanner s = new Scanner(System.in);

    System.out.print("Podaj dzien:\n");
    int DD = Integer.parseInt(s.nextLine());

    System.out.print("Podaj miesiac:\n");
    int MM = Integer.parseInt(s.nextLine());
    ;

    System.out.print("Podaj rok:\n");
    int rok = Integer.parseInt(s.nextLine());
    ;

    int CC = rok / 100;
    int YY = rok % 100;

    int A = (CC / 4) - 2 * CC - 1;
    int B = 5 * YY / 4;
    int C = 26 * (MM + 1) / 10;

    int wynik = (A + B + C + DD) % 7;

    switch (wynik) {
      case 1:
        System.out.print("pierwszym dniem tygodnia jest poniedzialek\n");
        break;

      case 2:
        System.out.print("drugim dniem tygodnia jest wtorek\n");
        break;

      case 3:
        System.out.print("trzecim dniem tygodnia jest sroda\n");
        break;

      case 4:
        System.out.print("czwartym dniem tygodnia jest czwartek\n");
        break;

      case 5:
        System.out.print("piatym dniem tygodnia jest piatek\n");
        break;

      case 6:
        System.out.print("szostym dniem tygodnia jest sobota\n");
        break;

      case 7:
        System.out.print("siodmym dniem tygodnia jest niedziela\n");
        break;

      default:
        System.out.print("bledne dane\n");
    }
  }
}

