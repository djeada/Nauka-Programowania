# Rozdział: Bity i systemy liczbowe

Poniższe zadania polegają na wczytywaniu danych ze **standardowego wejścia** (stdin) i wypisywaniu wyniku na **standardowe wyjście** (stdout).
**Każde zadanie (oraz każdy podpunkt w zadaniach wieloczęściowych) jest osobnym, niezależnym programem.**

**Konwencje wspólne:**

* Jeśli zadanie mówi „nie wypisuj nic” — nie drukuj nawet pustej linii.
* Reprezentacje binarne wypisuj jako ciąg znaków `0` i `1` **bez spacji**.
* Dla systemów o podstawie `> 10` używaj cyfr `0–9` oraz liter `A–Z` (wielkie).
* Nie wypisuj promptów typu „Podaj liczbę”.

---

## ZAD-01A — Dziesiętny → binarny

**Poziom:** ★☆☆
**Tagi:** `konwersja`, `binarne`, `pętle`

### Treść

Wczytaj liczbę naturalną w systemie dziesiętnym i wypisz jej reprezentację binarną.

### Wejście

* 1. linia: `n` (liczba naturalna)

### Wyjście

Jedna linia: zapis binarny `n`.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
11
```

### Uwagi o formacie

* Dla `n = 0` wypisz `0`.

---

## ZAD-01B — Binarny → dziesiętny

**Poziom:** ★☆☆
**Tagi:** `konwersja`, `string`, `binarne`

### Treść

Wczytaj liczbę naturalną w systemie binarnym (ciąg `0/1`) i wypisz jej wartość w systemie dziesiętnym.

### Wejście

* 1. linia: `b` (ciąg znaków `0` i `1`)

### Wyjście

Jedna linia: liczba w systemie dziesiętnym.

### Przykład

**Wejście:**

```
101
```

**Wyjście:**

```
5
```

---

## ZAD-02A — Wypisz binarnie tylko gdy liczba parzysta

**Poziom:** ★☆☆
**Tagi:** `warunki`, `parzystość`, `binarne`

### Treść

Wczytaj liczbę naturalną `n`. Jeśli `n` jest parzysta — wypisz jej zapis binarny. W przeciwnym razie nie wypisuj nic.

### Wejście

* 1. linia: `n` (liczba naturalna)

### Wyjście

* Jeśli `n % 2 == 0`: jedna linia z zapisem binarnym `n`
* W przeciwnym razie: brak wyjścia

### Przykład

**Wejście:**

```
7
```

**Wyjście:** *(brak)*

---

## ZAD-02B — Wypisz binarnie tylko gdy liczba pierwsza

**Poziom:** ★☆☆
**Tagi:** `pierwszość`, `warunki`, `binarne`

### Treść

Wczytaj liczbę naturalną `n`. Jeśli `n` jest liczbą pierwszą — wypisz jej zapis binarny. W przeciwnym razie nie wypisuj nic.

### Wejście

* 1. linia: `n` (liczba naturalna)

### Wyjście

* Jeśli `n` jest pierwsza: jedna linia z zapisem binarnym `n`
* W przeciwnym razie: brak wyjścia

### Przykład

**Wejście:**

```
7
```

**Wyjście:**

```
111
```

---

## ZAD-03A — Dodawanie bitowe

**Poziom:** ★☆☆
**Tagi:** `bitwise`, `XOR`, `AND`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`. Oblicz `a + b` używając wyłącznie operatorów bitowych (i przesunięć).

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba naturalna: `a + b`.

### Przykład

**Wejście:**

```
2
3
```

**Wyjście:**

```
5
```

---

## ZAD-03B — Odejmowanie bitowe

**Poziom:** ★☆☆
**Tagi:** `bitwise`, `pożyczki`, `XOR`

### Treść

Wczytaj `a` i `b`. Oblicz `a - b` używając wyłącznie operatorów bitowych.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba naturalna: `a - b`.

### Ograniczenia / gwarancje

* Zakładamy, że `a ≥ b` (wynik jest naturalny).

### Przykład

**Wejście:**

```
7
5
```

**Wyjście:**

```
2
```

---

## ZAD-03C — Mnożenie bitowe

**Poziom:** ★☆☆
**Tagi:** `bitwise`, `shift`, `pętle`

### Treść

