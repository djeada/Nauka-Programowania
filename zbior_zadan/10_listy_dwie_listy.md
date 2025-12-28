# Rozdział: Listy — Dwie listy (stdin/stdout)

Poniższe zadania polegają na wczytywaniu danych ze **standardowego wejścia** (stdin) i wypisywaniu wyniku na **standardowe wyjście** (stdout).
**Każde zadanie (oraz każdy podpunkt w zadaniach wieloczęściowych) jest osobnym, niezależnym programem.**

**Konwencje wspólne:**

* Listy w wejściu są podane w **jednej linii** w zapisie z nawiasami kwadratowymi, np. `[5, 3, 7, 2]`.
* Jeśli w danych są dwie listy — wczytaj je w kolejnych liniach: najpierw lista 1, potem lista 2.
* Gdy wynikiem jest lista — wypisz ją w formacie jak w przykładach, np. `[1, 2, 3]`.
* Jeśli wynik ma być w jednej linii z elementami oddzielonymi przecinkami **bez spacji**, trzymaj się dokładnie tego formatu.

---

## ZAD-01 — Wypisanie elementów dwóch list na przemian

**Poziom:** ★☆☆
**Tagi:** `list`, `iteracja`

### Treść

Wczytaj dwie listy liczb całkowitych i wypisz ich elementy **na przemian**:
pierwszy z listy 1, pierwszy z listy 2, drugi z listy 1, drugi z listy 2, itd.

Jeśli listy mają różne długości, po wyczerpaniu krótszej listy dopisz pozostałe elementy dłuższej listy w tej samej kolejności.

### Wejście

* 1 linia: lista 1
* 2 linia: lista 2

### Wyjście

* 1 linia: elementy obu list wypisane na przemian, oddzielone przecinkami **bez spacji**

### Przykład

**Wejście:**

```
[5, 3, 7, 2]
[1, -2, 3]
```

**Wyjście:**

```
5,1,3,-2,7,3,2
```

---

## ZAD-02 — Połączenie dwóch list

**Poziom:** ★☆☆
**Tagi:** `list`, `indeksy`, `concat`

### Treść

Wczytaj dwie listy liczb całkowitych i wykonaj niezależnie:

**a)** Połącz listy, doklejając drugą listę na koniec pierwszej.
**b)** W pierwszej liście **podmień** elementy o parzystych indeksach (0, 2, 4, …) elementami z drugiej listy o tych samych indeksach — o ile taki indeks istnieje w obu listach.

### Wejście

* 1 linia: lista 1
* 2 linia: lista 2

### Wyjście

* 1 linia: wynik dla **a)** jako lista
* 2 linia: wynik dla **b)** jako lista

### Przykład

**Wejście:**

```
[1, 2, 3]
[4, 5, 6]
```

**Wyjście:**

```
[1, 2, 3, 4, 5, 6]
[4, 2, 6]
```

---

## ZAD-03 — Suma elementów dwóch list

**Poziom:** ★☆☆
**Tagi:** `list`, `iteracja`

### Treść

Wczytaj dwie listy liczb całkowitych i zwróć listę, w której element o indeksie `i` jest sumą elementów o indeksie `i` z obu list.
Jeśli któraś lista jest krótsza, brakujące elementy traktuj jako `0`.

### Wejście

* 1 linia: lista 1
* 2 linia: lista 2

### Wyjście

* 1 linia: lista sum

### Przykład

**Wejście:**

```
[3, 1, 2, 5]
[2, 8, 6, 5]
```

**Wyjście:**

```
[5, 9, 8, 10]
```

---

## ZAD-04 — Iloczyn skalarny dwóch wektorów 3D

**Poziom:** ★☆☆
**Tagi:** `list`, `wektory`, `math`

### Treść

Wczytaj dwie listy długości 3 (wektory 3D) i oblicz ich **iloczyn skalarny**:
[
A_xB_x + A_yB_y + A_zB_z
]

### Wejście

* 1 linia: wektor A (lista 3 liczb całkowitych)
* 2 linia: wektor B (lista 3 liczb całkowitych)

### Wyjście

* 1 linia: jedna liczba całkowita — iloczyn skalarny

### Przykład

**Wejście:**

```
[1, 2, 3]
[3, 1, 2]
```

**Wyjście:**

```
11
```

---

## ZAD-05 — Obliczenie średniej ważonej

**Poziom:** ★☆☆
**Tagi:** `list`, `float`

### Treść

Wczytaj dwie listy liczb zmiennoprzecinkowych tej samej długości:

* lista wartości,
* lista wag.

