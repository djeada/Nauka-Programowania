/*
ZAD-02 — Wypisywanie liczb mniejszych od podanej

**Poziom:** ★☆☆
**Tagi:** `for`, `while`, `pętle`

### Treść

Wczytaj liczbę naturalną `n` (`n > 0`) i wypisz wszystkie liczby naturalne mniejsze od `n`, zaczynając od `n - 1` i kończąc na `1`.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n > 0`)

### Wyjście

Kolejne liczby naturalne mniejsze od `n`, każda w nowej linii, w kolejności malejącej.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
2
1
```

### Uwagi o formatowaniu

* Jeśli `n = 1`, nie wypisuj nic.

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Dla pobranej liczby, powinny zostac wyswietlone
    // wszystkie liczby naturalne mniejsze od podanej liczby.

    Scanner s = new Scanner(System.in);
    int n = Integer.parseInt(s.nextLine());

    for (int i = n - 1; i >= 1; i--) {
      System.out.println(i);
    }
  }
}

