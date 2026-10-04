# Rozdział 9: Listy — wprowadzenie

Zadania w tym rozdziale ćwiczą podstawowe operacje na listach: wczytywanie, przechodzenie pętlą, modyfikowanie elementów, wyszukiwanie i zliczanie.

**Konwencje wspólne:**

* Każde zadanie (i każdy podpunkt) to osobny program: czyta **standardowe wejście** i wypisuje wynik na **standardowe wyjście**.
* **Lista na wejściu** zajmuje dwie linie: w 1. linii jest liczba elementów `n`, a w 2. linii — `n` liczb oddzielonych pojedynczymi spacjami. Dodatkowe dane (np. szukany klucz) są w kolejnych liniach, po jednej wartości w linii.
* Taką listę wczytasz np. tak:

  ```python
  n = int(input())
  lista = [int(x) for x in input().split()]
  ```

* Gdy wynikiem jest lista, wypisz ją instrukcją `print(lista)`. Python wypisze ją w nawiasach kwadratowych, z elementami oddzielonymi przecinkiem i spacją, np. `[4, 10, 8]`. Pusta lista to `[]`.
* Jeśli zadanie mówi „oddzielone spacją” — użyj pojedynczej spacji.
* Indeksy elementów liczymy od `0`.
* Program nie wypisuje komunikatów typu „Podaj liczbę:”.

---

## ZAD-01 — Wczytaj i wypisz

**Poziom:** ★☆☆
**Tagi:** `listy`, `I/O`, `odwracanie`

### Treść

Wczytaj listę `n` liczb całkowitych, a następnie:

a) wypisz elementy listy od początku do końca — każdy w osobnej linii,
b) utwórz nową listę z tymi samymi elementami w odwrotnej kolejności i wypisz ją w **jednej** linii.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb całkowitych oddzielonych spacjami

### Wyjście

Najpierw `n` linii z elementami w kolejności wczytania (podpunkt a), a potem jedna linia z odwróconą listą, w formacie `print(lista)` (podpunkt b).

### Ograniczenia

* $n \ge 1$

### Przykład

**Wejście:**

```
3
8 12 7
```

**Wyjście:**

```
8
12
7
[7, 12, 8]
```

---

## ZAD-02 — Wczytaj, zmodyfikuj i wypisz

**Poziom:** ★☆☆
**Tagi:** `listy`, `indeksy`, `modyfikacja`

### Treść

Wczytaj listę `n` liczb całkowitych. Następnie utwórz i wypisz trzy nowe listy, każdą na podstawie **wczytanej** (oryginalnej) listy:

a) każdy element zwiększony o `1`,
b) każdy element pomnożony przez swój indeks,
c) wszystkie elementy zastąpione wartością pierwszego elementu.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb całkowitych oddzielonych spacjami

### Wyjście

Trzy linie — listy z podpunktów a), b), c) w tej kolejności, w formacie `print(lista)`.

### Ograniczenia

* $n \ge 1$

### Przykład

**Wejście:**

```
3
3 9 7
```

**Wyjście:**

```
[4, 10, 8]
[0, 9, 14]
[3, 3, 3]
```

W podpunkcie b): $3 \cdot 0 = 0$, $9 \cdot 1 = 9$, $7 \cdot 2 = 14$.

---

## ZAD-03 — Pierwsze wystąpienie klucza

**Poziom:** ★☆☆
**Tagi:** `listy`, `wyszukiwanie`, `indeksy`

### Treść

Wczytaj listę `n` liczb całkowitych oraz liczbę `klucz`. Wypisz indeks pierwszego wystąpienia liczby `klucz` w liście.
Jeśli `klucz` nie występuje w liście — wypisz `-1`.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb całkowitych oddzielonych spacjami
* 3. linia: liczba całkowita `klucz`

### Wyjście

Jedna liczba całkowita: indeks pierwszego wystąpienia klucza albo `-1`.

### Ograniczenia

* $n \ge 1$

### Przykład

**Wejście:**

```
5
2 9 -1 3 8
-1
```

**Wyjście:**

```
2
```

---

## ZAD-04 — Minimum oraz maksimum

**Poziom:** ★☆☆
**Tagi:** `listy`, `min`, `max`

