# Rozdział 7: Pętle — algorytmy matematyczne

Zadania w tym rozdziale łączą pętle z funkcjami: implementujesz klasyczne algorytmy matematyczne (potęgowanie, silnia, NWD, NWW, pierwiastek, test pierwszości) bez gotowych funkcji bibliotecznych.

**Konwencje wspólne:**

* Każde zadanie (i każdy podpunkt) to osobny program: czyta **standardowe wejście** i wypisuje wynik na **standardowe wyjście**.
* Program nie wypisuje komunikatów typu „Podaj liczbę:”. Tekst podany w `input("…")` jest ignorowany przez sprawdzarkę.
* Jeśli zadanie mówi „napisz funkcję”, zaimplementuj funkcję o podanej nazwie, która zwraca wynik przez `return`. Program wczytuje dane, wywołuje funkcję i wypisuje wynik — gotowy szkielet znajdziesz w sekcji **Kod startowy**.
* Dane wejściowe wczytuj dokładnie w podanej kolejności, każdą wartość z osobnej linii.

---

## ZAD-01 — Średnia, minimum i maksimum z n liczb

**Poziom:** ★☆☆
**Tagi:** `pętle`, `suma`, `średnia`, `minimum`, `maksimum`

### Treść

Wczytaj liczbę `n`, a następnie w pętli `n` liczb (każdą z osobnej linii). Wypisz ich średnią arytmetyczną, najmniejszą i największą z nich.

Nie zapamiętuj wszystkich liczb — wystarczą trzy zmienne aktualizowane w każdym obrocie pętli (tzw. **akumulatory**): bieżąca suma, bieżące minimum i bieżące maksimum.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 1`)
* kolejne `n` linii: liczby rzeczywiste (całkowite lub z kropką dziesiętną, np. `2.5`; mogą być ujemne)

### Wyjście

Trzy liczby, każda w osobnej linii i z dokładnością do **dwóch miejsc po przecinku**:

1. średnia arytmetyczna,
2. najmniejsza liczba,
3. największa liczba.

### Przykład

**Wejście:**

```
3
4
-1
6
```

**Wyjście:**

```
3.00
-1.00
6.00
```

### Uwagi

* Wczytuj liczby funkcją `float()`, bo mogą mieć część ułamkową.
* Minimum i maksimum najprościej zainicjować pierwszą wczytaną liczbą, a potem w pętli porównywać z nimi kolejne liczby.
* Możesz napisać pomocniczą funkcję, np. `formatuj(x)` zwracającą `f"{x:.2f}"`, ale wczytywanie danych zostaw w programie głównym.

---

## ZAD-02 — Potęgowanie liczby przy pomocy pętli

**Poziom:** ★☆☆
**Tagi:** `pętle`, `potęgowanie`, `mnożenie`

### Treść

Napisz funkcję `potega(a, b)`, która zwraca $a^b$ obliczone przy użyciu pętli — **bez** operatora `**` i funkcji `pow()`.

Program wczytuje `a` i `b`, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: `a` — liczba naturalna (`a ≥ 0`)
* 2. linia: `b` — liczba naturalna (`b ≥ 0`)

### Wyjście

Jedna liczba całkowita — wartość $a^b$.

### Przykład

**Wejście:**

```
3
5
```

**Wyjście:**

```
243
```

### Uwagi

* Dla `b = 0` wynik wynosi `1` (przyjmujemy też $0^0 = 1$).

### Kod startowy

```python
def potega(a, b):
    # Oblicz a do potęgi b, mnożąc w pętli.
    pass


a = int(input())
b = int(input())
print(potega(a, b))
```

---

## ZAD-03A — Mnożenie przy pomocy dodawania

**Poziom:** ★☆☆
**Tagi:** `pętle`, `dodawanie`, `mnożenie`

### Treść

Napisz funkcję `iloczyn(a, b)`, która zwraca $a \cdot b$ obliczone przy użyciu **tylko dodawania** i pętli (bez operatora `*`).

Program wczytuje `a` i `b`, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: `a` — liczba naturalna (`a ≥ 0`)
* 2. linia: `b` — liczba naturalna (`b ≥ 0`)

### Wyjście

Jedna liczba całkowita — iloczyn $a \cdot b$.

### Przykład

**Wejście:**

```
3
2
```

**Wyjście:**

```
6
```

$3 \cdot 2 = 2 + 2 + 2 = 6$.

### Kod startowy

```python
def iloczyn(a, b):
    # Oblicz a * b, dodając w pętli.
    pass


a = int(input())
b = int(input())
print(iloczyn(a, b))
```

---

## ZAD-03B — Dzielenie całkowite przy pomocy odejmowania

**Poziom:** ★☆☆
**Tagi:** `pętle`, `odejmowanie`, `dzielenie`

### Treść

Napisz funkcję `iloraz(a, b)`, która zwraca wynik dzielenia całkowitego `a // b` obliczony przy użyciu **tylko odejmowania** i pętli (bez operatorów `/`, `//` i `%`).

