# Rozdział 10: Dwie listy i zbiory

Zadania w tym rozdziale ćwiczą jednoczesną pracę na dwóch listach (lub dwóch napisach traktowanych jak ciągi znaków): łączenie, porównywanie, przechodzenie po indeksach i scalanie list posortowanych. Pod koniec rozdziału poznasz **zbiory** (`set`) — kolekcje bez powtórzeń, które pozwalają jednym działaniem wyznaczyć część wspólną, sumę czy różnicę dwóch list — oraz funkcje `zip` i `enumerate`, ułatwiające przechodzenie po dwóch ciągach naraz.

**Konwencje wspólne:**

* Każde zadanie jest osobnym programem: czyta **standardowe wejście** i wypisuje wynik na **standardowe wyjście**.
* Program nie wypisuje komunikatów typu „Podaj listę:”.
* Każda lista zajmuje na wejściu **jedną linię**, a jej elementy są oddzielone pojedynczymi spacjami, np. `5 3 7 2`. Najpierw podana jest lista 1, w następnej linii lista 2. Każda lista ma co najmniej jeden element.
* Listę liczb całkowitych wczytasz tak: `lista = [int(x) for x in input().split()]` (dla liczb zmiennoprzecinkowych użyj `float` zamiast `int`).
* Gdy wynikiem jest lista, wypisz ją tak, jak robi to `print(lista)` w Pythonie: w nawiasach kwadratowych, elementy oddzielone przecinkiem i spacją, np. `[1, 2, 3]`. Pusta lista to `[]`.
* Gdy treść mówi o elementach „oddzielonych przecinkami bez spacji”, wypisz je w jednej linii, np. `5,1,3`, bez przecinka na końcu — np. `print(*lista, sep=",")`.

---

## ZAD-01 — Wypisanie elementów dwóch list na przemian

**Poziom:** ★☆☆
**Tagi:** `listy`, `iteracja`, `indeksy`

### Treść

Wczytaj dwie listy liczb całkowitych i wypisz ich elementy **na przemian**:
pierwszy element listy 1, pierwszy element listy 2, drugi element listy 1, drugi element listy 2 itd.

Jeśli listy mają różne długości, po wyczerpaniu krótszej listy wypisz pozostałe elementy dłuższej listy w ich kolejności.

### Wejście

* 1. linia: lista 1 — liczby całkowite oddzielone spacjami
* 2. linia: lista 2 — liczby całkowite oddzielone spacjami

### Wyjście

Jedna linia: elementy obu list wypisane na przemian, oddzielone przecinkami **bez spacji**.

### Przykład

**Wejście:**

```
5 3 7 2
1 -2 3
```

**Wyjście:**

```
5,1,3,-2,7,3,2
```

---

## ZAD-02 — Połączenie dwóch list

**Poziom:** ★☆☆
**Tagi:** `listy`, `indeksy`, `łączenie`

### Treść

Wczytaj dwie listy liczb całkowitych i utwórz z nich dwie nowe listy:

a) Listę powstałą przez doklejenie listy 2 na koniec listy 1.
b) Kopię listy 1, w której elementy o **parzystych indeksach** (0, 2, 4, …) zastąpiono elementami listy 2 o tych samych indeksach. Element zastępujesz tylko wtedy, gdy indeks istnieje w obu listach — pozostałe elementy listy 1 zostają bez zmian.

Oba podpunkty wykonaj na **oryginalnych** listach z wejścia.

### Wejście

* 1. linia: lista 1 — liczby całkowite oddzielone spacjami
* 2. linia: lista 2 — liczby całkowite oddzielone spacjami

### Wyjście

* 1. linia: wynik podpunktu a) jako lista, np. `[1, 2, 3, 4, 5, 6]`
* 2. linia: wynik podpunktu b) jako lista

### Przykład 1

**Wejście:**

```
1 2 3
4 5 6
```

**Wyjście:**

```
[1, 2, 3, 4, 5, 6]
[4, 2, 6]
```

### Przykład 2

**Wejście:**

```
-2 8 3 6
7 5 0
```

**Wyjście:**

```
[-2, 8, 3, 6, 7, 5, 0]
[7, 8, 0, 6]
```