### Treść

Wczytaj listę `n` liczb całkowitych. Wypisz największą, a po niej najmniejszą liczbę z listy.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb całkowitych oddzielonych spacjami

### Wyjście

Jedna linia: największa i najmniejsza liczba, oddzielone spacją.

### Ograniczenia

* $n \ge 1$

### Przykład

**Wejście:**

```
9
4 -7 8 5 6 -9 10 2 -8
```

**Wyjście:**

```
10 -9
```

### Uwagi

* Spróbuj znaleźć obie wartości samodzielnie, w pętli, bez funkcji `max` i `min`.

---

## ZAD-05 — Zmodyfikuj elementy spełniające warunek

**Poziom:** ★☆☆
**Tagi:** `listy`, `warunki`, `liczby pierwsze`

### Treść

Wczytaj listę `n` liczb całkowitych. Wykonaj kolejno poniższe operacje — każda działa na liście **otrzymanej w poprzednim podpunkcie** (pierwsza na liście wczytanej). Po każdym podpunkcie wypisz aktualną listę.

a) Zwiększ o `1` elementy o **parzystych indeksach** ($0, 2, 4, \ldots$).
b) Ustaw na `0` elementy, które są **wielokrotnościami liczby 3**.
c) Podnieś do kwadratu elementy **mniejsze od 10**.
d) Oblicz sumę wszystkich elementów listy i wpisz ją w miejsce elementów o indeksach będących **liczbami pierwszymi** ($2, 3, 5, 7, 11, \ldots$).
e) Zamień każdy element na **iloczyn wszystkich pozostałych** elementów listy.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb całkowitych oddzielonych spacjami

### Wyjście

Pięć linii — lista po podpunktach a), b), c), d), e), w formacie `print(lista)`.

### Ograniczenia

* $n \ge 1$

### Przykład

**Wejście:**

```
4
1 4 2 5
```

**Wyjście:**

```
[2, 4, 3, 5]
[2, 4, 0, 5]
[4, 16, 0, 25]
[4, 16, 45, 45]
[32400, 8100, 2880, 2880]
```

a) indeksy 0 i 2: `1 → 2`, `2 → 3`; b) `3 → 0`; c) wszystkie elementy są mniejsze od 10; d) suma $4 + 16 + 0 + 25 = 45$ trafia na indeksy 2 i 3; e) np. dla indeksu 0: $16 \cdot 45 \cdot 45 = 32400$.

### Uwagi

* Indeksy `0` i `1` nie są liczbami pierwszymi.
* `0` (także po podpunkcie b) jest wielokrotnością liczby 3, a liczby ujemne są mniejsze od 10.
* Dla listy jednoelementowej iloczyn „pozostałych” elementów w podpunkcie e) wynosi `1` (iloczyn pustego zbioru).
* Jeśli w liście jest `0`, wiele iloczynów w podpunkcie e) będzie równych `0` — to normalne.

---

## ZAD-06 — Czy średnia elementów znajduje się w liście?

**Poziom:** ★☆☆
**Tagi:** `listy`, `średnia`, `wyszukiwanie`

### Treść

Wczytaj listę `n` liczb całkowitych. Oblicz średnią arytmetyczną jej elementów i sprawdź, czy ta średnia jest **dokładnie** równa któremuś z elementów listy.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb całkowitych oddzielonych spacjami

### Wyjście

Jedno słowo: `Tak`, jeśli średnia występuje w liście, albo `Nie` w przeciwnym razie.

### Ograniczenia

* $n \ge 1$

### Przykład

**Wejście:**

```
5
6 2 1 4 27
```

**Wyjście:**

```
Nie
```

Średnia wynosi $\frac{40}{5} = 8$, a liczby $8$ nie ma w liście.

### Uwagi

* Średnia może być ułamkiem (np. $1.5$) — wtedy na pewno nie jest elementem listy liczb całkowitych. Nie zaokrąglaj jej.

---

## ZAD-07 — Średnia dwóch największych liczb

**Poziom:** ★☆☆
**Tagi:** `listy`, `max`, `sortowanie`, `float`

### Treść

