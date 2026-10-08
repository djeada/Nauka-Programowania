# Rozdział 6: Funkcje — wprowadzenie

Zadania w tym rozdziale uczą pisania **funkcji**: definiowania ich instrukcją `def`, przekazywania argumentów i zwracania wyniku instrukcją `return`.

**Konwencje wspólne:**

* Każde zadanie (i każdy podpunkt a, b, c…) to osobny program: czyta **standardowe wejście** i wypisuje wynik na **standardowe wyjście**.
* Treść mówi, jaką funkcję napisać (nazwa, parametry, zwracana wartość). Program wczytuje dane, **wywołuje funkcję** i wypisuje zwrócony przez nią wynik.
* „Funkcja zwraca” oznacza użycie instrukcji `return`. Funkcja nie wczytuje danych i nie wypisuje wyniku sama — robi to reszta programu (chyba że treść zadania mówi inaczej).
* Sekcja „Kod startowy” zawiera gotowy szkielet: nagłówek funkcji oraz linie, które wczytują dane i wypisują wynik. Wystarczy uzupełnić ciało funkcji.
* Liczby na wejściu podane są w osobnych liniach — wczytuj je dokładnie w podanej kolejności.
* Program nie wypisuje komunikatów typu „Podaj liczbę:”.

---

## ZAD-01A — Zwracanie stałej wartości: liczba 3

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `return`, `int`

### Treść

Napisz bezargumentową funkcję `zwroc_liczbe()`, która zwraca liczbę całkowitą `3`.

Program wywołuje funkcję i wypisuje zwrócony wynik.

### Wejście

Brak.

### Wyjście

Jedna linia: wartość zwrócona przez funkcję, czyli `3`.

### Przykład

**Wejście:** *(brak)*

**Wyjście:**

```
3
```

### Kod startowy

```python
def zwroc_liczbe():
    # Uzupełnij funkcję.
    pass


print(zwroc_liczbe())
```

---

## ZAD-01B — Zwracanie stałej wartości: napis „Tak”

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `return`, `string`

### Treść

Napisz bezargumentową funkcję `zwroc_napis()`, która zwraca napis `Tak`.

Program wywołuje funkcję i wypisuje zwrócony wynik.

### Wejście

Brak.

### Wyjście

Jedna linia: napis zwrócony przez funkcję, czyli `Tak`.

### Przykład

**Wejście:** *(brak)*

**Wyjście:**

```
Tak
```

### Kod startowy

```python
def zwroc_napis():
    # Uzupełnij funkcję.
    pass


print(zwroc_napis())
```

---

## ZAD-01C — Zwracanie stałej wartości: True

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `return`, `bool`

### Treść

Napisz bezargumentową funkcję `zwroc_prawda()`, która zwraca wartość logiczną `True`.

Program wywołuje funkcję i wypisuje zwrócony wynik.

### Wejście

Brak.

### Wyjście

Jedna linia: wartość zwrócona przez funkcję, czyli `True`.

### Przykład

**Wejście:** *(brak)*

**Wyjście:**

```
True
```

### Uwagi

* Funkcja ma zwrócić wartość logiczną `True`, a nie napis `"True"`. Po wypisaniu wyglądają tak samo, ale to różne typy danych.

### Kod startowy

```python
def zwroc_prawda():
    # Uzupełnij funkcję.
    pass


print(zwroc_prawda())
```

---

## ZAD-02A — Suma dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `arytmetyka`

### Treść

Napisz funkcję `suma(a, b)`, która zwraca sumę $a + b$ dwóch liczb całkowitych.

Program wczytuje `a` i `b`, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: liczba całkowita `a`
* 2. linia: liczba całkowita `b`

### Wyjście

Jedna liczba całkowita: $a + b$.

### Przykład

**Wejście:**

```
3
5
```

**Wyjście:**

```
8
```

### Kod startowy

```python
def suma(a, b):
    # Uzupełnij funkcję.
    pass


a = int(input())
b = int(input())
print(suma(a, b))
```

---

## ZAD-02B — Różnica: b − a

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `arytmetyka`

### Treść

Napisz funkcję `roznica(a, b)`, która zwraca różnicę $b - a$ (od **drugiej** liczby odejmujemy pierwszą).

Program wczytuje `a` i `b`, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: liczba całkowita `a`
* 2. linia: liczba całkowita `b`

### Wyjście

