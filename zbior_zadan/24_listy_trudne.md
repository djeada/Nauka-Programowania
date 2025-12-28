# Rozdział: Listy — zadania dodatkowe (stdin/stdout)

Poniższe zadania polegają na wczytywaniu danych ze **standardowego wejścia** (stdin) i wypisywaniu wyniku na **standardowe wyjście** (stdout).
**Każde zadanie (oraz każdy podpunkt w zadaniach wieloczęściowych) jest osobnym, niezależnym programem.**

**Konwencje wspólne:**

* Jeśli na wejściu jest „lista” — w testach będzie podana w jednej linii w formacie podobnym do Pythona, np. `[1, 0, 1]`.
* Wypisuj wyniki dokładnie w formacie wymaganym w treści (liczba / lista / lista list).
* Indeksy liczymy od `0`.

---

## ZAD-01 — Najdłuższy ciąg jedynek

**Poziom:** ★★☆
**Tagi:** `list`, `0/1`, `analiza`, `indeksy`

### Treść

Otrzymujesz listę składającą się wyłącznie z `0` i `1`. Znajdź **indeks zera**, które po zamianie na `1` da **najdłuższy ciąg kolejnych jedynek**.

Jeśli lista składa się wyłącznie z zer **albo** wyłącznie z jedynek — wypisz `-1`.

### Wejście

* 1 linia: lista `A` (tylko `0` i `1`)

### Wyjście

* 1 linia: indeks (liczba całkowita) albo `-1`

### Przykład

**Wejście:**

```
[0, 0, 1, 0, 1, 1, 1, 0, 1, 1]
```

**Wyjście:**

```
7
```

### Uwagi

* Jeśli kilka zer daje ten sam maksymalny wynik — wybierz to o **najmniejszym indeksie** (jeśli nie określono inaczej w testach).

---

## ZAD-02 — Przesuń zera na koniec listy

**Poziom:** ★★☆
**Tagi:** `list`, `stabilność`, `przekształcenie`

### Treść

Otrzymujesz listę liczb całkowitych. Przenieś wszystkie zera na koniec listy, **zachowując kolejność** pozostałych elementów.

### Wejście

* 1 linia: lista liczb całkowitych `A`

### Wyjście

* 1 linia: lista po przekształceniu

### Przykład

**Wejście:**

```
[0, 1, 3, 0, 8, 12, 0, 4, 0, 7, 0]
```

**Wyjście:**

```
[1, 3, 8, 12, 4, 7, 0, 0, 0, 0, 0]
```

---

## ZAD-03 — Minimalny iloczyn trzech liczb

**Poziom:** ★★☆
**Tagi:** `list`, `min`, `math`

### Treść

Otrzymujesz listę liczb całkowitych. Znajdź **najmniejszy możliwy iloczyn trzech liczb** wybranych z tej listy.

Jeśli lista zawiera mniej niż 3 liczby — wypisz iloczyn wszystkich elementów listy.

### Wejście

* 1 linia: lista liczb całkowitych `A`

### Wyjście

* 1 linia: jedna liczba całkowita

### Przykład

**Wejście:**

```
[3, -1, -3, 2, 9, 4]
```

**Wyjście:**

```
-108
```

---

## ZAD-04 — Wspólny podciąg o największej długości (równe sumy)

**Poziom:** ★★★
**Tagi:** `list`, `prefix`, `hashmap`, `podciąg`

### Treść

Otrzymujesz dwie listy binarne `A` i `B` (zera i jedynki) o tej samej długości. Znajdź **maksymalną długość** podciągu (ciągłych elementów), dla którego suma elementów w podciągu z `A` jest równa sumie elementów w odpowiadającym podciągu z `B` (ten sam zakres indeksów).

### Wejście

* 1 linia: lista binarna `A`
* 2 linia: lista binarna `B` (tej samej długości)

### Wyjście

* 1 linia: maksymalna długość (liczba naturalna)

### Przykład

**Wejście:**

```
[0, 0, 1, 1, 1, 1]
[0, 1, 1, 0, 1, 0]
```

**Wyjście:**

```
5
```

---

## ZAD-05 — Zbiór potęgowy listy

