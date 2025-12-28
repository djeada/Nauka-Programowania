# Rozdział: Macierze i przedziały (stdin/stdout)

Poniższe zadania polegają na wczytywaniu danych ze **standardowego wejścia** (stdin) i wypisywaniu wyniku na **standardowe wyjście** (stdout).
**Każde zadanie (oraz każdy podpunkt) jest osobnym, niezależnym programem.**

**Konwencje wspólne:**

* Jeśli w danych wejściowych są liczby w osobnych liniach — wczytuj je dokładnie w tej kolejności.
* Jeśli w wierszu macierzy są liczby oddzielone spacjami — wczytaj cały wiersz i rozbij go po spacjach.
* W wyjściu macierzy: **każdy wiersz w osobnej linii**, elementy oddzielone **pojedynczą spacją**.

---

## ZAD-01 — Macierz z identycznymi wierszami 0..b

**Poziom:** ★☆☆
**Tagi:** `macierze`, `pętle`, `print`

### Treść

Wczytaj `a` i `b`. Wypisz macierz składającą się z `a` identycznych wierszy, gdzie każdy wiersz to liczby od `0` do `b` włącznie.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

* `a` wierszy, w każdym: `0 1 2 ... b`

### Przykład

**Wejście:**

```
3
2
```

**Wyjście:**

```
0 1 2
0 1 2
0 1 2
```

---

## ZAD-02 — Macierz n×n: iloczyn indeksów

**Poziom:** ★☆☆
**Tagi:** `macierze`, `pętle zagnieżdżone`

### Treść

Wczytaj `n`. Utwórz i wypisz macierz `n×n`, gdzie element `[i][j]` (indeksy od 0) ma wartość `i*j`.

### Wejście

* 1. linia: `n`

### Wyjście

* `n` wierszy po `n` liczb

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
0 0 0
0 1 2
0 2 4
```

---

## ZAD-03 — Macierz 2-kolumnowa z dwóch list

**Poziom:** ★☆☆
**Tagi:** `listy`, `macierze`

### Treść

Wczytaj dwie listy. Jeśli mają tę samą długość, wypisz macierz 2-kolumnową: wiersz `i` to `(lista1[i], lista2[i])`.
Jeśli długości są różne, wypisz: `Pusta macierz`

### Wejście

* 1. linia: `n`
* 2. linia: `m`
* następnie `n` liczb (pierwsza lista)
* następnie `m` liczb (druga lista)

### Wyjście

* Jeśli `n = m`: `n` wierszy `x y`
* Jeśli `n ≠ m`: jedna linia `Pusta macierz`

### Przykład

**Wejście:**

```
3
3
3
5
2
2
8
1
```

**Wyjście:**

```
3 2
5 8
2 1
```

---

## ZAD-04 — Dodawanie i odejmowanie macierzy

**Poziom:** ★☆☆
**Tagi:** `macierze`, `arytmetyka`

### Treść

Wczytaj dwie macierze `n×m`.
a) Wypisz ich sumę.
b) Wypisz różnicę: (pierwsza − druga).

### Wejście

* 1. linia: `n`
* 2. linia: `m`
* potem `n` wierszy pierwszej macierzy (po `m` liczb)
* potem `n` wierszy drugiej macierzy (po `m` liczb)

### Wyjście

Najpierw `n` wierszy sumy, potem `n` wierszy różnicy (bez dodatkowych napisów).

### Przykład

**Wejście:**

```
2
2
1 2
-2 0
5 -3
1 7
```

**Wyjście:**

```
6 -1
-1 7
-4 5
-3 -7
```

---

## ZAD-05 — Czy macierz jest magiczna?

**Poziom:** ★★☆
**Tagi:** `macierze`, `suma`, `warunki`

### Treść

Wczytaj macierz kwadratową `n×n` z dodatnimi liczbami naturalnymi. Sprawdź, czy to **kwadrat magiczny**: suma każdego wiersza, każdej kolumny oraz obu przekątnych jest taka sama.

### Wejście

* 1. linia: `n`
* następnie `n` wierszy po `n` liczb

### Wyjście

* `Prawda` albo `Fałsz`

### Przykład

**Wejście:**

```
3
6 7 2
1 5 9
8 3 4
```

**Wyjście:**

```
Prawda
```

---

## ZAD-06 — Scalanie przedziałów

**Poziom:** ★★☆
**Tagi:** `sortowanie`, `przedziały`, `algorytmy`

### Treść

Wczytaj `n` przedziałów `[a_i, b_i]` (a_i ≤ b_i). Scal przedziały nachodzące na siebie i wypisz wynik w kolejności rosnącej po początku.

### Wejście

* 1. linia: `n`
* następnie `n` linii: `a_i b_i`

### Wyjście

* Każdy scalony przedział w osobnej linii: `a b`

### Przykład

**Wejście:**

```
7
23 67
23 53
45 88
77 88
10 22
11 12
42 45
```

**Wyjście:**

```
10 22
23 88
```

### Uwagi

* Przedziały uznajemy za nachodzące, gdy `next_start <= current_end`.

---

## ZAD-07 — Zerowanie macierzy

**Poziom:** ★★☆
**Tagi:** `macierze`, `indeksy`

### Treść

Wczytaj macierz `n×m`. Jeśli w macierzy występuje `0`, to **cały wiersz i cała kolumna** tego zera mają zostać ustawione na `0` (dla wszystkich zer naraz).

### Wejście

* 1. linia: `n m`
* następnie `n` wierszy po `m` liczb

### Wyjście

* `n` wierszy zmodyfikowanej macierzy

### Przykład

**Wejście:**

```
3 3
1 2 3
4 0 6
7 8 9
```

**Wyjście:**

```
1 0 3
0 0 0
7 0 9
```

---

## ZAD-08 — Wypisanie elementów macierzy spiralnie

**Poziom:** ★★☆
**Tagi:** `macierze`, `spirala`

### Treść

Wczytaj macierz `n×m` i wypisz jej elementy spiralnie (zgodnie z ruchem wskazówek zegara), startując z lewego górnego rogu.

### Wejście

* 1. linia: `n m`
* następnie `n` wierszy po `m` liczb

### Wyjście

* 1 linia: elementy spiralnie, oddzielone spacjami

### Przykład

**Wejście:**

```
3 3
1 2 3
4 5 6
7 8 9
```

**Wyjście:**

```
1 2 3 6 9 8 7 4 5
```

---

## ZAD-09 — Klepsydra o największej sumie

**Poziom:** ★★☆
**Tagi:** `macierze`, `przeszukiwanie`

### Treść

Wczytaj macierz `n×m` (n,m ≥ 3). Znajdź maksymalną sumę „klepsydry” (7 pól):

```
a b c
  d
