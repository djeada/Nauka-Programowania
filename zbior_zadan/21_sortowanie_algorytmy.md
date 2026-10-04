# Rozdział 21: Sortowanie i wyszukiwanie — algorytmy

Zadania w tym rozdziale polegają na samodzielnym zaimplementowaniu klasycznych algorytmów sortowania i wyszukiwania. Żeby było widać, że program naprawdę wykonuje dany algorytm, w każdym zadaniu wypisujesz **stany pośrednie** — listę po kolejnych krokach algorytmu albo kolejno sprawdzane pozycje.

**Konwencje wspólne:**

* Każde zadanie to osobny program: czyta **standardowe wejście** i wypisuje wynik na **standardowe wyjście**.
* Wejście ma zawsze tę samą postać: w 1. linii liczba elementów $n$, w 2. linii $n$ liczb całkowitych oddzielonych spacjami. Jeśli algorytm potrzebuje dodatkowej wartości (np. szukanego klucza), znajduje się ona w 3. linii.
* Listę wypisuj w formacie Pythona — dokładnie tak, jak robi to `print(lista)`, np. `[1, 2, 4, 6, 27]`.
* Sortujemy zawsze **rosnąco** (niemalejąco — liczby mogą się powtarzać).
* **Zaimplementuj algorytm samodzielnie.** Nie używaj `sorted()`, `list.sort()`, `list.index()`, operatora `in` na liście ani innych gotowych funkcji sortujących i wyszukujących.
* Program nie wypisuje komunikatów typu „Podaj liczbę:”.

---

## ZAD-01 — Sortowanie bąbelkowe

**Poziom:** ★☆☆
**Tagi:** `sorting`, `bubble-sort`, `list`

### Treść

Napisz funkcję `sortowanie_babelkowe(lista)`, która sortuje listę rosnąco (w miejscu) algorytmem **sortowania bąbelkowego**.

Algorytm wykonuje kolejne **przebiegi**. W jednym przebiegu porównuje kolejne pary sąsiednich elementów — na pozycjach $(0, 1)$, $(1, 2)$, $(2, 3)$, … — i zamienia je miejscami, jeśli lewy element jest **większy** od prawego. Przebiegi powtarza tak długo, aż w całym przebiegu nie zajdzie żadna zamiana — wtedy lista jest posortowana i algorytm się kończy.

Po każdym przebiegu (także po ostatnim, w którym nie było już żadnej zamiany) funkcja wypisuje aktualny stan listy.

### Wejście

* 1. linia: liczba całkowita $n$ — liczba elementów
* 2. linia: $n$ liczb całkowitych oddzielonych spacjami

### Wyjście

Stan listy po każdym przebiegu — każdy w osobnej linii, w formacie listy Pythona. Ostatnia linia to lista posortowana.

### Ograniczenia

* $2 \le n \le 20$
* Elementy są liczbami całkowitymi z przedziału $[-1000, 1000]$.

### Przykład

**Wejście:**

```
5
6 2 1 4 27
```

**Wyjście:**

```
[2, 1, 4, 6, 27]
[1, 2, 4, 6, 27]
[1, 2, 4, 6, 27]
```

W 1. przebiegu zamieniane są pary $(6, 2)$, $(6, 1)$ i $(6, 4)$; w 2. przebiegu para $(2, 1)$; w 3. przebiegu nie ma żadnej zamiany, więc algorytm się kończy.

### Uwagi o algorytmie

* Po każdym przebiegu największy z nieposortowanych elementów „wypływa” na swoje miejsce na końcu listy, dlatego w kolejnych przebiegach możesz zmniejszać zakres sprawdzania o 1 — nie zmienia to wypisywanych stanów.
* Złożoność czasowa: $O(n^2)$, a dla listy już posortowanej — tylko jeden przebieg, czyli $O(n)$.

### Kod startowy

```python
def sortowanie_babelkowe(lista):
    # Uzupełnij: sortuj listę w miejscu; po każdym przebiegu wypisz print(lista).
    pass


n = int(input())
lista = [int(x) for x in input().split()]
sortowanie_babelkowe(lista)
```

