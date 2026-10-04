# Rozdział 14: Funkcje — wielomiany

Poniższe zadania dotyczą pisania **funkcji** operujących na wielomianach. Wielomian zapisujemy jako listę jego współczynników od najwyższej potęgi do wyrazu wolnego: lista `[a_n, a_{n-1}, ..., a_1, a_0]` oznacza wielomian $a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0$.

**Konwencje wspólne:**

* Każde zadanie to osobny program: czyta **standardowe wejście** i wypisuje wynik na **standardowe wyjście**. Główną pracę wykonuje funkcja opisana w treści zadania — program tylko wczytuje dane, wywołuje funkcję i wypisuje wynik (gotowy szkielet znajdziesz w sekcji „Kod startowy”).
* Wielomian stopnia `n` jest podawany w dwóch liniach: najpierw liczba `n`, a w następnej linii `n+1` liczb całkowitych `a_n a_{n-1} ... a_0` oddzielonych spacjami.
* Współczynniki są liczbami całkowitymi (mogą być ujemne). Dla `n ≥ 1` współczynnik `a_n` jest różny od zera.
* Gdy wynikiem jest wielomian, wypisz jego współczynniki od najwyższej potęgi w **jednej linii**, oddzielone pojedynczą spacją, bez nawiasów i przecinków.
* Program nie wypisuje komunikatów typu „Podaj liczbę:”.

---

## ZAD-01 — Wartość wielomianu w punkcie

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `wielomiany`, `Horner`

### Treść

