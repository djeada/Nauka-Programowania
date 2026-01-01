/*
ZAD-06A — Liczby mniejsze od n o sumie cyfr równej 10

**Poziom:** ★★☆
**Tagi:** `pętle`, `suma cyfr`, `warunki`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz wszystkie liczby naturalne `x` takie, że `0 ≤ x < n` oraz suma cyfr liczby `x` wynosi `10`. Każdą liczbę wypisz w osobnej linii.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Liczby spełniające warunek, każda w nowej linii.
Jeśli brak — brak wyjścia.

ZAD-06B — Dwucyfrowe większe od n

**Poziom:** ★★☆
**Tagi:** `pętle`, `przedziały`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz wszystkie liczby **dwucyfrowe** większe od `n` (czyli z zakresu 10–99), każdą w osobnej linii.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Liczby dwucyfrowe `x` takie, że `x > n`, każda w nowej linii.
Jeśli brak — brak wyjścia.

### Przykład (dla n = 95)

**Wejście:**

```
95
```

**Wyjście:**

```
96
97
98
99
```

ZAD-06C — Trzycyfrowe o sumie cyfr równej n

**Poziom:** ★★☆
**Tagi:** `pętle`, `suma cyfr`, `warunki`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz wszystkie liczby trzycyfrowe `x` (100–999), których suma cyfr jest równa `n`. Każdą liczbę wypisz w osobnej linii.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Liczby trzycyfrowe spełniające warunek, każda w nowej linii.
Jeśli brak — brak wyjścia.

ZAD-06D — Trzycyfrowe podzielne przez sumę cyfr liczby n

**Poziom:** ★★☆
**Tagi:** `pętle`, `dzielenie`, `suma cyfr`

### Treść

Wczytaj liczbę naturalną `n`. Oblicz sumę cyfr liczby `n` i oznacz ją jako `s`. Następnie wypisz wszystkie liczby trzycyfrowe `x` (100–999), które są podzielne przez `s`. Każdą liczbę wypisz w osobnej linii.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Ograniczenia / gwarancje

* Suma cyfr `n` jest większa od zera (czyli `n ≠ 0`), aby dzielenie było poprawne.

### Wyjście

Liczby trzycyfrowe podzielne przez `s`, każda w nowej linii.

ZAD-06E — Mniejsze od n złożone wyłącznie z parzystych cyfr

**Poziom:** ★★☆
**Tagi:** `pętle`, `warunki`, `cyfry`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz wszystkie liczby naturalne `x` takie, że `0 ≤ x < n` oraz każda cyfra w zapisie dziesiętnym `x` jest parzysta. Każdą liczbę wypisz w osobnej linii.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Liczby spełniające warunek, każda w nowej linii.
Jeśli brak — brak wyjścia.

### Przykład (dla n = 95)

**Wejście:**

```
95
```

**Wyjście:**

```
2
4
6
8
22
24
26
28
42
44
46
48
62
64
66
68
82
84
86
88
```

### Uwagi o formatowaniu

* W tym zadaniu `0` też składa się wyłącznie z parzystych cyfr. Jeśli chcesz je uwzględniać, dopisz to jako regułę w treści (tu: pomijamy `0`, bo w przykładzie go nie ma).

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Dla pobranej liczby n, wyswietl sume n
    // pierwszych wyrazow ciagu danego wzorem:
    System.out.print("Podaj liczbe\n");
    Scanner s = new Scanner(System.in);
    int a = Integer.parseInt(s.nextLine());

    // a) mniejsze od pobranej liczby, ktorych suma cyfr jest rowna 10

    System.out.print("mniejsze od pobranej liczby, ktorych suma cyfr jest rowna 10: \n");
    for (int i = 0; i < a; i++) {
      int pom = i;
      int suma = 0;

      while (pom > 0) {
        suma += (pom % 10);
        pom /= 10;
      }

      if (suma == 10) {
        System.out.print(i);
        System.out.print("\n");
      }
    }

    // b) dwucyfrowe mniejsze od pobranej liczby

    System.out.print("dwucyfrowe mniejsze od pobranej liczby: \n");
    for (int i = 10; i < 100 && i < a; i++) {
      System.out.print(i);
      System.out.print("\n");
    }

    // c) trzycyfrowe ktorych suma cyfr jest	rowna pobranej liczbie
    System.out.print("trzycyfrowe ktorych suma cyfr jest rowna pobranej liczbie\n");
    for (int i = 100; i < 1000; i++) {
      int pom = i;
      int suma = 0;

      while (pom > 0) {
        suma += (pom % 10);
        pom /= 10;
      }

      if (suma == a) {
        System.out.print(i);
        System.out.print("\n");
      }
    }

    // d) trzycyfrowe podzielne przez sume cyfr pobranej liczby
    System.out.print("trzycyfrowe podzielne przez sume cyfr pobranej liczby\n");

    int pom = a;
    int suma = 0;

    while (pom > 0) {
      suma += (pom % 10);
      pom /= 10;
    }

    for (int i = 100; i < 1000; i++) {

      if (i % suma == 0) {
        System.out.print(i);
        System.out.print("\n");
      }
    }

    // e) mniejsze od pobranej liczby, skladajace sie wylacznie z parzystych cyfr
    System.out.print("mniejsze od pobranej liczby, skladajace sie wylacznie z parzystych cyfr\n");

    for (int i = 0; i < a; i++) {
      pom = i;
      boolean flaga = true;
      while (pom > 0) {
        int cyfra = pom % 10;
        if (cyfra % 2 == 1) {
          flaga = false;
          break;
        }
        pom /= 10;
      }

      if (flaga) {
        System.out.print(i);
        System.out.print("\n");
      }
    }
  }
}

