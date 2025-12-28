# Rozdział: Pętla — Pętle zagnieżdżone

Poniższe zadania polegają na wczytywaniu danych ze **standardowego wejścia** (stdin) i wypisywaniu wyniku na **standardowe wyjście** (stdout).
**Każde zadanie (oraz każdy podpunkt w zadaniach wieloczęściowych) jest osobnym, niezależnym programem.**

**Konwencje wspólne:**

* Jeśli w danych wejściowych są liczby w osobnych liniach — wczytuj je dokładnie w tej kolejności.
* Jeśli w danych wyjściowych jest „każdy wiersz w osobnej linii” — po każdym wierszu wypisz znak nowej linii.
* W zadaniach z rysowaniem znakami **spacje są istotne** (nie przycinaj końcowych spacji — najlepiej ich nie drukować, ale w środku linii muszą być).
* Nie wypisuj promptów typu „Podaj n”.

---

## ZAD-01 — Kwadrat

**Poziom:** ★☆☆
**Tagi:** `pętle zagnieżdżone`, `print`, `string`

### Treść

Wczytaj liczbę naturalną `n` (`n ≥ 1`) i wypisz kwadrat `n × n` zbudowany z gwiazdek `*`.
Każdy wiersz ma zawierać dokładnie `n` gwiazdek (bez spacji).

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 1`)

### Wyjście

`n` linii, w każdej dokładnie `n` znaków `*`.

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
**
**
```

---

## ZAD-02 — Trójkąt prostokątny (rosnący)

**Poziom:** ★☆☆
**Tagi:** `pętle`, `print`, `string`

### Treść

Wczytaj `n` (`n ≥ 1`) i wypisz trójkąt o wysokości `n`, gdzie w wierszu `i` jest `i` gwiazdek (`i = 1..n`).

### Wejście

* 1. linia: `n` (`n ≥ 1`)

### Wyjście

`n` linii:

* 1. linia: `*`
* 2. linia: `**`
* …
* `n`-ta linia: `n` gwiazdek

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
*
**
***
```

---

## ZAD-03 — Trójkąt prostokątny (malejący)

**Poziom:** ★☆☆
**Tagi:** `pętle`, `print`, `string`

### Treść

Wczytaj `n` (`n ≥ 1`) i wypisz odwrócony trójkąt o wysokości `n`, zaczynając od `n` gwiazdek i kończąc na `1`.

### Wejście

* 1. linia: `n` (`n ≥ 1`)

### Wyjście

`n` linii:

* 1. linia: `n` gwiazdek
* 2. linia: `n-1` gwiazdek
* …
* ostatnia linia: `*`

### Przykład

**Wejście:**

```
4
```

**Wyjście:**

```
****
***
**
*
```

---

## ZAD-04 — Tabliczka mnożenia N × N

**Poziom:** ★★☆
**Tagi:** `pętle zagnieżdżone`, `formatowanie`, `arytmetyka`

### Treść

Wczytaj liczbę naturalną `N` (`N ≥ 1`) i wypisz tabliczkę mnożenia `N × N`.

W wierszu `i` i kolumnie `j` (licząc od 1) ma znaleźć się wartość `i*j`.
Liczby w jednym wierszu oddzielaj pojedynczą spacją.

### Wejście

* 1. linia: `N` (`N ≥ 1`)

### Wyjście

`N` linii, w każdej `N` liczb.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
1 2 3
2 4 6
3 6 9
```

### Uwagi o formatowaniu

* Nie dodawaj spacji na końcu wiersza.

---

## ZAD-05 — Litera „X”

**Poziom:** ★★☆
**Tagi:** `pętle zagnieżdżone`, `warunki`, `ASCII-art`

### Treść

Wczytaj `n` (`n ≥ 3`) i wypisz literę `X` o wysokości `n`, zbudowaną z `*` na obu przekątnych.

W wierszu `i` i kolumnie `j` (indeksy od 0):

