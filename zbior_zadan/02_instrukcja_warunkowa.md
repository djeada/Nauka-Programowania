# Rozdział 2: Instrukcja warunkowa (if / else)

Zadania w tym rozdziale ćwiczą podejmowanie decyzji w programie na podstawie warunków.

**Konwencje wspólne:**

* Każde zadanie jest **osobnym programem**: czyta **standardowe wejście** i wypisuje wynik na **standardowe wyjście**.
* Dane wejściowe wczytuj dokładnie w podanej kolejności, każdą wartość z osobnej linii (o ile nie napisano inaczej).
* Wyniki wypisuj dokładnie jak w specyfikacji (w tym wielkość liter, polskie znaki, kropki, spacje).
* Jeżeli zadanie mówi „nie wypisuj nic” — program ma zakończyć się bez żadnego wyjścia (bez spacji, bez pustej linii).
* Program nie wypisuje komunikatów typu „Podaj liczbę:”. Tekst podany w `input("…")` jest ignorowany przez sprawdzarkę.

---

## ZAD-01 — Liczba większa od 5

**Poziom:** ★☆☆
**Tagi:** `if`, `porównania`, `I/O`

### Treść

Wczytaj jedną liczbę naturalną `n`.
Jeśli $n > 5$, wypisz `n`. W przeciwnym razie nie wypisuj nic.

### Wejście

* 1 linia: `n` — liczba całkowita, $0 \le n \le 10^9$

### Wyjście

* Jeśli $n > 5$: jedna linia z liczbą `n`.
* Jeśli $n \le 5$: brak wyjścia.

### Przykład 1

**Wejście:**

```
10
```

**Wyjście:**

```
10
```

### Przykład 2

**Wejście:**

```
3
```

**Wyjście:** *(brak)*

---

## ZAD-02 — Porównanie dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `if-else`, `równość`, `string`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`.
Jeśli są równe, wypisz:
`Liczby są identyczne.`
W przeciwnym razie wypisz:
`Liczby są różne.`

### Wejście

* 1 linia: `a` — liczba całkowita, $0 \le a \le 10^9$
* 2 linia: `b` — liczba całkowita, $0 \le b \le 10^9$

### Wyjście

Jedna linia — dokładnie jeden z komunikatów.

### Przykład 1

**Wejście:**

```
7
4
```

**Wyjście:**

```
Liczby są różne.
```

### Przykład 2

**Wejście:**

```
5
5
```

**Wyjście:**

```
Liczby są identyczne.
```

---

## ZAD-03 — Określanie znaku liczby

**Poziom:** ★☆☆
**Tagi:** `if-elif-else`, `porównania`, `string`

### Treść

Wczytaj liczbę całkowitą `x` i wypisz jeden z komunikatów:

* dla $x < 0$: `Liczba jest ujemna.`
* dla $x > 0$: `Liczba jest dodatnia.`
* dla $x = 0$: `Liczba jest zerem.`

### Wejście

* 1 linia: `x` — liczba całkowita, $-10^9 \le x \le 10^9$

### Wyjście

Jedna linia — dokładnie jeden komunikat.

### Przykład 1

**Wejście:**

```
-5
```

**Wyjście:**

```
Liczba jest ujemna.
```

### Przykład 2

**Wejście:**

```
2
```

**Wyjście:**

```
Liczba jest dodatnia.
```

---

## ZAD-04 — Maksimum i minimum z dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `max`, `min`, `if`, `formatowanie`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`.
Wypisz je w jednej linii w kolejności: **najpierw większa, potem mniejsza**, oddzielone pojedynczą spacją.
Jeśli $a = b$, wypisz tę samą liczbę dwa razy.

### Wejście

* 1 linia: `a` — liczba całkowita, $0 \le a \le 10^9$
* 2 linia: `b` — liczba całkowita, $0 \le b \le 10^9$

### Wyjście

Jedna linia: większa liczba, spacja, mniejsza liczba.

### Przykład 1

**Wejście:**

```
1
4
```

**Wyjście:**

```
4 1
```

### Przykład 2

**Wejście:**

```
5
5
```

**Wyjście:**

```
5 5
```

### Uwagi

* Spróbuj rozwiązać zadanie instrukcją `if`, bez wbudowanych funkcji `max` i `min`.

---

## ZAD-05 — Sortowanie trzech liczb

**Poziom:** ★★☆
**Tagi:** `sort`, `warunki`, `porządkowanie`

### Treść

Wczytaj trzy liczby naturalne `a`, `b`, `c` i wypisz je w kolejności niemalejącej (od najmniejszej do największej).

