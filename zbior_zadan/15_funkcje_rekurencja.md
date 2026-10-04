# Rozdział 15: Funkcje — rekurencja

Poniższe zadania uczą **rekurencji**: funkcja rozwiązuje problem, wywołując samą siebie dla mniejszych danych, aż dojdzie do **przypadku bazowego**, w którym odpowiedź jest znana od razu (np. $0! = 1$).

**Konwencje wspólne:**

* Każde zadanie to osobny program: czyta **standardowe wejście** i wypisuje wynik na **standardowe wyjście**. Program wczytuje dane, wywołuje funkcję opisaną w treści i wypisuje wynik (gotowy szkielet znajdziesz w sekcji „Kod startowy”).
* **Rozwiązanie musi być rekurencyjne.** Właściwe obliczenia wykonuje funkcja, która wywołuje samą siebie. Nie używaj w niej pętli `for` ani `while`, ani gotowych narzędzi, które wykonają całą pracę za Ciebie (np. `sum()`, `pow()`, operatora `**`, `math.factorial()`, `list.index()`). Sprawdzarka porównuje tylko wynik, ale celem zadań jest ćwiczenie rekurencji.
* Każda funkcja rekurencyjna potrzebuje przypadku bazowego (kiedy przestajemy się wywoływać) i kroku rekurencyjnego (wywołania dla mniejszego problemu). Bez przypadku bazowego program przerwie działanie błędem `RecursionError`.
* Python ogranicza głębokość rekurencji (domyślnie do około 1000 zagnieżdżonych wywołań), dlatego dane w zadaniach są małe.
* Liczby naturalne liczymy od zera: $0, 1, 2, \dots$
* Program nie wypisuje komunikatów typu „Podaj liczbę:”.

---

## ZAD-01 — Liczby naturalne mniejsze od N

**Poziom:** ★☆☆
**Tagi:** `rekurencja`, `napisy`

### Treść

Napisz rekurencyjną funkcję `liczby_mniejsze(n)`, która zwraca napis złożony ze wszystkich liczb naturalnych mniejszych od $n$, od największej do najmniejszej, oddzielonych przecinkiem i spacją.

Program wczytuje $N$ i wypisuje wynik funkcji.

### Wejście

Jedna liczba naturalna `N`.

### Wyjście

Jedna linia: liczby `N-1, N-2, ..., 1, 0` oddzielone przecinkiem i spacją (`, `). Po ostatniej liczbie nie ma przecinka. Dla `N = 1` wynikiem jest samo `0`.

### Ograniczenia

* `1 ≤ N ≤ 100`

### Przykład

**Wejście:**

```
10
```

**Wyjście:**

```
9, 8, 7, 6, 5, 4, 3, 2, 1, 0
```

Liczba `10` nie jest mniejsza od `10`, więc napis zaczyna się od `9`.

### Uwagi

* Przypadek bazowy: dla $n = 1$ jedyną mniejszą liczbą naturalną jest `0`. W kroku rekurencyjnym dopisz $n-1$ przed wynikiem wywołania dla $n-1$.

### Kod startowy

```python
def liczby_mniejsze(n):
    # Uzupełnij funkcję rekurencyjną: zwróć napis "n-1, n-2, ..., 0".
    pass


n = int(input())
print(liczby_mniejsze(n))
```

---

## ZAD-02 — Suma liczb naturalnych mniejszych od N

**Poziom:** ★☆☆
**Tagi:** `rekurencja`, `suma`

### Treść

Napisz rekurencyjną funkcję `suma_mniejszych(n)`, która zwraca sumę wszystkich liczb naturalnych mniejszych od $n$, czyli $0 + 1 + 2 + \dots + (n-1)$.

Program wczytuje $N$ i wypisuje wynik funkcji.

### Wejście

Jedna liczba naturalna `N`.

### Wyjście

Jedna liczba naturalna — suma liczb naturalnych mniejszych od `N`. Dla `N = 0` nie ma takich liczb, więc suma wynosi `0`.

### Ograniczenia

* `0 ≤ N ≤ 100`

### Przykład

**Wejście:**

```
10
```

**Wyjście:**

```
45
```