Indeksy parzyste listy 1 to 0 i 2 — ich wartości (`-2` i `3`) zastępujemy wartościami `7` i `0` z listy 2.

---

## ZAD-03 — Suma elementów dwóch list

**Poziom:** ★☆☆
**Tagi:** `listy`, `iteracja`, `indeksy`

### Treść

Wczytaj dwie listy liczb całkowitych i utwórz listę, w której element o indeksie `i` jest sumą elementów o indeksie `i` z obu list.
Jeśli któraś lista jest krótsza, jej brakujące elementy traktuj jak `0` (wynik ma więc długość dłuższej listy).

### Wejście

* 1. linia: lista 1 — liczby całkowite oddzielone spacjami
* 2. linia: lista 2 — liczby całkowite oddzielone spacjami

### Wyjście

Jedna linia: lista sum, np. `[5, 9, 8, 10]`.

### Przykład

**Wejście:**

```
3 1 2 5
2 8 6 5
```

**Wyjście:**

```
[5, 9, 8, 10]
```

---

## ZAD-04 — Iloczyn skalarny dwóch wektorów 3D

**Poziom:** ★☆☆
**Tagi:** `listy`, `wektory`, `matematyka`

### Treść

Wczytaj dwa wektory w przestrzeni trójwymiarowej, $A = [A_x, A_y, A_z]$ oraz $B = [B_x, B_y, B_z]$, i oblicz ich **iloczyn skalarny**:
$A \cdot B = A_x B_x + A_y B_y + A_z B_z$.

### Wejście

* 1. linia: wektor $A$ — trzy liczby całkowite oddzielone spacjami
* 2. linia: wektor $B$ — trzy liczby całkowite oddzielone spacjami

### Wyjście

Jedna linia: iloczyn skalarny (liczba całkowita).

### Przykład

**Wejście:**

```
1 2 3
3 1 2
```

**Wyjście:**

```
11
```

$1 \cdot 3 + 2 \cdot 1 + 3 \cdot 2 = 11$.

---

## ZAD-05 — Obliczenie średniej ważonej

**Poziom:** ★☆☆
**Tagi:** `listy`, `float`, `średnia`

### Treść

Wczytaj dwie listy liczb zmiennoprzecinkowych tej samej długości: listę wartości $x_1, x_2, \ldots, x_n$ oraz listę odpowiadających im wag $w_1, w_2, \ldots, w_n$.
Oblicz średnią ważoną wartości:
$\frac{x_1 w_1 + x_2 w_2 + \ldots + x_n w_n}{w_1 + w_2 + \ldots + w_n}$.

### Wejście

* 1. linia: wartości — liczby zmiennoprzecinkowe oddzielone spacjami
* 2. linia: wagi — liczby zmiennoprzecinkowe oddzielone spacjami (tyle samo co wartości)

### Wyjście

Jedna linia: średnia ważona zaokrąglona do **2 miejsc po przecinku** (np. `0.29`, `7.50`).

### Ograniczenia

* Wagi są nieujemne, a ich suma jest większa od zera.

### Przykład

**Wejście:**

```
0.2 0.4 0.1 0.2 0.1
2.0 5.0 0.0 2.0 1.0
```

**Wyjście:**

```
0.29
```

$\frac{0.2 \cdot 2 + 0.4 \cdot 5 + 0.1 \cdot 0 + 0.2 \cdot 2 + 0.1 \cdot 1}{2 + 5 + 0 + 2 + 1} = \frac{2.9}{10} = 0.29$.

### Uwagi

* Wynik sformatujesz np. tak: `print(f"{wynik:.2f}")`.

---

## ZAD-06 — Znalezienie elementów wspólnych dwóch list

**Poziom:** ★☆☆
**Tagi:** `listy`, `część wspólna`

### Treść

Wczytaj dwie listy liczb całkowitych i utwórz listę elementów, które występują **w obu** listach.

* Elementy wyniku ustaw w kolejności ich pierwszego wystąpienia w liście 1.
* Każdy element wspólny umieść w wyniku **tylko raz**, nawet jeśli w listach się powtarza.
* Jeśli listy nie mają elementów wspólnych, wypisz `[]`.

### Wejście