### Wejście

* 1 linia: `a` — liczba całkowita, $0 \le a \le 10^9$
* 2 linia: `b` — liczba całkowita, $0 \le b \le 10^9$
* 3 linia: `c` — liczba całkowita, $0 \le c \le 10^9$

### Wyjście

Jedna linia: trzy liczby w kolejności niemalejącej, oddzielone pojedynczymi spacjami.
Liczby powtarzające się wypisz tyle razy, ile wystąpiły.

### Przykład

**Wejście:**

```
2
1
4
```

**Wyjście:**

```
1 2 4
```

### Uwagi

* Możesz użyć wbudowanego sortowania, ale spróbuj rozwiązać zadanie samymi instrukcjami warunkowymi.

---

## ZAD-06 — Maksimum z czterech liczb

**Poziom:** ★☆☆
**Tagi:** `max`, `if`, `porównania`

### Treść

Wczytaj cztery liczby naturalne i wypisz największą z nich.

### Wejście

4 linie: `a`, `b`, `c`, `d` — liczby całkowite z zakresu $0 \dots 10^9$.

### Wyjście

Jedna linia: największa z czterech liczb.

### Przykład

**Wejście:**

```
2
5
1
4
```

**Wyjście:**

```
5
```

### Uwagi

* Spróbuj rozwiązać zadanie instrukcją `if`, bez wbudowanej funkcji `max`.

---

## ZAD-07 — Prawa logiki (p, q, r)

**Poziom:** ★★☆
**Tagi:** `bool`, `logika`, `tabele prawdy`, `formatowanie`

### Treść

Wczytaj wartości logiczne `p`, `q` i `r` i sprawdź dla nich osiem praw logiki.
Każde prawo to równoważność lewej strony `L` i prawej strony `R`:

1. `Prawo wyłączonego środka` — `L = p or not p`, `R = True`
2. `Prawo niesprzeczności` — `L = not (p and not p)`, `R = True`
3. `Przemienność koniunkcji` — `L = p and q`, `R = q and p`
4. `Przemienność alternatywy` — `L = p or q`, `R = q or p`
5. `Pierwsze prawo de Morgana` — `L = not (p and q)`, `R = not p or not q`
6. `Drugie prawo de Morgana` — `L = not (p or q)`, `R = not p and not q`
7. `Rozdzielność koniunkcji względem alternatywy` — `L = p and (q or r)`, `R = (p and q) or (p and r)`
8. `Rozdzielność alternatywy względem koniunkcji` — `L = p or (q and r)`, `R = (p or q) and (p or r)`

Dla każdego prawa oblicz `L` i `R` dla wczytanych wartości i sprawdź instrukcją `if`, czy są równe.

### Wejście

* 1. linia: `p` — napis `True` albo `False`
* 2. linia: `q` — napis `True` albo `False`
* 3. linia: `r` — napis `True` albo `False`

### Wyjście

8 linii — po jednej dla każdego prawa, w kolejności z listy:

`<nazwa prawa>: L=<L> R=<R> -> równoważne`

gdy `L` jest równe `R`, albo `<nazwa prawa>: L=<L> R=<R> -> nierównoważne` w przeciwnym razie.
`<L>` i `<R>` to dosłownie `True` albo `False`. (Wszystkie prawa z listy są prawdziwe, więc poprawny program zawsze wypisze `równoważne` — różnić się będą wartości `L` i `R`).

### Przykład

**Wejście:**

```
False
True
False
```

**Wyjście:**

```
Prawo wyłączonego środka: L=True R=True -> równoważne
Prawo niesprzeczności: L=True R=True -> równoważne
Przemienność koniunkcji: L=False R=False -> równoważne
Przemienność alternatywy: L=True R=True -> równoważne
Pierwsze prawo de Morgana: L=True R=True -> równoważne
Drugie prawo de Morgana: L=False R=False -> równoważne
Rozdzielność koniunkcji względem alternatywy: L=False R=False -> równoważne
Rozdzielność alternatywy względem koniunkcji: L=False R=False -> równoważne
```

### Uwagi

* `input()` zwraca **napis**. Nie zamieniaj go przez `bool(...)` — `bool("False")` to `True` (każdy niepusty napis jest prawdziwy). Zamiast tego porównaj: `p = input() == "True"`.
* f-string wstawia wartość logiczną jako tekst: `f"L={True}"` daje `L=True`.

### Kod startowy

