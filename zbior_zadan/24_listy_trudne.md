# Rozdział 24: Listy — zadania dodatkowe

Trudniejsze zadania na listach: przekształcenia w miejscu, sumy prefiksowe, kopiec i programowanie dynamiczne. Liczy się nie tylko poprawny wynik, ale też dobry algorytm — w testach są także długie listy, na których rozwiązanie „sprawdzające wszystkie możliwości” nie zdąży się wykonać.

**Konwencje wspólne:**

* Każde zadanie to osobny program: czyta **standardowe wejście** i wypisuje wynik na **standardowe wyjście**.
* Program nie wypisuje komunikatów typu „Podaj liczbę:”. Tekst podany w `input("…")` jest ignorowany przez sprawdzarkę.
* Lista liczb jest podawana w dwóch liniach: w pierwszej jest liczba elementów `n`, w drugiej `n` liczb całkowitych oddzielonych spacjami (o ile zadanie nie mówi inaczej).
* Listę wynikową wypisuj w jednej linii, a jej elementy oddzielaj pojedynczą spacją (o ile zadanie nie mówi inaczej).
* Indeksy liczymy od `0`.

---

## ZAD-01 — Najdłuższy ciąg jedynek

**Poziom:** ★★☆
**Tagi:** `list`, `0/1`, `analiza`, `indeksy`

### Treść

Otrzymujesz listę składającą się wyłącznie z zer i jedynek. Znajdź **indeks zera**, którego zamiana na `1` da **najdłuższy nieprzerwany ciąg jedynek**.

* Jeśli kilka zer daje ciąg o tej samej, maksymalnej długości — wybierz zero o **najmniejszym indeksie**.
* Jeśli lista składa się wyłącznie z zer **albo** wyłącznie z jedynek — wypisz `-1`.

### Wejście

* 1. linia: `n` — długość listy
* 2. linia: `n` liczb `0` lub `1` oddzielonych spacjami

### Wyjście

Jedna liczba całkowita: indeks szukanego zera albo `-1`.

### Ograniczenia

* `1 ≤ n ≤ 1000`

### Przykład

**Wejście:**

```
10
0 0 1 0 1 1 1 0 1 1
```

**Wyjście:**

```
7
```

Zamiana zera o indeksie `7` daje sześć jedynek pod rząd (indeksy 4–9). Zamiana zera o indeksie `3` dałaby tylko pięć jedynek (indeksy 2–6).

### Uwagi

* Po zamianie zera łączą się jedynki stojące bezpośrednio przed nim i za nim — wystarczy więc znać pozycje sąsiednich zer. Da się to policzyć w jednym przejściu po liście, w czasie $O(n)$.

---

## ZAD-02 — Przesuń zera na koniec listy

**Poziom:** ★★☆
**Tagi:** `list`, `stabilność`, `przekształcenie`

### Treść

Otrzymujesz listę liczb całkowitych. Przenieś wszystkie zera na koniec listy, **zachowując kolejność** pozostałych elementów.

### Wejście

* 1. linia: `n` — długość listy
* 2. linia: `n` liczb całkowitych oddzielonych spacjami

### Wyjście

Jedna linia: `n` liczb listy po przekształceniu, oddzielonych spacjami.

### Ograniczenia

* `1 ≤ n ≤ 1000`
* elementy listy są z przedziału $[-10^6, 10^6]$

### Przykład

**Wejście:**

```
11
0 1 3 0 8 12 0 4 0 7 0
```

**Wyjście:**

```
1 3 8 12 4 7 0 0 0 0 0
```

### Uwagi

* Spróbuj przekształcić listę **w miejscu**, bez tworzenia nowej listy: przepisuj kolejne niezerowe elementy na początek listy, a resztę wypełnij zerami. Takie rozwiązanie działa w czasie $O(n)$.

---

## ZAD-03 — Minimalny iloczyn trzech liczb

**Poziom:** ★★☆
**Tagi:** `list`, `min`, `math`

### Treść

Otrzymujesz listę liczb całkowitych. Znajdź **najmniejszy możliwy iloczyn trzech elementów** tej listy (trzech elementów o różnych indeksach; wartości mogą się powtarzać).