e f g
```

### Wejście

* 1. linia: `n m`
* następnie `n` wierszy po `m` liczb całkowitych

### Wyjście

* 1 linia: maksymalna suma klepsydry

### Przykład

**Wejście:**

```
4 4
7 4 2 0
4 8 10 8
3 6 7 6
3 9 19 14
```

**Wyjście:**

```
75
```

---

## ZAD-10 — Obróć macierz o 90° w prawo

**Poziom:** ★★☆
**Tagi:** `macierze`, `transpozycja`

### Treść

Wczytaj kwadratową macierz `n×n` i wypisz ją po obrocie o 90° zgodnie z ruchem wskazówek zegara.

### Wejście

* 1. linia: `n`
* następnie `n` wierszy po `n` liczb

### Wyjście

* `n` wierszy obróconej macierzy

### Przykład

**Wejście:**

```
3
1 2 3
4 5 6
7 8 9
```

**Wyjście:**

```
7 4 1
8 5 2
9 6 3
```

---

## ZAD-11 — Gra w statki (projekt konsolowy)

**Poziom:** ★★★
**Tagi:** `macierze`, `losowanie`, `gra`, `pętle`

### Treść

Zaimplementuj grę w statki na planszy 10×10:

1. Plansza startowa: 10×10 wypełniona `.`
2. Losowo rozmieść statki (poziomo/pionowo), bez stykania bokami ani rogami:

   * 1× długość 4
   * 2× długość 3
   * 3× długość 2
   * 5× długość 1
3. Pętla gry:

   * wypisz planszę,
   * wczytaj `r c` (0..9),
   * jeśli trafienie: wstaw `o`, wypisz komunikat o trafieniu,
   * jeśli pudło: wstaw `x`, zwiększ licznik pudeł,
   * gra kończy się, gdy:

     * wszystkie pola statków trafione (wygrana), albo
     * 10 pudeł (przegrana).
   * po każdym ruchu wypisz zaktualizowaną planszę.

### Wejście

Wielokrotnie:

* `r c` (w jednej linii)

### Wyjście

* plansza i komunikaty w trakcie,
* na końcu komunikat o wygranej/przegranej.

### Uwagi praktyczne

* To zadanie jest **większym projektem** — format wyjścia bywa sprawdzany „ręcznie” (nie zawsze automatycznie), więc trzymaj się spójnego stylu wypisywania planszy.

---
