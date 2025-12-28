# Rozdział: Funkcje — Wprowadzenie

Poniższe zadania dotyczą pisania **funkcji**.
**Każde zadanie (oraz każdy podpunkt w zadaniach wieloczęściowych) jest osobnym, niezależnym programem / ćwiczeniem funkcji.**

**Konwencje wspólne:**

* Jeśli zadanie mówi „funkcja zwraca” — chodzi o użycie instrukcji `return`.
* Jeśli zadanie zawiera kilka podpunktów (a, b, c…) — każdy podpunkt to **osobna funkcja**.
* Jeśli w danych wejściowych są liczby w osobnych liniach — wczytuj je dokładnie w tej kolejności.
* Jeśli w danych wyjściowych jest „każda w oddzielnej linii” — po każdym wyniku wypisz znak nowej linii.

---

## ZAD-01A — Zwracanie stałej wartości: liczba 3

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `return`, `int`

### Treść

Napisz funkcję (bez argumentów), która zwraca liczbę całkowitą `3`.

### Wejście

Brak.

### Wyjście

Funkcja ma zwrócić:

* `3`

### Przykład

**Wywołanie funkcji:**

```python
wynik = zwroc_liczbe()
print(wynik)
```

**Wyjście:**

```
3
```

---

## ZAD-01B — Zwracanie stałej wartości: napis „Tak”

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `return`, `string`

### Treść

Napisz funkcję (bez argumentów), która zwraca napis `Tak`.

### Wejście

Brak.

### Wyjście

Funkcja ma zwrócić:

* `Tak`

### Przykład

**Wywołanie funkcji:**

```python
wynik = zwroc_napis()
print(wynik)
```

**Wyjście:**

```
Tak
```

---

## ZAD-01C — Zwracanie stałej wartości: True

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `return`, `bool`

### Treść

Napisz funkcję (bez argumentów), która zwraca wartość logiczną `True`.

### Wejście

Brak.

### Wyjście

Funkcja ma zwrócić:

* `True`

### Przykład

**Wywołanie funkcji:**

```python
wynik = zwroc_prawda()
print(wynik)
```

**Wyjście:**

```
True
```

---

## ZAD-02A — Suma dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `arytmetyka`

### Treść

Napisz funkcję `suma(a, b)`, która zwraca sumę dwóch liczb całkowitych.

### Wejście

Dwa argumenty funkcji:

* `a` (liczba całkowita)
* `b` (liczba całkowita)

### Wyjście

Funkcja zwraca:

* `a + b`

### Przykład

**Wywołanie funkcji:**

```python
print(suma(3, 5))
```

**Wyjście:**

```
8
```

---

## ZAD-02B — Różnica: b − a

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `arytmetyka`

### Treść

Napisz funkcję `roznica(a, b)`, która zwraca różnicę: `b - a`.

### Wejście

Dwa argumenty funkcji: `a`, `b` (liczby całkowite)

### Wyjście

Funkcja zwraca:

* `b - a`

### Przykład

**Wywołanie funkcji:**

```python
print(roznica(3, 5))
```

**Wyjście:**

```
2
```

---

## ZAD-02C — Iloczyn dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `arytmetyka`

### Treść

Napisz funkcję `iloczyn(a, b)`, która zwraca iloczyn `a * b`.

### Wejście

Dwa argumenty funkcji: `a`, `b` (liczby całkowite)

### Wyjście

Funkcja zwraca:

* `a * b`

### Przykład

**Wywołanie funkcji:**

```python
print(iloczyn(3, 5))
```

**Wyjście:**

```
15
```

---

## ZAD-02D — Iloraz całkowity: a // b

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `dzielenie`, `//`

### Treść

Napisz funkcję `iloraz(a, b)`, która zwraca iloraz całkowity `a // b`.

### Wejście

Dwa argumenty funkcji: `a`, `b` (liczby całkowite)

### Ograniczenia / gwarancje

* `b ≠ 0`

### Wyjście

Funkcja zwraca:

* `a // b`

### Przykład

**Wywołanie funkcji:**

```python
print(iloraz(3, 5))
```

**Wyjście:**

```
0
```

---

## ZAD-02E — Reszta z dzielenia: a % b

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `modulo`, `%`

### Treść

Napisz funkcję `reszta(a, b)`, która zwraca resztę z dzielenia `a % b`.

### Wejście

Dwa argumenty funkcji: `a`, `b` (liczby całkowite)

### Ograniczenia / gwarancje

* `b ≠ 0`

### Wyjście

Funkcja zwraca:

* `a % b`

### Przykład

**Wywołanie funkcji:**

```python
print(reszta(3, 5))
```

**Wyjście:**

```
3
```

---

## ZAD-03 — Sprawdzanie warunków logicznych

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `bool`, `warunki`

### Treść

Napisz funkcję `sprawdz_warunki(a, b)`, która dla dwóch liczb naturalnych zwraca cztery wartości logiczne (np. jako krotkę) odpowiadające warunkom:

a) Czy `a > b`?
b) Czy `a + b < 10`?
c) Czy obie liczby są nieparzyste?
d) Czy `max(a, b) < a^2`?

### Wejście

Dwa argumenty funkcji:

* `a` (liczba całkowita, `a ≥ 0`)
* `b` (liczba całkowita, `b ≥ 0`)

### Wyjście

Cztery wartości logiczne w kolejności a), b), c), d).

### Przykład

**Wywołanie funkcji:**

```python
A, B, C, D = sprawdz_warunki(3, 2)
print(A)
print(B)
print(C)
print(D)
```