**Poziom:** ★★★
**Tagi:** `list`, `subsets`, `combinatorics`

### Treść

Otrzymujesz listę liczb naturalnych (mogą występować powtórzenia). Wygeneruj zbiór wszystkich możliwych podzbiorów tej listy.

Wynik ma zawierać wszystkie podzbiory (włącznie z pustym).

### Wejście

* 1 linia: lista liczb naturalnych `A`

### Wyjście

* 1 linia: lista list (wszystkie podzbiory)

### Przykład

**Wejście:**

```
[1, 2, 1]
```

**Wyjście:**

```
[[], [1], [2], [1, 2], [1, 1], [2, 1], [1, 1, 2], [1, 2, 1]]
```

### Uwagi

* Jeśli sprawdzarka wymaga konkretnej kolejności podzbiorów, musi być ona opisana w treści — w przeciwnym razie dopuszczalna może być dowolna. (Jeśli chcesz, mogę dopisać sztywną konwencję kolejności, ale bez rozwiązań.)

---

## ZAD-06 — Połączenie posortowanych list (unikalne)

**Poziom:** ★★★
**Tagi:** `merge`, `heap`, `unique`, `sorted`

### Treść

Otrzymujesz listę zawierającą `M` posortowanych list liczb naturalnych. Połącz je w jedną **posortowaną** listę zawierającą wszystkie elementy **bez powtórzeń**.

### Wejście

* 1 linia: lista list (każda wewnętrzna lista jest posortowana)

### Wyjście

* 1 linia: jedna posortowana lista bez duplikatów

### Przykład

**Wejście:**

```
[[-6, 23, 29, 33], [6, 22, 35, 71], [5, 19, 21, 37], [-12, -7, -3, 28]]
```

**Wyjście:**

```
[-12, -7, -6, -3, 5, 6, 19, 21, 22, 23, 28, 29, 33, 35, 37, 71]
```

---

## ZAD-07 — Pojemność wody między słupkami

**Poziom:** ★★★
**Tagi:** `two pointers`, `prefix`, `trapping rain water`

### Treść

Otrzymujesz listę liczb naturalnych — wysokości słupków. Oblicz, ile jednostek wody może się zatrzymać pomiędzy słupkami po deszczu.

### Wejście

* 1 linia: lista wysokości `H`

### Wyjście

* 1 linia: jedna liczba naturalna — ilość wody

### Przykład

**Wejście:**

```
[3, 0, 1, 0, 2]
```

**Wyjście:**

```
5
```

---

## ZAD-08 — Maksymalny zysk ze sprzedaży sznurka

**Poziom:** ★★★
**Tagi:** `dp`, `rod cutting`, `optymalizacja`

### Treść

Masz sznurek o długości `n` i cennik: ceny kawałków długości od `1` do `n`. Możesz pociąć sznurek na kawałki o całkowitych długościach. Znajdź maksymalny zysk.

### Wejście

* 1 linia: lista `prices` (długości 1..n)
* 2 linia: `n` (liczba naturalna)

### Wyjście

* 1 linia: maksymalny zysk (liczba całkowita)

### Przykład

**Wejście:**

```
[1, 5, 8, 9, 10, 17, 17, 20]
4
```

**Wyjście:**

```
10
```

---

## ZAD-09 — Najdłuższy naprzemienny podciąg

**Poziom:** ★★★
**Tagi:** `dp`, `subsequence`, `naprzemienny`

### Treść

Otrzymujesz listę liczb całkowitych. Znajdź najdłuższy podciąg naprzemienny, w którym różnice między kolejnymi elementami zmieniają znak (raz dodatnia, raz ujemna, itd.).

### Wejście

* 1 linia: lista liczb całkowitych `A`

### Wyjście

* 1 linia: lista liczb — najdłuższy naprzemienny podciąg

### Przykład

**Wejście:**

```
[1, -2, 6, 4, -3, 2, -4, -3]
```

**Wyjście:**

```
[1, -2, 6, -3, 2, -4]
```

### Uwagi

* Jeśli istnieje kilka podciągów o tej samej maksymalnej długości — wybierz ten, który pojawia się „najwcześniej” (najmniejszy możliwy indeks startu), o ile sprawdzarka tego wymaga.

---
