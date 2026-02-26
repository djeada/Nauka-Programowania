# Rozdział: Funkcje — wielomiany (stdin/stdout)

Poniższe zadania polegają na wczytywaniu danych ze **standardowego wejścia** (stdin) i wypisywaniu wyniku na **standardowe wyjście** (stdout).
**Każde zadanie (oraz każdy podpunkt) jest osobnym, niezależnym programem.**

**Konwencje wspólne:**

* Wielomian jest podany jako lista współczynników w kolejności: `[a_n, a_{n-1}, ..., a_0]`.
* Liczby całkowite mogą być ujemne.
* Jeśli w wyjściu jest „lista” — wypisz współczynniki w **jednej linii**, oddzielone pojedynczą spacją.
  *Wyjątek:* jeśli lista ma być pusta, wypisz dokładnie: `[]`.
* Nie wypisuj żadnych dodatkowych opisów ani nawiasów (poza `[]` dla pustej listy).

---

## ZAD-01 — Wartość wielomianu w punkcie

**Poziom:** ★☆☆
**Tagi:** `wielomiany`, `Horner`, `I/O`

### Treść

Wczytaj współczynniki wielomianu $a_nx^n + a_{n-1}x^{n-1} + \dots + a_0$ oraz liczbę $x$. Oblicz wartość wielomianu w punkcie $x$.

### Wejście

* 1. linia: `n` — stopień wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb całkowitych: `a_n a_{n-1} ... a_0`
* 3. linia: `x` — liczba całkowita

### Wyjście

Jedna liczba całkowita — wartość wielomianu w punkcie `x`.

### Przykład

**Wejście:**

```
2
3 2 1
1
```

**Wyjście:**

```
6
```

### Uwagi o formatowaniu

* Użyj schematu Hornera (jest najprostszy i najszybszy).

---

## ZAD-02 — Iloczyn wielomianu przez skalar

**Poziom:** ★☆☆
**Tagi:** `wielomiany`, `listy`, `I/O`

### Treść

Wczytaj współczynniki wielomianu oraz liczbę `k`. Wypisz współczynniki wielomianu powstałego przez pomnożenie każdego współczynnika przez `k`.

### Wejście

* 1. linia: `n` — stopień wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb całkowitych: `a_n ... a_0`
* 3. linia: `k` — liczba całkowita (skalar)

### Wyjście

Jedna linia: `n+1` liczb całkowitych (współczynniki po mnożeniu), oddzielonych spacją.

### Przykład

**Wejście:**

```
2
4 -3 2
-2
```

**Wyjście:**

```
-8 6 -4
```

---

## ZAD-03 — Suma wielomianów

**Poziom:** ★☆☆
**Tagi:** `wielomiany`, `wyrównanie stopni`, `I/O`

### Treść

Wczytaj dwa wielomiany i wypisz współczynniki wielomianu będącego ich sumą.

### Wejście

* 1. linia: `n` — stopień pierwszego wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb: `a_n ... a_0`
* 3. linia: `m` — stopień drugiego wielomianu (`m ≥ 0`)
* 4. linia: `m+1` liczb: `b_m ... b_0`

### Wyjście

Jedna linia: współczynniki sumy od najwyższej potęgi, oddzielone spacją.

### Przykład

**Wejście:**

```
2
3 5 2
2
2 -8 1
```

**Wyjście:**

```
5 -3 3
```

### Uwagi o formatowaniu

* Jeśli stopnie są różne, wyrównaj listy „od końca” (od wyrazu wolnego), dopisując zera na początku krótszej.

---

## ZAD-04 — Mnożenie wielomianów

**Poziom:** ★★☆
**Tagi:** `wielomiany`, `konwolucja`, `I/O`

### Treść

Wczytaj dwa wielomiany i wypisz współczynniki wielomianu będącego ich iloczynem.

### Wejście

* 1. linia: `n` — stopień pierwszego wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb: `a_n ... a_0`
* 3. linia: `m` — stopień drugiego wielomianu (`m ≥ 0`)
* 4. linia: `m+1` liczb: `b_m ... b_0`

### Wyjście

Jedna linia: współczynniki iloczynu (długość `n+m+1`), oddzielone spacją.

### Przykład

**Wejście:**

```
3
5 0 10 6
2
1 2 4
```

**Wyjście:**

```
5 10 30 26 52 24
```

---

## ZAD-05 — k-ta pochodna wielomianu

**Poziom:** ★★☆
**Tagi:** `pochodna`, `wielomiany`, `I/O`

### Treść

Wczytaj wielomian stopnia `n` oraz liczbę `k`. Wypisz współczynniki wielomianu będącego `k`-tą pochodną.

### Wejście

* 1. linia: `n` — stopień wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb: `a_n ... a_0`
* 3. linia: `k` — rząd pochodnej (`k ≥ 1`)

### Wyjście

* Jeśli po zróżniczkowaniu `k` razy zostaje wielomian niezerowy: wypisz jego współczynniki w jednej linii (spacje).
* Jeśli wielomian „znika” (stopień < k): wypisz dokładnie `[]`.

### Przykład

**Wejście:**

```
2
4 -3 2
1
```

**Wyjście:**

```
8 -3
```

### Uwagi o formatowaniu

* Pochodna: jeśli aktualne współczynniki to `[c_d, c_{d-1}, ..., c_0]`, to pochodna ma współczynniki:
  `[d*c_d, (d-1)*c_{d-1}, ..., 1*c_1]`.

---

## ZAD-06 — Miejsca zerowe równania kwadratowego (rzeczywiste)

**Poziom:** ★★☆
**Tagi:** `delta`, `pierwiastki`, `I/O`

### Treść

Wczytaj współczynniki równania kwadratowego ( ax^2 + bx + c = 0 ). Wypisz wszystkie **rzeczywiste** miejsca zerowe w kolejności rosnącej.

### Wejście

* 1. linia: trzy liczby całkowite: `a b c` (oddzielone spacją)

### Wyjście

* Jeśli brak rzeczywistych pierwiastków: wypisz `[]`
* Jeśli jeden pierwiastek (delta = 0): wypisz go raz w formacie listy: `[x]`
* Jeśli dwa pierwiastki: wypisz w formacie listy: `[x1, x2]` gdzie `x1 ≤ x2`

**Format liczb:**

* wypisuj jako liczby zmiennoprzecinkowe (np. `-1.0`, `2.5`)

### Przykład

**Wejście:**

```
1 2 1
```

**Wyjście:**

```
[-1.0]
```

### Uwagi o formatowaniu

* Licz deltę: `Δ = b*b - 4*a*c`.
* Dla `Δ > 0`: policz oba pierwiastki i posortuj rosnąco.
* Zakładamy `a ≠ 0`.
