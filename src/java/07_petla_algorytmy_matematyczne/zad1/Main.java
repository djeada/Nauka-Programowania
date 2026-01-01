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

  public static double obliczSrednia() {
    Scanner s = new Scanner(System.in);
    int n = Integer.parseInt(s.nextLine());
    
    double sum = 0.0;
    for (int i = 0; i < n; i++) {
      double x = Double.parseDouble(s.nextLine());
      sum += x;
    }
    
    return sum / n;
  }

  public static void main(String[] args) {
    double result = obliczSrednia();
    System.out.println(result);
  }
}