$0 + 1 + 2 + \dots + 9 = 45$ (liczba `10` nie jest mniejsza od `10`).

### Uwagi

* Suma liczb mniejszych od $n$ to $(n-1)$ plus suma liczb mniejszych od $n-1$.

### Kod startowy

```python
def suma_mniejszych(n):
    # Uzupełnij funkcję rekurencyjną.
    pass


n = int(input())
print(suma_mniejszych(n))
```

---

## ZAD-03 — Potęga

**Poziom:** ★☆☆
**Tagi:** `rekurencja`, `potęgowanie`

### Treść

Napisz rekurencyjną funkcję `potega(a, b)`, która zwraca $a^b$, korzystając z zależności $a^0 = 1$ oraz $a^b = a \cdot a^{b-1}$ dla $b \ge 1$.

Program wczytuje $a$ i $b$, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: `a` — liczba całkowita (podstawa)
* 2. linia: `b` — liczba naturalna (wykładnik)

### Wyjście

Jedna liczba całkowita — wartość $a^b$. Przyjmujemy, że $0^0 = 1$.

### Ograniczenia

* `-10 ≤ a ≤ 10`
* `0 ≤ b ≤ 18`

### Przykład

**Wejście:**

```
2
3
```

**Wyjście:**

```
8
```

### Uwagi

* Nie używaj operatora `**` ani funkcji `pow()` — potęgę ma obliczyć Twoja funkcja.

### Kod startowy

```python
def potega(a, b):
    # Uzupełnij funkcję rekurencyjną.
    pass


a = int(input())
b = int(input())
print(potega(a, b))
```

---

## ZAD-04 — Silnia

**Poziom:** ★☆☆
**Tagi:** `rekurencja`, `silnia`

### Treść

Napisz rekurencyjną funkcję `silnia(n)`, która zwraca $n! = 1 \cdot 2 \cdot \ldots \cdot n$, korzystając z zależności $0! = 1$ oraz $n! = n \cdot (n-1)!$ dla $n \ge 1$.

Program wczytuje $N$ i wypisuje $N!$.

### Wejście

Jedna liczba naturalna `N`.

### Wyjście

Jedna liczba naturalna — wartość $N!$.

### Ograniczenia

* `0 ≤ N ≤ 20`

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
6
```

$3! = 3 \cdot 2 \cdot 1 = 6$.

### Kod startowy

```python
def silnia(n):
    # Uzupełnij funkcję rekurencyjną.
    pass


n = int(input())
print(silnia(n))
```

---

## ZAD-05 — Liczba Fibonacciego

**Poziom:** ★☆☆
**Tagi:** `rekurencja`, `Fibonacci`

### Treść

Napisz rekurencyjną funkcję `fibonacci(n)`, która zwraca $n$-ty wyraz ciągu Fibonacciego, zdefiniowanego następująco:

* $F_0 = 0$,
* $F_1 = 1$,
* $F_n = F_{n-1} + F_{n-2}$ dla $n \ge 2$.

Program wczytuje $N$ i wypisuje $F_N$.

### Wejście

Jedna liczba naturalna `N`.

### Wyjście

Jedna liczba naturalna — wartość $F_N$.

### Ograniczenia

* `0 ≤ N ≤ 25`

### Przykład

**Wejście:**

```
7
```

**Wyjście:**

```
13
```

Kolejne wyrazy ciągu to `0, 1, 1, 2, 3, 5, 8, 13, …`, a wyraz o numerze `7` (licząc od zera) to `13`.

### Uwagi

* Funkcja ma dwa przypadki bazowe ($n = 0$ i $n = 1$) i wywołuje samą siebie dwa razy.
* Ta prosta wersja wykonuje bardzo dużo powtórzonych obliczeń (liczba wywołań rośnie wykładniczo), ale dla $N \le 25$ działa wystarczająco szybko.

### Kod startowy

```python
def fibonacci(n):
    # Uzupełnij funkcję rekurencyjną.
    pass


