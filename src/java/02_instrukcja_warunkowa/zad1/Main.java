/*
ZAD-01 — Liczba większa od 5

**Poziom:** ★☆☆
**Tagi:** `if`, `porównania`, `I/O`

### Treść

Wczytaj jedną liczbę naturalną `n`.
Jeśli `n > 5`, wypisz `n`. W przeciwnym razie nie wypisuj nic.

### Wejście

* 1 linia: `n` (liczba całkowita, `n ≥ 0`)

### Wyjście

* Jeśli `n > 5`: jedna linia z liczbą `n`
* Jeśli `n ≤ 5`: brak wyjścia

### Przykład 1

**Wejście:**

```
10
```

**Wyjście:**

```
10
```

### Przykład 2

**Wejście:**

```
3
```

**Wyjście:** *(brak)*

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Wypisz pobrana od uzytkownika liczbe, jesli jest wieksza od 5.

    Scanner s = new Scanner(System.in);
    int n = Integer.parseInt(s.nextLine());

    if (n > 5) {
      System.out.println(n);
    }
  }
}