Wczytaj listę `n` liczb naturalnych. Znajdź dwa największe elementy listy i wypisz ich średnią arytmetyczną.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb naturalnych oddzielonych spacjami

### Wyjście

Jedna liczba: średnia dwóch największych elementów, z dokładnością do **jednego** miejsca po przecinku (np. `8.0`, `5.5`).

### Ograniczenia

* $n \ge 2$

### Przykład

**Wejście:**

```
6
9 2 3 2 1 7
```

**Wyjście:**

```
8.0
```

Dwa największe elementy to $9$ i $7$, a $\frac{9 + 7}{2} = 8$.

### Uwagi

* Jeśli największa wartość występuje w liście kilka razy, oba największe elementy mają tę samą wartość, np. dla `5 3 5` wynik to `5.0`.
* Liczbę z jednym miejscem po przecinku wypiszesz np. tak: `print(f"{wynik:.1f}")`.

---

## ZAD-08 — Usuń klucz

**Poziom:** ★☆☆
**Tagi:** `listy`, `remove`, `wyszukiwanie`

### Treść

Wczytaj listę `n` liczb całkowitych oraz liczbę `klucz`. Usuń z listy **pierwsze** wystąpienie liczby `klucz` (jeśli istnieje) i wypisz listę po tej zmianie.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb całkowitych oddzielonych spacjami
* 3. linia: liczba całkowita `klucz`

### Wyjście

Jedna linia: lista po usunięciu klucza, w formacie `print(lista)`.

### Ograniczenia

* $n \ge 1$

### Przykład

**Wejście:**

```
5
6 2 1 4 27
4
```

**Wyjście:**

```
[6, 2, 1, 27]
```

### Uwagi

* Jeśli `klucz` nie występuje w liście, wypisz listę bez zmian.
* Jeśli po usunięciu lista jest pusta, program wypisze `[]`.

---

## ZAD-09 — Usuń duplikaty (z zachowaniem kolejności)

**Poziom:** ★☆☆
**Tagi:** `listy`, `duplikaty`

### Treść

Wczytaj listę `n` liczb naturalnych i usuń z niej duplikaty tak, aby każda liczba występowała tylko raz — **zachowując kolejność pierwszych wystąpień**.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb naturalnych oddzielonych spacjami

### Wyjście

Jedna linia: lista bez duplikatów, w formacie `print(lista)`.

### Ograniczenia

* $n \ge 1$

### Przykład

**Wejście:**

```
6
3 2 1 3 2 2
```

**Wyjście:**

```
[3, 2, 1]
```

### Uwagi

* W rozdziale 10 poznasz zbiory (`set`) — też usuwają duplikaty, ale nie zachowują kolejności elementów, dlatego tutaj ich nie używaj.

---

## ZAD-10 — Czy punkty mogą być wierzchołkami trójkąta?

**Poziom:** ★★☆
**Tagi:** `geometria`, `warunki`, `listy`

### Treść

Wczytaj współrzędne trzech punktów $A(x_A, y_A)$, $B(x_B, y_B)$, $C(x_C, y_C)$.
Wypisz `Tak`, jeśli punkty mogą być wierzchołkami trójkąta (czyli **nie leżą** na jednej prostej), a w przeciwnym razie `Nie`.

### Wejście

Trzy linie — w każdej dwie liczby całkowite `x y` oddzielone spacją:

* 1. linia: współrzędne punktu `A`
* 2. linia: współrzędne punktu `B`
* 3. linia: współrzędne punktu `C`

### Wyjście

Jedno słowo: `Tak` albo `Nie`.

### Przykład

**Wejście:**

```
-3 -2
-3 1
-3 0
```

**Wyjście:**

```
Nie
```

Wszystkie trzy punkty leżą na prostej $x = -3$.

### Uwagi

* Punkty leżą na jednej prostej wtedy i tylko wtedy, gdy $(x_B - x_A)(y_C - y_A) - (y_B - y_A)(x_C - x_A) = 0$ (to wyrażenie jest równe podwojonemu polu trójkąta $ABC$, z dokładnością do znaku).
* Jeśli dwa punkty się pokrywają, trójkąta nie da się zbudować.

---

## ZAD-11 — Samochody jadące w przeciwnych kierunkach

