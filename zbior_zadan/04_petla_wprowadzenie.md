# Rozdział: Pętle i proste obliczenia (while / for)

Poniższe zadania polegają na wczytywaniu danych ze **standardowego wejścia** (stdin) i wypisywaniu wyniku na **standardowe wyjście** (stdout).
**Każde zadanie (oraz każdy podpunkt w zadaniach wieloczęściowych) jest osobnym, niezależnym programem.**

**Konwencje wspólne:**

* Jeśli w danych wejściowych są liczby w osobnych liniach — wczytuj je dokładnie w tej kolejności.
* Jeśli w danych wyjściowych jest „każda w oddzielnej linii” — po każdym wyniku wypisz znak nowej linii.
* Dla liczb zmiennoprzecinkowych stosuj formatowanie zgodne z poleceniem (np. `%.3f`, `format(x, ".3f")`).
* Jeśli zadanie mówi „brak danych wyjściowych” — program nie wypisuje nic (nawet pustej linii).

---

## ZAD-01 — Warunek kończący pętlę

**Poziom:** ★☆☆
**Tagi:** `while`, `break`, `I/O`

### Treść

Wczytuj kolejne liczby naturalne, dopóki nie pojawi się liczba `7`.
Po wczytaniu liczby `7` program kończy działanie **bez wypisywania czegokolwiek**.

### Wejście

Dowolna liczba liczb naturalnych (każda w osobnej linii).

### Ograniczenia / gwarancje

* W danych wejściowych na pewno pojawi się co najmniej jedna liczba `7`.

### Wyjście

Brak.

### Przykład

**Wejście:**

```
3
10
5
7
```

**Wyjście:**

```
```

*(brak danych wyjściowych)*

### Uwagi o formatowaniu

* Nie wypisuj żadnych komunikatów typu „Podaj liczbę”.
* Liczba `7` kończy wczytywanie i nie jest dalej przetwarzana.

---

## ZAD-02 — Wypisywanie liczb mniejszych od podanej

**Poziom:** ★☆☆
**Tagi:** `for`, `while`, `pętle`

### Treść

Wczytaj liczbę naturalną `n` (`n > 0`) i wypisz wszystkie liczby naturalne mniejsze od `n`, zaczynając od `n - 1` i kończąc na `1`.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n > 0`)

### Wyjście

Kolejne liczby naturalne mniejsze od `n`, każda w nowej linii, w kolejności malejącej.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
2
1
```

### Uwagi o formatowaniu

* Jeśli `n = 1`, nie wypisuj nic.

---

## ZAD-03 — Wypisywanie liczby π z określoną dokładnością

**Poziom:** ★☆☆
**Tagi:** `math.pi`, `formatowanie`, `pętle`

### Treść

1. Wczytaj liczbę naturalną `n` (`n > 0`).
2. Wypisz liczbę π dokładnie `n` razy.
3. Każda wypisana wartość ma mieć **dokładnie `n` miejsc po przecinku**.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n > 0`)

### Wyjście

`n` wierszy, w każdym liczba π z dokładnością do `n` miejsc po przecinku.

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
3.14
3.14
```

### Uwagi o formatowaniu

* Liczba miejsc po przecinku ma być **dokładnie** równa `n` (np. dla `n=1` wypisz `3.1`).
* Stosuj standardowe zaokrąglanie przy formatowaniu.

---

## ZAD-04 — Sumowanie liczb mniejszych od podanej

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

---

## ZAD-05 — Liczby z przedziału

**Poziom:** ★☆☆
**Tagi:** `pętle`, `przedziały`, `modulo`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`. Najpierw ustal:

* `lo = min(a, b)`
* `hi = max(a, b)`

Następnie:

a) Wypisz wszystkie liczby naturalne `x` takie, że `lo < x < hi` (każda w osobnej linii).

b) Wypisz wszystkie liczby naturalne `x` takie, że `lo < x < hi` oraz `x` jest podzielne przez `3` (każda w osobnej linii).

### Wejście

Dwie liczby naturalne:

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Najpierw wyniki podpunktu (a), potem wyniki podpunktu (b), każda liczba w osobnej linii.

### Przykład

**Wejście:**

```
9
5
```

**Wyjście:**

```
6
7
8
6
```

### Uwagi o formatowaniu

* Nie wypisuj nagłówków typu „a)” i „b)”.
* Jeśli w którymś podpunkcie nie ma liczb do wypisania, w tej części nie wypisuj nic.
* Nie dodawaj pustej linii między podpunktami.

---

## ZAD-06 — Sumowanie elementów ciągu

**Poziom:** ★☆☆
**Tagi:** `ciągi`, `sumowanie`, `pętle`

### Treść

Wczytaj liczbę naturalną `n` (`n ≥ 1`) i oblicz:

a) ( \sum_{k=1}^{n} (k^2 + k + 1) )

b) ( \sum_{k=1}^{n} (k^2 + 5k) )

c) ( \sum_{k=1}^{n} (k + 2k) )  (czyli ( \sum_{k=1}^{n} 3k ))

Wypisz trzy sumy w kolejności a), b), c).

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 1`)

### Wyjście

Trzy liczby naturalne — każda w oddzielnej linii:

1. suma dla (a)
2. suma dla (b)
3. suma dla (c)

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
10
16
9
```

### Uwagi o formatowaniu

* Wyniki są liczbami całkowitymi — nie stosuj żadnego dodatkowego zaokrąglania.

---

## ZAD-07 — Potęgowanie liczby π

**Poziom:** ★☆☆
**Tagi:** `math.pi`, `potęgi`, `formatowanie`

### Treść

Wczytaj liczbę naturalną `n` (`n ≥ 0`), oblicz wartość ( \pi^n ) i wypisz wynik z dokładnością do **dwóch miejsc po przecinku**.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Jedna liczba zmiennoprzecinkowa — ( \pi^n ) z dokładnością do dwóch miejsc po przecinku.

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
9.87
```

### Uwagi o formatowaniu

* Dla `n = 0` wypisz `1.00`.

---

## ZAD-08 — Obliczanie liczby kur i owiec na farmie

**Poziom:** ★★☆
**Tagi:** `układ równań`, `arytmetyka`

### Treść

Na farmie są kury i owce. Wiadomo, że:

* łączna liczba głów wynosi `a`,
* łączna liczba nóg wynosi `b`,
* kura ma 2 nogi, owca ma 4 nogi,
* każda ma dokładnie 1 głowę.

Oblicz liczbę kur oraz liczbę owiec.

### Wejście

Dwie liczby naturalne:

* 1. linia: `a` — liczba głów (`a ≥ 0`)
* 2. linia: `b` — liczba nóg (`b ≥ 0`)

### Ograniczenia / gwarancje

* Istnieje rozwiązanie w liczbach całkowitych nieujemnych.

### Wyjście

Dwie liczby naturalne, każda w oddzielnej linii:

1. liczba kur
2. liczba owiec

### Przykład

**Wejście:**

```
40
100
```

**Wyjście:**

```
30
10
```

### Uwagi o formatowaniu

* Nie wypisuj dodatkowych opisów — tylko liczby.
