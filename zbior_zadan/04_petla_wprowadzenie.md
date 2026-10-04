# Rozdział 4: Pętle — wprowadzenie (while / for)

Zadania w tym rozdziale ćwiczą powtarzanie instrukcji za pomocą pętli `while` i `for`: wczytywanie danych aż do spełnienia warunku, wypisywanie ciągów liczb, sumowanie i proste obliczenia.

**Konwencje wspólne:**

* Każde zadanie (i każdy podpunkt) to osobny program: czyta **standardowe wejście** i wypisuje wynik na **standardowe wyjście**.
* Program nie wypisuje komunikatów typu „Podaj liczbę:”. Tekst podany w `input("…")` jest ignorowany przez sprawdzarkę.
* Dane wejściowe wczytuj dokładnie w podanej kolejności, każdą wartość z osobnej linii (o ile nie napisano inaczej).
* Jeśli wynik ma być „każdy w osobnej linii”, po każdej wartości wypisz znak nowej linii.
* Jeśli zadanie mówi, że w danym przypadku nic nie trzeba wypisywać, program nie wypisuje nic (nawet pustej linii).

---

## ZAD-01 — Warunek kończący pętlę

**Poziom:** ★☆☆
**Tagi:** `while`, `break`, `I/O`

### Treść

Wczytuj kolejne liczby naturalne (każdą z osobnej linii), dopóki nie wczytasz liczby `7`.
Siódemka kończy wczytywanie — po niej program nie wczytuje już żadnych danych.

Na koniec wypisz, ile liczb wczytano **przed** pierwszą siódemką (samej siódemki nie liczymy).

### Wejście

Kolejne liczby naturalne, każda w osobnej linii.

### Wyjście

Jedna liczba całkowita — liczba wczytanych liczb poprzedzających pierwszą siódemkę.

### Ograniczenia

* Wśród danych na pewno jest co najmniej jedna liczba `7`.
* Po pierwszej siódemce mogą występować kolejne linie — program ma je pominąć.

### Przykład

**Wejście:**

```
3
10
5
7
```

**Wyjście:**

```
3
```

Przed siódemką wczytano trzy liczby: `3`, `10` i `5`.

### Uwagi

* Jeśli pierwszą wczytaną liczbą jest `7`, wypisz `0`.
* Liczby takie jak `17` czy `70` nie kończą wczytywania — liczy się tylko liczba równa `7`.

---

## ZAD-02 — Wypisywanie liczb mniejszych od podanej

**Poziom:** ★☆☆
**Tagi:** `for`, `while`, `pętle`

### Treść

Wczytaj liczbę naturalną `n` i wypisz wszystkie liczby naturalne dodatnie mniejsze od `n` w kolejności malejącej — od `n - 1` do `1`.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 1`)

### Wyjście

Liczby `n - 1`, `n - 2`, …, `1`, każda w osobnej linii.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
2
1
```

### Uwagi

* Dla `n = 1` nie wypisuj nic.

---

## ZAD-03 — Wypisywanie liczby π z rosnącą dokładnością

**Poziom:** ★☆☆
**Tagi:** `math.pi`, `formatowanie`, `pętle`

### Treść

Wczytaj liczbę naturalną `n` i wypisz liczbę $\pi$ w `n` liniach: w pierwszej z dokładnością do `1` miejsca po przecinku, w drugiej do `2` miejsc, …, w `n`-tej do `n` miejsc po przecinku.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 1`)

### Wyjście

`n` linii; w `k`-tej linii liczba $\pi$ zaokrąglona do `k` miejsc po przecinku.

### Ograniczenia

* `1 ≤ n ≤ 15`

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
3.1
3.14
3.142
```

### Uwagi

* Wartość $\pi$ weź z modułu `math` (`math.pi`).
* Liczbę miejsc po przecinku możesz podać w f-stringu jako zmienną: `f"{math.pi:.{k}f}"` wypisze $\pi$ z dokładnością do `k` miejsc.
* Stosuj standardowe zaokrąglanie, np. przy `4` miejscach wypisz `3.1416`.
* Liczby zmiennoprzecinkowe mają ograniczoną precyzję — `math.pi` jest dokładne mniej więcej do 15. miejsca po przecinku, dlatego `n ≤ 15`.

---

## ZAD-04 — Sumowanie liczb mniejszych od podanej

**Poziom:** ★☆☆
**Tagi:** `sumowanie`, `pętle`, `arytmetyka`

### Treść