---

## ZAD-02 — Sortowanie przez wybieranie

**Poziom:** ★★☆
**Tagi:** `sorting`, `selection-sort`, `list`

### Treść

Napisz funkcję `sortowanie_przez_wybieranie(lista)`, która sortuje listę rosnąco (w miejscu) algorytmem **sortowania przez wybieranie**.

Dla każdej pozycji $i = 0, 1, \dots, n-2$:

1. znajdź najmniejszy element we fragmencie od pozycji $i$ do końca listy — jeśli najmniejsza wartość występuje w nim kilka razy, wybierz jej **pierwsze** wystąpienie (o najmniejszym indeksie),
2. zamień ten element z elementem na pozycji $i$ (jeśli to ta sama pozycja, lista się nie zmienia),
3. wypisz aktualny stan listy.

### Wejście

* 1. linia: liczba całkowita $n$ — liczba elementów
* 2. linia: $n$ liczb całkowitych oddzielonych spacjami

### Wyjście

$n - 1$ linii: stan listy po każdym kroku $i$, w formacie listy Pythona. Ostatnia linia to lista posortowana.

### Ograniczenia

* $2 \le n \le 20$
* Elementy są liczbami całkowitymi z przedziału $[-1000, 1000]$.

### Przykład

**Wejście:**

```
5
6 2 1 4 27
```

**Wyjście:**

```
[1, 2, 6, 4, 27]
[1, 2, 6, 4, 27]
[1, 2, 4, 6, 27]
[1, 2, 4, 6, 27]
```

Krok $i = 0$: najmniejszy element to `1` — zamieniamy go z `6`. Krok $i = 1$: najmniejszy z `[2, 6, 4, 27]` to `2`, stoi już na swoim miejscu. Krok $i = 2$: zamieniamy `4` z `6`.

### Uwagi o algorytmie

* Po kroku $i$ na pozycjach $0, \dots, i$ stoją już najmniejsze elementy listy w kolejności rosnącej.
* Złożoność czasowa: $O(n^2)$ — niezależnie od danych.

### Kod startowy

```python
def sortowanie_przez_wybieranie(lista):
    # Uzupełnij: sortuj listę w miejscu; po każdym kroku wypisz print(lista).
    pass


n = int(input())
lista = [int(x) for x in input().split()]
sortowanie_przez_wybieranie(lista)
```

---

## ZAD-03 — Sortowanie przez wstawianie

**Poziom:** ★★☆
**Tagi:** `sorting`, `insertion-sort`, `list`

### Treść

Napisz funkcję `sortowanie_przez_wstawianie(lista)`, która sortuje listę rosnąco (w miejscu) algorytmem **sortowania przez wstawianie**.

Algorytm buduje posortowany fragment od lewej strony. Dla każdej pozycji $i = 1, 2, \dots, n-1$:

1. zapamiętaj element `lista[i]` (klucz),
2. przesuwaj o jedną pozycję w prawo te elementy posortowanego fragmentu `lista[0..i-1]`, które są **większe** od klucza (idąc od prawej strony),
3. wstaw klucz na zwolnione miejsce,
4. wypisz aktualny stan listy.

### Wejście

* 1. linia: liczba całkowita $n$ — liczba elementów
* 2. linia: $n$ liczb całkowitych oddzielonych spacjami

### Wyjście

$n - 1$ linii: stan listy po wstawieniu każdego kolejnego elementu, w formacie listy Pythona. Ostatnia linia to lista posortowana.

### Ograniczenia

* $2 \le n \le 20$
* Elementy są liczbami całkowitymi z przedziału $[-1000, 1000]$.

### Przykład

**Wejście:**

```
5
6 2 1 4 27
```

**Wyjście:**

```
[2, 6, 1, 4, 27]
[1, 2, 6, 4, 27]
[1, 2, 4, 6, 27]
[1, 2, 4, 6, 27]
```