**Poziom:** ★★☆
**Tagi:** `listy`, `zliczanie`, `string`

### Treść

Wczytaj `n` oraz napis długości `n` złożony z liter `A` i `B`, opisujący samochody na drodze:

* `A` oznacza samochód jadący na wschód,
* `B` oznacza samochód jadący na zachód.

Para samochodów minie się, jeśli samochód `A` stoi w napisie **przed** samochodem `B` (niekoniecznie bezpośrednio). Policz wszystkie takie pary.

### Wejście

* 1. linia: liczba samochodów `n`
* 2. linia: napis długości `n` złożony tylko z liter `A` i `B` (bez spacji)

### Wyjście

Jedna liczba naturalna: liczba mijających się par.

### Ograniczenia

* $n \ge 1$

### Przykład

**Wejście:**

```
5
ABABB
```

**Wyjście:**

```
5
```

Pierwszy samochód `A` minie trzy samochody `B`, a drugi `A` — dwa: $3 + 2 = 5$.

---

## ZAD-12 — Rotacja w lewo / prawo

**Poziom:** ★★☆
**Tagi:** `listy`, `rotacja`, `modulo`

### Treść

Wczytaj listę `n` liczb całkowitych, kierunek rotacji oraz liczbę `k`. Przesuń cyklicznie elementy listy o `k` pozycji:

* `kierunek = 0` — w lewo (pierwszy element trafia na koniec),
* `kierunek = 1` — w prawo (ostatni element trafia na początek).

Wypisz listę po rotacji.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb całkowitych oddzielonych spacjami
* 3. linia: `kierunek` (`0` albo `1`)
* 4. linia: liczba przesunięć `k`

### Wyjście

Jedna linia: lista po rotacji, w formacie `print(lista)`.

### Ograniczenia

* $n \ge 1$
* $k \ge 0$ (`k` może być większe od `n`)

### Przykład

**Wejście:**

```
7
5 27 6 2 1 10 8
0
2
```

**Wyjście:**

```
[6, 2, 1, 10, 8, 5, 27]
```

### Uwagi

* Rotacja o `n` pozycji nie zmienia listy, więc wystarczy przesunąć ją o $k \bmod n$ pozycji.

---

## ZAD-13 — Brakujący element w ciągu arytmetycznym

**Poziom:** ★★☆
**Tagi:** `sortowanie`, `ciąg arytmetyczny`, `listy`

### Treść

Wczytaj listę `n` liczb naturalnych. Po uzupełnieniu o **jeden brakujący wyraz** i uporządkowaniu rosnąco elementy listy tworzą ciąg arytmetyczny. Znajdź i wypisz brakujący wyraz.