Wczytaj liczbę naturalną `n` i za pomocą pętli oblicz sumę wszystkich liczb naturalnych dodatnich mniejszych od `n`, czyli $1 + 2 + \ldots + (n - 1)$.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 1`)

### Wyjście

Jedna liczba całkowita — suma liczb od `1` do `n - 1`.

### Przykład

**Wejście:**

```
5
```

**Wyjście:**

```
10
```

$1 + 2 + 3 + 4 = 10$.

### Uwagi

* Dla `n = 1` suma jest pusta, więc wynik to `0`.

---

## ZAD-05 — Liczby z przedziału

**Poziom:** ★☆☆
**Tagi:** `pętle`, `przedziały`, `modulo`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`. Niech `lo` będzie mniejszą, a `hi` większą z nich.

a) Wypisz w kolejności rosnącej wszystkie liczby naturalne `x` takie, że `lo < x < hi`.

b) Następnie wypisz w kolejności rosnącej te z nich, które są podzielne przez `3`.

### Wejście

* 1. linia: `a` — liczba naturalna
* 2. linia: `b` — liczba naturalna

### Wyjście

Najpierw liczby z podpunktu a), potem liczby z podpunktu b) — każda w osobnej linii.

### Przykład

**Wejście:**

```
9
5
```

**Wyjście:**

```
6
7
8
6
```

Między `5` a `9` leżą liczby `6`, `7`, `8` (podpunkt a); spośród nich przez `3` dzieli się tylko `6` (podpunkt b).

### Uwagi

* Liczby `a` i `b` nie należą do przedziału (nierówności są ostre).
* Nie wypisuj nagłówków typu „a)” i „b)” ani pustej linii między podpunktami.
* Jeśli w którymś podpunkcie nie ma liczb do wypisania, ta część wyjścia jest pusta.

---

## ZAD-06 — Sumowanie elementów ciągu

**Poziom:** ★☆☆
**Tagi:** `ciągi`, `sumowanie`, `pętle`

### Treść

Wczytaj liczbę naturalną `n` i za pomocą pętli oblicz trzy sumy:

a) $\sum_{k=1}^{n} (k^2 + k + 1)$

b) $\sum_{k=1}^{n} (k^2 + 5k)$

c) $\sum_{k=1}^{n} 3k$

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 1`)

### Wyjście

Trzy liczby całkowite, każda w osobnej linii: suma a), suma b) i suma c).

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
10
20
9
```

Dla `n = 2`: a) $3 + 7 = 10$, b) $6 + 14 = 20$, c) $3 + 6 = 9$.

---

## ZAD-07 — Potęgowanie liczby π

**Poziom:** ★☆☆
**Tagi:** `math.pi`, `potęgi`, `formatowanie`

### Treść

Wczytaj liczbę naturalną `n` i oblicz $\pi^n$, mnożąc w pętli liczbę $\pi$ przez siebie. Wypisz wynik z dokładnością do **dwóch miejsc po przecinku**.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Jedna liczba — $\pi^n$ zaokrąglona do dwóch miejsc po przecinku.

### Ograniczenia

* `0 ≤ n ≤ 20`

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
9.87
```

### Uwagi

* $\pi^0 = 1$, więc dla `n = 0` wypisz `1.00`.

---

## ZAD-08 — Obliczanie liczby kur i owiec na farmie

**Poziom:** ★★☆
**Tagi:** `pętle`, `układ równań`, `arytmetyka`

### Treść

Na farmie są wyłącznie kury i owce. Każde zwierzę ma jedną głowę, kura ma 2 nogi, a owca 4 nogi.
Znając łączną liczbę głów `a` i łączną liczbę nóg `b`, oblicz, ile jest kur, a ile owiec.

### Wejście

* 1. linia: `a` — liczba głów (`a ≥ 0`)
* 2. linia: `b` — liczba nóg (`b ≥ 0`)

### Wyjście

Dwie liczby całkowite, każda w osobnej linii:

1. liczba kur,
2. liczba owiec.

### Ograniczenia

* Dane są poprawne: istnieje dokładnie jedno rozwiązanie w liczbach całkowitych nieujemnych.

### Przykład

**Wejście:**

```
40
100
```

**Wyjście:**

```
30
10
```

30 kur ma 60 nóg, a 10 owiec ma 40 nóg — razem 40 głów i 100 nóg.

### Uwagi

* Możesz sprawdzać w pętli kolejne możliwe liczby kur (od `0` do `a`) i szukać tej, dla której zgadza się liczba nóg.

---

## ZAD-09 — Ciąg Collatza

**Poziom:** ★☆☆
**Tagi:** `while`, `pętle`, `warunki`

### Treść

Ciąg Collatza zaczyna się od liczby `n`. Każdy kolejny wyraz powstaje z poprzedniego `x` według reguły:

* jeśli `x` jest parzyste, następny wyraz to $\frac{x}{2}$,
* jeśli `x` jest nieparzyste, następny wyraz to $3x + 1$.

Ciąg kończy się, gdy osiągnie wartość `1`.

Wczytaj `n` i wypisz, ile kroków (przejść do kolejnego wyrazu) potrzeba, aby dojść do `1`, oraz jaka jest największa wartość, która pojawiła się w ciągu (łącznie z samym `n`).

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 1`)

