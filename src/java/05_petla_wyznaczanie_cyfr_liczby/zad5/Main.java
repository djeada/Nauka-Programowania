/*
ZAD-05 — Sprawdzanie, czy liczba jest palindromem

**Poziom:** ★★☆
**Tagi:** `string`, `pętle`, `odwracanie`

### Treść

Wczytaj liczbę naturalną `n`. Sprawdź, czy jest palindromem (czyli czy po odwróceniu cyfr pozostaje taka sama). Wypisz odpowiedni komunikat:

* `Liczba jest palindromem.`
* `Liczba nie jest palindromem.`

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Jeden komunikat tekstowy (dokładnie jeden z powyższych).

### Przykład

**Wejście:**

```
13231
```

**Wyjście:**

```
Liczba jest palindromem.
```

### Uwagi o formatowaniu

* `0` jest palindromem.

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Dla pobranej liczby, sprawdz czy jest palindromem.

    System.out.print("Podaj liczbe\n");
    Scanner s = new Scanner(System.in);
    int a = Integer.parseInt(s.nextLine());

    int odwrocona = 0;
    int pom = a;

    while (pom > 0) {
      int cyfra = pom % 10;
      odwrocona = (odwrocona * 10 + cyfra);
      pom /= 10;
    }

    if (odwrocona == a) {
      System.out.print("podana liczba jest palindromem\n");
    } else {
      System.out.print("podana liczba nie jest palindromem\n");
    }
  }
}