* 1. linia: lista 1 — liczby całkowite oddzielone spacjami
* 2. linia: lista 2 — liczby całkowite oddzielone spacjami

### Wyjście

Jedna linia: lista elementów wspólnych.

### Przykład

**Wejście:**

```
9 2 5 4
4 2 1
```

**Wyjście:**

```
[2, 4]
```

---

## ZAD-07 — Różnica między dwoma listami

**Poziom:** ★☆☆
**Tagi:** `listy`, `różnica symetryczna`

### Treść

Wczytaj dwie listy liczb całkowitych i utwórz listę elementów, które występują **tylko w jednej** z list (tzw. różnica symetryczna).

* Najpierw umieść elementy listy 1, których nie ma w liście 2 (w kolejności z listy 1), a potem elementy listy 2, których nie ma w liście 1 (w kolejności z listy 2).
* Każdy element umieść w wyniku **tylko raz**, nawet jeśli w liście się powtarza.
* Jeśli takich elementów nie ma, wypisz `[]`.

### Wejście

* 1. linia: lista 1 — liczby całkowite oddzielone spacjami
* 2. linia: lista 2 — liczby całkowite oddzielone spacjami

### Wyjście

Jedna linia: lista elementów występujących tylko w jednej z list.

### Przykład

**Wejście:**

```
9 2 5 4
4 2 1
```

**Wyjście:**

```
[9, 5, 1]
```

---

## ZAD-08 — Połącz posortowane listy w posortowaną listę bez duplikatów

**Poziom:** ★★☆
**Tagi:** `listy`, `scalanie`, `sortowanie`

### Treść

Wczytaj dwie listy liczb całkowitych, każdą **posortowaną niemalejąco**, i scal je w jedną listę, która:

* jest posortowana rosnąco,
* zawiera każdą wartość **tylko raz** (bez duplikatów — także tych, które powtarzają się w obrębie jednej listy).

Wykorzystaj to, że listy wejściowe są już posortowane: przechodź jednocześnie po obu listach i za każdym razem dobieraj mniejszy z dwóch bieżących elementów.

### Wejście

* 1. linia: lista 1 (posortowana niemalejąco) — liczby całkowite oddzielone spacjami
* 2. linia: lista 2 (posortowana niemalejąco) — liczby całkowite oddzielone spacjami

### Wyjście

Jedna linia: scalona, posortowana lista bez duplikatów.

### Przykład

**Wejście:**

```
2 4 7
3 5 9
```

**Wyjście:**

```
[2, 3, 4, 5, 7, 9]
```

---

## ZAD-09 — Usuń z pierwszej listy część wspólną obu list

**Poziom:** ★★☆
**Tagi:** `listy`, `filtrowanie`

### Treść

Wczytaj dwie listy liczb całkowitych. Usuń z listy 1 **wszystkie** elementy (także powtórzenia), które występują w liście 2.

* Zachowaj kolejność pozostałych elementów listy 1.
* Jeśli usunięte zostaną wszystkie elementy, wypisz `[]`.

### Wejście

* 1. linia: lista 1 — liczby całkowite oddzielone spacjami
* 2. linia: lista 2 — liczby całkowite oddzielone spacjami

### Wyjście

Jedna linia: lista 1 po usunięciu elementów występujących w liście 2.

### Przykład

**Wejście:**

```
9 2 5 4
4 2 1
```

**Wyjście:**

```
[9, 5]
```

### Uwagi

* Uważaj na usuwanie elementów z listy podczas przechodzenia po niej pętlą `for` — łatwo wtedy pominąć element. Bezpieczniej zbudować nową listę z elementów, które zostają.

---

## ZAD-10 — Mediana dwóch posortowanych list

**Poziom:** ★★☆
**Tagi:** `listy`, `mediana`, `scalanie`

### Treść

Wczytaj dwie listy liczb całkowitych. Obie są posortowane niemalejąco i mają **tę samą** długość $n \ge 1$.

Znajdź medianę wszystkich $2n$ liczb z obu list. Ponieważ liczb jest parzyście wiele, mediana to średnia arytmetyczna dwóch środkowych wartości po ustawieniu wszystkich liczb w kolejności niemalejącej.

### Wejście

