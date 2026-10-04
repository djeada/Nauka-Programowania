# Rozdział 8: Pętle — pętle zagnieżdżone

Zadania w tym rozdziale ćwiczą pętle zagnieżdżone: pętla zewnętrzna przechodzi po wierszach, a wewnętrzna po kolumnach. W ten sposób rysujemy figury ze znaków, budujemy tabele liczb i przeszukujemy kolejne liczby.

**Konwencje wspólne:**

* Każde zadanie to osobny program: czyta **standardowe wejście** i wypisuje wynik na **standardowe wyjście**.
* Program nie wypisuje komunikatów typu „Podaj n:”. Tekst podany w `input("…")` jest ignorowany przez sprawdzarkę.
* Każdy wiersz figury lub tabeli wypisz w osobnej linii.
* W rysunkach spacje na początku i w środku wiersza są istotne. Spacje na końcu wiersza są ignorowane przez sprawdzarkę, więc nie musisz ich wypisywać.

---

## ZAD-01 — Kwadrat

**Poziom:** ★☆☆
**Tagi:** `pętle zagnieżdżone`, `print`, `string`

### Treść

Wczytaj liczbę naturalną `n` i wypisz kwadrat o boku `n` zbudowany z gwiazdek `*`.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 1`)

### Wyjście

`n` linii, w każdej dokładnie `n` znaków `*` (bez spacji).

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

### Uwagi

* Spróbuj użyć dwóch pętli: zewnętrznej dla wierszy i wewnętrznej dla gwiazdek w wierszu (`print("*", end="")`).

---

## ZAD-02 — Trójkąt prostokątny (rosnący)

**Poziom:** ★☆☆
**Tagi:** `pętle zagnieżdżone`, `print`, `string`

### Treść

Wczytaj liczbę naturalną `n` i wypisz trójkąt o wysokości `n`: w wierszu numer `i` (licząc od `1`) ma być `i` gwiazdek.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 1`)

### Wyjście

`n` linii: w pierwszej `1` gwiazdka, w drugiej `2` gwiazdki, …, w ostatniej `n` gwiazdek.

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
**Tagi:** `pętle zagnieżdżone`, `print`, `string`

### Treść

Wczytaj liczbę naturalną `n` i wypisz odwrócony trójkąt o wysokości `n`: w pierwszym wierszu `n` gwiazdek, w każdym kolejnym o jedną mniej.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 1`)

### Wyjście

`n` linii: w pierwszej `n` gwiazdek, w drugiej `n - 1`, …, w ostatniej `1` gwiazdka.

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

Wczytaj liczbę naturalną `N` i wypisz tabliczkę mnożenia o wymiarach `N × N`: w wierszu `i` i kolumnie `j` (licząc od `1`) ma znaleźć się iloczyn $i \cdot j$.

Aby kolumny tworzyły równą tabelę, każdą liczbę wyrównaj do prawej w polu o szerokości `w`, gdzie `w` to liczba cyfr największej liczby w tabeli, czyli `w = len(str(N * N))`. Kolejne pola w wierszu oddzielaj pojedynczą spacją.

### Wejście

* 1. linia: `N` — liczba naturalna (`N ≥ 1`)

### Wyjście

`N` linii; w każdej `N` pól o szerokości `w` (liczba wyrównana do prawej, z lewej uzupełniona spacjami), oddzielonych pojedynczą spacją.

### Ograniczenia

* `1 ≤ N ≤ 30`

### Przykład

**Wejście:**

```
4
```

**Wyjście:**

```
 1  2  3  4
 2  4  6  8
 3  6  9 12
 4  8 12 16
```

Największa liczba to `16`, więc `w = 2`: liczby jednocyfrowe są poprzedzone dodatkową spacją.

### Uwagi

* Zapis `f"{x:>{w}}"` w f-stringu wypisuje `x` wyrównane do prawej (`>`) w polu o szerokości `w` znaków; brakujące miejsca są uzupełniane spacjami z lewej. Na przykład `f"{7:>3}"` daje `"  7"`, a `f"{123:>3}"` daje `"123"`.
* `len(str(x))` to liczba cyfr liczby naturalnej `x`, np. `len(str(144))` wynosi `3`.
* Spacje na początku wiersza są istotne. Nie dodawaj spacji na końcu wiersza.

---

## ZAD-05 — Litera X

**Poziom:** ★★☆
**Tagi:** `pętle zagnieżdżone`, `warunki`, `ASCII-art`

### Treść

Wczytaj liczbę naturalną `n` i wypisz literę `X` o wysokości i szerokości `n`, zbudowaną z gwiazdek leżących na obu przekątnych kwadratu.

W wierszu `i` i kolumnie `j` (numerowanych od `0` do `n - 1`) wypisz `*`, gdy `j == i` **lub** `j == n - 1 - i`. W przeciwnym razie wypisz spację.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 3`)