n = int(input())
print(fibonacci(n))
```

---

## ZAD-06 — N-ty wyraz ciągu danego wzorem rekurencyjnym

**Poziom:** ★☆☆
**Tagi:** `rekurencja`, `ciągi`

### Treść

Ciąg jest zdefiniowany wzorem rekurencyjnym:

* $a_1 = 1$,
* $a_n = 1 + 2 \cdot a_{n-1}$ dla $n \ge 2$.

Napisz rekurencyjną funkcję `wyraz_ciagu(n)`, która zwraca $a_n$. Program wczytuje $N$ i wypisuje $a_N$.

### Wejście

Jedna liczba naturalna `N` (`N ≥ 1`).

### Wyjście

Jedna liczba naturalna — wartość $a_N$.

### Ograniczenia

* `1 ≤ N ≤ 30`

### Przykład

**Wejście:**

```
5
```

**Wyjście:**

```
31
```

Kolejne wyrazy: $a_1 = 1$, $a_2 = 3$, $a_3 = 7$, $a_4 = 15$, $a_5 = 31$.

### Kod startowy

```python
def wyraz_ciagu(n):
    # Uzupełnij funkcję rekurencyjną.
    pass


n = int(input())
print(wyraz_ciagu(n))
```

---

## ZAD-07 — Wyszukiwanie liniowe rekurencyjnie

**Poziom:** ★★☆
**Tagi:** `rekurencja`, `listy`, `wyszukiwanie`

### Treść

Napisz rekurencyjną funkcję `wyszukaj(lista, klucz, indeks=0)`, która zwraca indeks **pierwszego** wystąpienia liczby `klucz` w liście, sprawdzając kolejne elementy od pozycji `indeks`. Jeśli klucz nie występuje w liście, funkcja zwraca `-1`.

Program wczytuje listę i klucz, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: `n` — liczba elementów listy
* 2. linia: `n` liczb całkowitych oddzielonych spacjami
* 3. linia: `klucz` — liczba całkowita

### Wyjście

Jedna liczba całkowita — indeks pierwszego wystąpienia klucza (indeksy liczymy od `0`) albo `-1`, jeśli klucza nie ma w liście.

### Ograniczenia

* `1 ≤ n ≤ 100`
* elementy listy i klucz są z zakresu `-1000 … 1000`

### Przykład

**Wejście:**

```
3
1 2 2
2
```

**Wyjście:**

```
1
```

Liczba `2` występuje na pozycjach `1` i `2` — wypisujemy pierwszą z nich.

### Uwagi

* Przypadki bazowe: `indeks` wyszedł poza listę (klucza nie ma) albo `lista[indeks]` jest równe kluczowi. W przeciwnym razie szukaj dalej od pozycji `indeks + 1`.

### Kod startowy

```python
def wyszukaj(lista, klucz, indeks=0):
    # Uzupełnij funkcję rekurencyjną: zwróć indeks pierwszego wystąpienia klucza albo -1.
    pass


n = int(input())
lista = [int(x) for x in input().split()]
klucz = int(input())
print(wyszukaj(lista, klucz))
```

---

## ZAD-08 — Wieża Hanoi

**Poziom:** ★★☆
**Tagi:** `rekurencja`, `Hanoi`

### Treść

Na słupku `A` leży `N` krążków o różnych średnicach: na dole największy, a każdy kolejny jest mniejszy od poprzedniego. Słupki `B` i `C` są puste. Należy przenieść wszystkie krążki na słupek `B`, korzystając ze słupka `C` jako pomocniczego. Obowiązują zasady:

* w jednym ruchu przenosimy dokładnie jeden krążek — górny krążek z jednego słupka na inny,
* nie wolno położyć większego krążka na mniejszym.

Napisz rekurencyjną funkcję `hanoi(n, skad, dokad, pomocniczy)`, która wypisuje ruchy przenoszące `n` krążków ze słupka `skad` na słupek `dokad`. Program wczytuje `N` i wypisuje **najkrótszą** sekwencję ruchów (ma ona $2^N - 1$ ruchów i jest wyznaczona jednoznacznie).

### Wejście

Jedna liczba naturalna `N`.

### Wyjście

$2^N - 1$ linii — kolejne ruchy w formacie `X -> Y`, gdzie `X` to słupek, z którego zdejmujemy krążek, a `Y` to słupek, na który go kładziemy.

### Ograniczenia

* `1 ≤ N ≤ 10`

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
A -> B
A -> C
B -> C
A -> B
C -> A
C -> B
A -> B
```