* 1. linia: lista 1 (posortowana niemalejąco) — liczby całkowite oddzielone spacjami
* 2. linia: lista 2 (posortowana niemalejąco, tej samej długości) — liczby całkowite oddzielone spacjami

### Wyjście

Jedna linia: mediana jako liczba zmiennoprzecinkowa, np. `4.5`. Jeśli mediana jest liczbą całkowitą, wypisz ją z `.0`, np. `4.0`.

### Przykład

**Wejście:**

```
2 4 7
3 5 9
```

**Wyjście:**

```
4.5
```

Po scaleniu otrzymujemy `[2, 3, 4, 5, 7, 9]`; dwie środkowe wartości to `4` i `5`, więc mediana wynosi $\frac{4 + 5}{2} = 4.5$.

---

## ZAD-11 — Operacje na zbiorach

**Poziom:** ★☆☆
**Tagi:** `zbiory`, `set`, `listy`

### Treść

Wczytaj dwie listy liczb całkowitych i zamień każdą z nich na zbiór: $A$ (z listy 1) i $B$ (z listy 2). Powtórzenia elementów w listach znikają, bo zbiór przechowuje każdą wartość tylko raz.

Wypisz:

1. sumę zbiorów $A \cup B$ (elementy należące do $A$ lub do $B$),
2. część wspólną $A \cap B$ (elementy należące do $A$ i do $B$),
3. różnicę $A \setminus B$ (elementy $A$, których nie ma w $B$),
4. różnicę symetryczną (elementy należące do dokładnie jednego ze zbiorów),
5. odpowiedź na pytanie, czy $A$ jest podzbiorem $B$ (czy każdy element $A$ należy do $B$).

### Wejście

* 1. linia: lista 1 — liczby całkowite oddzielone spacjami
* 2. linia: lista 2 — liczby całkowite oddzielone spacjami

### Wyjście

Pięć linii:

* linie 1–4: wyniki działań 1–4 jako listy posortowane rosnąco, wypisane przez `print(sorted(...))`, np. `[1, 2, 5]`; pusty wynik to `[]`,
* linia 5: `Tak`, jeśli $A$ jest podzbiorem $B$, w przeciwnym razie `Nie`.

### Przykład 1

**Wejście:**

```
1 2 3 4 2
3 4 5
```

**Wyjście:**

```
[1, 2, 3, 4, 5]
[3, 4]
[1, 2]
[1, 2, 5]
Nie
```

### Przykład 2

**Wejście:**

```
2 2 1
1 2 3
```

**Wyjście:**

```
[1, 2, 3]
[1, 2]
[]
[3]
Tak
```

### Uwagi

* Zbiór tworzysz z listy funkcją `set`, np. `set([2, 2, 1])` to zbiór `{1, 2}`.
* Działania na zbiorach w Pythonie: `A | B` (suma), `A & B` (część wspólna), `A - B` (różnica), `A ^ B` (różnica symetryczna), `A <= B` (czy $A$ jest podzbiorem $B$ — wynik `True` lub `False`).
* Zbiór nie pamięta kolejności elementów, dlatego przed wypisaniem zamień go na posortowaną listę: `sorted(A | B)`.

---

## ZAD-12 — Sprawdzanie testu (zip, enumerate)

**Poziom:** ★☆☆
**Tagi:** `zip`, `enumerate`, `napisy`

### Treść

Uczeń rozwiązał test wyboru. Wczytaj klucz poprawnych odpowiedzi oraz odpowiedzi ucznia — oba jako napisy, w których znak na pozycji `i` to odpowiedź na pytanie `i + 1` (np. `ABCDA` oznacza: pytanie 1 — `A`, pytanie 2 — `B` itd.).

Dla każdego pytania wypisz, czy uczeń odpowiedział poprawnie, a na końcu podsumuj wynik.

### Wejście

* 1. linia: klucz odpowiedzi — napis z wielkich liter `A`–`E`, bez spacji
* 2. linia: odpowiedzi ucznia — napis tej samej długości co klucz, z wielkich liter `A`–`E`

### Wyjście

* Dla każdego pytania (numerowanych od 1) jedna linia:
  * `nr: OK` — gdy odpowiedź jest poprawna,
  * `nr: źle (poprawna: X)` — gdy jest błędna, gdzie `X` to poprawna odpowiedź z klucza.