Jedna liczba całkowita: $b - a$.

### Przykład

**Wejście:**

```
3
5
```

**Wyjście:**

```
2
```

### Kod startowy

```python
def roznica(a, b):
    # Uzupełnij funkcję.
    pass


a = int(input())
b = int(input())
print(roznica(a, b))
```

---

## ZAD-02C — Iloczyn dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `arytmetyka`

### Treść

Napisz funkcję `iloczyn(a, b)`, która zwraca iloczyn $a \cdot b$.

Program wczytuje `a` i `b`, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: liczba całkowita `a`
* 2. linia: liczba całkowita `b`

### Wyjście

Jedna liczba całkowita: $a \cdot b$.

### Przykład

**Wejście:**

```
3
5
```

**Wyjście:**

```
15
```

### Kod startowy

```python
def iloczyn(a, b):
    # Uzupełnij funkcję.
    pass


a = int(input())
b = int(input())
print(iloczyn(a, b))
```

---

## ZAD-02D — Iloraz całkowity: a // b

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `dzielenie`, `//`

### Treść

Napisz funkcję `iloraz(a, b)`, która zwraca iloraz całkowity `a // b`.

Program wczytuje `a` i `b`, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: liczba całkowita `a`
* 2. linia: liczba całkowita `b`

### Wyjście

Jedna liczba całkowita: `a // b`.

### Ograniczenia

* $b \neq 0$

### Przykład

**Wejście:**

```
3
5
```

**Wyjście:**

```
0
```

### Uwagi

* Operator `//` zaokrągla wynik dzielenia **w dół**, także dla liczb ujemnych, np. `-7 // 2` daje `-4`.

### Kod startowy

```python
def iloraz(a, b):
    # Uzupełnij funkcję.
    pass


a = int(input())
b = int(input())
print(iloraz(a, b))
```

---

## ZAD-02E — Reszta z dzielenia: a % b

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `modulo`, `%`

### Treść

Napisz funkcję `reszta(a, b)`, która zwraca resztę z dzielenia `a % b`.

Program wczytuje `a` i `b`, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: liczba całkowita `a`
* 2. linia: liczba całkowita `b`

### Wyjście

Jedna liczba całkowita: `a % b`.

### Ograniczenia

* $b \neq 0$

### Przykład

**Wejście:**

```
3
5
```

**Wyjście:**

```
3
```

### Uwagi

* W Pythonie wynik `a % b` ma ten sam znak co `b`, np. `-7 % 3` daje `2`.

### Kod startowy

```python
def reszta(a, b):
    # Uzupełnij funkcję.
    pass


a = int(input())
b = int(input())
print(reszta(a, b))
```

---

## ZAD-03 — Sprawdzanie warunków logicznych

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `bool`, `warunki`

### Treść

Napisz funkcję `sprawdz_warunki(a, b)`, która dla dwóch liczb naturalnych zwraca **krotkę** czterech wartości logicznych, odpowiadających kolejno pytaniom:

a) Czy $a > b$?
b) Czy $a + b < 10$?
c) Czy obie liczby są nieparzyste?
d) Czy większa z liczb jest mniejsza od kwadratu `a`, czyli czy $\max(a, b) < a^2$?

Program wczytuje `a` i `b`, wywołuje funkcję i wypisuje cztery zwrócone wartości.

### Wejście

* 1. linia: liczba naturalna `a`
* 2. linia: liczba naturalna `b`

### Wyjście

Cztery linie z wartościami `True` albo `False` — odpowiedzi na pytania a), b), c), d) w tej kolejności.

### Ograniczenia

* $a \ge 0$, $b \ge 0$

### Przykład

**Wejście:**

```
3
2
```

**Wyjście:**

```
True
True
False
True
```

$3 > 2$, $3 + 2 = 5 < 10$, liczba $2$ jest parzysta, $\max(3, 2) = 3 < 9$.

### Uwagi

* Kilka wartości zwrócisz naraz instrukcją `return w1, w2, w3, w4` — Python spakuje je w krotkę.

### Kod startowy

```python
def sprawdz_warunki(a, b):
    # Uzupełnij funkcję: zwróć cztery wartości logiczne.
    pass


a = int(input())
b = int(input())
w1, w2, w3, w4 = sprawdz_warunki(a, b)
print(w1)
print(w2)
print(w3)
print(w4)
```

---

## ZAD-04A — Minimum z dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `min`

