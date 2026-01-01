/*
ZAD-06A — Liczby mniejsze od n o sumie cyfr równej 10

**Poziom:** ★★☆
**Tagi:** `pętle`, `suma cyfr`, `warunki`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz wszystkie liczby naturalne `x` takie, że `0
≤ x < n` oraz suma cyfr liczby `x` wynosi `10`. Każdą liczbę wypisz w osobnej
linii.

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

Wczytaj liczbę naturalną `n`. Wypisz wszystkie liczby **dwucyfrowe** większe od
`n` (czyli z zakresu 10–99), każdą w osobnej linii.

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

Wczytaj liczbę naturalną `n`. Wypisz wszystkie liczby trzycyfrowe `x` (100–999),
których suma cyfr jest równa `n`. Każdą liczbę wypisz w osobnej linii.

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

Wczytaj liczbę naturalną `n`. Oblicz sumę cyfr liczby `n` i oznacz ją jako `s`.
Następnie wypisz wszystkie liczby trzycyfrowe `x` (100–999), które są podzielne
przez `s`. Każdą liczbę wypisz w osobnej linii.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Ograniczenia / gwarancje

* Suma cyfr `n` jest większa od zera (czyli `n ≠ 0`), aby dzielenie było
poprawne.

### Wyjście

Liczby trzycyfrowe podzielne przez `s`, każda w nowej linii.

ZAD-06E — Mniejsze od n złożone wyłącznie z parzystych cyfr

**Poziom:** ★★☆
**Tagi:** `pętle`, `warunki`, `cyfry`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz wszystkie liczby naturalne `x` takie, że `0
≤ x < n` oraz każda cyfra w zapisie dziesiętnym `x` jest parzysta. Każdą liczbę
wypisz w osobnej linii.

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

* W tym zadaniu `0` też składa się wyłącznie z parzystych cyfr. Jeśli chcesz je
uwzględniać, dopisz to jako regułę w treści (tu: pomijamy `0`, bo w przykładzie
go nie ma).

*/
#include <iostream>

// Funkcja pomocnicza do obliczania sumy cyfr
int suma_cyfr(int n) {
  int suma = 0;
  while (n > 0) {
    suma += (n % 10);
    n /= 10;
  }
  return suma;
}

// Funkcja pomocnicza do sprawdzania czy wszystkie cyfry są parzyste
bool wszystkie_parzyste(int n) {
  if (n == 0) return true;
  while (n > 0) {
    int cyfra = n % 10;
    if (cyfra % 2 == 1) return false;
    n /= 10;
  }
  return true;
}

int main() {
  int n;
  std::cin >> n;

  // ZAD-06A: Liczby < n o sumie cyfr równej 10
  for (int x = 0; x < n; x++) {
    if (suma_cyfr(x) == 10) 
      std::cout << x << std::endl;
  }

  // ZAD-06B: Dwucyfrowe większe od n
  for (int x = 10; x < 100; x++) {
    if (x > n) 
      std::cout << x << std::endl;
  }

  // ZAD-06C: Trzycyfrowe o sumie cyfr równej n
  for (int x = 100; x < 1000; x++) {
    if (suma_cyfr(x) == n) 
      std::cout << x << std::endl;
  }

  // ZAD-06D: Trzycyfrowe podzielne przez sumę cyfr n
  int s = suma_cyfr(n);
  for (int x = 100; x < 1000; x++) {
    if (x % s == 0) 
      std::cout << x << std::endl;
  }

  // ZAD-06E: Mniejsze od n złożone wyłącznie z parzystych cyfr
  for (int x = 2; x < n; x++) {
    if (wszystkie_parzyste(x)) 
      std::cout << x << std::endl;
  }

  return 0;
}
