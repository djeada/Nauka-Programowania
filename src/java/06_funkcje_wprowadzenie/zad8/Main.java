/*
ZAD-08 — Iloraz w dół bez / i %

**Poziom:** ★★☆
**Tagi:** `funkcje`, `pętle`, `odejmowanie`

### Treść

Napisz funkcję `zaokraglij_w_dol(a, b)`, która zwraca wartość `a // b`, ale **nie używa** operatorów `/` ani `%`.

### Wejście

Dwa argumenty:

* `a` (liczba naturalna, `a ≥ 0`)
* `b` (liczba naturalna)

### Ograniczenia / gwarancje

* `b > 0`

### Wyjście

Funkcja zwraca liczbę naturalną — iloraz `a` przez `b` zaokrąglony w dół.

### Przykład

**Wywołanie funkcji:**

```python
print(zaokraglij_w_dol(7, 2))
```

**Wyjście:**

```
3
```

*/
import java.util.*;

public class Main {
  // Napisz funkcje realizujaca zaokraglanie ilorazu bez uzycia '/' i '%'.

  public static int zaokraglij(int a, int b) {
    int count = 0;
    while (a >= b) {
      a -= b;
      count++;
    }
    return count;
  }

  public static void main(String[] args) {

    Scanner s = new Scanner(System.in);
    int a = Integer.parseInt(s.nextLine());
    int b = Integer.parseInt(s.nextLine());

    System.out.println(zaokraglij(a, b));
  }
}