### Treść

Napisz funkcję `min_z_dwoch(a, b)`, która zwraca mniejszą z dwóch liczb naturalnych.

Program wczytuje `a` i `b`, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: liczba naturalna `a`
* 2. linia: liczba naturalna `b`

### Wyjście

Jedna liczba naturalna: mniejsza z liczb `a` i `b`.

### Ograniczenia

* $a \ge 0$, $b \ge 0$

### Przykład

**Wejście:**

```
3
1
```

**Wyjście:**

```
1
```

### Uwagi

* Spróbuj napisać funkcję bez wbudowanej funkcji `min` — porównaj liczby instrukcją `if`.
* Jeśli liczby są równe, zwróć dowolną z nich.

### Kod startowy

```python
def min_z_dwoch(a, b):
    # Uzupełnij funkcję.
    pass


a = int(input())
b = int(input())
print(min_z_dwoch(a, b))
```

---

## ZAD-04B — Ograniczenie liczby do przedziału

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `min`, `max`

### Treść

Napisz funkcję `ogranicz(x, dolna, gorna)`, która „przycina” liczbę `x` do przedziału $[\text{dolna}, \text{gorna}]$ i zwraca:

* `dolna`, jeśli $x < \text{dolna}$,
* `gorna`, jeśli $x > \text{gorna}$,
* samo `x` w pozostałych przypadkach (gdy $\text{dolna} \le x \le \text{gorna}$).

Program wczytuje `x`, `dolna` i `gorna`, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: liczba całkowita `x`
* 2. linia: liczba całkowita `dolna` — lewy koniec przedziału
* 3. linia: liczba całkowita `gorna` — prawy koniec przedziału

### Wyjście

Jedna liczba całkowita: wartość `x` ograniczona do przedziału $[\text{dolna}, \text{gorna}]$.

### Ograniczenia

* $\text{dolna} \le \text{gorna}$
* $-10^9 \le x, \text{dolna}, \text{gorna} \le 10^9$

### Przykład

**Wejście:**

```
15
0
10
```

**Wyjście:**

```
10
```

Liczba $15$ wychodzi poza przedział $[0, 10]$ z prawej strony, więc zostaje zastąpiona prawym końcem — $10$.

### Uwagi

* Funkcja przydaje się np. w grach, gdy pozycja postaci nie może wyjść poza planszę, albo gdy głośność ma się mieścić w zakresie od $0$ do $100$.
* Całe ciało funkcji da się zapisać jednym wyrażeniem złożonym z minimum i maksimum dwóch liczb: najpierw $\max(x, \text{dolna})$, a z tego wyniku $\min(\ldots, \text{gorna})$. Możesz skorzystać z funkcji `min_z_dwoch` z zadania ZAD-04A.

### Kod startowy

```python
def ogranicz(x, dolna, gorna):
    # Uzupełnij funkcję.
    pass


x = int(input())
dolna = int(input())
gorna = int(input())
print(ogranicz(x, dolna, gorna))
```

---

## ZAD-04C — Środkowa z trzech liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `min`, `max`, `warunki`

### Treść

Napisz funkcję `srodkowa_z_trzech(a, b, c)`, która zwraca **środkową** z trzech liczb naturalnych, czyli tę, która po ustawieniu liczb od najmniejszej do największej znajdzie się w środku (tzw. medianę trzech liczb).

Program wczytuje `a`, `b` i `c`, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: liczba naturalna `a`
* 2. linia: liczba naturalna `b`
* 3. linia: liczba naturalna `c`

### Wyjście

Jedna liczba naturalna: środkowa z liczb `a`, `b`, `c`.

### Ograniczenia

* $a \ge 0$, $b \ge 0$, $c \ge 0$

### Przykład

**Wejście:**

```
3
1
2
```

**Wyjście:**

```
2
```

Po uporządkowaniu liczby tworzą ciąg $1, 2, 3$ — w środku stoi $2$.

### Uwagi

* Liczby mogą się powtarzać: dla `5`, `5`, `1` uporządkowany ciąg to $1, 5, 5$, więc wynikiem jest `5`.
* Nie sortuj liczb — wystarczą porównania. Liczba `a` jest środkowa, jeśli $b \le a \le c$ albo $c \le a \le b$; podobnie sprawdzisz `b`, a jeśli żadna z nich nie jest środkowa, zostaje `c`.
* Inny sposób: suma trzech liczb minus najmniejsza i minus największa z nich to właśnie liczba środkowa.