### Uwagi

* Aby przenieść `n` krążków ze słupka `skad` na `dokad`: przenieś `n-1` górnych krążków na słupek `pomocniczy`, przenieś największy krążek na `dokad`, a na koniec przenieś `n-1` krążków ze słupka `pomocniczy` na `dokad`. Przypadek bazowy: jeden krążek (albo zero krążków — wtedy nic nie robimy).

### Kod startowy

```python
def hanoi(n, skad, dokad, pomocniczy):
    # Uzupełnij funkcję rekurencyjną: wypisz ruchy w formacie "X -> Y".
    pass


n = int(input())
hanoi(n, "A", "B", "C")
```

---

## ZAD-09 — Słowa elfickie

**Poziom:** ★★☆
**Tagi:** `rekurencja`, `napisy`

### Treść

**Słowem elfickim** nazywamy napis, w którym każda z liter słowa `elf` (czyli `e`, `l` i `f`) występuje co najmniej raz, w dowolnej kolejności i na dowolnych pozycjach.

Napisz rekurencyjną funkcję `czy_elfickie(slowo, litery="elf")`, która sprawdza, czy każda litera z napisu `litery` występuje w napisie `slowo`. Program wczytuje słowo i wypisuje wynik sprawdzenia.

### Wejście

Jedna linia: słowo złożone z małych liter alfabetu łacińskiego (`a`–`z`).

### Wyjście

`Prawda`, jeśli słowo jest elfickie, w przeciwnym razie `Fałsz`.

### Ograniczenia

* długość słowa: od 1 do 100 znaków

### Przykład

**Wejście:**

```
reflektor
```

**Wyjście:**

```
Prawda
```

W słowie `reflektor` występują litery `e`, `l` i `f`.

### Uwagi

* Sprawdź, czy w słowie występuje pierwsza litera z `litery`, i wywołaj funkcję dla pozostałych liter (`litery[1:]`). Gdy `litery` jest pusty, wszystkie litery zostały znalezione.
* Samo szukanie litery w słowie też możesz zapisać rekurencyjnie: litera występuje w słowie, jeśli jest jego pierwszym znakiem albo występuje w reszcie słowa.

### Kod startowy

```python
def czy_elfickie(slowo, litery="elf"):
    # Uzupełnij funkcję rekurencyjną: zwróć True albo False.
    pass


slowo = input().strip()
print("Prawda" if czy_elfickie(slowo) else "Fałsz")
```

---

## ZAD-10 — Gra

**Poziom:** ★★☆
**Tagi:** `rekurencja`, `kombinatoryka`

### Treść

W grze w każdym ruchu gracz zdobywa `3`, `5` albo `10` punktów. Gracz wygrywa, gdy uzbiera **dokładnie** `N` punktów.

Napisz rekurencyjną funkcję `liczba_sposobow(n, ruchy)`, która zwraca, na ile sposobów można uzbierać dokładnie `n` punktów, używając ruchów o wartościach z listy `ruchy`. Sposoby różniące się tylko kolejnością ruchów traktujemy jako ten sam sposób — liczy się tylko, ile razy gracz zdobył `3`, ile razy `5`, a ile razy `10` punktów.

Program wczytuje `N` i wypisuje liczbę sposobów wygrania gry.

### Wejście

Jedna liczba naturalna `N` (`N ≥ 1`).

### Wyjście

Jedna liczba naturalna — liczba sposobów (może wynosić `0`).

### Ograniczenia

* `1 ≤ N ≤ 100`

### Przykład

**Wejście:**

```
20
```

**Wyjście:**

```
4
```

Sposoby: $10 + 10$, $10 + 5 + 5$, $5 + 5 + 5 + 5$ oraz $5 + 3 + 3 + 3 + 3 + 3$.

### Uwagi

* Rozbij problem na dwa mniejsze: sposoby, w których **co najmniej raz** użyjemy pierwszego ruchu z listy (wtedy zostaje `n - ruchy[0]` punktów, a lista ruchów się nie zmienia), oraz sposoby, w których tego ruchu **nie użyjemy wcale** (te same `n` punktów, lista `ruchy[1:]`). Wynik to suma obu liczb.
* Przypadki bazowe: `n == 0` — znaleźliśmy jeden sposób; `n < 0` albo pusta lista ruchów — żadnego sposobu.

