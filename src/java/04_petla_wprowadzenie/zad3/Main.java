/*
ZAD-03 — Wypisywanie liczby π z określoną dokładnością

**Poziom:** ★☆☆
**Tagi:** `math.pi`, `formatowanie`, `pętle`

### Treść

1. Wczytaj liczbę naturalną `n` (`n > 0`).
2. Wypisz liczbę π dokładnie `n` razy.
3. Każda wypisana wartość ma mieć **dokładnie `n` miejsc po przecinku**.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n > 0`)

### Wyjście

`n` wierszy, w każdym liczba π z dokładnością do `n` miejsc po przecinku.

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
3.14
3.14
```

### Uwagi o formatowaniu

* Liczba miejsc po przecinku ma być **dokładnie** równa `n` (np. dla `n=1` wypisz `3.1`).
* Stosuj standardowe zaokrąglanie przy formatowaniu.

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Dla pobranej liczby, wyswietl liczbe Pi tyle razy
    // ile wynosi pobrana liczba, z dokladnoscia do tylu
    // miejsc po przescinku ile wynosi pobrana liczba.

    System.out.print("Podaj liczbe: \n");
    Scanner s = new Scanner(System.in);
    int n = Integer.parseInt(s.nextLine());

    for (int i = 0; i < n; i++) {
      System.out.printf("%f", 3.14);
      System.out.printf("%f", " ");
    }
  }
}