Wczytaj `a` i `b`. Oblicz `a * b` używając wyłącznie operatorów bitowych (np. metoda „shift-and-add”).

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba naturalna: `a * b`.

### Przykład

**Wejście:**

```
4
4
```

**Wyjście:**

```
16
```

---

## ZAD-03D — Dzielenie całkowite bitowe

**Poziom:** ★☆☆
**Tagi:** `bitwise`, `dzielenie`, `shift`

### Treść

Wczytaj `a` i `b`. Oblicz `a // b` używając wyłącznie operatorów bitowych.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Ograniczenia / gwarancje

* `b > 0`

### Wyjście

Jedna liczba naturalna: `a // b`.

### Przykład

**Wejście:**

```
9
3
```

**Wyjście:**

```
3
```

---

## ZAD-04A — Liczba zer w zapisie binarnym

**Poziom:** ★☆☆
**Tagi:** `binarne`, `zliczanie`

### Treść

Wczytaj liczbę naturalną `n`. Policz, ile znaków `0` zawiera jej binarna reprezentacja (bez wiodących zer).

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: liczba zer w zapisie binarnym `n`.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
0
```

### Uwagi

* Dla `n = 0` binarnie to `0`, więc liczba zer wynosi `1`.

---

## ZAD-04B — Liczba jedynek w zapisie binarnym

**Poziom:** ★☆☆
**Tagi:** `popcount`, `binarne`

### Treść

Wczytaj `n`. Policz, ile bitów `1` ma liczba w zapisie binarnym.

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: liczba jedynek w zapisie binarnym `n`.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
2
```

---

## ZAD-05A — Minimum bez instrukcji warunkowych