Oblicz średnią ważoną:
[
\frac{\sum (wartość_i \cdot waga_i)}{\sum waga_i}
]

### Wejście

* 1 linia: lista wartości (float)
* 2 linia: lista wag (float)

### Wyjście

* 1 linia: jedna liczba zmiennoprzecinkowa — średnia ważona **z dokładnością do 2 miejsc po przecinku**

### Przykład

**Wejście:**

```
[0.2, 0.4, 0.1, 0.2, 0.1]
[2.0, 5.0, 0.0, 2.0, 1.0]
```

**Wyjście:**

```
0.29
```

---

## ZAD-06 — Znalezienie elementów wspólnych dwóch list

**Poziom:** ★☆☆
**Tagi:** `list`, `set`

### Treść

Wczytaj dwie listy liczb całkowitych. Wypisz listę elementów, które występują w obu listach:

* zachowaj **kolejność występowania w pierwszej liście**,
* jeśli element z pierwszej listy występuje w drugiej liście, dodaj go do wyniku,
* jeśli nie ma elementów wspólnych — wypisz `[]`.

### Wejście

* 1 linia: lista 1
* 2 linia: lista 2

### Wyjście

* 1 linia: lista elementów wspólnych

### Przykład

**Wejście:**

```
[9, 2, 5, 4]
[4, 2, 1]
```

**Wyjście:**

```
[2, 4]
```

---

## ZAD-07 — Różnica między dwoma listami

**Poziom:** ★☆☆
**Tagi:** `list`, `set`

### Treść

Wczytaj dwie listy liczb całkowitych i wypisz elementy, które występują **tylko w jednej** z list (różnica symetryczna).

* Kolejność elementów w wyniku może być **dowolna**.
* Jeśli wszystkie elementy są wspólne — wypisz `[]`.

### Wejście

* 1 linia: lista 1
* 2 linia: lista 2

### Wyjście

* 1 linia: lista elementów niewspólnych

### Przykład

**Wejście:**

```
[9, 2, 5, 4]
[4, 2, 1]
```

**Wyjście (jedna z poprawnych odpowiedzi):**

```
[9, 5, 1]
```

---

## ZAD-08 — Połącz posortowane listy w posortowaną listę bez duplikatów

**Poziom:** ★★☆
**Tagi:** `list`, `merge`, `sort`

### Treść

Wczytaj dwie listy liczb całkowitych, każda **posortowana rosnąco**. Połącz je w jedną listę:

* wynik ma być posortowany rosnąco,
* wynik ma zawierać **unikalne** elementy (bez duplikatów).

### Wejście

* 1 linia: lista 1 (posortowana rosnąco)
* 2 linia: lista 2 (posortowana rosnąco)

### Wyjście

* 1 linia: jedna posortowana lista bez duplikatów

### Przykład

**Wejście:**

```
[2, 4, 7]
[3, 5, 9]
```

**Wyjście:**

```
[2, 3, 4, 5, 7, 9]
```

---

## ZAD-09 — Usuń z pierwszej listy część wspólną obu list

**Poziom:** ★★☆
**Tagi:** `list`, `filter`

### Treść

Wczytaj dwie listy liczb całkowitych. Usuń z pierwszej listy wszystkie elementy, które występują również w drugiej liście.

* Zachowaj kolejność pozostałych elementów z pierwszej listy.
* Jeśli wszystko zostanie usunięte — wypisz `[]`.

### Wejście

* 1 linia: lista 1
* 2 linia: lista 2

### Wyjście

* 1 linia: lista 1 po usunięciu elementów wspólnych

### Przykład

**Wejście:**

```
[9, 2, 5, 4]
[4, 2, 1]
```

**Wyjście:**

```
[9, 5]
```

---

## ZAD-10 — Mediana dwóch posortowanych list

**Poziom:** ★★☆
**Tagi:** `list`, `median`, `sort`

### Treść

Wczytaj dwie listy liczb całkowitych:

* obie są posortowane rosnąco,
* obie mają tę samą, niezerową długość.

Znajdź medianę zbioru wszystkich elementów z obu list (czyli medianę po „złączeniu” obu list).

### Wejście

* 1 linia: lista 1 (posortowana rosnąco)
* 2 linia: lista 2 (posortowana rosnąco)

### Wyjście

* 1 linia: mediana jako liczba zmiennoprzecinkowa
  (jeśli mediana jest całkowita, wypisz ją z `.0`, np. `4.0`)

### Przykład

**Wejście:**

```
[2, 4, 7]
[3, 5, 9]
```

**Wyjście:**

```
4.5
```
