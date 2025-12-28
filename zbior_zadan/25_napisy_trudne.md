# Rozdział: Napisy — zadania dodatkowe

Poniższe zadania polegają na wczytywaniu danych ze **standardowego wejścia** (stdin) i wypisywaniu wyniku na **standardowe wyjście** (stdout).
**Każde zadanie (oraz każdy podpunkt w zadaniach wieloczęściowych) jest osobnym, niezależnym programem.**

**Konwencje wspólne:**

* Jeśli wejściem jest „napis” — wczytaj całą linię (razem ze spacjami), o ile zadanie nie mówi inaczej.
* Wypisuj dokładnie to, co wynika z polecenia: jeden napis / `Prawda` / `Fałsz` / lista.
* Wielkość liter ma znaczenie, jeśli nie napisano inaczej.
* Dla list w wyjściu przyjmujemy zapis w stylu Pythona, np. `['a', 'b']`, jeśli zadanie mówi „lista”.

---

## ZAD-01 — Podmiana słowa w zdaniu

**Poziom:** ★★☆
**Tagi:** `string`, `replace`, `substring`

### Treść

Masz trzy napisy:

1. Zdanie (tekst do modyfikacji),
2. Słowo A (podnapis do znalezienia),
3. Słowo B (podnapis zastępujący).

Zamień **wszystkie wystąpienia** słowa/podnapisu **A** na **B** w podanym zdaniu.

> Uwaga: A może być częścią innych słów — zamiana dotyczy **każdego wystąpienia podnapisu**.

### Wejście

* 1 linia: zdanie `S`
* 2 linia: napis `A`
* 3 linia: napis `B`

### Wyjście

* 1 linia: zdanie po zamianie

### Przykład

**Wejście:**

```
Lezy jezy na wiezy
zy
rzy
```

**Wyjście:**

```
Lerzy jerzy na wierzy
```

---

## ZAD-02 — Usuń podnapis

**Poziom:** ★★☆
**Tagi:** `string`, `replace`, `substring`

### Treść

Dostajesz dwa napisy:

1. Napis główny,
2. Podnapis do usunięcia.

Usuń **wszystkie wystąpienia** podnapisu z napisu głównego.

### Wejście

* 1 linia: napis `S`
* 2 linia: napis `T` (do usunięcia)

### Wyjście

* 1 linia: wynikowy napis po usunięciu wszystkich wystąpień

### Przykład

**Wejście:**

```
Lezy jezy na wiezy
zy
```

**Wyjście:**

```
Le je na wie
```

---

## ZAD-03 — Czy napis A jest początkiem napisu B?

**Poziom:** ★★☆
**Tagi:** `string`, `prefix`

### Treść

Otrzymujesz dwa napisy:

1. Napis `A` — potencjalny przedrostek,
2. Napis `B` — napis testowany.

Sprawdź, czy `B` **zaczyna się** od `A`.

### Wejście

* 1 linia: `A`
* 2 linia: `B`

### Wyjście

* 1 linia: `Prawda` albo `Fałsz`

### Przykład

**Wejście:**

```
Dino
Dinozaur jest zly
```

**Wyjście:**

```
Prawda
```

---

## ZAD-04 — Usuń powtórzenia znaków

**Poziom:** ★★★
**Tagi:** `string`, `set`, `unique`, `kolejność`

### Treść

Otrzymujesz napis. Usuń wszystkie powtórzenia znaków tak, aby **każdy znak wystąpił tylko raz**, zachowując **kolejność pierwszych wystąpień**.

### Wejście

* 1 linia: napis `S`

### Wyjście

* 1 linia: napis z unikalnymi znakami

### Przykład

**Wejście:**

```
AAAAAAAAAABBBBBBBBA
```

**Wyjście:**

```
AB
```

---

## ZAD-05 — Usuń powtórzenia sąsiadujących znaków

**Poziom:** ★★★
**Tagi:** `string`, `compress`, `run-length`

### Treść

Otrzymujesz napis. Usuń powtórzenia znaków występujących **bezpośrednio obok siebie**, pozostawiając jedno wystąpienie z każdej „serii”.

### Wejście

* 1 linia: napis `S`

### Wyjście

* 1 linia: napis po redukcji sąsiadów

### Przykład

**Wejście:**

```
AAAAAAAAAABBBBBBBBA
```

**Wyjście:**

```
ABA
```

---

## ZAD-06 — Rotacje napisów

**Poziom:** ★★★
**Tagi:** `string`, `rotation`, `substring`

### Treść

Otrzymujesz dwa napisy `A` i `B`. Sprawdź, czy jeden z nich jest **rotacją** drugiego (mają tę samą długość i da się uzyskać jeden przez przesunięcie cykliczne drugiego).

### Wejście

* 1 linia: napis `A`
* 2 linia: napis `B`

### Wyjście

* 1 linia: `Prawda` albo `Fałsz`

### Przykład

**Wejście:**

```
malpka
pkamal
```

**Wyjście:**

```
Prawda
```

---

## ZAD-07 — Powtarzające się podnapisy

**Poziom:** ★★★
**Tagi:** `string`, `substrings`, `count`

### Treść

Otrzymujesz napis. Znajdź wszystkie **podnapisy**, które występują w nim **więcej niż jeden raz**.

### Wejście

* 1 linia: napis `S`

### Wyjście

* 1 linia: lista napisów — wszystkie powtarzające się podnapisy

### Przykład

**Wejście:**

```
pythonpython
```

**Wyjście:**

```
['python']
```

### Uwagi

* Jeśli sprawdzarka wymaga konkretnej kolejności (np. rosnąco po długości/alfabetycznie) — musi to być opisane. W przeciwnym razie dopuszczalna może być dowolna kolejność.

---

## ZAD-08 — Najdłuższy wspólny przedrostek

**Poziom:** ★★★
**Tagi:** `string`, `prefix`, `list`

### Treść

Otrzymujesz listę napisów (w kolejnych liniach). Znajdź najdłuższy przedrostek wspólny dla wszystkich.

### Wejście

* 1 linia: `n` — liczba napisów
* kolejne `n` linii: napisy

### Wyjście

* 1 linia: najdłuższy wspólny przedrostek (może być pusty)

### Przykład

**Wejście:**

```
3
Remolada
Remux
Remmy
```

**Wyjście:**

```
Rem
```

---

## ZAD-09 — Najdłuższy wspólny podnapis

**Poziom:** ★★★
**Tagi:** `string`, `dp`, `substring`

### Treść

Otrzymujesz dwa napisy. Znajdź **najdłuższy wspólny podnapis** (ciągły fragment), który występuje w obu napisach.

### Wejście

* 1 linia: napis `A`
* 2 linia: napis `B`

### Wyjście

* 1 linia: najdłuższy wspólny podnapis
  (jeśli jest kilka o tej samej długości — wybierz ten, który występuje **najwcześniej w A**; jeśli nadal remis, najwcześniej w B)

### Przykład

**Wejście:**

```
ijkabcdl
xxxxabcd
```

**Wyjście:**

```
abcd
```

