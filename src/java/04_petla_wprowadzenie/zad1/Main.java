/*
ZAD-01 — Warunek kończący pętlę

**Poziom:** ★☆☆
**Tagi:** `while`, `break`, `I/O`

### Treść

Wczytuj kolejne liczby naturalne, dopóki nie pojawi się liczba `7`.
Po wczytaniu liczby `7` program kończy działanie **bez wypisywania czegokolwiek**.

### Wejście

Dowolna liczba liczb naturalnych (każda w osobnej linii).

### Ograniczenia / gwarancje

* W danych wejściowych na pewno pojawi się co najmniej jedna liczba `7`.

### Wyjście

Brak.

### Przykład

**Wejście:**

```
3
10
5
7
```

**Wyjście:**

```
```

*(brak danych wyjściowych)*

### Uwagi o formatowaniu

* Nie wypisuj żadnych komunikatów typu „Podaj liczbę”.
* Liczba `7` kończy wczytywanie i nie jest dalej przetwarzana.

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {
    // Pros uzytkownika o podanie liczby, dopoki
    // nie zostanie podana liczba 7.

    Scanner s = new Scanner(System.in);
    int a = 0;

    while (a != 7) {
      a = Integer.parseInt(s.nextLine());
    }
  }
}