### Kod startowy

```python
def srodkowa_z_trzech(a, b, c):
    # Uzupełnij funkcję.
    pass


a = int(input())
b = int(input())
c = int(input())
print(srodkowa_z_trzech(a, b, c))
```

---

## ZAD-04D — Maksimum z trzech liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `max`

### Treść

Napisz funkcję `max_z_trzech(a, b, c)`, która zwraca największą z trzech liczb naturalnych.

Program wczytuje `a`, `b` i `c`, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: liczba naturalna `a`
* 2. linia: liczba naturalna `b`
* 3. linia: liczba naturalna `c`

### Wyjście

Jedna liczba naturalna: największa z liczb `a`, `b`, `c`.

### Ograniczenia

* $a \ge 0$, $b \ge 0$, $c \ge 0$

### Przykład

**Wejście:**

```
3
2
1
```

**Wyjście:**

```
3
```

### Uwagi

* Pamiętaj o przypadku, gdy dwie lub trzy liczby są równe.
* Wewnątrz funkcji możesz wywołać inną funkcję. Napisz najpierw pomocniczą funkcję `max_z_dwoch(a, b)` (analogiczną do `min_z_dwoch` z zadania ZAD-04A) i wywołaj ją dwa razy.

### Kod startowy

```python
def max_z_trzech(a, b, c):
    # Uzupełnij funkcję.
    pass


a = int(input())
b = int(input())
c = int(input())
print(max_z_trzech(a, b, c))
```

---

## ZAD-05 — Zamiana wartości miejscami

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `krotka`, `zmienne`

### Treść

Napisz funkcję `zamien_wartosci(a, b)`, która zwraca dwie otrzymane wartości w odwróconej kolejności, czyli parę `(b, a)`.

Program wczytuje `a` i `b`, zamienia ich wartości instrukcją `a, b = zamien_wartosci(a, b)` i wypisuje nowe wartości zmiennych.

### Wejście

* 1. linia: liczba naturalna `a`
* 2. linia: liczba naturalna `b`

### Wyjście

Dwie linie w formacie:

```
a = <nowa wartość a>
b = <nowa wartość b>
```

Nowa wartość `a` to stara wartość `b` i odwrotnie.

### Przykład

**Wejście:**

```
8
5
```

**Wyjście:**

```
a = 5
b = 8
```

### Kod startowy

```python
def zamien_wartosci(a, b):
    # Uzupełnij funkcję: zwróć parę (b, a).
    pass


a = int(input())
b = int(input())
a, b = zamien_wartosci(a, b)
print("a =", a)
print("b =", b)
```

---

## ZAD-06 — Suma cyfr liczby (funkcja)

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `pętle`, `modulo`

### Treść

Napisz funkcję `suma_cyfr(n)`, która zwraca sumę cyfr liczby naturalnej `n`.

Program wczytuje `n`, wywołuje funkcję i wypisuje wynik.

### Wejście

Jedna liczba naturalna `n`.

### Wyjście

Jedna liczba naturalna: suma cyfr liczby `n`.

### Ograniczenia

* $n \ge 0$

### Przykład

**Wejście:**

```
13231
```

**Wyjście:**

```
10
```

$1 + 3 + 2 + 3 + 1 = 10$.

### Uwagi

* Dla $n = 0$ suma cyfr wynosi `0`.
* Ostatnią cyfrę liczby otrzymasz jako `n % 10`, a liczbę bez ostatniej cyfry jako `n // 10`.

### Kod startowy

```python
def suma_cyfr(n):
    # Uzupełnij funkcję.
    pass


n = int(input())
print(suma_cyfr(n))
```

---

## ZAD-07 — Weryfikacja nazwy użytkownika i hasła

**Poziom:** ★★☆
**Tagi:** `funkcje`, `while`, `string`, `porównania`

### Treść

Napisz dwie funkcje:

1. `pobierz_dane()` — wczytuje nazwę użytkownika (login) i hasło, po czym zwraca je jako parę `(login, haslo)`.
2. `sprawdz_dane(poprawny_login, poprawne_haslo)` — w pętli wczytuje kolejne próby logowania (login i hasło), dopóki nie będą identyczne z przekazanymi danymi.
   Po każdej nieudanej próbie wypisuje `Błędne dane. Spróbuj ponownie.`, a po udanej — `Dane poprawne. Dostęp przyznany.` i kończy działanie.