### Kod startowy

```python
def liczba_sposobow(n, ruchy):
    # Uzupełnij funkcję rekurencyjną.
    pass


n = int(input())
print(liczba_sposobow(n, [10, 5, 3]))
```

---

## ZAD-11 — Fibonacci z zapamiętywaniem

**Poziom:** ★★☆
**Tagi:** `rekurencja`, `Fibonacci`, `memoizacja`

### Treść

Oblicz $F_N$ — $N$-ty wyraz ciągu Fibonacciego ($F_0 = 0$, $F_1 = 1$, $F_n = F_{n-1} + F_{n-2}$), ale tym razem dla $N$ aż do $90$. Prosta rekurencja z ZAD-05 nie zdąży: dla $N = 90$ wykonałaby około $10^{19}$ wywołań.

Napisz rekurencyjną funkcję `fibonacci(n, pamiec)`, która **zapamiętuje** obliczone wyniki (memoizacja): `pamiec` to lista, w której `pamiec[k]` jest równe `None`, dopóki $F_k$ nie zostało obliczone, a potem przechowuje jego wartość. Każdy wyraz ciągu jest wtedy liczony tylko raz.

### Wejście

Jedna liczba naturalna `N`.

### Wyjście

Jedna liczba naturalna — wartość $F_N$.

### Ograniczenia

* `0 ≤ N ≤ 90`

### Przykład

**Wejście:**

```
40
```

**Wyjście:**

```
102334155
```

### Uwagi

* Funkcja: jeśli $n < 2$, zwróć $n$. Jeśli `pamiec[n]` nie jest `None`, zwróć zapamiętaną wartość. W przeciwnym razie oblicz `fibonacci(n - 1, pamiec) + fibonacci(n - 2, pamiec)`, zapisz wynik w `pamiec[n]` i zwróć go.
* Porównanie liczby wywołań: wersja bez pamięci liczy te same wyrazy wielokrotnie — dla $N$ wykonuje $2F_{N+1} - 1$ wywołań, czyli liczba wywołań rośnie **wykładniczo** (dla $N = 40$ to już ponad 300 milionów). Wersja z pamięcią oblicza każdy wyraz raz, więc wykonuje mniej niż $2N$ wywołań — liczba wywołań rośnie **liniowo**.
* Dla chętnych: Python ma gotowy mechanizm zapamiętywania. Dekorator `@lru_cache` z modułu `functools`, dopisany nad definicją funkcji, sam zapamiętuje wyniki dla każdego argumentu:

  ```python
  from functools import lru_cache

  @lru_cache(maxsize=None)
  def fib(n):
      if n < 2:
          return n
      return fib(n - 1) + fib(n - 2)
  ```

### Kod startowy

```python
def fibonacci(n, pamiec):
    # Uzupełnij funkcję rekurencyjną: pamiec[k] to zapamiętane F_k albo None.
    pass


n = int(input())
pamiec = [None] * (n + 1)
print(fibonacci(n, pamiec))
```

---

## ZAD-12 — Szybkie potęgowanie modulo

**Poziom:** ★★☆
**Tagi:** `rekurencja`, `potęgowanie`, `modulo`

### Treść

Oblicz $a^b \bmod m$, czyli resztę z dzielenia $a^b$ przez $m$, dla wykładnika $b$ nawet rzędu $10^{18}$.

Napisz rekurencyjną funkcję `potega_modulo(a, b, m)`, która **połowi wykładnik**:

* $a^0 = 1$,
* jeśli $b$ jest parzyste: $a^b = \left(a^{b/2}\right)^2$,
* jeśli $b$ jest nieparzyste: $a^b = a \cdot \left(a^{(b-1)/2}\right)^2$,

a po każdym mnożeniu bierze resztę z dzielenia przez $m$.

### Wejście

Jedna linia: trzy liczby całkowite `a b m` oddzielone spacjami.

### Wyjście

