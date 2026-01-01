/*
ZAD-04 — Sumowanie liczb mniejszych od podanej

**Poziom:** ★☆☆
**Tagi:** `sumowanie`, `pętle`, `arytmetyka`

### Treść

Wczytaj liczbę naturalną `n` (`n ≥ 1`). Oblicz sumę wszystkich liczb naturalnych mniejszych od `n`, czyli:
`1 + 2 + ... + (n - 1)`
Następnie wypisz wynik.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 1`)

### Wyjście

Jedna liczba naturalna — suma liczb od `1` do `n - 1`.

### Przykład

**Wejście:**

```
5
```

**Wyjście:**

```
10
```

### Uwagi o formatowaniu

* Dla `n = 1` wynik to `0`.

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Dla pobranej liczby, powinna zostac wyswietlona suma
    // wszystkich liczb naturalnych mniejszych od pobranej liczby.

    Scanner s = new Scanner(System.in);
    int n = Integer.parseInt(s.nextLine());

    int suma = 0;
    for (int i = 1; i < n; i++) {
      suma += i;
    }

    System.out.println(suma);
  }
}

