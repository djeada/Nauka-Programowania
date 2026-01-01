/*
ZAD-01 — Liczenie cyfr w liczbie

**Poziom:** ★☆☆
**Tagi:** `pętle`, `modulo`, `dzielenie całkowite`

### Treść

Wczytaj liczbę naturalną `n` i wypisz, z ilu cyfr składa się jej zapis dziesiętny.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Jedna liczba naturalna — liczba cyfr w `n`.

### Przykład

**Wejście:**

```
342
```

**Wyjście:**

```
3
```

### Ograniczenia / gwarancje

* `n` mieści się w typowym zakresie liczb całkowitych.

### Uwagi o formatowaniu

* Dla `n = 0` poprawna odpowiedź to `1` (liczba „0” ma jedną cyfrę).

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {
    // Dla pobranej od uzytkownika liczby,
    // zwroc liczbe cyfr pobranej liczby.

    Scanner s = new Scanner(System.in);
    int n = Integer.parseInt(s.nextLine());

    if (n == 0) {
      System.out.println(1);
      return;
    }

    int count = 0;
    while (n > 0) {
      n = n / 10;
      count++;
    }

    System.out.println(count);
  }
}