```python
p = input() == "True"
q = input() == "True"
r = input() == "True"

L = p or not p
R = True
if L == R:
    print(f"Prawo wyłączonego środka: L={L} R={R} -> równoważne")
else:
    print(f"Prawo wyłączonego środka: L={L} R={R} -> nierównoważne")

# Uzupełnij: w ten sam sposób oblicz i wypisz pozostałe siedem praw.
```

---

## ZAD-08 — Czy można zbudować trójkąt?

**Poziom:** ★☆☆
**Tagi:** `if`, `geometria`, `warunek trójkąta`

### Treść

Wczytaj trzy dodatnie długości odcinków `a`, `b`, `c`.
Sprawdź, czy można z nich zbudować trójkąt (niezdegenerowany).

Trójkąt istnieje wtedy i tylko wtedy, gdy spełnione są **wszystkie** trzy nierówności:

* $a + b > c$
* $a + c > b$
* $b + c > a$

Wypisz:

* jeśli tak: `Trójkąt można zbudować z podanych boków.`
* jeśli nie: `Trójkąta nie można zbudować z podanych boków.`

### Wejście

* 1 linia: `a` — liczba całkowita
* 2 linia: `b` — liczba całkowita
* 3 linia: `c` — liczba całkowita

### Wyjście

Jedna linia — dokładnie jeden z komunikatów.

### Ograniczenia

* $1 \le a, b, c \le 10^9$

### Przykład 1

**Wejście:**

```
3
4
5
```

**Wyjście:**

```
Trójkąt można zbudować z podanych boków.
```

### Przykład 2

**Wejście:**

```
1
2
5
```

**Wyjście:**

```
Trójkąta nie można zbudować z podanych boków.
```

### Uwagi

* Jeśli suma dwóch boków jest **równa** trzeciemu (np. 1, 2, 3), odcinki leżą na jednej prostej — taki „trójkąt” nie istnieje.

---

## ZAD-09 — Ocena z punktów

**Poziom:** ★☆☆
**Tagi:** `if-elif-else`, `porównania`, `zakresy`

### Treść

Wczytaj liczbę punktów zdobytych na sprawdzianie i wypisz ocenę według progów:

* 0–49 punktów → `2`
* 50–69 punktów → `3`
* 70–84 punktów → `4`
* 85–100 punktów → `5`

Jeśli liczba punktów jest spoza zakresu 0–100, wypisz:
`Niepoprawna liczba punktów.`

### Wejście

* 1 linia: `punkty` — liczba całkowita, $-1000 \le punkty \le 1000$

### Wyjście

Jedna linia: ocena (`2`, `3`, `4` albo `5`) lub komunikat o błędzie.

### Przykład 1

**Wejście:**

```
77
```

**Wyjście:**

```
4
```

### Przykład 2

**Wejście:**

```
120
```

**Wyjście:**

```
Niepoprawna liczba punktów.
```

### Uwagi

* Najpierw obsłuż punkty spoza zakresu, a potem sprawdzaj progi po kolei w łańcuchu `if`/`elif` — każdy kolejny warunek może wtedy zakładać, że poprzednie nie zaszły.
* Python pozwala łączyć porównania: `50 <= punkty <= 69` znaczy to samo co `50 <= punkty and punkty <= 69`.

---

## ZAD-10 — Prosty kalkulator

**Poziom:** ★★☆
**Tagi:** `if-elif-else`, `arytmetyka`, `string`, `float`

### Treść

Wczytaj liczbę `a`, operator i liczbę `b`, a następnie wypisz wynik działania `a <operator> b`.
Obsługiwane operatory to: `+` (dodawanie), `-` (odejmowanie), `*` (mnożenie), `/` (dzielenie).

Przypadki szczególne:

* jeśli operator to `/`, a $b = 0$, wypisz `Nie można dzielić przez zero.`
* jeśli operator nie jest jednym z czterech powyższych, wypisz `Nieznany operator.` (niezależnie od wartości `b`).

### Wejście

* 1. linia: `a` — liczba rzeczywista
* 2. linia: operator — jeden znak
* 3. linia: `b` — liczba rzeczywista

### Wyjście

Jedna linia: wynik do **2 miejsc po przecinku** (np. `f"{wynik:.2f}"`) albo jeden z komunikatów.

### Ograniczenia

* $-10^6 \le a, b \le 10^6$

### Przykład 1

**Wejście:**

```
7
/
2
```

**Wyjście:**

```
3.50
```

### Przykład 2

**Wejście:**

```
5
/
0
```

**Wyjście:**

```
Nie można dzielić przez zero.
```

### Uwagi

* Operator wczytaj jako napis (`dzialanie = input()`) i porównuj go z napisami, np. `if dzialanie == "+":`.
