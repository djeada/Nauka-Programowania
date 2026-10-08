/*
ZAD-06A — Liczby mniejsze od n o sumie cyfr równej 10

**Poziom:** ★★☆
**Tagi:** `pętle`, `suma cyfr`, `warunki`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz w kolejności rosnącej wszystkie liczby naturalne `x` takie, że `x < n` i suma cyfr liczby `x` wynosi `10`.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Liczby spełniające warunek, każda w osobnej linii.
Jeśli takich liczb nie ma, nie wypisuj nic.

### Przykład

**Wejście:**

```
50
```

**Wyjście:**

```
19
28
37
46
```

### Uwagi

* Nierówność jest ostra: samej liczby `n` nie wypisujemy, nawet jeśli suma jej cyfr wynosi `10`.

ZAD-06B — Dwucyfrowe większe od n o różnych cyfrach

**Poziom:** ★★☆
**Tagi:** `pętle`, `cyfry`, `warunki`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz w kolejności rosnącej wszystkie liczby dwucyfrowe `x` (od `10` do `99`) takie, że `x > n` i cyfra dziesiątek liczby `x` jest **różna** od jej cyfry jedności.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Liczby spełniające warunek, każda w osobnej linii.
Jeśli takich liczb nie ma, nie wypisuj nic.

### Przykład

**Wejście:**

```
90
```

**Wyjście:**

```
91
92
93
94
95
96
97
98
```

Liczba `99` jest większa od `90`, ale ma dwie jednakowe cyfry, więc jej nie wypisujemy.

### Uwagi

* Cyfrę jedności liczby `x` daje `x % 10`, a cyfrę dziesiątek liczby dwucyfrowej — `x // 10`.
* Nierówność jest ostra: samej liczby `n` nie wypisujemy.
* Dla `n ≥ 98` żadna liczba nie spełnia warunku.

ZAD-06C — Trzycyfrowe o sumie cyfr równej n

**Poziom:** ★★☆
**Tagi:** `pętle`, `suma cyfr`, `warunki`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz w kolejności rosnącej wszystkie liczby trzycyfrowe (od `100` do `999`), których suma cyfr jest równa `n`.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Liczby trzycyfrowe spełniające warunek, każda w osobnej linii.
Jeśli takich liczb nie ma, nie wypisuj nic.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
102
111
120
201
210
300
```

### Uwagi

* Suma cyfr liczby trzycyfrowej wynosi od `1` do `27`, więc dla innych `n` wynik jest pusty.

ZAD-06D — Trzycyfrowe podzielne przez sumę cyfr liczby n

**Poziom:** ★★☆
**Tagi:** `pętle`, `dzielenie`, `suma cyfr`

### Treść

Wczytaj liczbę naturalną `n` i oblicz sumę jej cyfr `s`. Następnie wypisz w kolejności rosnącej wszystkie liczby trzycyfrowe (od `100` do `999`), które są podzielne przez `s`.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 1`)

### Wyjście

Liczby trzycyfrowe podzielne przez `s`, każda w osobnej linii.
Jeśli takich liczb nie ma, nie wypisuj nic.

### Ograniczenia

* `n ≥ 1`, więc `s ≥ 1` i dzielenie jest zawsze wykonalne.

### Przykład

**Wejście:**

```
9999999
```

**Wyjście:**

```
126
189
252
315
378
441
504
567
630
693
756
819
882
945
```

Suma cyfr to $s = 7 \cdot 9 = 63$, a wypisane liczby to kolejne trzycyfrowe wielokrotności `63`.

ZAD-06E — Mniejsze od n złożone wyłącznie z parzystych cyfr

**Poziom:** ★★☆
**Tagi:** `pętle`, `warunki`, `cyfry`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz w kolejności rosnącej wszystkie liczby naturalne `x` takie, że `1 ≤ x < n` i **każda** cyfra liczby `x` jest parzysta.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Liczby spełniające warunek, każda w osobnej linii.
Jeśli takich liczb nie ma, nie wypisuj nic.

### Przykład

**Wejście:**

```
50
```

**Wyjście:**

```
2
4
6
8
20
22
24
26
28
40
42
44
46
48
```

### Uwagi

* `0` jest cyfrą parzystą, więc np. `20` i `40` spełniają warunek.
* Samą liczbę `0` pomijamy (zaczynamy od `x = 1`).

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

    // b) dwucyfrowe wieksze od n o roznych cyfrach
    for (int i = Math.max(10, n + 1); i < 100; i++) {
      if (i / 10 != i % 10) {
        System.out.println(i);
      }
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