Program wczytuje `a` i `b`, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: `a` — liczba naturalna (`a ≥ 0`)
* 2. linia: `b` — liczba naturalna (`b ≥ 1`)

### Wyjście

Jedna liczba całkowita — wynik dzielenia całkowitego `a // b`.

### Przykład

**Wejście:**

```
17
5
```

**Wyjście:**

```
3
```

Od `17` można trzy razy odjąć `5` (zostaje reszta `2`), więc wynik to `3`.

### Uwagi

* Gdy `a < b`, wynik wynosi `0`.

### Kod startowy

```python
def iloraz(a, b):
    # Odejmuj b od a w pętli i licz, ile razy się udało.
    pass


a = int(input())
b = int(input())
print(iloraz(a, b))
```

---

## ZAD-04 — Obliczanie silni liczby

**Poziom:** ★☆☆
**Tagi:** `pętle`, `silnia`, `mnożenie`

### Treść

Napisz funkcję `silnia(n)`, która zwraca $n! = 1 \cdot 2 \cdot \ldots \cdot n$ obliczone przy użyciu pętli. Przyjmij, że $0! = 1$.

Program wczytuje `n`, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Jedna liczba całkowita — wartość $n!$.

### Ograniczenia

* `0 ≤ n ≤ 20`

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
6
```

### Kod startowy

```python
def silnia(n):
    # Oblicz n! w pętli.
    pass


n = int(input())
print(silnia(n))
```

---

## ZAD-05 — Największy wspólny dzielnik (NWD)

**Poziom:** ★☆☆
**Tagi:** `Euklides`, `modulo`, `pętle`

### Treść

Napisz funkcję `nwd(a, b)`, która zwraca największy wspólny dzielnik liczb `a` i `b`. Użyj pętli (np. algorytmu Euklidesa), a nie funkcji `math.gcd()`.

Program wczytuje `a` i `b`, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: `a` — liczba naturalna (`a ≥ 1`)
* 2. linia: `b` — liczba naturalna (`b ≥ 1`)

### Wyjście

Jedna liczba całkowita — $\text{NWD}(a, b)$.

### Przykład

**Wejście:**

```
60
45
```

**Wyjście:**

```
15
```

### Uwagi

* Algorytm Euklidesa: dopóki $b \neq 0$, zastępuj parę $(a, b)$ parą $(b, a \bmod b)$. Na końcu wynikiem jest $a$.

### Kod startowy

```python
def nwd(a, b):
    # Oblicz NWD algorytmem Euklidesa.
    pass


a = int(input())
b = int(input())
print(nwd(a, b))
```

---

## ZAD-06 — Najmniejsza wspólna wielokrotność (NWW)

**Poziom:** ★☆☆
**Tagi:** `nww`, `nwd`, `arytmetyka`

### Treść

Napisz funkcję `nww(a, b)`, która zwraca najmniejszą wspólną wielokrotność liczb `a` i `b`.

Program wczytuje `a` i `b`, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: `a` — liczba naturalna (`a ≥ 1`)
* 2. linia: `b` — liczba naturalna (`b ≥ 1`)

### Wyjście

Jedna liczba całkowita — $\text{NWW}(a, b)$.

### Przykład

**Wejście:**

```
7
9
```

**Wyjście:**

```
63
```

### Uwagi

* Możesz skorzystać z funkcji `nwd` z poprzedniego zadania i zależności $\text{NWW}(a, b) = \frac{a \cdot b}{\text{NWD}(a, b)}$.
* Wynik jest liczbą całkowitą — użyj dzielenia całkowitego `//`.

### Kod startowy

```python
def nwd(a, b):
    # Oblicz NWD algorytmem Euklidesa.
    pass


def nww(a, b):
    # Oblicz NWW, korzystając z funkcji nwd.
    pass


a = int(input())
b = int(input())
print(nww(a, b))
```

---

## ZAD-07 — Pierwiastek metodą Newtona (Herona)

**Poziom:** ★★☆
**Tagi:** `Newton`, `float`, `pętle`, `dokładność`

### Treść

Napisz funkcję `pierwiastek(n)`, która zwraca przybliżenie $\sqrt{n}$ obliczone metodą Newtona (Herona), bez użycia `math.sqrt()` ani potęgowania.

Zacznij od $x_0 = n$ i obliczaj kolejne przybliżenia ze wzoru $x_{k+1} = \frac{1}{2}\left(x_k + \frac{n}{x_k}\right)$, aż dwa kolejne przybliżenia będą różnić się o mniej niż $0.0001$, czyli $|x_{k+1} - x_k| < 0.0001$. Zwróć ostatnie obliczone przybliżenie $x_{k+1}$.