Jeśli lista ma mniej niż 3 elementy — wypisz iloczyn wszystkich jej elementów.

### Wejście

* 1. linia: `n` — długość listy
* 2. linia: `n` liczb całkowitych oddzielonych spacjami

### Wyjście

Jedna liczba całkowita — najmniejszy iloczyn.

### Ograniczenia

* `1 ≤ n ≤ 1000`
* elementy listy są z przedziału $[-1000, 1000]$

### Przykład

**Wejście:**

```
6
3 -1 -3 2 9 4
```

**Wyjście:**

```
-108
```

Najmniejszy iloczyn daje trójka $-3 \cdot 9 \cdot 4 = -108$.

### Uwagi

* Uważaj na liczby ujemne: iloczyn dwóch ujemnych jest dodatni. Wystarczy porównać dwóch kandydatów: trzy najmniejsze liczby oraz najmniejszą liczbę razy dwie największe.
* Sprawdzanie wszystkich trójek zajmuje czas $O(n^3)$ — przy $n = 1000$ to ponad $10^8$ trójek. Oczekiwane rozwiązanie działa w czasie $O(n \log n)$ (sortowanie) albo $O(n)$.

---

## ZAD-04 — Najdłuższy fragment o równych sumach

**Poziom:** ★★★
**Tagi:** `list`, `prefix`, `hashmap`, `podciąg`

### Treść

Otrzymujesz dwie listy binarne `A` i `B` (zera i jedynki) o tej samej długości `n`. Znajdź **największą długość** fragmentu (ciągłego zakresu indeksów od `i` do `j`), dla którego suma elementów `A` w tym zakresie jest równa sumie elementów `B` w tym samym zakresie, czyli $A_i + A_{i+1} + \ldots + A_j = B_i + B_{i+1} + \ldots + B_j$.

Jeśli taki fragment nie istnieje — wypisz `0`.

### Wejście

* 1. linia: `n` — długość list
* 2. linia: `n` liczb `0`/`1` — lista `A`
* 3. linia: `n` liczb `0`/`1` — lista `B`

### Wyjście

Jedna liczba całkowita — największa długość fragmentu albo `0`.

### Ograniczenia

* `1 ≤ n ≤ 1000`

### Przykład

**Wejście:**

```
6
0 0 1 1 1 1
0 1 1 0 1 0
```

**Wyjście:**

```
5
```

Dla indeksów 0–4 obie sumy są równe 3, więc istnieje fragment długości 5. Dłuższego nie ma: dla całych list sumy wynoszą 4 i 3.

### Uwagi

* Suma `A` i `B` na fragmencie `i..j` jest równa wtedy, gdy różnica sum prefiksowych $\sum A - \sum B$ jest taka sama tuż przed indeksem `i` i na indeksie `j`. Zapamiętuj w słowniku, gdzie każda różnica pojawiła się po raz pierwszy — da to rozwiązanie w czasie $O(n)$.

---

## ZAD-05 — Zbiór potęgowy listy

**Poziom:** ★★★
**Tagi:** `list`, `subsets`, `combinatorics`, `rekurencja`

### Treść

Otrzymujesz listę liczb całkowitych (mogą się powtarzać). Wypisz **wszystkie różne podzbiory** tej listy, łącznie ze zbiorem pustym i całą listą.

Kolejność elementów w podzbiorze nie ma znaczenia: z listy `1 2 1` podzbiór złożony z `1` i `2` powstaje na dwa sposoby, ale wypisujemy go **tylko raz**.

### Wejście

* 1. linia: `n` — długość listy
* 2. linia: `n` liczb całkowitych oddzielonych spacjami

### Wyjście

Każdy podzbiór w osobnej linii, zapisany jak lista w Pythonie (tak wypisuje ją `print(lista)`):

* elementy podzbioru w kolejności niemalejącej, w nawiasach kwadratowych, oddzielone przecinkiem i spacją, np. `[1, 1, 2]`; pusty podzbiór to `[]`,
* podzbiory uporządkowane **leksykograficznie**: porównujemy pierwsze elementy (jako liczby, więc `9` jest przed `10`), przy remisie drugie itd.; podzbiór, który jest początkiem dłuższego, stoi przed nim (np. `[1]` przed `[1, 1]`). Tak porównuje listy Python, więc `sorted()` na liście list daje dokładnie tę kolejność.