### Wyjście

`n` linii z gwiazdkami i spacjami tworzących literę `X`.

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

### Uwagi

* Dla parzystego `n` przekątne nie przecinają się w jednym punkcie — w dwóch środkowych wierszach gwiazdki stoją obok siebie.

---

## ZAD-06 — Litera Z

**Poziom:** ★★☆
**Tagi:** `pętle zagnieżdżone`, `warunki`, `ASCII-art`

### Treść

Wczytaj liczbę naturalną `n` i wypisz literę `Z` o wysokości i szerokości `n`:

* pierwszy i ostatni wiersz składają się z `n` gwiazdek,
* w pozostałych wierszach jest jedna gwiazdka leżąca na przekątnej biegnącej z prawego górnego do lewego dolnego rogu.

W wierszu `i` i kolumnie `j` (numerowanych od `0` do `n - 1`) wypisz `*`, gdy `i == 0`, `i == n - 1` lub `j == n - 1 - i`. W przeciwnym razie wypisz spację.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 3`)

### Wyjście

`n` linii z gwiazdkami i spacjami tworzących literę `Z`.

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

Wczytaj liczbę naturalną `N` i wypisz choinkę złożoną z `N` trójkątów ustawionych jeden pod drugim. Pierwszy trójkąt ma wysokość `1`, drugi `2`, …, ostatni `N`.

Każdy trójkąt jest rosnący (jak w ZAD-02): w jego `i`-tym wierszu jest `i` gwiazdek.

### Wejście

* 1. linia: `N` — liczba naturalna (`N ≥ 1`)

### Wyjście

$1 + 2 + \ldots + N$ linii — kolejne trójkąty, bez pustych linii między nimi.

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

---

## ZAD-08 — Trójkąt Pascala

**Poziom:** ★★☆
**Tagi:** `pętle zagnieżdżone`, `kombinatoryka`

### Treść

Wczytaj liczbę naturalną `n` i wypisz `n` pierwszych wierszy trójkąta Pascala.

Każdy wiersz zaczyna się i kończy liczbą `1`, a każda liczba w środku wiersza jest sumą dwóch liczb stojących nad nią w poprzednim wierszu:

```
1
1 1
1 2 1
1 3 3 1
```

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 1`)

### Wyjście

`n` linii; w `i`-tej linii jest `i` liczb oddzielonych pojedynczą spacją.

### Ograniczenia

* `1 ≤ n ≤ 30`

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

### Uwagi

* Liczby w wierszu numer $r$ (licząc od $0$) to symbole Newtona $\binom{r}{0}, \binom{r}{1}, \ldots, \binom{r}{r}$. Kolejną liczbę w wierszu można obliczyć z poprzedniej: $\binom{r}{k+1} = \binom{r}{k} \cdot \frac{r - k}{k + 1}$ — wtedy nie potrzebujesz zapamiętywać poprzedniego wiersza.

---

## ZAD-09 — N pierwszych liczb pierwszych

**Poziom:** ★★☆
**Tagi:** `pętle zagnieżdżone`, `pierwszość`

### Treść

Wczytaj liczbę naturalną `N` i wypisz `N` pierwszych liczb pierwszych w jednej linii, w kolejności rosnącej.

### Wejście

* 1. linia: `N` — liczba naturalna (`N ≥ 1`)

### Wyjście

Jedna linia: `N` liczb pierwszych oddzielonych pojedynczą spacją.

### Ograniczenia

* `1 ≤ N ≤ 1000`

### Przykład

**Wejście:**

```
5
```

**Wyjście:**

```
2 3 5 7 11
```

### Uwagi

* Pętla zewnętrzna sprawdza kolejne liczby, a wewnętrzna szuka ich dzielników. Wystarczy sprawdzać dzielniki `d` spełniające $d \cdot d \leq x$.