**Poziom:** ★★☆
**Tagi:** `bit-trick`, `min/max`, `bez if`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`. Wypisz mniejszą z nich **bez użycia instrukcji warunkowych** (`if`, `?:`) i bez bibliotek.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba naturalna: `min(a, b)`.

### Przykład

**Wejście:**

```
3
2
```

**Wyjście:**

```
2
```

### Uwagi

* Dopuszczalne są operacje arytmetyczne i bitowe.

---

## ZAD-05B — Maksimum bez instrukcji warunkowych

**Poziom:** ★★☆
**Tagi:** `bit-trick`, `min/max`, `bez if`

### Treść

Wczytaj `a` i `b`. Wypisz większą z nich **bez użycia instrukcji warunkowych** i bez bibliotek.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba naturalna: `max(a, b)`.

### Przykład

**Wejście:**

```
3
2
```

**Wyjście:**

```
3
```

---

## ZAD-06 — Konwersja między dowolnymi systemami (2..36)

**Poziom:** ★★☆
**Tagi:** `konwersja`, `base`, `string`

### Treść

Wczytaj:

1. liczbę `X` zapisaną w systemie o podstawie `p`
2. podstawę `p` (2..36)
3. podstawę docelową `q` (2..36)

i wypisz reprezentację `X` w systemie o podstawie `q`.

### Wejście

Trzy linie:

1. `X` (zapis liczby; dla podstaw >10 może zawierać litery `A-Z`)
2. `p` (2..36)
3. `q` (2..36)

### Wyjście

Jedna linia: zapis liczby w systemie o podstawie `q` (używaj `0–9` i `A–Z`).

### Przykład

**Wejście:**

```
4301
10
4
```

**Wyjście:**

```
1003031
```

### Uwagi o formacie

* `X` może być duże — traktuj jako napis, a nie typ int „na wejściu”.
* Dla wartości 10..35 stosuj `A..Z`.

---

## ZAD-07 — Zamiana sąsiadujących bitów

**Poziom:** ★☆☆
**Tagi:** `bitwise`, `maski`, `swap bits`

### Treść

Wczytaj liczbę naturalną `n`. Zamień miejscami każdą parę sąsiadujących bitów w jej zapisie binarnym:

* bit 0 z bitem 1,
* bit 2 z bitem 3,
* bit 4 z bitem 5,
* itd.

Następnie wypisz wynik w systemie dziesiętnym.

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: wynik po zamianie bitów.

### Przykład

**Wejście:**

```
9131
```

**Wyjście:**

```
4951
```

### Uwagi

* Jeśli liczba ma nieparzystą liczbę bitów, najwyższy (samotny) bit pozostaje bez zmian.

---

## ZAD-08 — Najbliższa potęga dwójki (>= n)

**Poziom:** ★☆☆
**Tagi:** `potęgi 2`, `bitwise`, `pętle`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz najmniejszą potęgę liczby 2, która jest **większa lub równa** `n`.

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: najmniejsze `2^k ≥ n`.

### Przykład

**Wejście:**

```
111
```

**Wyjście:**

```
128
```

### Uwagi

* Dla `n = 0` przyjmij wynik `1`.

---

## ZAD-09A — Wielkie → małe (bitowo)

**Poziom:** ★★☆
**Tagi:** `ASCII`, `bitwise`, `string`

### Treść

Wczytaj napis z liter alfabetu łacińskiego. Zamień wszystkie wielkie litery na małe, używając operacji bitowych na kodach ASCII.

### Wejście

* 1. linia: napis

### Wyjście

Jedna linia: napis po konwersji.

### Przykład

**Wejście:**

```
Test
```

**Wyjście:**

```
test
```

---

## ZAD-09B — Małe → wielkie (bitowo)

**Poziom:** ★★☆
**Tagi:** `ASCII`, `bitwise`, `string`

### Treść

Wczytaj napis. Zamień wszystkie małe litery na wielkie, używając operacji bitowych na ASCII.

### Wejście

* 1. linia: napis

### Wyjście

Jedna linia: napis po konwersji.

### Przykład

**Wejście:**

```
Test
```

**Wyjście:**

```
TEST
```

---

## ZAD-09C — Odwróć wielkość liter (bitowo)

**Poziom:** ★★☆
**Tagi:** `ASCII`, `bitwise`, `toggle case`

### Treść

Wczytaj napis. Zamień wielkość każdej litery na przeciwną (mała↔wielka) używając operacji bitowych na ASCII.

### Wejście

* 1. linia: napis

### Wyjście

Jedna linia: napis po zmianie.

### Przykład

**Wejście:**

```
Test
```

**Wyjście:**

```
tEST
```

---

## ZAD-10 — Ile bitów trzeba odwrócić (A → B)

**Poziom:** ★★☆
**Tagi:** `XOR`, `popcount`, `bitwise`

### Treść

Wczytaj dwie liczby naturalne `A` i `B`. Oblicz, ile bitów trzeba odwrócić w `A`, aby otrzymać `B`.

### Wejście

* 1. linia: `A`
* 2. linia: `B`

### Wyjście

Jedna liczba naturalna: liczba różniących się bitów.

### Przykład

**Wejście:**

```
34
73
```

**Wyjście:**

```
5
```

---

## ZAD-11 — Palindrom w systemie binarnym

**Poziom:** ★★☆
**Tagi:** `binarne`, `palindrom`, `string`

### Treść

Wczytaj liczbę naturalną `n`. Sprawdź, czy jej reprezentacja binarna (bez wiodących zer) jest palindromem.

Wypisz:

* `Prawda` — jeśli tak,
* `Fałsz` — jeśli nie.

### Wejście

* 1. linia: `n`

### Wyjście

Jedno słowo: `Prawda` lub `Fałsz`.

### Przykład

**Wejście:**

```
26
```

**Wyjście:**

```
Fałsz
```

### Uwagi (ważne)

* `26` ma zapis binarny `11010`, który **nie** jest palindromem.
  (W Twoim wcześniejszym przykładzie było to opisane błędnie — tu trzymamy się definicji palindromu 1:1.)

---

## ZAD-12 — Najdłuższy ciąg zer otoczony jedynkami

**Poziom:** ★★★
**Tagi:** `binarne`, `binary gap`, `pętle`

### Treść

Wczytaj liczbę naturalną `n`. W jej reprezentacji binarnej znajdź długość najdłuższego ciągu kolejnych zer, który jest **z obu stron otoczony jedynkami** (tzw. *binary gap*).

Jeśli nie ma takiego ciągu — wypisz `0`.

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: długość najdłuższego „gapu”.

### Przykład

**Wejście:**

```
14
```

**Wyjście:**

```
0
```

### Uwagi (ważne)

* `14` ma zapis `1110` — zero na końcu **nie jest otoczone jedynkami z prawej**, więc wynik to `0`.
  Dla przykładu `20` (`10100`) najdłuższy gap ma długość `1` (między `1` i `1`).