* wypisz `*`, gdy `j == i` **lub** `j == n - 1 - i`,
* w przeciwnym razie wypisz spację.

### Wejście

* 1. linia: `n` (`n ≥ 3`)

### Wyjście

`n` linii po `n` znaków (`*` lub spacja).

### Przykład

**Wejście:**

```
5
```

**Wyjście:**

```
*   *
 * *
  *
 * *
*   *
```

---

## ZAD-06 — Litera „Z”

**Poziom:** ★★☆
**Tagi:** `pętle zagnieżdżone`, `warunki`, `ASCII-art`

### Treść

Wczytaj `n` (`n ≥ 3`) i wypisz literę `Z` o wysokości `n`:

* pierwszy wiersz: `n` gwiazdek,
* ostatni wiersz: `n` gwiazdek,
* w środku: jedna gwiazdka na przekątnej od prawej do lewej.

W wierszu `i` (0..n-1) i kolumnie `j`:

* jeśli `i == 0` lub `i == n-1` → `*`
* else jeśli `j == n-1-i` → `*`
* else → spacja

### Wejście

* 1. linia: `n` (`n ≥ 3`)

### Wyjście

`n` linii po `n` znaków.

### Przykład

**Wejście:**

```
5
```

**Wyjście:**

```
*****
   *
  *
 *
*****
```

---

## ZAD-07 — Choinka z N trójkątów

**Poziom:** ★★☆
**Tagi:** `pętle zagnieżdżone`, `generowanie`, `print`

### Treść

Wczytaj liczbę naturalną `N` (`N ≥ 1`). Wypisz choinkę składającą się z `N` trójkątów ustawionych jeden pod drugim:

* 1. trójkąt ma wysokość 1,
* 2. trójkąt ma wysokość 2,
* …
* `N`-ty trójkąt ma wysokość `N`.

Każdy trójkąt jest „rosnący” (jak w ZAD-02): w jego wierszu `i` wypisz `i` gwiazdek.

### Wejście

* 1. linia: `N` (`N ≥ 1`)

### Wyjście

Suma wysokości wszystkich trójkątów, czyli `1 + 2 + ... + N` linii.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
*
*
**
*
**
***
```

### Uwagi o formatowaniu

* Nie dodawaj pustych linii między trójkątami.

---

## ZAD-08 — Trójkąt Pascala

**Poziom:** ★★☆
**Tagi:** `pętle zagnieżdżone`, `listy`, `kombinatoryka`

### Treść

Wczytaj `n` (`n ≥ 1`) i wypisz trójkąt Pascala o wysokości `n`.

Wiersz 1: `1`
Wiersz 2: `1 1`
Wiersz 3: `1 2 1`
itd.

Liczby w wierszu oddzielaj pojedynczą spacją.

### Wejście

* 1. linia: `n` (`n ≥ 1`)

### Wyjście

`n` linii, w `i`-tej linii jest `i` liczb.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
1
1 1
1 2 1
```

### Uwagi o formatowaniu

* Nie dodawaj spacji na końcu wiersza.

---

## ZAD-09 — N pierwszych liczb pierwszych

**Poziom:** ★★☆
**Tagi:** `pętle`, `pierwszość`, `wydajność`

### Treść

Wczytaj liczbę naturalną `N` (`N ≥ 1`) i wypisz pierwsze `N` liczb pierwszych w **jednej linii**, oddzielone pojedynczą spacją.

### Wejście

* 1. linia: `N` (`N ≥ 1`)

### Wyjście

Jedna linia: `N` liczb pierwszych oddzielonych spacjami.

### Przykład

**Wejście:**

```
5
```

**Wyjście:**

```
2 3 5 7 11
```

### Uwagi o formatowaniu

* Nie dodawaj spacji na końcu linii.
* Do sprawdzania pierwszości wystarczy test dzielnikami do `⌊sqrt(x)⌋`.
