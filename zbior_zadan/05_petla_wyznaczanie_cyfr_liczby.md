# Rozdział 5: Pętle — cyfry liczby (dzielenie przez 10, modulo)

Zadania w tym rozdziale ćwiczą wyznaczanie cyfr liczby w pętli: ostatnią cyfrę liczby `n` daje `n % 10`, a dzielenie całkowite `n // 10` usuwa ją z liczby.

**Konwencje wspólne:**

* Każde zadanie (i każdy podpunkt) to osobny program: czyta **standardowe wejście** i wypisuje wynik na **standardowe wyjście**.
* Program nie wypisuje komunikatów typu „Podaj liczbę:”. Tekst podany w `input("…")` jest ignorowany przez sprawdzarkę.
* „Cyfry od końca” oznacza kolejność od cyfry jedności do najwyższej cyfry (tak, jak wyznacza je `n % 10` i `n // 10`).
* Liczba `0` ma jedną cyfrę: `0`.
* Jeśli zadanie mówi, że w danym przypadku nic nie trzeba wypisywać, program nie wypisuje nic (nawet pustej linii).

---

## ZAD-01 — Liczenie cyfr w liczbie

**Poziom:** ★☆☆
**Tagi:** `pętle`, `modulo`, `dzielenie całkowite`

### Treść

Wczytaj liczbę naturalną `n` i wypisz, z ilu cyfr składa się jej zapis dziesiętny.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Jedna liczba całkowita — liczba cyfr liczby `n`.

### Przykład

**Wejście:**

```
342
```

**Wyjście:**

```
3
```

### Uwagi

* Dla `n = 0` poprawna odpowiedź to `1`.
* Licz cyfry w pętli, dzieląc liczbę przez `10`.

---

## ZAD-02 — Wypisywanie cyfr liczby w odwrotnej kolejności

**Poziom:** ★☆☆
**Tagi:** `pętle`, `modulo`, `dzielenie całkowite`

### Treść

Wczytaj liczbę naturalną `n` i wypisz jej cyfry od końca — zaczynając od cyfry jedności, a kończąc na najwyższej cyfrze.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Cyfry liczby `n` od końca, każda w osobnej linii.

### Przykład

**Wejście:**

```
8214
```

**Wyjście:**

```
4
1
2
8
```

### Uwagi

* Dla `n = 0` wypisz jedną linię: `0`.
* Zera w środku i na końcu liczby też są cyframi — np. dla `120` wypisz `0`, `2`, `1`.

---

## ZAD-03 — Sumowanie cyfr liczby

**Poziom:** ★☆☆
**Tagi:** `pętle`, `modulo`, `dzielenie całkowite`

### Treść

Wczytaj liczbę naturalną `n`, oblicz sumę jej cyfr i wypisz wynik.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Jedna liczba całkowita — suma cyfr liczby `n`.

### Przykład

**Wejście:**

```
129
```

**Wyjście:**

```
12
```

$1 + 2 + 9 = 12$.

### Uwagi

* Dla `n = 0` suma cyfr wynosi `0`.

---

## ZAD-04A — Cyfry parzyste

**Poziom:** ★☆☆
**Tagi:** `pętle`, `modulo`, `warunki`

### Treść

Wczytaj liczbę naturalną `n` i wypisz od końca wszystkie jej cyfry, które są **parzyste**.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Parzyste cyfry liczby `n` od końca, każda w osobnej linii.
Jeśli `n` nie ma parzystych cyfr, nie wypisuj nic.

### Przykład

**Wejście:**

```
932
```

**Wyjście:**

```
2
```

### Uwagi

* `0` jest cyfrą parzystą, więc dla `n = 0` wypisz `0`.
* Każde wystąpienie cyfry wypisz osobno — np. dla `4004` wypisz `4`, `0`, `0`, `4`.

---

## ZAD-04B — Cyfry mniejsze niż 5

**Poziom:** ★☆☆
**Tagi:** `pętle`, `modulo`, `warunki`

### Treść

Wczytaj liczbę naturalną `n` i wypisz od końca wszystkie jej cyfry, które są **mniejsze niż 5**.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Cyfry liczby `n` mniejsze niż `5`, od końca, każda w osobnej linii.
Jeśli takich cyfr nie ma, nie wypisuj nic.

### Przykład

**Wejście:**

```
101
```

**Wyjście:**

```
1
0
1
```