Najpierw `2` trafia przed `6`, potem `1` przed `2`, potem `4` między `2` a `6`; `27` zostaje na swoim miejscu.

### Uwagi o algorytmie

* Po kroku $i$ fragment `lista[0..i]` jest posortowany, a reszta listy jest jeszcze nieruszona.
* Algorytm działa bardzo szybko dla danych prawie posortowanych; w najgorszym przypadku ma złożoność $O(n^2)$.

### Kod startowy

```python
def sortowanie_przez_wstawianie(lista):
    # Uzupełnij: sortuj listę w miejscu; po każdym wstawieniu wypisz print(lista).
    pass


n = int(input())
lista = [int(x) for x in input().split()]
sortowanie_przez_wstawianie(lista)
```

---

## ZAD-04 — Sortowanie przez scalanie

**Poziom:** ★★☆
**Tagi:** `sorting`, `merge-sort`, `recursion`

### Treść

Napisz rekurencyjną funkcję `sortowanie_przez_scalanie(lista)`, która zwraca nową, posortowaną rosnąco listę, korzystając z algorytmu **sortowania przez scalanie**:

1. Jeśli lista ma mniej niż 2 elementy — jest posortowana, zwróć ją.
2. Podziel listę na dwie części: lewa to pierwsze $\lfloor n/2 \rfloor$ elementów (`lista[:n // 2]`), prawa — pozostałe.
3. Rekurencyjnie posortuj najpierw lewą, a potem prawą część.
4. **Scal** obie posortowane części w jedną posortowaną listę (pomocnicza funkcja `scal(lewa, prawa)`), **wypisz** wynik scalenia i go zwróć.

Scalanie: dopóki obie listy mają elementy, porównuj ich pierwsze (najmniejsze) nieużyte elementy i dopisuj do wyniku mniejszy z nich; na koniec dopisz pozostałe elementy.

### Wejście

* 1. linia: liczba całkowita $n$ — liczba elementów
* 2. linia: $n$ liczb całkowitych oddzielonych spacjami

### Wyjście

$n - 1$ linii: wynik każdego scalenia, w kolejności wykonywania, w formacie listy Pythona. Ostatnie scalenie daje całą posortowaną listę.

### Ograniczenia

* $2 \le n \le 20$
* Elementy są liczbami całkowitymi z przedziału $[-1000, 1000]$.

### Przykład

**Wejście:**

```
5
6 2 1 4 27
```

**Wyjście:**

```
[2, 6]
[4, 27]
[1, 4, 27]
[1, 2, 4, 6, 27]
```

Lista dzieli się na `[6, 2]` i `[1, 4, 27]`. Lewa część daje scalenie `[6]` + `[2]` → `[2, 6]`. Prawa dzieli się na `[1]` i `[4, 27]`; najpierw scalane są `[4]` + `[27]`, potem `[1]` + `[4, 27]`. Na końcu scalane są obie połowy.

### Uwagi o algorytmie

* Złożoność czasowa: $O(n \log n)$.

### Kod startowy

```python
def scal(lewa, prawa):
    # Uzupełnij: zwróć jedną posortowaną listę z dwóch posortowanych list.
    pass


def sortowanie_przez_scalanie(lista):
    # Uzupełnij: podziel listę, posortuj obie części rekurencyjnie,
    # scal je, wypisz wynik scalenia i go zwróć.
    pass


n = int(input())
lista = [int(x) for x in input().split()]
sortowanie_przez_scalanie(lista)
```

---

## ZAD-05 — Sortowanie szybkie

**Poziom:** ★★☆
**Tagi:** `sorting`, `quick-sort`, `recursion`

### Treść

Napisz rekurencyjną funkcję `sortowanie_szybkie(lista)`, która zwraca nową, posortowaną rosnąco listę, korzystając z algorytmu **Quick Sort**:

