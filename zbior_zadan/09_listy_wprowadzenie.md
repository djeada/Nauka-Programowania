# Rozdział: Listy — Wprowadzenie

Poniższe zadania polegają na wczytywaniu danych ze **standardowego wejścia** (stdin) i wypisywaniu wyniku na **standardowe wyjście** (stdout).
**Każde zadanie (oraz każdy podpunkt w zadaniach wieloczęściowych) jest osobnym, niezależnym programem.**

**Konwencje wspólne:**

* Jeśli w danych wejściowych są liczby w osobnych liniach — wczytuj je dokładnie w tej kolejności.
* Jeśli w danych wyjściowych jest „elementy oddzielone przecinkami” — użyj przecinka **bez spacji**.
* Jeśli w danych wyjściowych jest „oddzielone spacją” — użyj pojedynczej spacji.
* Nie wypisuj promptów typu „Podaj N”.

---

## ZAD-01 — Wczytaj i wypisz

**Poziom:** ★☆☆
**Tagi:** `listy`, `I/O`, `odwracanie`

### Treść

Wczytaj `N`, następnie `N` liczb całkowitych do listy.

a) Wypisz elementy listy od początku do końca — każdy w osobnej linii.
b) Wypisz elementy listy od końca do początku — w **jednej** linii, oddzielone przecinkami (bez spacji).

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite

### Wyjście

a) `N` linii — elementy w kolejności wczytania.
b) 1 linia — elementy w kolejności odwrotnej, oddzielone przecinkami.

### Przykład

**Wejście:**

```
3
8
12
7
```

**Wyjście:**

```
8
12
7
7,12,8
```

### Uwagi o formatowaniu

* W podpunkcie (b) nie dodawaj przecinka na końcu.

---

## ZAD-02 — Wczytaj, zmodyfikuj i wypisz

**Poziom:** ★☆☆
**Tagi:** `listy`, `indeksy`, `modyfikacja`

### Treść

Wczytaj `N` oraz `N` liczb całkowitych do listy. Następnie:

a) Zwiększ każdy element o `1`.
b) Pomnóż każdy element przez jego indeks (indeksy od `0`).
c) Zastąp wszystkie elementy wartością pierwszego elementu.

Po każdym podpunkcie wypisz wynikową listę w **jednej** linii, elementy oddzielone przecinkami.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite

### Wyjście

Trzy linie:

1. wynik po (a)
2. wynik po (b)
3. wynik po (c)

Elementy w linii oddzielone przecinkami (bez spacji).

### Przykład

**Wejście:**

```
3
3
9
7
```

**Wyjście:**

```
4,10,8
0,9,14
3,3,3
```

---

## ZAD-03 — Pierwsze wystąpienie klucza

**Poziom:** ★☆☆
**Tagi:** `listy`, `wyszukiwanie`, `indeksy`

### Treść

Wczytaj listę liczb całkowitych oraz liczbę `klucz`. Wypisz indeks pierwszego wystąpienia `klucz` w liście.
Jeśli `klucz` nie występuje — wypisz `-1`.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite
* ostatnia linia: `klucz` (liczba całkowita)

### Wyjście

Jedna liczba całkowita — indeks (od `0`) lub `-1`.

### Przykład

**Wejście:**