### Uwagi

* Cyfra `5` nie jest mniejsza niż `5`.
* Dla `n = 0` wypisz `0`.

---

## ZAD-04C — Cyfry różne od zera

**Poziom:** ★☆☆
**Tagi:** `pętle`, `modulo`, `warunki`

### Treść

Wczytaj liczbę naturalną `n` i wypisz od końca wszystkie jej cyfry, które są **różne od zera**.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Niezerowe cyfry liczby `n` od końca, każda w osobnej linii.
Jeśli takich cyfr nie ma (czyli `n = 0`), nie wypisuj nic.

### Przykład

**Wejście:**

```
650
```

**Wyjście:**

```
5
6
```

Ostatnia cyfra `0` jest pomijana, potem wypisujemy `5` i `6`.

---

## ZAD-05 — Sprawdzanie, czy liczba jest palindromem

**Poziom:** ★★☆
**Tagi:** `pętle`, `modulo`, `palindrom`

### Treść

Wczytaj liczbę naturalną `n` i sprawdź, czy jest palindromem, czyli czy czytana od końca jest taka sama (np. `1221`, `7`). Wypisz odpowiedni komunikat.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Dokładnie jeden z komunikatów:

* `Liczba jest palindromem.`
* `Liczba nie jest palindromem.`

### Przykład

**Wejście:**

```
13231
```

**Wyjście:**

```
Liczba jest palindromem.
```

### Przykład 2

**Wejście:**

```
1231
```

**Wyjście:**

```
Liczba nie jest palindromem.
```

### Uwagi

* Każda liczba jednocyfrowa (także `0`) jest palindromem.
* Liczba zakończona zerem (np. `10`, `120`) nie jest palindromem, bo zapis liczby nie zaczyna się od `0`.
* Wskazówka: zbuduj w pętli liczbę o odwróconych cyfrach i porównaj ją z `n`.

---

## ZAD-06A — Liczby mniejsze od n o sumie cyfr równej 10

**Poziom:** ★★☆
**Tagi:** `pętle`, `suma cyfr`, `warunki`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz w kolejności rosnącej wszystkie liczby naturalne `x` takie, że `x < n` i suma cyfr liczby `x` wynosi `10`.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Liczby spełniające warunek, każda w osobnej linii.
Jeśli takich liczb nie ma, nie wypisuj nic.

### Przykład

**Wejście:**

```
50
```

**Wyjście:**

```
19
28
37
46
```

### Uwagi

* Nierówność jest ostra: samej liczby `n` nie wypisujemy, nawet jeśli suma jej cyfr wynosi `10`.

---

## ZAD-06B — Dwucyfrowe większe od n o różnych cyfrach

**Poziom:** ★★☆
**Tagi:** `pętle`, `cyfry`, `warunki`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz w kolejności rosnącej wszystkie liczby dwucyfrowe `x` (od `10` do `99`) takie, że `x > n` i cyfra dziesiątek liczby `x` jest **różna** od jej cyfry jedności.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Liczby spełniające warunek, każda w osobnej linii.
Jeśli takich liczb nie ma, nie wypisuj nic.

### Przykład

**Wejście:**

```
90
```

**Wyjście:**

```
91
92
93
94
95
96
97
98
```

Liczba `99` jest większa od `90`, ale ma dwie jednakowe cyfry, więc jej nie wypisujemy.

### Uwagi

* Cyfrę jedności liczby `x` daje `x % 10`, a cyfrę dziesiątek liczby dwucyfrowej — `x // 10`.
* Nierówność jest ostra: samej liczby `n` nie wypisujemy.
* Dla `n ≥ 98` żadna liczba nie spełnia warunku.

---

## ZAD-06C — Trzycyfrowe o sumie cyfr równej n

**Poziom:** ★★☆
**Tagi:** `pętle`, `suma cyfr`, `warunki`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz w kolejności rosnącej wszystkie liczby trzycyfrowe (od `100` do `999`), których suma cyfr jest równa `n`.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Liczby trzycyfrowe spełniające warunek, każda w osobnej linii.
Jeśli takich liczb nie ma, nie wypisuj nic.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
102
111
120
201
210
300
```

### Uwagi

* Suma cyfr liczby trzycyfrowej wynosi od `1` do `27`, więc dla innych `n` wynik jest pusty.

---

## ZAD-06D — Trzycyfrowe podzielne przez sumę cyfr liczby n

**Poziom:** ★★☆
**Tagi:** `pętle`, `dzielenie`, `suma cyfr`

### Treść

Wczytaj liczbę naturalną `n` i oblicz sumę jej cyfr `s`. Następnie wypisz w kolejności rosnącej wszystkie liczby trzycyfrowe (od `100` do `999`), które są podzielne przez `s`.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 1`)