**Wyjście:**

```
True
True
False
True
```

---

## ZAD-04A — Minimum z dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `min`

### Treść

Napisz funkcję `min_z_dwoch(a, b)`, która zwraca mniejszą z dwóch liczb naturalnych.

### Wejście

Dwa argumenty: `a`, `b` (`a ≥ 0`, `b ≥ 0`)

### Wyjście

Funkcja zwraca:

* `min(a, b)`

### Przykład

**Wywołanie funkcji:**

```python
print(min_z_dwoch(3, 1))
```

**Wyjście:**

```
1
```

---

## ZAD-04B — Maksimum z dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `max`

### Treść

Napisz funkcję `max_z_dwoch(a, b)`, która zwraca większą z dwóch liczb naturalnych.

### Wejście

Dwa argumenty: `a`, `b` (`a ≥ 0`, `b ≥ 0`)

### Wyjście

Funkcja zwraca:

* `max(a, b)`

### Przykład

**Wywołanie funkcji:**

```python
print(max_z_dwoch(3, 1))
```

**Wyjście:**

```
3
```

---

## ZAD-04C — Minimum z trzech liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `min`

### Treść

Napisz funkcję `min_z_trzech(a, b, c)`, która zwraca najmniejszą z trzech liczb naturalnych.

### Wejście

Trzy argumenty: `a`, `b`, `c` (`a ≥ 0`, `b ≥ 0`, `c ≥ 0`)

### Wyjście

Funkcja zwraca:

* `min(a, b, c)`

### Przykład

**Wywołanie funkcji:**

```python
print(min_z_trzech(3, 2, 1))
```

**Wyjście:**

```
1
```

---

## ZAD-04D — Maksimum z trzech liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `max`

### Treść

Napisz funkcję `max_z_trzech(a, b, c)`, która zwraca największą z trzech liczb naturalnych.

### Wejście

Trzy argumenty: `a`, `b`, `c` (`a ≥ 0`, `b ≥ 0`, `c ≥ 0`)

### Wyjście

Funkcja zwraca:

* `max(a, b, c)`

### Przykład

**Wywołanie funkcji:**

```python
print(max_z_trzech(3, 2, 1))
```

**Wyjście:**

```
3
```

---

## ZAD-05 — Zamiana wartości miejscami

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `krotka`, `zmienne`

### Treść

Napisz funkcję `zamien_wartosci(a, b)`, która zamienia wartości miejscami i zwraca je jako parę `(b, a)`.

### Wejście

Dwa argumenty: `a`, `b` (liczby naturalne)

### Wyjście

Dwie liczby naturalne zwrócone jako krotka / para:

* najpierw nowa wartość `a` (czyli stare `b`)
* potem nowa wartość `b` (czyli stare `a`)

### Przykład

**Wywołanie funkcji:**

```python
a, b = zamien_wartosci(8, 5)
print("a =", a)
print("b =", b)
```

**Wyjście:**

```
a = 5
b = 8
```

---

## ZAD-06 — Suma cyfr liczby (funkcja)

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `pętle`, `modulo`

### Treść

Napisz funkcję `suma_cyfr(n)`, która zwraca sumę cyfr liczby naturalnej `n`.

### Wejście

Jeden argument: `n` (`n ≥ 0`)

### Wyjście

Funkcja zwraca sumę cyfr.

### Przykład

**Wywołanie funkcji:**

```python
print(suma_cyfr(13231))
```

**Wyjście:**

```
10
```

### Uwagi

* Dla `n = 0` suma cyfr to `0`.

---

## ZAD-07 — Weryfikacja nazwy użytkownika i hasła

**Poziom:** ★★☆
**Tagi:** `funkcje`, `while`, `string`, `porównania`

### Treść

Napisz dwie funkcje:

1. `pobierz_dane()` — pobiera od użytkownika nazwę użytkownika i hasło i zwraca je (np. jako parę).
2. `sprawdz_dane(poprawny_login, poprawne_haslo)` — w pętli wczytuje login i hasło aż będą identyczne z przekazanymi. Po poprawnym wczytaniu wypisuje:
   `Dane poprawne. Dostęp przyznany.`

### Wejście

* `pobierz_dane()` wczytuje dwie linie:

  1. login
  2. hasło
* `sprawdz_dane(...)` wczytuje kolejne pary (login, hasło), po dwie linie na próbę.

### Wyjście

Jedna linia (tylko raz, po poprawnym dopasowaniu):

* `Dane poprawne. Dostęp przyznany.`

### Ograniczenia / gwarancje

* W pewnym momencie użytkownik poda poprawne dane.

### Uwagi o formatowaniu

* **Nie wypisuj promptów** typu „Podaj nazwę użytkownika:”.
* Porównanie jest czułe na wielkość liter.

---

## ZAD-08 — Iloraz w dół bez / i %

**Poziom:** ★★☆
**Tagi:** `funkcje`, `pętle`, `odejmowanie`

### Treść

Napisz funkcję `zaokraglij_w_dol(a, b)`, która zwraca wartość `a // b`, ale **nie używa** operatorów `/` ani `%`.

### Wejście

Dwa argumenty:

* `a` (liczba naturalna, `a ≥ 0`)
* `b` (liczba naturalna)

### Ograniczenia / gwarancje

* `b > 0`

### Wyjście

Funkcja zwraca liczbę naturalną — iloraz `a` przez `b` zaokrąglony w dół.

### Przykład

**Wywołanie funkcji:**

```python
print(zaokraglij_w_dol(7, 2))
```

**Wyjście:**

```
3
```