### Ograniczenia

* `1 ≤ n ≤ 10`
* elementy listy są z przedziału $[-100, 100]$

### Przykład

**Wejście:**

```
3
1 2 1
```

**Wyjście:**

```
[]
[1]
[1, 1]
[1, 1, 2]
[1, 2]
[2]
```

### Uwagi

* Wygodnie jest najpierw posortować listę, a potem generować podzbiory rekurencyjnie (dla każdego elementu: bierzemy go albo nie). Aby uniknąć powtórzeń, na danym poziomie rekurencji pomijaj element równy poprzedniemu.

### Kod startowy

```python
def podzbiory(liczby):
    wynik = []
    # Uzupełnij: dodaj do wyniku wszystkie różne podzbiory
    # (każdy jako posortowana lista) w kolejności leksykograficznej.
    return wynik


n = int(input())
liczby = [int(x) for x in input().split()]
for podzbior in podzbiory(liczby):
    print(podzbior)
```

---

## ZAD-06 — Połączenie posortowanych list (bez powtórzeń)

**Poziom:** ★★★
**Tagi:** `merge`, `heap`, `unique`, `sorted`

### Treść

Otrzymujesz `M` list liczb całkowitych, z których każda jest posortowana niemalejąco. Połącz je w jedną listę posortowaną **rosnąco** i zawierającą każdą wartość **tylko raz** (powtórzenia mogą występować zarówno w obrębie jednej listy, jak i między listami). Niektóre listy mogą być puste.

### Wejście

* 1. linia: `M` — liczba list
* kolejne `M` linii: opis jednej listy — najpierw jej długość `k`, a po niej `k` liczb posortowanych niemalejąco (wszystko oddzielone spacjami); pusta lista to linia zawierająca samo `0`

### Wyjście

Jedna linia: elementy połączonej listy oddzielone spacjami. Jeśli wszystkie listy są puste, wypisz pustą linię.

### Ograniczenia

* `1 ≤ M ≤ 100`
* `0 ≤ k ≤ 100`
* elementy list są z przedziału $[-10^6, 10^6]$

### Przykład

**Wejście:**

```
4
4 -6 23 29 33
4 6 22 35 71
4 5 19 21 37
4 -12 -7 -3 28
```

**Wyjście:**

```
-12 -7 -6 -3 5 6 19 21 22 23 28 29 33 35 37 71
```

Pierwsza liczba w każdej linii to długość listy, a nie jej element.

### Uwagi

* Najmniejszy element wyniku to najmniejszy z **pierwszych** elementów list. Trzymaj w kopcu (`heapq`) po jednym „bieżącym” elemencie z każdej listy: zdejmuj najmniejszy, a na jego miejsce wkładaj następny element z tej samej listy. Dla $N$ elementów łącznie daje to czas $O(N \log M)$.
* Powtórzenia łatwo pominąć: wynik powstaje w kolejności rosnącej, więc wystarczy porównać nowy element z ostatnio dopisanym.

### Kod startowy

```python
def polacz_listy(listy):
    wynik = []
    # Uzupełnij: scal posortowane listy w jedną rosnącą listę bez powtórzeń.
    return wynik


m = int(input())
listy = []
for _ in range(m):
    dane = [int(x) for x in input().split()]
    listy.append(dane[1:])  # pierwsza liczba to długość listy
print(" ".join(str(x) for x in polacz_listy(listy)))
```

---

## ZAD-07 — Pojemność wody między słupkami

**Poziom:** ★★★
**Tagi:** `two pointers`, `prefix`, `trapping rain water`

### Treść

Otrzymujesz wysokości `n` słupków stojących obok siebie; każdy słupek ma szerokość `1`. Oblicz, ile jednostek wody zatrzyma się pomiędzy słupkami po deszczu (woda spływa poza pierwszy i ostatni słupek).

Nad słupkiem o indeksie `i` zatrzyma się $\min(L_i, P_i) - h_i$ jednostek wody, gdzie $L_i$ to najwyższy słupek na lewo od `i` (włącznie z nim), a $P_i$ — najwyższy słupek na prawo od `i` (włącznie z nim).