Brakujący wyraz nie jest ani pierwszym, ani ostatnim wyrazem ciągu (leży między najmniejszym a największym elementem listy). Elementy listy mogą być podane w dowolnej kolejności.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` różnych liczb naturalnych oddzielonych spacjami

### Wyjście

Jedna liczba naturalna: brakujący wyraz ciągu.

### Ograniczenia

* $n \ge 2$
* Różnica ciągu jest dodatnia (elementy są różne).

### Przykład

**Wejście:**

```
4
5 2 1 3
```

**Wyjście:**

```
4
```

Po uzupełnieniu i uporządkowaniu otrzymujemy ciąg $1, 2, 3, 4, 5$.

### Uwagi

* Pełny ciąg ma $n + 1$ wyrazów, od najmniejszego do największego elementu listy. Suma wyrazów ciągu arytmetycznego to $\frac{(a_1 + a_{n+1})(n + 1)}{2}$.

---

## ZAD-14 — Element bez pary

**Poziom:** ★★☆
**Tagi:** `listy`, `zliczanie`

### Treść

Wczytaj listę `n` liczb całkowitych. Każda wartość w liście poza jedną występuje **parzystą** liczbę razy (wszystkie jej wystąpienia da się połączyć w pary), a jedna wartość występuje **nieparzystą** liczbę razy. Znajdź i wypisz tę wartość.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb całkowitych oddzielonych spacjami

### Wyjście

Jedna liczba całkowita: wartość bez pary.

### Ograniczenia

* $n \ge 1$, `n` jest nieparzyste

### Przykład

**Wejście:**

```
7
1 3 1 7 3 1 1
```

**Wyjście:**

```
7
```

Wartość $1$ występuje 4 razy, $3$ — 2 razy, a $7$ — tylko raz.

### Uwagi

* Ciekawostka na później: w rozdziale 16 (operacje bitowe) zobaczysz, że to zadanie da się rozwiązać jednym przejściem po liście operatorem XOR (`^`), bo $x \oplus x = 0$ i $x \oplus 0 = x$.

---

## ZAD-15 — Element dominujący

**Poziom:** ★★☆
**Tagi:** `listy`, `zliczanie`, `pętle`

### Treść

Wczytaj listę `n` liczb naturalnych. Jeśli istnieje wartość, która występuje w liście **więcej niż** $\frac{n}{2}$ razy, wypisz ją. W przeciwnym razie wypisz `-1`.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb naturalnych oddzielonych spacjami

### Wyjście

Jedna liczba: element dominujący albo `-1`.

### Ograniczenia

* $n \ge 1$
* Elementy listy są nieujemne.

### Przykład

**Wejście:**

```
5
4 7 4 4 2
```

**Wyjście:**

```
4
```

Wartość $4$ występuje $3$ razy, a $3 > \frac{5}{2}$.

### Uwagi

* Wartość występująca dokładnie $\frac{n}{2}$ razy nie jest elementem dominującym.
* Wystarczy dla każdego elementu policzyć (pętlą albo metodą `lista.count(x)`), ile razy występuje w liście. Szybszy sposób, ze słownikiem, poznasz w rozdziale 17.

---

## ZAD-16 — Indeksy pierwszej pary o sumie x

**Poziom:** ★★☆
**Tagi:** `listy`, `indeksy`, `pętle zagnieżdżone`

### Treść

Wczytaj listę `n` liczb całkowitych oraz liczbę `x`. Znajdź indeksy `i`, `j` (gdzie $i < j$) takie, że `lista[i] + lista[j] == x`.

Jeśli takich par jest kilka, wybierz tę o najmniejszym `i`, a przy równym `i` — o najmniejszym `j`. Jeśli nie ma żadnej — wypisz `-1 -1`.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb całkowitych oddzielonych spacjami
* 3. linia: liczba całkowita `x`

### Wyjście

Jedna linia: dwie liczby `i j` oddzielone spacją albo `-1 -1`.

### Ograniczenia

* $n \ge 2$

### Przykład

**Wejście:**

```
5
1 3 4 5 2
5
```

**Wyjście:**

```
0 2
```

Sumę $5$ dają pary indeksów $(0, 2)$: $1 + 4$ oraz $(1, 4)$: $3 + 2$. Pierwsza z nich ma mniejsze `i`.

### Uwagi

* Para składa się z dwóch **różnych** pozycji w liście — elementu nie można dodać do samego siebie.
* Wystarczą dwie zagnieżdżone pętle: zewnętrzna po `i`, wewnętrzna po `j` od `i + 1` do końca listy. Szybszy sposób, ze słownikiem, poznasz w rozdziale 17.

---

## ZAD-17 — Wszystkie pary o sumie x (wartości)

**Poziom:** ★★☆
**Tagi:** `listy`, `2-sum`, `pary`

### Treść

Wczytaj listę `n` liczb całkowitych oraz liczbę `x`. Wypisz wszystkie pary **wartości** `a b` (nie indeksów) takie, że $a + b = x$, gdzie `a` i `b` to elementy listy stojące na **różnych** pozycjach.

Każdą parę wartości wypisz tylko raz, mniejszą liczbę jako pierwszą ($a \le b$). Pary uporządkuj rosnąco według `a`.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb całkowitych oddzielonych spacjami
* 3. linia: liczba całkowita `x`

### Wyjście

Każda para w osobnej linii, w formacie `a b`. Jeśli nie ma żadnej pary — program nic nie wypisuje.

### Ograniczenia

* $n \ge 2$

### Przykład

**Wejście:**

```
5
1 2 4 3 7
5
```

**Wyjście:**

```
1 4
2 3
```

### Uwagi

* Para `a a` (dwie takie same wartości) jest poprawna tylko wtedy, gdy wartość `a` występuje w liście co najmniej dwa razy.
* Jeśli jakaś wartość występuje w liście wielokrotnie, ta sama para wartości i tak jest wypisywana tylko raz.

---

## ZAD-18 — Indeks najmniejszego elementu w przesuniętej liście

**Poziom:** ★★☆
**Tagi:** `binarne`, `rotacja`, `minimum`

### Treść

Wczytaj listę `n` różnych liczb całkowitych, która była posortowana rosnąco, a następnie została cyklicznie przesunięta w prawo o nieznaną liczbę miejsc (być może o zero). Znajdź indeks najmniejszego elementu.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` różnych liczb całkowitych oddzielonych spacjami

