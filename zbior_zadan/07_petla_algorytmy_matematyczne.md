# Rozdział: Pętla — Algorytmy Matematyczne

Poniższe zadania polegają na wczytywaniu danych ze **standardowego wejścia** (stdin) i wypisywaniu wyniku na **standardowe wyjście** (stdout).
**Każde zadanie (oraz każdy podpunkt w zadaniach wieloczęściowych) jest osobnym, niezależnym programem / ćwiczeniem funkcji.**

**Konwencje wspólne:**

* Jeśli zadanie mówi „napisz funkcję” — implementujesz funkcję o podanej nazwie i zwracasz wynik przez `return`.
* Jeśli w danych wejściowych są liczby w osobnych liniach — wczytuj je dokładnie w tej kolejności.
* Jeśli w danych wyjściowych jest „każda w oddzielnej linii” — po każdym wyniku wypisz znak nowej linii.
* Dla liczb zmiennoprzecinkowych stosuj formatowanie zgodne z poleceniem.

---

## ZAD-01 — Obliczanie średniej z n liczb

**Poziom:** ★☆☆
**Tagi:** `pętle`, `suma`, `średnia`, `float`

### Treść

Napisz funkcję `oblicz_srednia()`, która:

1. Wczytuje liczbę naturalną `n` (`n ≥ 1`).
2. Wczytuje następnie `n` liczb (całkowitych lub zmiennoprzecinkowych).
3. Zwraca ich średnią arytmetyczną.

### Wejście

* 1. linia: `n` (`n ≥ 1`)
* kolejne `n` linii: liczby (int lub float)

### Wyjście

Funkcja zwraca jedną liczbę zmiennoprzecinkową — średnią arytmetyczną.

### Przykład

**Wejście:**

```
2
4
6
```

**Wywołanie funkcji:**

```python
wynik = oblicz_srednia()
print(wynik)
```

**Wyjście:**

```
5.0
```

### Uwagi o formatowaniu

* Nie narzucamy liczby miejsc po przecinku — wypisz wynik w domyślnym formacie języka (lub jako `float`).

---

## ZAD-02 — Potęgowanie liczby przy pomocy pętli

**Poziom:** ★☆☆
**Tagi:** `pętle`, `potęgowanie`, `mnożenie`

### Treść

Napisz funkcję `potega(a, b)`, która oblicza `a^b` przy użyciu pętli (bez operatora potęgowania).

### Wejście

Dwa argumenty funkcji:

* `a` (liczba naturalna, `a ≥ 0`)
* `b` (liczba naturalna, `b ≥ 0`)

### Wyjście

Funkcja zwraca jedną liczbę naturalną — wartość `a^b`.

### Przykład

**Wywołanie funkcji:**

```python
print(potega(3, 5))
```

**Wyjście:**

```
243
```

### Uwagi o formatowaniu

* Dla `b = 0` wynik ma wynosić `1`.

---

## ZAD-03A — Mnożenie przy pomocy dodawania

**Poziom:** ★☆☆
**Tagi:** `pętle`, `dodawanie`, `mnożenie`

### Treść

Napisz funkcję `iloczyn(a, b)`, która oblicza `a * b` używając **tylko dodawania** i pętli.

### Wejście

Dwa argumenty funkcji:

* `a` (liczba naturalna, `a ≥ 0`)
* `b` (liczba naturalna, `b ≥ 0`)

### Wyjście

Funkcja zwraca jedną liczbę naturalną — `a * b`.

### Przykład

**Wywołanie funkcji:**

```python
print(iloczyn(3, 2))
```

**Wyjście:**

```
6
```

---

## ZAD-03B — Dzielenie całkowite przy pomocy odejmowania

**Poziom:** ★☆☆
**Tagi:** `pętle`, `odejmowanie`, `dzielenie`

### Treść

Napisz funkcję `iloraz(a, b)`, która oblicza `a // b` używając **tylko odejmowania** i pętli.

### Wejście

Dwa argumenty funkcji:

* `a` (liczba naturalna, `a ≥ 0`)
* `b` (liczba naturalna)

### Ograniczenia / gwarancje

* `b > 0`

### Wyjście

Funkcja zwraca jedną liczbę naturalną — `a // b`.

### Przykład

**Wywołanie funkcji:**