Program najpierw wywołuje `pobierz_dane()`, aby ustalić poprawne dane, a potem przekazuje je do `sprawdz_dane(...)`.

W tym zadaniu funkcje same wczytują dane (`input()`), a `sprawdz_dane` sama wypisuje komunikaty.

### Wejście

* 1. linia: poprawny login
* 2. linia: poprawne hasło
* kolejne linie: próby logowania — po dwie linie na próbę (login, potem hasło)

### Wyjście

Dla każdej nieudanej próby linia:

```
Błędne dane. Spróbuj ponownie.
```

a na końcu (po pierwszej udanej próbie) linia:

```
Dane poprawne. Dostęp przyznany.
```

### Ograniczenia

* Jedna z prób jest poprawna — program nie musi obsługiwać końca danych bez udanej próby.

### Przykład

**Wejście:**

```
admin
1234
root
pass
admin
1234
```

**Wyjście:**

```
Błędne dane. Spróbuj ponownie.
Dane poprawne. Dostęp przyznany.
```

Poprawne dane to `admin` / `1234`. Pierwsza próba (`root` / `pass`) jest błędna, druga — poprawna.

### Uwagi

* Próba jest udana tylko wtedy, gdy zgadzają się **oba** pola: login i hasło.
* Porównanie uwzględnia wielkość liter (`Admin` to nie to samo co `admin`).

### Kod startowy

```python
def pobierz_dane():
    # Wczytaj login i hasło, a następnie zwróć je jako parę.
    pass


def sprawdz_dane(poprawny_login, poprawne_haslo):
    # W pętli wczytuj login i hasło, dopóki nie będą poprawne.
    pass


login, haslo = pobierz_dane()
sprawdz_dane(login, haslo)
```


---

## ZAD-08 — Liczby doskonałe, obfite i deficytowe

**Poziom:** ★★☆
**Tagi:** `funkcje`, `pętle`, `dzielniki`

### Treść

**Dzielnik właściwy** liczby naturalnej `n` to jej dzielnik mniejszy od `n` — np. dzielnikami właściwymi liczby `12` są `1`, `2`, `3`, `4` i `6`. Porównując sumę dzielników właściwych z samą liczbą, dzielimy liczby na trzy rodzaje:

* **doskonałe** — suma jest równa `n` (np. $6 = 1 + 2 + 3$),
* **obfite** — suma jest większa od `n` (np. $1 + 2 + 3 + 4 + 6 = 16 > 12$),
* **deficytowe** — suma jest mniejsza od `n` (np. dla `8`: $1 + 2 + 4 = 7 < 8$).

Napisz dwie funkcje:

1. `suma_dzielnikow(n)` — zwraca sumę dzielników właściwych liczby `n`,
2. `rodzaj_liczby(n)` — **wywołuje** funkcję `suma_dzielnikow(n)` i na podstawie jej wyniku zwraca napis `doskonała`, `obfita` albo `deficytowa`.

Program wczytuje `k` liczb i dla każdej wypisuje jej rodzaj.

### Wejście

* 1. linia: `k` — liczba liczb do sprawdzenia
* kolejne `k` linii: liczby naturalne `n` — po jednej w linii

### Wyjście

`k` linii w formacie:

```
<n>: <rodzaj>
```

gdzie `<rodzaj>` to `doskonała`, `obfita` albo `deficytowa` (małymi literami, z polskimi znakami).

### Ograniczenia

* $1 \le k \le 100$
* $1 \le n \le 10000$

### Przykład

**Wejście:**

```
3
6
12
15
```

**Wyjście:**

```
6: doskonała
12: obfita
15: deficytowa
```

Dla `15` suma dzielników właściwych to $1 + 3 + 5 = 9 < 15$.

### Uwagi

* Liczba `1` nie ma dzielników właściwych, więc ich suma wynosi `0` — `1` jest liczbą deficytową.
* Wydzielenie obliczeń do osobnej funkcji sprawia, że `rodzaj_liczby` jest krótka i czytelna, a `suma_dzielnikow` da się sprawdzić i wykorzystać niezależnie.

### Kod startowy