### Wyjście

Jedna liczba całkowita: indeks najmniejszego elementu.

### Ograniczenia

* $n \ge 1$

### Przykład

**Wejście:**

```
5
7 8 -1 4 5
```

**Wyjście:**

```
2
```

### Uwagi

* Najmniejszy element to jedyne miejsce, w którym kolejny element listy jest mniejszy od poprzedniego. Jeśli takiego miejsca nie ma, lista nie została przesunięta.

---

## ZAD-19 — Wycinki listy

**Poziom:** ★☆☆
**Tagi:** `listy`, `wycinki`, `slicing`

### Treść

Wczytaj listę `n` liczb całkowitych oraz liczbę `k`. Wypisz kolejno:

1. pierwsze `k` elementów listy,
2. ostatnie `k` elementów listy,
3. co drugi element listy, zaczynając od pierwszego (indeksy $0, 2, 4, \ldots$),
4. listę odwróconą,
5. listę bez pierwszego i ostatniego elementu.

Każdą z tych list uzyskaj jednym **wycinkiem** (ang. *slicing*), bez pętli.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb całkowitych oddzielonych spacjami
* 3. linia: liczba `k`

### Wyjście

Pięć linii — listy z punktów 1–5 w tej kolejności, w formacie `print(lista)`.

### Ograniczenia

* $1 \le k \le n$

### Przykład

**Wejście:**

```
6
1 2 3 4 5 6
2
```

**Wyjście:**

```
[1, 2]
[5, 6]
[1, 3, 5]
[6, 5, 4, 3, 2, 1]
[2, 3, 4, 5]
```

### Uwagi

* Wycinek `lista[start:stop]` to nowa lista z elementami o indeksach od `start` do `stop - 1`, np. dla `lista = [10, 20, 30, 40, 50]` wycinek `lista[1:3]` to `[20, 30]`.
* Pominięty `start` oznacza „od początku”, a pominięty `stop` — „do końca”: `lista[2:]` to `[30, 40, 50]`.
* Indeksy ujemne liczymy od końca: `lista[-1]` to ostatni element (`50`), a `lista[-2]` — przedostatni (`40`).
* Trzecia liczba to krok: `lista[start:stop:krok]` bierze co `krok`-ty element, np. `lista[1::3]` to `[20, 50]`. Krok może być ujemny — wtedy elementy są brane od końca.
* Wycinek nigdy nie zmienia oryginalnej listy.

---

## ZAD-20 — Wyrażenia listowe

**Poziom:** ★☆☆
**Tagi:** `listy`, `wyrażenia listowe`, `list comprehension`

### Treść

Wczytaj listę `n` liczb całkowitych i utwórz z niej trzy nowe listy — każdą **jednym wyrażeniem listowym**:

1. `kwadraty` — kwadraty wszystkich elementów (w tej samej kolejności),
2. `ujemne` — tylko elementy ujemne (w kolejności występowania),
3. `etykiety` — dla każdego elementu napis `"P"`, jeśli jest parzysty, albo `"N"`, jeśli jest nieparzysty.

Wypisz te trzy listy.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb całkowitych oddzielonych spacjami

### Wyjście

Trzy linie — listy `kwadraty`, `ujemne` i `etykiety` w formacie `print(lista)`. Lista napisów wypisuje się z apostrofami, np. `['N', 'P']`. Jeśli nie ma elementów ujemnych, druga linia to `[]`.

### Ograniczenia

* $n \ge 1$

### Przykład

**Wejście:**