### Wejście

* 1. linia: `n` — liczba słupków
* 2. linia: `n` nieujemnych liczb całkowitych — wysokości słupków

### Wyjście

Jedna liczba całkowita — łączna ilość wody.

### Ograniczenia

* `1 ≤ n ≤ 1000`
* $0 \le h_i \le 10^4$

### Przykład

**Wejście:**

```
5
3 0 1 0 2
```

**Wyjście:**

```
5
```

Nad słupkami o indeksach 1, 2 i 3 woda sięga wysokości $\min(3, 2) = 2$, więc zatrzyma się tam odpowiednio $2 + 1 + 2 = 5$ jednostek.

### Uwagi

* Liczenie $L_i$ i $P_i$ od nowa dla każdego słupka daje czas $O(n^2)$. Oczekiwane rozwiązanie działa w czasie $O(n)$: policz maksima prefiksowe i sufiksowe w dwóch przejściach albo użyj dwóch wskaźników idących od końców listy.

---

## ZAD-08 — Maksymalny zysk ze sprzedaży sznurka

**Poziom:** ★★★
**Tagi:** `dp`, `rod cutting`, `optymalizacja`

### Treść

Masz sznurek o długości `n` i cennik: $c_d$ to cena kawałka o długości `d` (dla `d = 1, 2, …, n`). Ceny nie muszą rosnąć razem z długością. Możesz pociąć sznurek na dowolną liczbę kawałków o całkowitych długościach (albo nie ciąć go wcale) i sprzedać wszystkie kawałki. Oblicz **maksymalny możliwy zysk**.

### Wejście

* 1. linia: `n` — długość sznurka
* 2. linia: `n` nieujemnych liczb całkowitych $c_1, c_2, \ldots, c_n$ oddzielonych spacjami

### Wyjście

Jedna liczba całkowita — maksymalny zysk.

### Ograniczenia

* `1 ≤ n ≤ 500`
* $0 \le c_d \le 10^4$

### Przykład

**Wejście:**

```
4
1 5 8 9
```

**Wyjście:**

```
10
```

Najlepiej pociąć sznurek na dwa kawałki o długości 2: $5 + 5 = 10$.

### Przykład 2

**Wejście:**

```
8
1 5 8 9 10 17 17 20
```

**Wyjście:**

```
22
```

Kawałki o długościach 2 i 6: $5 + 17 = 22$.

### Uwagi

* Sprawdzanie wszystkich sposobów pocięcia (jest ich $2^{n-1}$) jest zdecydowanie za wolne — w testach `n` sięga kilkuset. Użyj programowania dynamicznego: najlepszy zysk dla długości `d` to maksimum z $c_k + \text{najlepszy}(d - k)$ po wszystkich długościach pierwszego kawałka `k`. Daje to czas $O(n^2)$.

---

## ZAD-09 — Najdłuższy naprzemienny podciąg

**Poziom:** ★★★
**Tagi:** `dp`, `subsequence`, `naprzemienny`

### Treść

Ciąg $x_1, x_2, \ldots, x_k$ jest **naprzemienny** (zygzakowaty), jeśli różnice między kolejnymi elementami są na przemian dodatnie i ujemne, czyli $x_1 < x_2 > x_3 < x_4 > \ldots$ albo $x_1 > x_2 < x_3 > x_4 < \ldots$

Ciąg jednoelementowy też jest naprzemienny. Dwa równe sąsiednie elementy psują naprzemienność (różnica `0` nie jest ani dodatnia, ani ujemna).

Otrzymujesz listę liczb całkowitych. Wyznacz **długość najdłuższego naprzemiennego podciągu** tej listy. Podciąg powstaje przez usunięcie z listy dowolnych elementów (być może żadnego) bez zmiany kolejności pozostałych — jego elementy nie muszą ze sobą sąsiadować na liście.

### Wejście

* 1. linia: `n` — długość listy
* 2. linia: `n` liczb całkowitych oddzielonych spacjami

### Wyjście

Jedna liczba całkowita — długość najdłuższego naprzemiennego podciągu.