1. Jeśli lista ma mniej niż 2 elementy — jest posortowana, zwróć ją.
2. Jako **pivot** wybierz **pierwszy** element listy.
3. Podziel elementy listy na trzy grupy (zachowując ich kolejność z listy):
   * `mniejsze` — mniejsze od pivota,
   * `rowne` — równe pivotowi (w tym sam pivot),
   * `wieksze` — większe od pivota.
4. **Wypisz** trzy grupy w jednej linii: `print(mniejsze, rowne, wieksze)`.
5. Rekurencyjnie posortuj najpierw grupę `mniejsze`, a potem `wieksze`.
6. Zwróć sklejony wynik: posortowane `mniejsze` + `rowne` + posortowane `wieksze`.

Program wczytuje listę, sortuje ją i na końcu wypisuje posortowaną listę.

### Wejście

* 1. linia: liczba całkowita $n$ — liczba elementów
* 2. linia: $n$ liczb całkowitych oddzielonych spacjami

### Wyjście

* Dla każdego podziału (w kolejności wykonywania) jedna linia z trzema listami oddzielonymi spacją, np. `[2, 1, 4] [6] [27]`. Pusta grupa to `[]`.
* Ostatnia linia: posortowana lista w formacie listy Pythona.

### Ograniczenia

* $2 \le n \le 20$
* Elementy są liczbami całkowitymi z przedziału $[-1000, 1000]$.

### Przykład

**Wejście:**

```
5
6 2 1 4 27
```

**Wyjście:**

```
[2, 1, 4] [6] [27]
[1] [2] [4]
[1, 2, 4, 6, 27]
```

Pierwszy podział (pivot `6`) daje grupy `[2, 1, 4]`, `[6]`, `[27]`. Grupa `[2, 1, 4]` jest dzielona dalej (pivot `2`). Grupy jednoelementowe są już posortowane, więc nie są dzielone.

### Uwagi o algorytmie

* Średnio: $O(n \log n)$, w pesymistycznym przypadku (np. lista już posortowana przy pivocie z początku): $O(n^2)$.
* Wybór pivota ma wpływ na wydajność.

### Kod startowy

```python
def sortowanie_szybkie(lista):
    # Uzupełnij: podziel listę względem pivota, wypisz grupy,
    # posortuj rekurencyjnie grupy mniejsze i większe, zwróć wynik.
    pass


n = int(input())
lista = [int(x) for x in input().split()]
print(sortowanie_szybkie(lista))
```

---

## ZAD-06 — Wyszukiwanie binarne

**Poziom:** ★★☆
**Tagi:** `searching`, `binary-search`, `list`

### Treść

Napisz funkcję `wyszukiwanie_binarne(lista, klucz)`, która w liście posortowanej rosnąco znajduje indeks elementu równego `klucz` algorytmem **wyszukiwania binarnego**:

1. Ustaw granice przeszukiwanego fragmentu: `lo = 0`, `hi = n - 1`.
2. Dopóki `lo <= hi`:
   * wyznacz środek `mid = (lo + hi) // 2` i zapamiętaj go na liście sprawdzonych indeksów,
   * jeśli `lista[mid] == klucz` — klucz znaleziony, wynikiem jest `mid`,
   * jeśli `lista[mid] < klucz` — klucz może być tylko na prawo od środka: `lo = mid + 1`,
   * w przeciwnym razie — tylko na lewo od środka: `hi = mid - 1`.
3. Jeśli fragment stał się pusty (`lo > hi`), klucza nie ma w liście — wynikiem jest `-1`.

Funkcja wypisuje listę sprawdzonych indeksów i zwraca wynik, który program wypisuje w następnej linii.

### Wejście

* 1. linia: liczba elementów $n$
* 2. linia: $n$ różnych liczb całkowitych posortowanych rosnąco, oddzielonych spacjami
* 3. linia: liczba całkowita $x$ — szukany klucz

### Wyjście

* 1. linia: kolejno sprawdzane indeksy `mid` w formacie listy Pythona, np. `[3, 5]`
* 2. linia: indeks elementu równego $x$ albo `-1`, jeśli takiego elementu nie ma