```
5
2
9
-1
3
8
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

Wczytaj `N` liczb całkowitych. Wypisz:

1. największą liczbę w liście
2. najmniejszą liczbę w liście

w jednej linii, oddzielone pojedynczą spacją.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite

### Wyjście

Jedna linia:

* `max min`

### Przykład

**Wejście:**

```
9
4
-7
8
5
6
-9
10
2
-8
```

**Wyjście:**

```
10 -9
```

---

## ZAD-05 — Zmodyfikuj elementy spełniające warunek

**Poziom:** ★☆☆
**Tagi:** `listy`, `warunki`, `liczby pierwsze`

### Treść

Wczytaj listę liczb całkowitych. Dla każdego podpunktu utwórz **nową listę** na podstawie listy z poprzedniego podpunktu i wypisz ją w jednej linii (przecinki bez spacji):

a) Zwiększ o 1 elementy o **parzystych indeksach** (0,2,4,...).
b) Ustaw na `0` elementy będące **wielokrotnością 3**.
c) Podnieś do kwadratu elementy **mniejsze niż 10**.
d) Oblicz sumę wszystkich elementów listy i wstaw tę sumę na indeksy, które są **liczbami pierwszymi** (2,3,5,7,11,...) — tylko te, które mieszczą się w zakresie listy.
e) Zamień każdy element na **iloczyn wszystkich pozostałych elementów** listy.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite

### Wyjście

Pięć linii (po kolei: a, b, c, d, e), w każdej lista oddzielona przecinkami.

### Przykład

**Wejście:**

```
5
5
7
9
4
2
```

**Wyjście:**

```
6,7,10,4,3
6,7,0,4,3
36,49,0,16,9
36,49,36,36,9
0,0,0,0,0
```

### Uwagi o formatowaniu

* W podpunkcie (d) indeks 0 i 1 nie są pierwsze.
* W podpunkcie (e) jeśli w liście jest `0`, to wiele wyników będzie `0` — to normalne.
* Nie dodawaj przecinków na końcu linii.

---

## ZAD-06 — Czy średnia elementów znajduje się w liście?

**Poziom:** ★☆☆
**Tagi:** `listy`, `średnia`, `wyszukiwanie`

### Treść

Wczytaj listę liczb całkowitych. Oblicz średnią arytmetyczną elementów i sprawdź, czy ta średnia jest **dokładnie** jednym z elementów listy.

Wypisz:

* `Tak` — jeśli średnia występuje w liście,
* `Nie` — w przeciwnym razie.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite

### Wyjście

Jedno słowo: `Tak` lub `Nie`.

### Przykład

**Wejście:**

```
5
6
2
1
4
27
```

**Wyjście:**

```
Nie
```

### Uwagi

* Średnia może być ułamkiem — wtedy na pewno nie znajduje się w liście liczb całkowitych.

---

## ZAD-07 — Średnia dwóch największych liczb

**Poziom:** ★☆☆
**Tagi:** `listy`, `max`, `sortowanie`, `float`

### Treść

Wczytaj `N` liczb naturalnych (`N ≥ 2`). Znajdź największą i drugą największą wartość, a następnie wypisz ich średnią arytmetyczną jako liczbę zmiennoprzecinkową z dokładnością do **jednego** miejsca po przecinku.

### Wejście

* 1. linia: `N` (`N ≥ 2`)
* kolejne `N` linii: liczby naturalne

### Wyjście

Jedna liczba zmiennoprzecinkowa w formacie `%.1f`.

### Przykład

**Wejście:**

```
6
9
2
3
2
1
7
```

**Wyjście:**

```
8.0
```

---

## ZAD-08 — Usuń klucz

**Poziom:** ★☆☆
**Tagi:** `listy`, `remove`, `wyszukiwanie`

### Treść

Wczytaj listę liczb całkowitych oraz `klucz`. Usuń **pierwsze** wystąpienie `klucz` (jeśli istnieje). Następnie wypisz listę po modyfikacji w jednej linii, elementy oddzielone przecinkami.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite
* ostatnia linia: `klucz` (liczba całkowita)

### Wyjście

Jedna linia: lista po usunięciu, elementy oddzielone przecinkami.

### Przykład

**Wejście:**

```
5
6
2
1
4
27
4
```

**Wyjście:**

```
6,2,1,27
```

### Uwagi

* Jeśli `klucz` nie występuje, wypisz listę bez zmian.

---

## ZAD-09 — Usuń duplikaty (z zachowaniem kolejności)

**Poziom:** ★☆☆
**Tagi:** `listy`, `duplikaty`, `set`

### Treść

Wczytaj listę liczb naturalnych i usuń duplikaty tak, aby każda liczba występowała tylko raz — **zachowując kolejność pierwszego wystąpienia**.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby naturalne

### Wyjście

Jedna linia: lista bez duplikatów, elementy oddzielone przecinkami.

### Przykład

**Wejście:**

```
6
3
2
1
3
2
2
```

**Wyjście:**

```
3,2,1
```

---

## ZAD-10 — Czy punkty mogą być wierzchołkami trójkąta?

**Poziom:** ★★☆
**Tagi:** `geometria`, `warunki`, `listy`

### Treść

Wczytaj współrzędne trzech punktów `A(xA, yA)`, `B(xB, yB)`, `C(xC, yC)`.
Wypisz `Tak`, jeśli punkty **nie są współliniowe** (mogą tworzyć trójkąt), w przeciwnym razie `Nie`.

### Wejście

Sześć liczb całkowitych (każda w osobnej linii):

1. `xA`
2. `yA`
3. `xB`
4. `yB`
5. `xC`
6. `yC`

### Wyjście

Jedno słowo: `Tak` lub `Nie`.

### Przykład

**Wejście:**

```
-3
-2
-3
1
-3
0
```

**Wyjście:**

```
Nie
```

### Uwagi

* Sprawdź pole trójkąta: jeśli równe `0`, punkty są współliniowe.

---

## ZAD-11 — Samochody jadące w przeciwnych kierunkach

**Poziom:** ★★☆
**Tagi:** `listy`, `zliczanie`, `string`

### Treść

Wczytaj `N` oraz napis długości `N` złożony z liter `A` i `B`:

* `A` oznacza samochód jadący na wschód,
* `B` oznacza samochód jadący na zachód.

Policz, ile par samochodów minie się, gdy uznamy, że para mija się wtedy, gdy `A` stoi **przed** `B` w ciągu.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* 2. linia: napis długości `N`, tylko `A` i `B` (bez spacji)

### Wyjście

Jedna liczba naturalna — liczba mijających się par.

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

---

## ZAD-12 — Rotacja w lewo / prawo

**Poziom:** ★★☆
**Tagi:** `listy`, `rotacja`, `modulo`

### Treść

Wczytaj listę liczb całkowitych, a następnie:

* `kierunek = 0` → rotacja w lewo,
* `kierunek = 1` → rotacja w prawo,

o `K` pozycji (gdzie `K ≥ 0`). Wypisz listę po rotacji, przecinkami bez spacji.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite
* kolejna linia: `kierunek` (0 lub 1)
* ostatnia linia: `K` (`K ≥ 0`)

### Wyjście

Jedna linia: lista po rotacji, elementy oddzielone przecinkami.

### Przykład

**Wejście:**

```
7
5
27
6
2
1
10
8
0
2
```

**Wyjście:**

```
6,2,1,10,8,5,27
```

### Uwagi

* Zredukuj `K` przez `K % N`.

---

## ZAD-13 — Brakujący element w ciągu arytmetycznym

**Poziom:** ★★☆
**Tagi:** `sortowanie`, `ciąg arytmetyczny`, `listy`

### Treść

Wczytaj `N` liczb naturalnych. Lista jest fragmentem ciągu arytmetycznego z **jednym brakującym elementem**. Znajdź i wypisz brakującą wartość.

### Wejście

* 1. linia: `N` (`N ≥ 2`)
* kolejne `N` linii: liczby naturalne

### Wyjście

Jedna liczba naturalna — brakujący element.

### Przykład

**Wejście:**

```
4
5
2
1
3
```

**Wyjście:**

```
4
```

---

## ZAD-14 — Element bez pary

**Poziom:** ★★☆
**Tagi:** `XOR`, `listy`, `zliczanie`

### Treść

Wczytaj listę liczb całkowitych o nieparzystej długości: wszystkie liczby poza jedną występują dokładnie dwa razy. Znajdź liczbę bez pary.

### Wejście

* 1. linia: `N` (nieparzyste, `N ≥ 1`)
* kolejne `N` linii: liczby całkowite

### Wyjście

Jedna liczba całkowita — element bez pary.

### Przykład

**Wejście:**

```
7
1
3
1
7
3
1
1
```

**Wyjście:**

```
7
```

---

## ZAD-15 — Element dominujący

**Poziom:** ★★☆
**Tagi:** `zliczanie`, `dict`, `majority`

### Treść

Wczytaj listę liczb naturalnych. Jeśli istnieje liczba, która występuje **więcej niż N/2 razy**, wypisz ją. W przeciwnym razie wypisz `-1`.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby naturalne

### Wyjście

Jedna liczba naturalna — element dominujący lub `-1`.

### Przykład

**Wejście:**

```
5
4
7
4
4
2
```

**Wyjście:**

```
4
```

---

## ZAD-16 — Indeksy pierwszej pary o sumie x

**Poziom:** ★★☆
**Tagi:** `hashmap`, `indeksy`, `2-sum`

### Treść

Wczytaj listę liczb całkowitych oraz liczbę `x`. Znajdź indeksy **pierwszej** pary `(i, j)` (z `i < j`) takiej, że `lista[i] + lista[j] == x`.

Jeśli nie istnieje taka para — wypisz `-1 -1`.

### Wejście

* 1. linia: `N` (`N ≥ 2`)
* kolejne `N` linii: liczby całkowite
* ostatnia linia: `x` (liczba całkowita)

### Wyjście

Dwie liczby całkowite w jednej linii (oddzielone spacją): `i j` albo `-1 -1`.

### Przykład

**Wejście:**

```
5
1
3
4
5
2
5
```

**Wyjście:**

```
0 2
```

---

## ZAD-17 — Wszystkie pary o sumie x (wartości)

**Poziom:** ★★☆
**Tagi:** `listy`, `2-sum`, `pary`

### Treść

Wczytaj listę liczb całkowitych oraz `x`. Wypisz wszystkie pary **wartości** `(a, b)` z listy (nie indeksy), takie że `a + b == x`. Każdą parę wypisz w osobnej linii jako:
`a b`

Każdą parę wypisz tylko raz (nie dubluj `(a,b)` i `(b,a)`).

### Wejście

* 1. linia: `N` (`N ≥ 2`)
* kolejne `N` linii: liczby całkowite
* ostatnia linia: `x` (liczba całkowita)

### Wyjście

Wiele linii — po jednej parze na linię.
Jeśli brak par — brak wyjścia.

### Przykład

**Wejście:**

```
5
1
2
4
3
7
5
```

**Wyjście:**

```
1 4
2 3
```

---

## ZAD-18 — Indeks najmniejszego elementu w przesuniętej liście

**Poziom:** ★★☆
**Tagi:** `binarne`, `rotacja`, `minimum`

### Treść

Wczytaj listę liczb całkowitych, która była posortowana rosnąco i została przesunięta w prawo o nieznaną liczbę miejsc. Znajdź indeks najmniejszego elementu.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite

### Wyjście

Jedna liczba całkowita — indeks najmniejszego elementu (od `0`).

### Przykład

**Wejście:**

```
5
7
8
-1
4
5
```

**Wyjście:**

```
2
```