### Ograniczenia

* `1 ≤ n ≤ 1000`
* elementy listy są z przedziału $[-10^6, 10^6]$

### Przykład

**Wejście:**

```
8
1 -2 6 4 -3 2 -4 -3
```

**Wyjście:**

```
7
```

Przykładowy najdłuższy podciąg naprzemienny (pominięto `4`): $1 > -2 < 6 > -3 < 2 > -4 < -3$.

### Uwagi

* Podciągów jest $2^n$, więc sprawdzanie wszystkich jest wykluczone — w testach są listy z setkami elementów.
* Programowanie dynamiczne: idąc po liście, pamiętaj długość najdłuższego naprzemiennego podciągu kończącego się **wzrostem** i kończącego się **spadkiem**. Gdy bieżący element jest większy od poprzedniego, podciąg „kończący się spadkiem” można przedłużyć wzrostem (i odwrotnie). Daje to czas $O(n)$; rozwiązanie $O(n^2)$ też zdąży.

---

## ZAD-10 — Maksymalna suma spójnego fragmentu (algorytm Kadane'a)

**Poziom:** ★★☆
**Tagi:** `list`, `kadane`, `dp`, `fragment`

### Treść

Otrzymujesz listę liczb całkowitych. Znajdź **niepusty spójny fragment** listy (kolejne elementy od indeksu `p` do indeksu `k` włącznie, $p \le k$) o **największej sumie**. Wypisz tę sumę oraz indeksy początku i końca fragmentu.

* Jeśli kilka fragmentów ma tę samą, największą sumę — wybierz ten o **najmniejszym indeksie początku** `p`, a jeśli nadal jest remis — **najkrótszy** (o najmniejszym `k`).
* Fragment musi mieć co najmniej jeden element, więc gdy wszystkie liczby są ujemne, wynikiem jest największa z nich (pierwsze jej wystąpienie).

### Wejście

* 1. linia: `n` — długość listy
* 2. linia: `n` liczb całkowitych oddzielonych spacjami

### Wyjście

* 1. linia: największa suma
* 2. linia: dwie liczby `p k` oddzielone spacją — indeksy (liczone od `0`) pierwszego i ostatniego elementu fragmentu

### Ograniczenia

* $1 \le n \le 10^5$
* elementy listy są z przedziału $[-10^4, 10^4]$

### Przykład

**Wejście:**

```
9
-2 1 -3 4 -1 2 1 -5 4
```

**Wyjście:**

```
6
3 6
```

Fragment od indeksu 3 do 6: $4 + (-1) + 2 + 1 = 6$.

### Przykład 2

**Wejście:**

```
5
4 -4 1 3 -1
```

**Wyjście:**

```
4
0 0
```

Sumę 4 mają fragmenty `0..0`, `0..3` i `2..3`. Najwcześniej zaczynają się dwa pierwsze, a z nich krótszy jest `0..0`.

### Uwagi

* Sprawdzanie wszystkich fragmentów to około $n^2/2$ par `(p, k)` — przy $n = 10^5$ to miliardy działań. **Algorytm Kadane'a** robi to w jednym przejściu, w czasie $O(n)$: idąc po liście, pamiętaj sumę najlepszego fragmentu **kończącego się** na bieżącym elemencie oraz jego początek. Jeśli ta suma przed dołożeniem nowego elementu jest ujemna, opłaca się zacząć nowy fragment od bieżącego elementu; w przeciwnym razie przedłużasz dotychczasowy.
* Remisy rozstrzygną się zgodnie z treścią, jeśli nowy fragment zaczniesz tylko przy sumie **ściśle ujemnej** (przy sumie `0` przedłużaj — początek zostaje wcześniejszy), a najlepszy wynik zmienisz tylko na **ściśle większy**.

### Kod startowy

```python
def maks_fragment(liczby):
    najlepsza, poczatek, koniec = liczby[0], 0, 0
    # Uzupełnij: algorytm Kadane'a.
    return najlepsza, poczatek, koniec


n = int(input())
liczby = [int(x) for x in input().split()]
suma, poczatek, koniec = maks_fragment(liczby)
print(suma)
print(poczatek, koniec)
```

---