### Wyjście

Liczby trzycyfrowe podzielne przez `s`, każda w osobnej linii.
Jeśli takich liczb nie ma, nie wypisuj nic.

### Ograniczenia

* `n ≥ 1`, więc `s ≥ 1` i dzielenie jest zawsze wykonalne.

### Przykład

**Wejście:**

```
9999999
```

**Wyjście:**

```
126
189
252
315
378
441
504
567
630
693
756
819
882
945
```

Suma cyfr to $s = 7 \cdot 9 = 63$, a wypisane liczby to kolejne trzycyfrowe wielokrotności `63`.

---

## ZAD-06E — Mniejsze od n złożone wyłącznie z parzystych cyfr

**Poziom:** ★★☆
**Tagi:** `pętle`, `warunki`, `cyfry`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz w kolejności rosnącej wszystkie liczby naturalne `x` takie, że `1 ≤ x < n` i **każda** cyfra liczby `x` jest parzysta.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Liczby spełniające warunek, każda w osobnej linii.
Jeśli takich liczb nie ma, nie wypisuj nic.

### Przykład

**Wejście:**

```
50
```

**Wyjście:**

```
2
4
6
8
20
22
24
26
28
40
42
44
46
48
```

### Uwagi

* `0` jest cyfrą parzystą, więc np. `20` i `40` spełniają warunek.
* Samą liczbę `0` pomijamy (zaczynamy od `x = 1`).

---

## ZAD-07 — Algorytm Luhna (numer karty)

**Poziom:** ★★☆
**Tagi:** `pętle`, `modulo`, `suma kontrolna`

### Treść

Numery kart płatniczych mają ostatnią cyfrę kontrolną, dzięki której łatwo wykryć literówkę. Sprawdza się ją **algorytmem Luhna**:

1. Numeruj cyfry od prawej strony, zaczynając od `1` (ostatnia cyfra ma pozycję `1`, przedostatnia `2` itd.).
2. Każdą cyfrę na pozycji parzystej (`2`, `4`, `6`, …) pomnóż przez `2`. Jeśli wynik jest większy niż `9`, odejmij od niego `9`.
3. Zsumuj wszystkie otrzymane wartości: zmienione cyfry z pozycji parzystych i niezmienione cyfry z pozycji nieparzystych.
4. Numer jest poprawny, jeśli suma jest podzielna przez `10`.

Wczytaj numer jako liczbę całkowitą i sprawdź go algorytmem Luhna, wyznaczając cyfry za pomocą `% 10` i `// 10`.

### Wejście

* 1. linia: `n` — numer karty, liczba naturalna mająca od `1` do `19` cyfr

### Wyjście

Jedno słowo: `Poprawny`, jeśli numer przechodzi test Luhna, w przeciwnym razie `Niepoprawny`.

### Przykład

**Wejście:**

```
79927398713
```

**Wyjście:**

```
Poprawny
```

Cyfry od prawej: `3 1 7 8 9 3 7 2 9 9 7`. Cyfry z pozycji parzystych (`1`, `8`, `3`, `2`, `9`) po podwojeniu i ewentualnym odjęciu `9` dają `2`, `7`, `6`, `4`, `9` (suma `28`). Pozostałe cyfry (`3`, `7`, `9`, `7`, `9`, `7`) sumują się do `42`. Razem $28 + 42 = 70$, a `70` dzieli się przez `10`.

### Przykład 2

**Wejście:**

```
79927398710
```

**Wyjście:**

```
Niepoprawny
```

### Uwagi

* W każdym obrocie pętli weź ostatnią cyfrę (`n % 10`), a potem usuń ją z liczby (`n //= 10`). Dodatkowy licznik (albo zmienna przełączana na zmianę) powie Ci, czy bieżąca cyfra stoi na pozycji parzystej.
* Odjęcie `9` od podwojonej cyfry to to samo, co zsumowanie cyfr wyniku, np. $2 \cdot 8 = 16$, a $16 - 9 = 7 = 1 + 6$.