```python
print(iloraz(3, 2))
```

**Wyjście:**

```
1
```

---

## ZAD-04 — Obliczanie silni liczby

**Poziom:** ★☆☆
**Tagi:** `pętle`, `silnia`, `mnożenie`

### Treść

Napisz funkcję `silnia(n)`, która zwraca `n!` obliczone przy użyciu pętli.
Przyjmij, że `0! = 1`.

### Wejście

Jeden argument funkcji:

* `n` (liczba naturalna, `n ≥ 0`)

### Wyjście

Funkcja zwraca jedną liczbę naturalną — `n!`.

### Przykład

**Wywołanie funkcji:**

```python
print(silnia(3))
```

**Wyjście:**

```
6
```

---

## ZAD-05 — Największy wspólny dzielnik (NWD)

**Poziom:** ★☆☆
**Tagi:** `Euklides`, `modulo`, `pętle`

### Treść

Napisz funkcję `nwd(a, b)`, która zwraca największy wspólny dzielnik dwóch liczb naturalnych.

### Wejście

Dwa argumenty funkcji:

* `a` (liczba naturalna, `a > 0`)
* `b` (liczba naturalna, `b > 0`)

### Wyjście

Funkcja zwraca jedną liczbę naturalną — `NWD(a, b)`.

### Przykład

**Wywołanie funkcji:**

```python
print(nwd(60, 45))
```

**Wyjście:**

```
15
```

---

## ZAD-06 — Najmniejsza wspólna wielokrotność (NWW)

**Poziom:** ★☆☆
**Tagi:** `nww`, `nwd`, `arytmetyka`

### Treść

Napisz funkcję `nww(a, b)`, która zwraca najmniejszą wspólną wielokrotność liczb `a` i `b`.

### Wejście

Dwa argumenty funkcji:

* `a` (liczba naturalna, `a > 0`)
* `b` (liczba naturalna, `b > 0`)

### Wyjście

Funkcja zwraca jedną liczbę naturalną — `NWW(a, b)`.

### Przykład

**Wywołanie funkcji:**

```python
print(nww(7, 9))
```

**Wyjście:**

```
63
```

### Ograniczenia / gwarancje

* Możesz użyć zależności: `NWW(a, b) = (a * b) // NWD(a, b)`.

---

## ZAD-07 — Pierwiastek metodą Newtona (Herona)

**Poziom:** ★★☆
**Tagi:** `Newton`, `float`, `pętle`, `dokładność`

### Treść

Napisz funkcję `pierwiastek(n)`, która dla `n ≥ 0` zwraca przybliżenie `sqrt(n)` metodą Newtona:

$$
x_{k+1} = \frac{1}{2}\left(x_k + \frac{n}{x_k}\right)
$$

Iteruj do momentu, aż:
$$
|x_{k+1} - x_k| < 0.0001
$$

### Wejście

Jeden argument funkcji:

* `n` (liczba naturalna, `n ≥ 0`)

### Wyjście

Funkcja zwraca jedną liczbę zmiennoprzecinkową — przybliżony pierwiastek z `n`.

### Przykład

**Wywołanie funkcji:**

```python
print(pierwiastek(16))
```

**Wyjście:**

```
4.0
```

### Ograniczenia / gwarancje

* Dla `n = 0` funkcja ma zwrócić `0.0`.

---

## ZAD-08 — Naiwny test pierwszości liczby

**Poziom:** ★★☆
**Tagi:** `pierwszość`, `pętle`, `dzielniki`

### Treść

Napisz funkcję `czy_pierwsza(n)`, która zwraca `True`, jeśli `n` jest liczbą pierwszą, w przeciwnym razie `False`.

### Wejście

Jeden argument funkcji:

* `n` (liczba naturalna, `n ≥ 2`)

### Wyjście

Funkcja zwraca wartość logiczną:

* `True` lub `False`

### Przykład

**Wywołanie funkcji:**

```python
print(czy_pierwsza(7))
print(czy_pierwsza(4))
```

**Wyjście:**

```
True
False
```

### Uwagi

* Dla prostego rozwiązania możesz sprawdzać dzielniki od `2` do `n-1`.
* Dla szybszego rozwiązania możesz sprawdzać dzielniki do `⌊sqrt(n)⌋`.