### Ograniczenia

* $1 \le n \le 1000$
* Elementy listy są różne i są liczbami całkowitymi z przedziału $[-10^6, 10^6]$.

### Przykład

**Wejście:**

```
8
1 3 5 7 9 11 13 15
11
```

**Wyjście:**

```
[3, 5]
5
```

Najpierw sprawdzamy `mid = (0 + 7) // 2 = 3`: `lista[3] = 7 < 11`, więc `lo = 4`. Potem `mid = (4 + 7) // 2 = 5`: `lista[5] = 11` — znaleziono.

### Uwagi o algorytmie

* Każde sprawdzenie zmniejsza przeszukiwany fragment mniej więcej o połowę, dlatego liczba sprawdzeń nie przekracza $\lfloor \log_2 n \rfloor + 1$ — dla $n = 1000$ to najwyżej 10 sprawdzeń, a dla miliona elementów najwyżej 20. Złożoność czasowa: $O(\log n)$.
* Wyszukiwanie binarne działa tylko na liście **posortowanej**.

### Kod startowy

```python
def wyszukiwanie_binarne(lista, klucz):
    # Uzupełnij: zapisuj sprawdzane indeksy na liście, wypisz ją
    # i zwróć indeks klucza albo -1.
    pass


n = int(input())
lista = [int(x) for x in input().split()]
klucz = int(input())
print(wyszukiwanie_binarne(lista, klucz))
```

---

## ZAD-07 — Sortowanie przez zliczanie

**Poziom:** ★☆☆
**Tagi:** `sorting`, `counting-sort`, `list`

### Treść

Napisz funkcję `sortowanie_przez_zliczanie(lista, k)`, która sortuje rosnąco listę liczb całkowitych z przedziału $[0, k]$ algorytmem **sortowania przez zliczanie**:

1. Utwórz listę liczności `licznosci` długości $k + 1$ wypełnioną zerami.
2. Przejdź po liście i dla każdego elementu $x$ zwiększ `licznosci[x]` o 1. Po tym kroku `licznosci[v]` to liczba wystąpień wartości $v$.
3. **Wypisz** listę liczności.
4. Zbuduj wynik: dla kolejnych wartości $v = 0, 1, \dots, k$ dopisz do niego $v$ dokładnie `licznosci[v]` razy. Zwróć wynik.

Algorytm w ogóle nie porównuje elementów ze sobą.

### Wejście

* 1. linia: liczba elementów $n$
* 2. linia: $n$ liczb całkowitych z przedziału $[0, k]$ oddzielonych spacjami
* 3. linia: liczba całkowita $k$ — największa możliwa wartość

### Wyjście

* 1. linia: lista liczności (długości $k + 1$) w formacie listy Pythona
* 2. linia: posortowana lista w formacie listy Pythona

### Ograniczenia

* $1 \le n \le 100$
* $0 \le k \le 100$

### Przykład

**Wejście:**

```
8
3 0 5 3 1 0 3 5
5
```

**Wyjście:**

```
[2, 1, 0, 3, 0, 2]
[0, 0, 1, 3, 3, 3, 5, 5]
```

Wartość `0` występuje 2 razy, `1` — raz, `2` — ani razu, `3` — 3 razy, `4` — ani razu, `5` — 2 razy.

### Uwagi o algorytmie

* Złożoność czasowa: $O(n + k)$ — dla małych wartości $k$ to szybciej niż $O(n \log n)$ najlepszych algorytmów opartych na porównaniach.
* Algorytm nadaje się tylko do sortowania liczb całkowitych z niewielkiego zakresu (lista liczności ma $k + 1$ elementów).

### Kod startowy

```python
def sortowanie_przez_zliczanie(lista, k):
    # Uzupełnij: policz wystąpienia wartości 0..k, wypisz listę liczności
    # i zwróć posortowaną listę.
    pass


n = int(input())
lista = [int(x) for x in input().split()]
k = int(input())
print(sortowanie_przez_zliczanie(lista, k))
```