```python
def suma_dzielnikow(n):
    # Uzupełnij funkcję: zwróć sumę dzielników właściwych n.
    pass


def rodzaj_liczby(n):
    # Uzupełnij funkcję: wywołaj suma_dzielnikow(n) i zwróć rodzaj liczby.
    pass


k = int(input())
for _ in range(k):
    n = int(input())
    print(f"{n}: {rodzaj_liczby(n)}")
```

---

## ZAD-09 — Cena końcowa (argumenty domyślne i nazwane)

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `argumenty domyślne`, `argumenty nazwane`, `float`

### Treść

Napisz funkcję `cena_koncowa(netto, vat=23, rabat=0)`, która zwraca cenę brutto towaru po rabacie:

* najpierw od ceny `netto` odejmujemy rabat — `rabat` procent ceny netto,
* potem do tak obniżonej ceny doliczamy podatek VAT — `vat` procent.

Czyli funkcja zwraca $\text{netto} \cdot \left(1 - \frac{\text{rabat}}{100}\right) \cdot \left(1 + \frac{\text{vat}}{100}\right)$ — bez zaokrąglania.

Parametry `vat` i `rabat` mają **wartości domyślne** (23 i 0), więc przy wywołaniu można je pominąć.

Program wczytuje cenę netto oraz rabat i wywołuje funkcję czterema sposobami:

1. `cena_koncowa(netto)` — domyślny VAT 23% i brak rabatu,
2. `cena_koncowa(netto, 8)` — VAT 8% (drugi argument trafia do parametru `vat`), brak rabatu,
3. `cena_koncowa(netto, rabat=rabat)` — domyślny VAT 23% i wczytany rabat,
4. `cena_koncowa(netto, rabat=rabat, vat=5)` — VAT 5% i wczytany rabat.

### Wejście

* 1. linia: cena netto — liczba rzeczywista
* 2. linia: rabat w procentach — liczba całkowita

### Wyjście

Cztery linie — wyniki wywołań 1–4 w tej kolejności, każdy z dokładnością do **dwóch** miejsc po przecinku.

### Ograniczenia

* $\text{netto} \ge 0$
* $0 \le \text{rabat} \le 100$

### Przykład

**Wejście:**

```
100
10
```

**Wyjście:**

```
123.00
108.00
110.70
94.50
```

Np. trzecie wywołanie: $100 \cdot 0.9 = 90$, a $90 \cdot 1.23 = 110.7$.

### Uwagi

* **Argument domyślny** to wartość parametru podana w nagłówku funkcji (`vat=23`). Jeśli przy wywołaniu nie podasz tego argumentu, parametr dostanie wartość domyślną.
* **Argument nazwany** podajesz w postaci `nazwa=wartość`, np. `cena_koncowa(100, rabat=10)`. Dzięki temu możesz pominąć `vat`, a ustawić `rabat`. Kolejność argumentów nazwanych jest dowolna: `cena_koncowa(100, rabat=10, vat=5)` to to samo co `cena_koncowa(100, vat=5, rabat=10)`.
* Argumenty podane bez nazwy (pozycyjne) trafiają do parametrów po kolei: w `cena_koncowa(100, 8)` liczba `8` to `vat`.

### Kod startowy

```python
def cena_koncowa(netto, vat=23, rabat=0):
    # Uzupełnij funkcję: zwróć cenę brutto po rabacie.
    pass


netto = float(input())
rabat = int(input())
print(f"{cena_koncowa(netto):.2f}")
print(f"{cena_koncowa(netto, 8):.2f}")
print(f"{cena_koncowa(netto, rabat=rabat):.2f}")
print(f"{cena_koncowa(netto, rabat=rabat, vat=5):.2f}")
```

---

## ZAD-10 — Średnia z dowolnej liczby argumentów

**Poziom:** ★★☆
**Tagi:** `funkcje`, `*args`, `krotka`, `float`

### Treść

Napisz funkcję `srednia(*liczby)`, którą można wywołać z **dowolną liczbą argumentów** — np. `srednia(2, 4)`, `srednia(1, 2, 3, 4, 5)` albo `srednia()`. Funkcja zwraca średnią arytmetyczną otrzymanych liczb, a jeśli nie dostała żadnego argumentu — zwraca `None`.

Program wczytuje linię z liczbami, przekazuje je do funkcji jako osobne argumenty (`srednia(*liczby)`) i wypisuje wynik.

### Wejście

Jedna linia: zero lub więcej liczb rzeczywistych oddzielonych spacjami. Pusta linia oznacza brak liczb.

### Wyjście

Jedna linia:

* średnia z dokładnością do **dwóch** miejsc po przecinku albo
* `Brak danych`, jeśli funkcja zwróciła `None`.

### Przykład

**Wejście:**

```
2 4 9
```

**Wyjście:**

```
5.00
```

$\frac{2 + 4 + 9}{3} = 5$.

### Uwagi

* Gwiazdka w nagłówku `def srednia(*liczby):` sprawia, że wszystkie argumenty wywołania trafiają do jednej **krotki** `liczby`. Np. po wywołaniu `srednia(2, 4, 9)` zmienna `liczby` to `(2, 4, 9)`, a po `srednia()` — pusta krotka `()`.
* Po krotce przejdziesz pętlą `for x in liczby:`, a liczbę jej elementów poda `len(liczby)`.
* Gwiazdka przy wywołaniu działa odwrotnie: `srednia(*liczby)` „rozpakowuje” listę `liczby` na osobne argumenty.
* Linia `liczby = [float(x) for x in input().split()]` w kodzie startowym zamienia wczytaną linię na listę liczb — listy poznasz dokładnie w rozdziale 9.
* `None` to specjalna wartość oznaczająca „brak wyniku”. Sprawdzamy ją warunkiem `wynik is None`.

### Kod startowy

```python
def srednia(*liczby):
    # Uzupełnij funkcję: zwróć średnią albo None.
    pass


liczby = [float(x) for x in input().split()]
wynik = srednia(*liczby)
if wynik is None:
    print("Brak danych")
else:
    print(f"{wynik:.2f}")
```

---

## ZAD-11 — Funkcja sprawdzona testami (assert)

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `assert`, `testy`, `bool`

### Treść

Napisz funkcję `czy_przestepny(rok)`, która zwraca `True`, jeśli `rok` jest przestępny, a `False` w przeciwnym razie.

Rok jest przestępny, jeśli jest podzielny przez 4, ale nie przez 100 — albo jeśli jest podzielny przez 400.

Kod startowy zawiera pięć **testów** funkcji zapisanych instrukcją `assert`. Są wykonywane, zanim program zacznie wczytywać dane. Następnie program wczytuje `n` lat i dla każdego wypisuje `Tak` (rok przestępny) albo `Nie`.

### Wejście

* 1. linia: liczba lat `n`
* kolejne `n` linii: lata — po jednej liczbie naturalnej w linii

### Wyjście

`n` linii — dla każdego roku `Tak` albo `Nie`.

### Ograniczenia

* $n \ge 1$
* $1 \le \text{rok} \le 10000$

### Przykład

**Wejście:**

```
3
2024
1900
2000
```

**Wyjście:**

```
Tak
Nie
Tak
```

Rok 1900 jest podzielny przez 100, ale nie przez 400, więc nie jest przestępny.

### Uwagi

* `assert warunek` nie robi nic, jeśli warunek jest prawdziwy. Jeśli jest fałszywy, program **natychmiast się zatrzymuje** z błędem `AssertionError`. Dzięki temu od razu widać, że funkcja działa źle.
* Gdy test się nie powiedzie, zobaczysz komunikat w rodzaju:

  ```
  Traceback (most recent call last):
    File "main.py", line 9, in <module>
      assert czy_przestepny(1900) == False
  AssertionError
  ```

  Czytaj go od dołu: `AssertionError` mówi, że nie powiódł się test, a linia nad nim (i jej numer, zależny od Twojego kodu) pokazuje, który — tutaj funkcja zwróciła złą odpowiedź dla roku 1900. Popraw funkcję i uruchom program ponownie.
* Do testu możesz dopisać komunikat, który pojawi się przy błędzie: `assert czy_przestepny(1900) == False, "1900 nie jest przestępny"`.
* Nie usuwaj testów — możesz za to dopisać własne.

### Kod startowy

```python
def czy_przestepny(rok):
    # Uzupełnij funkcję: zwróć True albo False.
    pass


# Testy funkcji: jeśli któryś się nie powiedzie, program zatrzyma się z błędem AssertionError.
assert czy_przestepny(2024) == True
assert czy_przestepny(2023) == False
assert czy_przestepny(1900) == False
assert czy_przestepny(2000) == True
assert czy_przestepny(2100) == False

n = int(input())
for _ in range(n):
    rok = int(input())
    if czy_przestepny(rok):
        print("Tak")
    else:
        print("Nie")
```