Jedna liczba całkowita — wartość $a^b \bmod m$ (z zakresu `0 … m-1`). Przyjmujemy $a^0 = 1$, także dla $a = 0$.

### Ograniczenia

* `0 ≤ a ≤ 10^9`
* `0 ≤ b ≤ 10^18`
* `1 ≤ m ≤ 10^9`

### Przykład

**Wejście:**

```
2 10 1000
```

**Wyjście:**

```
24
```

$2^{10} = 1024$, a $1024 \bmod 1000 = 24$.

### Uwagi

* Nie używaj `pow(a, b, m)`, `pow(a, b)` ani operatora `**` — potęgowanie ma wykonać Twoja funkcja.
* W ZAD-03 wykładnik malał o 1, więc potrzeba było $b$ wywołań — dla $b = 10^{18}$ to niewykonalne (a głębokość rekurencji przekroczyłaby limit). Połowienie wykładnika daje tylko około $\log_2 b$ wywołań: dla $b = 10^{18}$ to około $60$.
* Wywołaj funkcję dla połowy wykładnika **raz**, zapisz wynik w zmiennej i dopiero ją podnieś do kwadratu (`x * x`). Dwa osobne wywołania dla tej samej połowy znów dałyby około $b$ wywołań.
* Reszta z iloczynu nie zmieni się, jeśli czynniki wcześniej zastąpimy ich resztami: $(x \cdot y) \bmod m = ((x \bmod m) \cdot (y \bmod m)) \bmod m$. Dzięki temu liczby w obliczeniach pozostają małe.
* Pamiętaj o przypadku $m = 1$: każda liczba daje resztę `0`, więc dla $b = 0$ wynikiem jest `1 % m`, a nie `1`.

### Kod startowy

```python
def potega_modulo(a, b, m):
    # Uzupełnij funkcję rekurencyjną: zwróć a^b mod m.
    pass


a, b, m = [int(s) for s in input().split()]
print(potega_modulo(a, b, m))
```

---

## ZAD-13 — Ciągi binarne bez sąsiednich jedynek

**Poziom:** ★★☆
**Tagi:** `rekurencja`, `backtracking`, `napisy`

### Treść

Ciąg binarny to napis złożony ze znaków `0` i `1`. Wypisz wszystkie ciągi binarne długości `n`, w których **żadne dwie jedynki nie stoją obok siebie** (np. `1010` jest poprawny, a `0110` nie), w kolejności leksykograficznej (słownikowej), a na końcu ich liczbę.

Napisz rekurencyjną funkcję `generuj(n, ciag)`, która wypisuje wszystkie poprawne ciągi długości `n` zaczynające się od napisu `ciag` i zwraca ich liczbę. Program wywołuje `generuj(n, "")` i wypisuje zwróconą liczbę.

### Wejście

Jedna liczba naturalna `n`.

### Wyjście

Najpierw wszystkie poprawne ciągi, każdy w osobnej linii, w kolejności leksykograficznej. W ostatniej linii — liczba tych ciągów.

### Ograniczenia

* `1 ≤ n ≤ 12`

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
000
001
010
100
101
5
```

Pozostałe ciągi długości 3 (`011`, `110`, `111`) mają dwie sąsiednie jedynki.

### Uwagi

* To przykład **przeszukiwania z nawrotami** (ang. *backtracking*): budujemy ciąg znak po znaku. W każdym kroku najpierw próbujemy dopisać `0` (zawsze wolno), a potem `1` — ale tylko wtedy, gdy `ciag` jest pusty albo kończy się na `0`. Gdy `ciag` ma już długość `n`, wypisujemy go i zwracamy `1`.
* Próbowanie `0` przed `1` sprawia, że ciągi pojawiają się od razu w kolejności leksykograficznej — nie trzeba ich sortować.
* Ciekawostka: liczba takich ciągów to kolejne liczby Fibonacciego ($2, 3, 5, 8, 13, \dots$).

### Kod startowy

```python
def generuj(n, ciag):
    # Uzupełnij funkcję rekurencyjną: wypisz wszystkie poprawne ciągi długości n
    # zaczynające się od ciag i zwróć ich liczbę.
    pass


n = int(input())
print(generuj(n, ""))
```