### Wyjście

Dwie liczby całkowite, każda w osobnej linii:

1. liczba kroków potrzebnych do osiągnięcia `1`,
2. największa wartość w ciągu.

### Ograniczenia

* `1 ≤ n ≤ 1000000`

### Przykład

**Wejście:**

```
6
```

**Wyjście:**

```
8
16
```

Ciąg ma postać $6 \to 3 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1$: to `8` kroków, a największy wyraz to `16`.

### Uwagi

* Nie wiadomo z góry, ile kroków wykona pętla — to typowe zastosowanie pętli `while`.
* Dla `n = 1` ciąg od razu jest w `1`: wypisz `0` i `1`.
* Do dzielenia używaj `//`, żeby wyrazy ciągu pozostały liczbami całkowitymi.
* Nikt nie udowodnił, że ciąg Collatza zawsze dochodzi do `1` (to słynna hipoteza Collatza), ale sprawdzono to dla wszystkich liczb z zakresu zadania.

---

## ZAD-10 — Walidacja danych wejściowych

**Poziom:** ★★☆
**Tagi:** `while`, `break`, `continue`, `try/except`

### Treść

Program prosi o liczbę całkowitą z przedziału $[1, 100]$ i nie poddaje się, dopóki jej nie dostanie.

Wczytuj kolejne linie. Dla każdej linii:

* jeśli nie jest liczbą całkowitą — wypisz `To nie jest liczba całkowita.` i wczytaj następną linię,
* jeśli jest liczbą całkowitą spoza przedziału $[1, 100]$ — wypisz `Liczba spoza zakresu.` i wczytaj następną linię,
* jeśli jest liczbą całkowitą z przedziału $[1, 100]$ — zakończ wczytywanie i wypisz `Przyjęto: X`, gdzie `X` to ta liczba.

Linia jest liczbą całkowitą, jeśli funkcja `int()` potrafi ją zamienić na liczbę (np. `42`, `-7`). Napisy takie jak `abc`, `3.5` czy pusta linia nie są liczbami całkowitymi.

### Wejście

Kolejne linie tekstu.

### Wyjście

Jeden komunikat o błędzie dla każdej niepoprawnej linii (w kolejności wczytywania), a na końcu linia `Przyjęto: X`.

### Ograniczenia

* Wśród danych na pewno jest co najmniej jedna poprawna liczba.
* Po pierwszej poprawnej liczbie mogą występować kolejne linie — program ma je pominąć.

### Przykład

**Wejście:**

```
abc
150
3.5
42
```

**Wyjście:**

```
To nie jest liczba całkowita.
Liczba spoza zakresu.
To nie jest liczba całkowita.
Przyjęto: 42
```

### Uwagi

* Wywołanie `int("abc")` kończy się błędem `ValueError`. Taki błąd można „złapać” konstrukcją `try`/`except`: Python wykonuje instrukcje z bloku `try`, a jeśli w którejś z nich wystąpi `ValueError`, zamiast przerywać program przechodzi do bloku `except ValueError:`.

  ```python
  try:
      liczba = int("abc")
      print("To się nie wykona.")
  except ValueError:
      print("Nie udało się zamienić napisu na liczbę.")
  ```

* `continue` przerywa bieżący obrót pętli i od razu przechodzi do następnego, a `break` kończy całą pętlę.
* Pętla `while True:` kręci się „w nieskończoność” — kończy ją dopiero `break`.
* Granice przedziału należą do niego: `1` i `100` są poprawne.

### Kod startowy

```python
while True:
    linia = input()
    try:
        liczba = int(linia)
    except ValueError:
        # Uzupełnij: wypisz komunikat i przejdź do kolejnej linii (continue).
        pass

    # Uzupełnij: jeśli liczba jest spoza przedziału [1, 100], wypisz komunikat
    # i przejdź do kolejnej linii; w przeciwnym razie zakończ pętlę (break).

print(f"Przyjęto: {liczba}")
```