* Ostatnia linia: `Wynik: p/n (q%)`, gdzie `p` to liczba poprawnych odpowiedzi, `n` — liczba pytań, a `q` — procent poprawnych odpowiedzi z **jedną cyfrą po przecinku** (np. `80.0`, `66.7`).

### Przykład

**Wejście:**

```
ABCDA
ACCDA
```

**Wyjście:**

```
1: OK
2: źle (poprawna: B)
3: OK
4: OK
5: OK
Wynik: 4/5 (80.0%)
```

### Uwagi

* `zip(a, b)` łączy dwa ciągi w pary kolejnych elementów: `zip("AB", "AC")` daje pary `("A", "A")` i `("B", "C")`.
* `enumerate(ciag, start=1)` dodaje do każdego elementu jego numer, licząc od 1: `enumerate("XY", start=1)` daje pary `(1, "X")` i `(2, "Y")`.
* Razem:

  ```python
  for nr, (poprawna, udzielona) in enumerate(zip(klucz, odpowiedzi), start=1):
      ...
  ```

* Procent sformatujesz tak: `f"{procent:.1f}"`.

---

## ZAD-13 — Poprawność numeru PESEL

**Poziom:** ★★☆
**Tagi:** `zip`, `cyfra kontrolna`, `napisy`

### Treść

Numer PESEL składa się z 11 cyfr $c_1 c_2 \ldots c_{11}$. Ostatnia cyfra $c_{11}$ jest **cyfrą kontrolną**: mnożymy pierwsze 10 cyfr przez wagi `1 3 7 9 1 3 7 9 1 3`, sumujemy iloczyny, a cyfra kontrolna to

$c_{11} = (10 - S \bmod 10) \bmod 10$, gdzie $S = 1 \cdot c_1 + 3 \cdot c_2 + 7 \cdot c_3 + 9 \cdot c_4 + 1 \cdot c_5 + 3 \cdot c_6 + 7 \cdot c_7 + 9 \cdot c_8 + 1 \cdot c_9 + 3 \cdot c_{10}$.

Dziesiąta cyfra $c_{10}$ oznacza płeć: parzysta — kobieta, nieparzysta — mężczyzna.

Wczytaj napis i sprawdź, czy jest poprawnym numerem PESEL, czyli czy:

* ma dokładnie 11 znaków,
* każdy znak jest cyfrą,
* cyfra kontrolna zgadza się z wyliczoną ze wzoru.

Dla poprawnego numeru wypisz dodatkowo płeć. **Nie sprawdzaj** poprawności daty urodzenia zapisanej w numerze (cyfry 1–6).

### Wejście

* 1. linia: napis bez spacji (może zawierać znaki niebędące cyframi i mieć dowolną długość)

### Wyjście

* Dla poprawnego numeru dwie linie: `Poprawny`, a w drugiej `kobieta` lub `mężczyzna`.
* W przeciwnym razie jedna linia: `Niepoprawny`.

### Przykład 1

**Wejście:**

```
44051401359
```

**Wyjście:**

```
Poprawny
mężczyzna
```

$S = 1 \cdot 4 + 3 \cdot 4 + 7 \cdot 0 + 9 \cdot 5 + 1 \cdot 1 + 3 \cdot 4 + 7 \cdot 0 + 9 \cdot 1 + 1 \cdot 3 + 3 \cdot 5 = 101$, więc cyfra kontrolna to $(10 - 1) \bmod 10 = 9$ — zgadza się. Dziesiąta cyfra `5` jest nieparzysta.

### Przykład 2

**Wejście:**

```
44051401358
```

**Wyjście:**

```
Niepoprawny
```

### Uwagi

* To, czy znak jest cyfrą, sprawdzisz warunkiem `znak in "0123456789"`, a cyfrę zamienisz na liczbę przez `int(znak)`.
* Wagi zapisz w liście `[1, 3, 7, 9, 1, 3, 7, 9, 1, 3]` i przejdź po parach (cyfra, waga) za pomocą `zip(numer, wagi)` — `zip` kończy na krótszym ciągu, więc weźmie tylko 10 pierwszych cyfr.
