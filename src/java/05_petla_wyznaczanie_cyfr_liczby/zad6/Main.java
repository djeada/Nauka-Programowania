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

    // Dla pobranej liczby n, wyswietl liczby spelniajace rozne warunki

    Scanner s = new Scanner(System.in);
    int n = Integer.parseInt(s.nextLine());

    // a) mniejsze od n, ktorych suma cyfr jest rowna 10
    for (int i = 0; i < n; i++) {
      int temp = i;
      int sum = 0;
      while (temp > 0) {
        sum += (temp % 10);
        temp /= 10;
      }
      if (sum == 10) {
        System.out.println(i);
      }
    }

    // b) dwucyfrowe wieksze od n
    for (int i = Math.max(10, n + 1); i < 100; i++) {
      System.out.println(i);
    }

    // c) trzycyfrowe ktorych suma cyfr jest rowna n
    for (int i = 100; i < 1000; i++) {
      int temp = i;
      int sum = 0;
      while (temp > 0) {
        sum += (temp % 10);
        temp /= 10;
      }
      if (sum == n) {
        System.out.println(i);
      }
    }

    // d) trzycyfrowe podzielne przez sume cyfr n
    int temp = n;
    int sumN = 0;
    while (temp > 0) {
      sumN += (temp % 10);
      temp /= 10;
    }
    if (sumN > 0) {
      for (int i = 100; i < 1000; i++) {
        if (i % sumN == 0) {
          System.out.println(i);
        }
      }
    }

    // e) mniejsze od n, skladajace sie wylacznie z parzystych cyfr
    for (int i = 0; i < n; i++) {
      temp = i;
      boolean allEven = true;
      if (i == 0) {
        allEven = true; // 0 is considered all even
      } else {
        while (temp > 0) {
          int digit = temp % 10;
          if (digit % 2 == 1) {
            allEven = false;
            break;
          }
          temp /= 10;
        }
      }
      if (allEven) {
        System.out.println(i);
      }
    }
  }
}