Program wczytuje `n`, wywołuje funkcję i wypisuje wynik z dokładnością do **czterech miejsc po przecinku**.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Jedna liczba — przybliżenie $\sqrt{n}$ zaokrąglone do czterech miejsc po przecinku.

### Przykład

**Wejście:**

```
16
```

**Wyjście:**

```
4.0000
```

### Uwagi

* Dla `n = 0` funkcja ma zwrócić `0.0` (wzór wymagałby dzielenia przez zero).
* Wartość bezwzględną obliczysz funkcją `abs()`.

### Kod startowy

```python
def pierwiastek(n):
    # Oblicz przybliżenie pierwiastka z n metodą Newtona.
    pass


n = int(input())
print(f"{pierwiastek(n):.4f}")
```

---

## ZAD-08 — Naiwny test pierwszości liczby

**Poziom:** ★★☆
**Tagi:** `pierwszość`, `pętle`, `dzielniki`

### Treść

Napisz funkcję `czy_pierwsza(n)`, która zwraca `True`, jeśli `n` jest liczbą pierwszą, a w przeciwnym razie `False`.

Liczba pierwsza to liczba naturalna większa od `1`, której jedynymi dzielnikami są `1` i ona sama.

Program wczytuje `n`, wywołuje funkcję i wypisuje zwróconą wartość logiczną (`print(czy_pierwsza(n))`).

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 1`)

### Wyjście

Jedno słowo: `True`, jeśli `n` jest liczbą pierwszą, w przeciwnym razie `False`.

### Przykład

**Wejście:**

```
7
```

**Wyjście:**

```
True
```

### Przykład 2

**Wejście:**

```
4
```

**Wyjście:**

```
False
```

### Uwagi

* `1` nie jest liczbą pierwszą.
* W prostym rozwiązaniu sprawdzasz dzielniki od `2` do `n - 1`. Wystarczy jednak sprawdzać dzielniki `d` spełniające $d \cdot d \leq n$, czyli do $\lfloor \sqrt{n} \rfloor$.

### Kod startowy

```python
def czy_pierwsza(n):
    # Zwróć True, jeśli n jest liczbą pierwszą, w przeciwnym razie False.
    pass


n = int(input())
print(czy_pierwsza(n))
```

---

## ZAD-09 — Rozkład na czynniki pierwsze

**Poziom:** ★★☆
**Tagi:** `pętle`, `pierwszość`, `dzielniki`, `złożoność`

### Treść

Napisz funkcję `wypisz_rozklad(n)`, która wypisuje rozkład liczby `n` na czynniki pierwsze: czynniki w kolejności niemalejącej, oddzielone znakiem `*`, bez spacji. Każdy czynnik powtarzamy tyle razy, ile razy dzieli `n`.

Program wczytuje `n` i wywołuje funkcję.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 2`)

### Wyjście

Jedna linia: czynniki pierwsze liczby `n` oddzielone znakiem `*`. Jeśli `n` jest liczbą pierwszą, wypisz samo `n`.

### Ograniczenia

* $2 \leq n \leq 10^{10}$

### Przykład

**Wejście:**

```
60
```

**Wyjście:**

```
2*2*3*5
```

$60 = 2 \cdot 2 \cdot 3 \cdot 5$.

### Uwagi

* Sprawdzaj kolejne dzielniki `d = 2, 3, 4, …`. Dopóki `d` dzieli `n`, wypisz `d` i podziel `n` przez `d`. Złożone `d` (np. `4`) nigdy nie podzielą `n`, bo ich czynniki pierwsze zostały już wcześniej „wydzielone”.
* **Wystarczy sprawdzać dzielniki `d`, dla których $d \cdot d \leq n$.** Gdyby liczba `n` była złożona, czyli $n = a \cdot b$ dla $2 \leq a \leq b$, to $a \cdot a \leq a \cdot b = n$ — miałaby więc dzielnik nie większy niż $\sqrt{n}$. Jeśli po zakończeniu pętli zostało `n > 1`, to pozostała liczba jest pierwsza i jest ostatnim czynnikiem.
* To ważna oszczędność: dla liczby pierwszej rzędu $10^{10}$ pętla aż do `n` wykonałaby ok. $10^{10}$ obrotów (zbyt długo), a pętla do $\sqrt{n}$ — tylko ok. $10^5$.
* Aby wypisać czynniki w jednej linii, użyj `print(d, end="")`, a znak `*` wypisuj przed każdym czynnikiem poza pierwszym.

### Kod startowy

```python
def wypisz_rozklad(n):
    # Wypisz czynniki pierwsze liczby n oddzielone znakiem *.
    pass


n = int(input())
wypisz_rozklad(n)
```