```
5
3 -2 0 -7 4
```

**Wyjście:**

```
[9, 4, 0, 49, 16]
[-2, -7]
['N', 'P', 'P', 'N', 'P']
```

### Uwagi

* Wyrażenie listowe buduje listę w jednej linii: `[wyrażenie for x in lista]`, np. `[x + 1 for x in [1, 2, 3]]` daje `[2, 3, 4]`. Takiego wyrażenia używa już linia wczytująca listę: `[int(x) for x in input().split()]`.
* **Filtrowanie** — warunek na końcu zostawia tylko pasujące elementy: `[x for x in lista if x > 2]`; dla `[1, 2, 3, 4]` daje `[3, 4]`.
* **Wybór wartości** — wyrażenie `a if warunek else b` na początku wybiera wartość dla każdego elementu: `["duża" if x > 2 else "mała" for x in lista]`; dla `[1, 3]` daje `['mała', 'duża']`.
* Zwróć uwagę na różnicę: `if` na końcu (bez `else`) **usuwa** elementy, a `if … else …` na początku **zamienia** każdy element — lista wynikowa ma wtedy tyle samo elementów co wejściowa.
* `0` jest liczbą parzystą.

### Kod startowy

```python
n = int(input())
lista = [int(x) for x in input().split()]

kwadraty = [...]  # Uzupełnij: kwadraty wszystkich elementów.
ujemne = [...]  # Uzupełnij: tylko elementy ujemne.
etykiety = [...]  # Uzupełnij: "P" dla parzystych, "N" dla nieparzystych.

print(kwadraty)
print(ujemne)
print(etykiety)
```

---

## ZAD-21 — Rzuty kostką z ziarnem

**Poziom:** ★☆☆
**Tagi:** `listy`, `random`, `zliczanie`

### Treść

Zasymuluj `n` rzutów sześcienną kostką do gry i policz, ile razy wypadła każda liczba oczek.

Wczytaj `ziarno` i `n`. Ustaw ziarno generatora liczb losowych instrukcją `random.seed(ziarno)`, a następnie wykonaj `n` rzutów — każdy to jedno wywołanie `random.randint(1, 6)`. Wyniki zliczaj w liście sześciu liczników.

### Wejście

* 1. linia: liczba całkowita `ziarno`
* 2. linia: liczba rzutów `n`

### Wyjście

Sześć linii w formacie `oczka: liczba`, dla oczek od `1` do `6` po kolei — np. `3: 1` oznacza, że trójka wypadła raz.

### Ograniczenia

* $n \ge 0$

### Przykład

**Wejście:**

```
42
10
```

**Wyjście:**

```
1: 3
2: 3
3: 1
4: 0
5: 0
6: 3
```

Dla ziarna `42` kolejne rzuty to: 6, 1, 1, 6, 3, 2, 2, 2, 6, 1.

### Uwagi

* Moduł `random` (dołączany instrukcją `import random`) losuje liczby. `random.randint(a, b)` zwraca losową liczbę całkowitą od `a` do `b` **włącznie**.
* Liczby z komputera są tak naprawdę **pseudolosowe**: wylicza je wzór, który zaczyna od pewnej wartości początkowej — **ziarna**. Po `random.seed(ziarno)` z tym samym ziarnem zawsze otrzymasz ten sam ciąg liczb. Dzięki temu wynik programu da się sprawdzić automatycznie.
* Aby otrzymać dokładnie te same wyniki co sprawdzarka, wywołaj `random.randint(1, 6)` dokładnie `n` razy, po jednym razie na rzut, i nie losuj nic innego.
* `[0] * 6` tworzy listę sześciu zer `[0, 0, 0, 0, 0, 0]`. Wygodnie jest liczyć `k` oczek w elemencie o indeksie `k - 1`.

### Kod startowy

```python
import random

ziarno = int(input())
n = int(input())
random.seed(ziarno)

liczniki = [0] * 6  # liczniki[0] — liczba jedynek, …, liczniki[5] — liczba szóstek
# Uzupełnij: wykonaj n rzutów random.randint(1, 6) i zlicz wyniki.

for oczka in range(1, 7):
    print(f"{oczka}: {liczniki[oczka - 1]}")
```
