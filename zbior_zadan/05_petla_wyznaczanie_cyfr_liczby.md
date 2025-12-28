# Rozdział: Cyfry w liczbie (dzielenie przez 10, modulo)

Poniższe zadania polegają na wczytywaniu danych ze **standardowego wejścia** (stdin) i wypisywaniu wyniku na **standardowe wyjście** (stdout).
**Każde zadanie (oraz każdy podpunkt w zadaniach wieloczęściowych) jest osobnym, niezależnym programem.**

**Konwencje wspólne:**

* Jeśli w danych wejściowych są liczby w osobnych liniach — wczytuj je dokładnie w tej kolejności.
* Jeśli w danych wyjściowych jest „każda w oddzielnej linii” — po każdym wyniku wypisz znak nowej linii.
* Dla liczb zmiennoprzecinkowych stosuj formatowanie zgodne z poleceniem.
* Jeżeli zadanie wymaga „brak danych wyjściowych”, program nie wypisuje nic (nawet pustej linii).

---

## ZAD-01 — Liczenie cyfr w liczbie

**Poziom:** ★☆☆
**Tagi:** `pętle`, `modulo`, `dzielenie całkowite`

### Treść

Wczytaj liczbę naturalną `n` i wypisz, z ilu cyfr składa się jej zapis dziesiętny.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Jedna liczba naturalna — liczba cyfr w `n`.

### Przykład

**Wejście:**

```
342
```

**Wyjście:**

```
3
```

### Ograniczenia / gwarancje

* `n` mieści się w typowym zakresie liczb całkowitych.

### Uwagi o formatowaniu

* Dla `n = 0` poprawna odpowiedź to `1` (liczba „0” ma jedną cyfrę).

---

## ZAD-02 — Wypisywanie cyfr liczby w odwrotnej kolejności

**Poziom:** ★☆☆
**Tagi:** `pętle`, `modulo`, `dzielenie całkowite`

### Treść

Wczytaj liczbę naturalną `n` i wypisz jej cyfry w kolejności od cyfry jedności (czyli w odwrotnej kolejności niż w zapisie liczby). Każdą cyfrę wypisz w osobnej linii.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Kolejne cyfry `n` w odwrotnej kolejności, każda w nowej linii.

### Przykład

**Wejście:**

```
8214
```

**Wyjście:**

```
4
1
2
8
```

### Uwagi o formatowaniu

* Dla `n = 0` wypisz jedną linię z `0`.

---

## ZAD-03 — Sumowanie cyfr liczby

**Poziom:** ★☆☆
**Tagi:** `pętle`, `modulo`, `dzielenie całkowite`

### Treść

Wczytaj liczbę naturalną `n` i oblicz sumę jej cyfr. Następnie wypisz wynik.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Jedna liczba naturalna — suma cyfr liczby `n`.

### Przykład

**Wejście:**

```
129
```

**Wyjście:**

```
12
```

### Uwagi o formatowaniu

* Dla `n = 0` suma cyfr wynosi `0`.

---

## ZAD-04A — Cyfry parzyste

**Poziom:** ★☆☆
**Tagi:** `pętle`, `modulo`, `warunki`

### Treść

Wczytaj liczbę naturalną `n` i wypisz wszystkie jej cyfry, które są **parzyste**. Każdą cyfrę wypisz w osobnej linii.

Cyfry analizuj od końca (od jedności), czyli w tej samej kolejności, co w zadaniu o wypisywaniu cyfr w odwrotnej kolejności.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Cyfry parzyste liczby `n`, każda w nowej linii (w kolejności od jedności do najwyższej cyfry).
Jeśli nie ma takich cyfr — brak wyjścia.

### Przykład

**Wejście:**

```
932
```

**Wyjście:**

```
2
```

---

## ZAD-04B — Cyfry mniejsze niż 5

**Poziom:** ★☆☆
**Tagi:** `pętle`, `modulo`, `warunki`

### Treść

Wczytaj liczbę naturalną `n` i wypisz wszystkie jej cyfry, które są **mniejsze niż 5**. Każdą cyfrę wypisz w osobnej linii.

Cyfry analizuj od końca (od jedności).

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Cyfry < 5, każda w nowej linii.
Jeśli brak — brak wyjścia.

### Przykład

**Wejście:**

```
101
```

**Wyjście:**

```
1
0
1
```

---

## ZAD-04C — Cyfry różne od zera

**Poziom:** ★☆☆
**Tagi:** `pętle`, `modulo`, `warunki`

### Treść

Wczytaj liczbę naturalną `n` i wypisz wszystkie jej cyfry, które są **różne od zera**. Każdą cyfrę wypisz w osobnej linii.

Cyfry analizuj od końca (od jedności).

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Cyfry ≠ 0, każda w nowej linii.
Jeśli brak — brak wyjścia.

### Przykład

**Wejście:**

```
650
```

**Wyjście:**

```
5
6
```

### Uwagi o formatowaniu

* W przykładzie widać kolejność od jedności: najpierw `5`, potem `6`.

---

## ZAD-05 — Sprawdzanie, czy liczba jest palindromem

**Poziom:** ★★☆
**Tagi:** `string`, `pętle`, `odwracanie`

### Treść

Wczytaj liczbę naturalną `n`. Sprawdź, czy jest palindromem (czyli czy po odwróceniu cyfr pozostaje taka sama). Wypisz odpowiedni komunikat:

* `Liczba jest palindromem.`
* `Liczba nie jest palindromem.`

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Jeden komunikat tekstowy (dokładnie jeden z powyższych).

### Przykład

**Wejście:**

```
13231
```

**Wyjście:**

```
Liczba jest palindromem.
```

### Uwagi o formatowaniu

* `0` jest palindromem.

---

## ZAD-06A — Liczby mniejsze od n o sumie cyfr równej 10

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

---

## ZAD-06B — Dwucyfrowe większe od n

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

---

## ZAD-06C — Trzycyfrowe o sumie cyfr równej n

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

---

## ZAD-06D — Trzycyfrowe podzielne przez sumę cyfr liczby n

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

---

## ZAD-06E — Mniejsze od n złożone wyłącznie z parzystych cyfr

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
