/*
ZAD-02 — Pełnoletność (18 lat)

**Poziom:** ★☆☆
**Tagi:** `daty`, `porównywanie`, `if`

### Treść

Wczytaj datę urodzenia oraz datę „dzisiaj” i sprawdź, czy osoba ma **ukończone 18 lat** w dniu daty aktualnej.

Wypisz:

* `Osoba jest pełnoletnia.` — jeśli ma ≥ 18 lat,
* `Osoba nie jest pełnoletnia.` — w przeciwnym razie.

### Wejście

6 liczb całkowitych (każda w osobnej linii):

1. `d1` — dzień urodzenia
2. `m1` — miesiąc urodzenia
3. `y1` — rok urodzenia
4. `d2` — aktualny dzień
5. `m2` — aktualny miesiąc
6. `y2` — aktualny rok

### Wyjście

Jedna linia — jeden z komunikatów.

### Ograniczenia / gwarancje

* Obie daty są poprawne (nie musisz walidować).
* Pełnoletność jest osiągana **dokładnie w dniu 18. urodzin**.

### Uwagi (jak to porównać)

Osoba jest pełnoletnia wtedy, gdy data `y1+18, m1, d1` jest **nie późniejsza** niż data aktualna.

### Przykład

**Wejście:**

```
5
12
1999
20
11
2020
```

**Wyjście:**

```
Osoba jest pełnoletnia.
```

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Czy osoba jest pelnoletnia?

    System.out.print("Podaj trzy liczby reprezentujace dzien, miesiac i rok urodzenia osoby:\n");

    int dzien;
    int miesiac;
    int rok;

    Scanner s = new Scanner(System.in);

    dzien = Integer.parseInt(s.nextLine());
    miesiac = Integer.parseInt(s.nextLine());
    rok = Integer.parseInt(s.nextLine());

    System.out.print("Podaj trzy liczby reprezentujace dzisiejsza date:\n");

    int dzienAktualny;
    int miesiacAktualny;
    int rokAktualny;

    dzienAktualny = Integer.parseInt(s.nextLine());
    miesiacAktualny = Integer.parseInt(s.nextLine());
    rokAktualny = Integer.parseInt(s.nextLine());

    int roznicaLata = rokAktualny - rok;
    int roznicaMiesiace = miesiacAktualny - miesiac;
    int roznicaDni = dzienAktualny - dzien;

    if (roznicaLata > 18) {
      System.out.print("osoba jest pelnoletnia\n");
    } else if (roznicaLata == 18) {

      if (roznicaMiesiace > 0) {
        System.out.print("osoba jest pelnoletnia\n");
      } else if (roznicaMiesiace == 0) {

        if (roznicaDni >= 0) {
          System.out.print("osoba jest pelnoletnia\n");
        } else {
          System.out.print("osoba nie jest pelnoletnia\n");
        }
      } else {
        System.out.print("osoba nie jest pelnoletnia\n");
      }
    } else {
      System.out.print("osoba nie jest pelnoletnia\n");
    }
  }
}

