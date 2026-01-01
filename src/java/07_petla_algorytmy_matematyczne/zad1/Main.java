/*
ZAD-01 — Obliczanie średniej z n liczb

**Poziom:** ★☆☆
**Tagi:** `pętle`, `suma`, `średnia`, `float`

### Treść

Napisz funkcję `oblicz_srednia()`, która:

1. Wczytuje liczbę naturalną `n` (`n ≥ 1`).
2. Wczytuje następnie `n` liczb (całkowitych lub zmiennoprzecinkowych).
3. Zwraca ich średnią arytmetyczną.

### Wejście

* 1. linia: `n` (`n ≥ 1`)
* kolejne `n` linii: liczby (int lub float)

### Wyjście

Funkcja zwraca jedną liczbę zmiennoprzecinkową — średnią arytmetyczną.

### Przykład

**Wejście:**

```
2
4
6
```

**Wywołanie funkcji:**

```python
wynik = oblicz_srednia()
print(wynik)
```

**Wyjście:**

```
5.0
```

### Uwagi o formatowaniu

* Nie narzucamy liczby miejsc po przecinku — wypisz wynik w domyślnym formacie języka (lub jako `float`).

*/
import java.util.*;

public class Main {
  // Napisz funkcje, ktora dla otrzymanej liczby n,
  // poprosi uzytkownika o podanie n liczb i zwroci
  // ich srednia arytmetyczna

  public static float srednia(int n) {

    float suma = 0.0F;
    int x;

    for (int i = 0; i < n; i++) {
      System.out.print("Podaj liczbe: \n");
      Scanner s = new Scanner(System.in);
      x = Integer.parseInt(s.nextLine());
      suma += x;
    }

    return suma / n;
  }

  public static void main(String[] args) {
    System.out.print("Podaj liczbe: \n");
    Scanner s = new Scanner(System.in);
    int n = Integer.parseInt(s.nextLine());

    float wynik = srednia(n);

    System.out.print("Srednia z podanych liczb to " + wynik + "\n");
  }
}