Napisz funkcję `wartosc_wielomianu(wspolczynniki, x)`, która otrzymuje listę współczynników wielomianu $W(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_0$ oraz liczbę $x$ i zwraca wartość $W(x)$.

Program wczytuje wielomian i liczbę $x$, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: `n` — stopień wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb całkowitych `a_n a_{n-1} ... a_0`
* 3. linia: `x` — liczba całkowita

### Wyjście

Jedna liczba całkowita — wartość wielomianu w punkcie `x`.

### Ograniczenia

* `0 ≤ n ≤ 10`
* `-100 ≤ a_i ≤ 100`, `-10 ≤ x ≤ 10`

### Przykład

**Wejście:**

```
2
3 2 1
1
```

**Wyjście:**

```
6
```

Wielomian to $3x^2 + 2x + 1$, a $3 \cdot 1^2 + 2 \cdot 1 + 1 = 6$.

### Uwagi

* Najprościej skorzystać ze **schematu Hornera**: $W(x) = (\dots((a_n x + a_{n-1}) x + a_{n-2}) x + \dots) x + a_0$. Zacznij od wyniku równego `0` i dla każdego kolejnego współczynnika `a` wykonaj `wynik = wynik * x + a`.

### Kod startowy

```python
def wartosc_wielomianu(wspolczynniki, x):
    # Uzupełnij funkcję: zwróć wartość wielomianu w punkcie x.
    pass


n = int(input())
wspolczynniki = [int(s) for s in input().split()]
x = int(input())
print(wartosc_wielomianu(wspolczynniki, x))
```

---

## ZAD-02 — Iloczyn wielomianu przez skalar

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `wielomiany`, `skalar`

### Treść

Napisz funkcję `pomnoz_przez_skalar(wspolczynniki, k)`, która zwraca **nową** listę współczynników wielomianu $k \cdot W(x)$, czyli wielomianu powstałego przez pomnożenie każdego współczynnika przez liczbę $k$.

Program wczytuje wielomian i liczbę $k$, wywołuje funkcję i wypisuje współczynniki wyniku.

### Wejście

* 1. linia: `n` — stopień wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb całkowitych `a_n ... a_0`
* 3. linia: `k` — liczba całkowita (skalar)

### Wyjście

Jedna linia: `n+1` liczb całkowitych — współczynniki po pomnożeniu, oddzielone spacją. Liczba współczynników się nie zmienia (także dla `k = 0`).

### Ograniczenia

* `0 ≤ n ≤ 10`
* `-100 ≤ a_i ≤ 100`, `-100 ≤ k ≤ 100`

### Przykład

**Wejście:**

```
2
4 -3 2
-2
```

**Wyjście:**

```
-8 6 -4
```

### Kod startowy

```python
def pomnoz_przez_skalar(wspolczynniki, k):
    # Uzupełnij funkcję: zwróć nową listę współczynników.
    pass


n = int(input())
wspolczynniki = [int(s) for s in input().split()]
k = int(input())
print(*pomnoz_przez_skalar(wspolczynniki, k))
```

---

## ZAD-03 — Suma wielomianów

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `wielomiany`, `listy`

### Treść

Napisz funkcję `suma_wielomianow(a, b)`, która otrzymuje listy współczynników dwóch wielomianów (mogą mieć różne stopnie) i zwraca listę współczynników ich sumy.

Program wczytuje oba wielomiany, wywołuje funkcję i wypisuje współczynniki wyniku.

### Wejście

* 1. linia: `n` — stopień pierwszego wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb całkowitych `a_n ... a_0`
* 3. linia: `m` — stopień drugiego wielomianu (`m ≥ 0`)
* 4. linia: `m+1` liczb całkowitych `b_m ... b_0`

### Wyjście

Jedna linia: dokładnie `max(n, m) + 1` liczb całkowitych — współczynniki sumy od najwyższej potęgi, oddzielone spacją. Nie usuwaj zer z początku wyniku (np. gdy najwyższe potęgi się zredukują).

### Ograniczenia

* `0 ≤ n, m ≤ 10`
* `-100 ≤ a_i, b_i ≤ 100`

### Przykład

**Wejście:**

```
2
3 5 2
2
2 -8 1
```

**Wyjście:**

```
5 -3 3
```

$(3x^2 + 5x + 2) + (2x^2 - 8x + 1) = 5x^2 - 3x + 3$.

### Uwagi

* Jeśli stopnie są różne, wyrównaj listy „od końca” (od wyrazu wolnego), dopisując zera na początku krótszej listy. Np. `1 2 3 4` + `5 6` = `1 2 8 10`.

### Kod startowy

```python
def suma_wielomianow(a, b):
    # Uzupełnij funkcję: zwróć listę współczynników sumy.
    pass


n = int(input())
a = [int(s) for s in input().split()]
m = int(input())
b = [int(s) for s in input().split()]
print(*suma_wielomianow(a, b))
```

---

## ZAD-04 — Mnożenie wielomianów

**Poziom:** ★★☆
**Tagi:** `funkcje`, `wielomiany`, `konwolucja`

### Treść

Napisz funkcję `iloczyn_wielomianow(a, b)`, która otrzymuje listy współczynników dwóch wielomianów i zwraca listę współczynników ich iloczynu.

Program wczytuje oba wielomiany, wywołuje funkcję i wypisuje współczynniki wyniku.

### Wejście

* 1. linia: `n` — stopień pierwszego wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb całkowitych `a_n ... a_0`
* 3. linia: `m` — stopień drugiego wielomianu (`m ≥ 0`)
* 4. linia: `m+1` liczb całkowitych `b_m ... b_0`

### Wyjście

Jedna linia: dokładnie `n + m + 1` liczb całkowitych — współczynniki iloczynu od najwyższej potęgi, oddzielone spacją.

### Ograniczenia

* `0 ≤ n, m ≤ 10`
* `-100 ≤ a_i, b_i ≤ 100`

### Przykład

**Wejście:**

```
3
5 0 10 6
2
1 2 4
```

**Wyjście:**

```
5 10 30 26 52 24
```

$(5x^3 + 10x + 6)(x^2 + 2x + 4) = 5x^5 + 10x^4 + 30x^3 + 26x^2 + 52x + 24$.

### Uwagi

* Każdy wyraz pierwszego wielomianu mnożymy przez każdy wyraz drugiego: $a_i x^i \cdot b_j x^j = a_i b_j x^{i+j}$. Utwórz listę `n + m + 1` zer i dla każdej pary pozycji `i` (w liście `a`) oraz `j` (w liście `b`) dodaj `a[i] * b[j]` do pozycji `i + j` wyniku.

### Kod startowy

```python
def iloczyn_wielomianow(a, b):
    # Uzupełnij funkcję: zwróć listę współczynników iloczynu.
    pass


n = int(input())
a = [int(s) for s in input().split()]
m = int(input())
b = [int(s) for s in input().split()]
print(*iloczyn_wielomianow(a, b))
```

---

## ZAD-05 — k-ta pochodna wielomianu

**Poziom:** ★★☆
**Tagi:** `funkcje`, `pochodna`, `wielomiany`

### Treść

Napisz funkcję `pochodna(wspolczynniki, k)`, która zwraca listę współczynników wielomianu będącego `k`-tą pochodną danego wielomianu (czyli wielomianu zróżniczkowanego `k` razy).

Program wczytuje wielomian i liczbę `k`, wywołuje funkcję i wypisuje współczynniki wyniku.

### Wejście

* 1. linia: `n` — stopień wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb całkowitych `a_n ... a_0`
* 3. linia: `k` — rząd pochodnej (`k ≥ 1`)

### Wyjście

Jedna linia: współczynniki `k`-tej pochodnej od najwyższej potęgi, oddzielone spacją. Jeśli `k > n`, pochodna jest wielomianem zerowym — wypisz wtedy `0`.

### Ograniczenia

* `0 ≤ n ≤ 10`, `1 ≤ k ≤ 12`
* `-100 ≤ a_i ≤ 100`

### Przykład

**Wejście:**

```
2
4 -3 2
1
```

**Wyjście:**

```
8 -3
```

$(4x^2 - 3x + 2)' = 8x - 3$.

### Uwagi

* Pochodna jednomianu: $(a x^d)' = d \cdot a x^{d-1}$, a pochodna stałej to $0$. Jeśli współczynniki to `[c_d, c_{d-1}, ..., c_1, c_0]`, to pierwsza pochodna ma współczynniki `[d*c_d, (d-1)*c_{d-1}, ..., 1*c_1]` (o jeden mniej).
* `k`-tą pochodną otrzymasz, licząc pierwszą pochodną `k` razy.

### Kod startowy

```python
def pochodna(wspolczynniki, k):
    # Uzupełnij funkcję: zwróć listę współczynników k-tej pochodnej
    # (dla wielomianu zerowego zwróć [0]).
    pass


n = int(input())
wspolczynniki = [int(s) for s in input().split()]
k = int(input())
print(*pochodna(wspolczynniki, k))
```

---

## ZAD-06 — Miejsca zerowe równania kwadratowego (rzeczywiste)

**Poziom:** ★★☆
**Tagi:** `funkcje`, `delta`, `pierwiastki`

### Treść

Napisz funkcję `miejsca_zerowe(a, b, c)`, która zwraca listę wszystkich **rzeczywistych** rozwiązań równania $ax^2 + bx + c = 0$, posortowaną rosnąco. Pierwiastek podwójny umieść na liście tylko raz.

Program wczytuje współczynniki, wywołuje funkcję i wypisuje wynik.

### Wejście

Jedna linia: trzy liczby całkowite `a b c` oddzielone spacją (`a ≠ 0`).

### Wyjście

* Jeśli równanie ma rozwiązania rzeczywiste: jedna linia z rozwiązaniami w kolejności rosnącej, oddzielonymi spacją, każde z dokładnością do **2 miejsc po przecinku** (np. `-1.62 0.62`). Pierwiastek podwójny wypisz raz.
* Jeśli równanie nie ma rozwiązań rzeczywistych: dokładnie `Brak miejsc zerowych`.

### Ograniczenia

* `-100 ≤ a, b, c ≤ 100`, `a ≠ 0`

### Przykład

**Wejście:**

```
1 2 1
```

**Wyjście:**

```
-1.00
```

$\Delta = 2^2 - 4 \cdot 1 \cdot 1 = 0$, więc jest jeden (podwójny) pierwiastek $x = -1$.

### Przykład 2

**Wejście:**

```
1 0 1
```

**Wyjście:**

```
Brak miejsc zerowych
```

### Uwagi

* Oblicz $\Delta = b^2 - 4ac$. Dla $\Delta < 0$ brak rozwiązań, dla $\Delta = 0$ jest jedno: $x = \frac{-b}{2a}$, a dla $\Delta > 0$ dwa: $x_{1,2} = \frac{-b \pm \sqrt{\Delta}}{2a}$.
* Uważaj na kolejność: gdy $a < 0$, wzór z „$+$” daje **mniejszy** pierwiastek — posortuj wynik.

### Kod startowy

```python
import math


def miejsca_zerowe(a, b, c):
    # Uzupełnij funkcję: zwróć posortowaną listę rzeczywistych pierwiastków.
    pass


a, b, c = [int(s) for s in input().split()]
pierwiastki = miejsca_zerowe(a, b, c)
if pierwiastki:
    print(" ".join(f"{x:.2f}" for x in pierwiastki))
else:
    print("Brak miejsc zerowych")
```

---

## ZAD-07 — Upraszczanie bez skutków ubocznych

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `wielomiany`, `listy`, `skutki uboczne`

### Treść

Zapis wielomianu może zaczynać się od zbędnych zer, np. lista `[0, 0, 3, 0, 1]` oznacza ten sam wielomian co `[3, 0, 1]`, czyli $3x^2 + 1$. W tym zadaniu (wyjątkowo) dane mogą więc zaczynać się od zer.

Napisz funkcję `uprosc(w)`, która zwraca **nową** listę współczynników bez zer wiodących. Wielomian zerowy (same zera) upraszczamy do listy `[0]`. Funkcja **nie może zmieniać** otrzymanej listy `w` — program po wywołaniu funkcji wypisuje także oryginalną listę, żeby to sprawdzić.

### Wejście

* 1. linia: `k` — liczba współczynników (`k ≥ 1`)
* 2. linia: `k` liczb całkowitych — współczynniki od najwyższej potęgi (mogą zaczynać się od zer)

### Wyjście

Dwie linie, liczby oddzielone spacją:

* 1. linia: współczynniki uproszczonego wielomianu (dla wielomianu zerowego: `0`),
* 2. linia: oryginalna lista po wywołaniu funkcji — musi być identyczna z wczytaną.

### Ograniczenia

* `1 ≤ k ≤ 20`
* `-100 ≤ a_i ≤ 100`

### Przykład

**Wejście:**

```
5
0 0 3 0 1
```

**Wyjście:**

```
3 0 1
0 0 3 0 1
```

Usuwamy tylko zera z początku — zero w środku zapisu (przy $x^1$) zostaje.

### Uwagi

* Funkcja **czysta** tylko oblicza i zwraca wynik. Funkcja ze **skutkiem ubocznym** zmienia coś poza sobą — np. listę, którą dostała jako argument.
* Lista przekazana do funkcji **nie jest kopiowana**: parametr `w` i zmienna `wspolczynniki` w programie to ta sama lista. Dlatego poniższa funkcja zwraca dobry wynik, ale psuje listę wywołującego (druga linia wyjścia byłaby `3 0 1`):

  ```python
  def uprosc_zle(w):
      while len(w) > 1 and w[0] == 0:
          w.pop(0)  # usuwa element z ORYGINALNEJ listy!
      return w
  ```

* Zamiast usuwać elementy, znajdź indeks `i` pierwszego niezerowego współczynnika i zwróć wycinek `w[i:]` — wycinek to nowa lista, a oryginał zostaje nietknięty.

### Kod startowy

```python
def uprosc(w):
    # Uzupełnij funkcję: zwróć NOWĄ listę bez zer wiodących
    # (dla wielomianu zerowego [0]). Nie zmieniaj listy w!
    pass


k = int(input())
wspolczynniki = [int(s) for s in input().split()]
wynik = uprosc(wspolczynniki)
print(*wynik)
print(*wspolczynniki)
```
