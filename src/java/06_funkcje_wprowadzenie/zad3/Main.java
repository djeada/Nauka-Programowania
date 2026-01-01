/*
ZAD-03 — Sprawdzanie warunków logicznych

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `bool`, `warunki`

### Treść

Napisz funkcję `sprawdz_warunki(a, b)`, która dla dwóch liczb naturalnych zwraca cztery wartości logiczne (np. jako krotkę) odpowiadające warunkom:

a) Czy `a > b`?
b) Czy `a + b < 10`?
c) Czy obie liczby są nieparzyste?
d) Czy `max(a, b) < a^2`?

### Wejście

Dwa argumenty funkcji:

* `a` (liczba całkowita, `a ≥ 0`)
* `b` (liczba całkowita, `b ≥ 0`)

### Wyjście

Cztery wartości logiczne w kolejności a), b), c), d).

### Przykład

**Wywołanie funkcji:**

```python
A, B, C, D = sprawdz_warunki(3, 2)
print(A)
print(B)
print(C)
print(D)
```

**Wyjście:**

```
True
True
False
True
```

*/
import java.util.*;

public class Main {
  // Pobierz dwie liczby od uzytkownika. Napisz funkcje, ktora
  // dla otrzymanych dwoch liczb ustali czy:

  // a) pierwsza liczba jest wieksza od drugiej
  public static boolean czyWieksza(int a, int b) {
    return a > b;
  }

  // b) czy suma liczb jest mneijsza niz 10
  public static boolean czySumaMniejsza(int a, int b) {
    int suma = a + b;
    return suma < 10;
  }

  // c) czy obie sa nieparzyste
  public static boolean czyObieNieparzyste(int a, int b) {
    return a % 2 == 1 && b % 2 == 1;
  }

  // d) czy wieksza liczba jest mniejsza
  // od pierwszej podniesionej do kwadratu
  public static int wieksza(int a, int b) {
    return a > b ? a : b;
  }

  public static boolean czyWiekszaNizKwad(int a, int b) {
    return wieksza(a, b) < Math.pow(a, 2);
  }

  public static void main(String[] args) {

    System.out.print("Podaj dwie liczby: \n");

    Scanner s = new Scanner(System.in);

    int a = Integer.parseInt(s.nextLine());
    int b = Integer.parseInt(s.nextLine());

    System.out.print("Pierwsza liczba jest wieksza od drugiej: ");
    System.out.printf("%b", czyWieksza(a, b));
    System.out.printf("\n");

    System.out.printf("Suma liczb jest mniejsza od 10: ");
    System.out.printf("%b", czySumaMniejsza(a, b));
    System.out.printf("\n");

    System.out.printf("Obie liczby nieparzyste: ");
    System.out.printf("%b", czyObieNieparzyste(a, b));
    System.out.printf("\n");

    System.out.printf("Wieksza liczba jest mniejsza od pierwszej podniesionej do kwadratu: ");
    System.out.printf("%b", czyWiekszaNizKwad(a, b));
    System.out.printf("\n");
  }
}

