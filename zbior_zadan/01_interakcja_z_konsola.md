# Rozdział 1: Interakcja z konsolą

Poniższe zadania polegają na wczytywaniu danych ze **standardowego wejścia** (stdin) i wypisywaniu wyniku na **standardowe wyjście** (stdout).
**Każde zadanie (oraz każdy podpunkt w zadaniach wieloczęściowych, np. ZAD-05A … ZAD-05E) jest osobnym, niezależnym programem.**

**Konwencje wspólne:**

* Każda wartość wejściowa znajduje się w osobnej linii — wczytuj je dokładnie w podanej kolejności (np. `float(input())`).
* Jeśli w danych wyjściowych jest „każda w oddzielnej linii” — po każdym wyniku wypisz znak nowej linii.
* „Do 3 miejsc po przecinku” oznacza wypisanie liczby z **dokładnie** trzema cyframi po kropce, np. `f"{y:.3f}"` (`19.000`, `-2.500`). Analogicznie dla 2 miejsc.
* Program nie wypisuje komunikatów typu „Podaj liczbę:”. Tekst podany w `input("…")` jest ignorowany przez sprawdzarkę.

---

## ZAD-01 — Wypisywanie tekstu na ekran

**Poziom:** ★☆☆
**Tagi:** `I/O`, `print`, `string`

### Treść

Napisz program, który wypisze dokładnie:
`Witaj, świecie!`

### Wejście

Brak.

### Wyjście

Jedna linia: `Witaj, świecie!`

### Przykład

**Wejście:** *(brak)*

**Wyjście:**

```
Witaj, świecie!
```

### Uwagi

* Tekst musi być identyczny (łącznie z polskimi znakami, przecinkiem, spacją i wykrzyknikiem).

---

## ZAD-02 — Zamiana kolejności liczb

**Poziom:** ★☆☆
**Tagi:** `I/O`, `zmienne`

### Treść

Wczytaj dwie liczby całkowite i wypisz je w odwrotnej kolejności (każdą w osobnej linii).

### Wejście

* 1. linia: `a` — liczba całkowita
* 2. linia: `b` — liczba całkowita

### Wyjście

Dwie linie:

* 1. linia: `b`
* 2. linia: `a`

### Ograniczenia

* $-10^9 \le a, b \le 10^9$

### Przykład

**Wejście:**

```
-7
4
```

**Wyjście:**

```
4
-7
```

---

## ZAD-03 — Rysowanie kształtów znakami

**Poziom:** ★☆☆
**Tagi:** `print`, `formatowanie`, `string`

### Treść

Wypisz na wyjście trzy kształty:

1. **Kwadrat 2×2** z liter `x`.
2. **Trójkąt liczbowy** z 3 linii: w linii numer `i` wypisz `i` razy cyfrę `i` (dla `i` = 1, 2, 3).
3. **Romb z jedynek** o maksymalnej szerokości 5 znaków.

Kształty oddziel **dokładnie jedną pustą linią**.

### Wejście

Brak.

### Wyjście

Dokładnie 12 linii:

* 2 linie kwadratu,
* pusta linia,
* 3 linie trójkąta,
* pusta linia,
* 5 linii rombu.

### Przykład

**Wejście:** *(brak)*

**Wyjście:**

```
xx
xx

1
22
333

  1
 111
11111
 111
  1
```

### Uwagi

* W rombie spacje na **początku** linii są istotne (spacje na końcu linii są ignorowane).
* Nie dodawaj pustych linii na początku wyjścia.

---

## ZAD-04 — Podstawowe operacje arytmetyczne

**Poziom:** ★☆☆
**Tagi:** `arytmetyka`, `I/O`

### Treść

Wczytaj dwie liczby naturalne `a` i `b` i wypisz kolejno:

1. sumę $a + b$,
2. różnicę $a - b$,
3. iloczyn $a \cdot b$,
4. iloraz całkowity $\lfloor a / b \rfloor$ (w Pythonie `a // b`),
5. resztę z dzielenia `a` przez `b` (w Pythonie `a % b`),
6. potęgę $a^b$ (w Pythonie `a ** b`).

### Wejście

* 1. linia: `a` — liczba całkowita
* 2. linia: `b` — liczba całkowita

### Wyjście

6 linii — wyniki działań w kolejności 1–6, każdy jako liczba całkowita.

### Ograniczenia

* $0 \le a \le 1000$
* $1 \le b \le 10$ (dzięki temu dzielenie i reszta są zawsze poprawne)
* $a^b \le 10^{18}$

### Przykład

**Wejście:**

```
3
2
```

**Wyjście:**

```
5
1
6
1
1
9
```

---

## ZAD-05A — Funkcja liniowa: y = 3x + 10

**Poziom:** ★☆☆
**Tagi:** `arytmetyka`, `float`, `formatowanie`

### Treść

Wczytaj liczbę rzeczywistą $x$ i oblicz wartość funkcji $y = 3x + 10$.

### Wejście

* 1 linia: `x` — liczba całkowita lub zmiennoprzecinkowa

### Wyjście

Jedna linia: `y` do **3 miejsc po przecinku**.

### Ograniczenia

* $-1000 \le x \le 1000$

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
19.000
```

---

## ZAD-05B — Funkcja liniowa: y = ax + b

**Poziom:** ★☆☆
**Tagi:** `arytmetyka`, `float`

### Treść

Wczytaj współczynniki $a$, $b$ oraz argument $x$ i oblicz wartość funkcji liniowej $y = ax + b$.

### Wejście

3 liczby rzeczywiste, każda w osobnej linii:

* 1. linia: `a`
* 2. linia: `b`
* 3. linia: `x`

### Wyjście

Jedna linia: `y` do **3 miejsc po przecinku**.

### Ograniczenia

* $-1000 \le a, b, x \le 1000$

### Przykład

**Wejście:**

```
1
2
3
```

**Wyjście:**

```
5.000
```

---

## ZAD-05C — Funkcja sześcienna: y = x³ + 2

**Poziom:** ★☆☆
**Tagi:** `potęgi`, `float`

### Treść

Wczytaj liczbę rzeczywistą $x$ i oblicz $y = x^3 + 2$.

### Wejście

* 1 linia: `x` — liczba rzeczywista

### Wyjście

Jedna linia: `y` do **3 miejsc po przecinku**.

### Ograniczenia

* $-100 \le x \le 100$

### Przykład

**Wejście:**

```
5
```

**Wyjście:**

```
127.000
```

---

## ZAD-05D — Wielomian z potęgami: y = a·x^m + b·x^n + c − a

**Poziom:** ★☆☆
**Tagi:** `potęgi`, `float`

### Treść

Wczytaj współczynniki $a$, $b$, $c$, wykładniki $m$, $n$ oraz argument $x$ i oblicz:

$y = a \cdot x^m + b \cdot x^n + c - a$

### Wejście

6 liczb, każda w osobnej linii:

* 1. linia: `a` — liczba rzeczywista
* 2. linia: `b` — liczba rzeczywista
* 3. linia: `c` — liczba rzeczywista
* 4. linia: `m` — liczba całkowita nieujemna
* 5. linia: `n` — liczba całkowita nieujemna
* 6. linia: `x` — liczba rzeczywista

### Wyjście

Jedna linia: `y` do **3 miejsc po przecinku**.

### Ograniczenia

* $-100 \le a, b, c, x \le 100$
* $0 \le m, n \le 5$ (liczby całkowite)
* Jeśli $x = 0$, to $m, n \ge 1$ (nie pojawia się wyrażenie $0^0$).

### Przykład

**Wejście:**

```
1
1
1
1
1
1
```

**Wyjście:**

```
2.000
```

Dla $a = b = c = m = n = x = 1$: $y = 1 \cdot 1^1 + 1 \cdot 1^1 + 1 - 1 = 2$.

---

## ZAD-05E — Funkcja z trygonometrią, wykładniczą i logarytmem

**Poziom:** ★★☆
**Tagi:** `math`, `trygonometria`, `log`, `exp`, `float`

### Treść

Wczytaj liczbę rzeczywistą $x$ (kąt w radianach) i oblicz:

$y = \sin^3(x) \cdot \cos^2(x) + e^{x^2} + \ln(x^3 + 2x^2 - x - 3)$

gdzie $\ln$ oznacza logarytm naturalny, a $e$ — podstawę logarytmu naturalnego.

### Wejście

* 1 linia: `x` — liczba zmiennoprzecinkowa (w radianach)

### Wyjście

Jedna linia: `y` do **3 miejsc po przecinku**.

### Ograniczenia

* $1.2 \le x \le 3$, więc spełniony jest warunek dziedziny logarytmu $x^3 + 2x^2 - x - 3 > 0$.

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
57.126
```

### Uwagi

* Skorzystaj z modułu `math`: `math.sin`, `math.cos`, `math.exp`, `math.log` (logarytm naturalny).

---

## ZAD-06A — Kilogramy → gramy

**Poziom:** ★☆☆
**Tagi:** `konwersje`

### Treść

Wczytaj masę w kilogramach `kg` i przelicz ją na gramy: $g = kg \cdot 1000$.

### Wejście

* 1 linia: `kg` — liczba całkowita lub zmiennoprzecinkowa

### Wyjście

Jedna linia: `g` jako **liczba całkowita** (bez części ułamkowej).

### Ograniczenia

* $0 \le kg \le 10^6$
* `kg` ma co najwyżej 3 cyfry po przecinku, więc wynik w gramach jest całkowity.

### Przykład

**Wejście:**

```
2.5
```

**Wyjście:**

```
2500
```

### Uwagi

* Uwaga na błędy zaokrągleń liczb zmiennoprzecinkowych: np. `1.001 * 1000` daje w Pythonie `1000.9999999999999`, więc `int(...)` zwróciłoby `1000`. Zamiast obcinać, zaokrąglij wynik: `round(kg * 1000)`.

---

## ZAD-06B — Cale → centymetry

**Poziom:** ★☆☆
**Tagi:** `konwersje`, `float`

### Treść

Wczytaj długość w calach `inch` i przelicz ją na centymetry: $cm = inch \cdot 2.54$.

### Wejście

* 1 linia: `inch` — liczba rzeczywista, $inch \ge 0$

### Wyjście

Jedna linia: `cm` do **2 miejsc po przecinku**.

### Przykład

**Wejście:**

```
10
```

**Wyjście:**

```
25.40
```

---

## ZAD-06C — Sekundy → pełne godziny

**Poziom:** ★☆☆
**Tagi:** `dzielenie całkowite`

### Treść

Wczytaj liczbę sekund `s` i wypisz, ile **pełnych godzin** się w niej mieści (godzina ma 3600 sekund).

### Wejście

* 1 linia: `s` — liczba całkowita, $0 \le s \le 10^9$

### Wyjście

Jedna linia: liczba pełnych godzin, czyli $\lfloor s / 3600 \rfloor$ (w Pythonie `s // 3600`).

### Przykład

**Wejście:**

```
8639
```

**Wyjście:**

```
2
```

8639 sekund to 2 godziny i 1439 sekund, więc pełne godziny są 2.

---

## ZAD-06D — Euro → złotówki (kurs stały)

**Poziom:** ★☆☆
**Tagi:** `konwersje`, `float`

### Treść

Wczytaj kwotę w euro `eur` i przelicz ją na złotówki przy stałym kursie 4,40 zł za 1 euro: $pln = eur \cdot 4.4$.

### Wejście

* 1 linia: `eur` — liczba rzeczywista, $eur \ge 0$

### Wyjście

Jedna linia: `pln` do **2 miejsc po przecinku**.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
13.20
```

---

## ZAD-06E — Stopnie → radiany

**Poziom:** ★☆☆
**Tagi:** `pi`, `float`

### Treść

Wczytaj kąt w stopniach `deg` i przelicz go na radiany: $rad = \frac{deg \cdot \pi}{180}$.

### Wejście

* 1 linia: `deg` — liczba rzeczywista

### Wyjście

Jedna linia: `rad` do **3 miejsc po przecinku**.

### Przykład

**Wejście:**

```
180
```

**Wyjście:**

```
3.142
```

### Uwagi

* Wartość $\pi$ weź z modułu `math` (`math.pi`).

---

## ZAD-06F — Fahrenheit → Celsius i Kelviny

**Poziom:** ★☆☆
**Tagi:** `konwersje`, `float`

### Treść

Wczytaj temperaturę w stopniach Fahrenheita $F$. Oblicz temperaturę w stopniach Celsjusza oraz w kelwinach:

* $C = \frac{5}{9} (F - 32)$
* $K = C + 273.15$

### Wejście

* 1 linia: `F` — liczba rzeczywista

### Wyjście

Dwie linie:

1. `C` do **3 miejsc po przecinku**,
2. `K` do **3 miejsc po przecinku**.

### Przykład

**Wejście:**

```
32
```

**Wyjście:**

```
0.000
273.150
```

### Uwagi

* `K` obliczaj z niezaokrąglonej wartości `C` — zaokrąglaj dopiero przy wypisywaniu.

---

## ZAD-07A — Pole trójkąta

**Poziom:** ★☆☆
**Tagi:** `geometria`, `float`

### Treść

Wczytaj długość podstawy $a$ i wysokość $h$ trójkąta i oblicz jego pole ze wzoru $P = \frac{1}{2} a h$.

### Wejście

* 1. linia: `a` — liczba rzeczywista, $a > 0$
* 2. linia: `h` — liczba rzeczywista, $h > 0$

### Wyjście

Jedna linia: `P` do **3 miejsc po przecinku**.

### Przykład

**Wejście:**

```
6
4
```

**Wyjście:**

```
12.000
```

---

## ZAD-07B — Pole prostokąta

**Poziom:** ★☆☆
**Tagi:** `geometria`, `float`

### Treść

Wczytaj długości boków prostokąta $a$ i $b$ i oblicz jego pole ze wzoru $P = a b$.

### Wejście

* 1. linia: `a` — liczba rzeczywista, $a > 0$
* 2. linia: `b` — liczba rzeczywista, $b > 0$

### Wyjście

Jedna linia: `P` do **3 miejsc po przecinku**.

### Przykład

**Wejście:**

```
2.5
4
```

**Wyjście:**

```
10.000
```

---

## ZAD-07C — Pole rombu

**Poziom:** ★☆☆
**Tagi:** `geometria`, `float`

### Treść

Wczytaj długości przekątnych rombu $d_1$ i $d_2$ i oblicz jego pole ze wzoru $P = \frac{1}{2} d_1 d_2$.

### Wejście

* 1. linia: `d1` — liczba rzeczywista, $d_1 > 0$
* 2. linia: `d2` — liczba rzeczywista, $d_2 > 0$

### Wyjście

Jedna linia: `P` do **3 miejsc po przecinku**.

### Przykład

**Wejście:**

```
10
6
```

**Wyjście:**

```
30.000
```

---

## ZAD-07D — Objętość kuli

**Poziom:** ★☆☆
**Tagi:** `geometria`, `pi`, `float`

### Treść

Wczytaj promień kuli $r$ i oblicz jej objętość ze wzoru $V = \frac{4}{3}\pi r^3$.

### Wejście

* 1 linia: `r` — liczba rzeczywista, $r > 0$

### Wyjście

Jedna linia: `V` do **3 miejsc po przecinku**.

### Przykład

**Wejście:**

```
1
```

**Wyjście:**

```
4.189
```

---

## ZAD-07E — Objętość stożka

**Poziom:** ★☆☆
**Tagi:** `geometria`, `pi`, `float`

### Treść

Wczytaj promień podstawy $r$ i wysokość $h$ stożka i oblicz jego objętość ze wzoru $V = \frac{1}{3}\pi r^2 h$.

### Wejście

* 1. linia: `r` — liczba rzeczywista, $r > 0$
* 2. linia: `h` — liczba rzeczywista, $h > 0$

### Wyjście

Jedna linia: `V` do **3 miejsc po przecinku**.

### Przykład

**Wejście:**

```
2
3
```

**Wyjście:**

```
12.566
```

---

## ZAD-07F — Objętość prostopadłościanu

**Poziom:** ★☆☆
**Tagi:** `geometria`, `float`

### Treść

Wczytaj długości krawędzi prostopadłościanu $a$, $b$, $c$ i oblicz jego objętość ze wzoru $V = a b c$.

### Wejście

* 1. linia: `a` — liczba rzeczywista, $a > 0$
* 2. linia: `b` — liczba rzeczywista, $b > 0$
* 3. linia: `c` — liczba rzeczywista, $c > 0$

### Wyjście

Jedna linia: `V` do **3 miejsc po przecinku**.

### Przykład

**Wejście:**

```
2
3
4
```

**Wyjście:**

```
24.000
```

---

## ZAD-08 — Koszt pokrycia podłogi płytkami

**Poziom:** ★★☆
**Tagi:** `ceil`, `arytmetyka`, `formatowanie`, `geometria`

### Treść

Dane są:

* cena jednej płytki `p` (w złotych),
* bok kwadratowej płytki `t` (w centymetrach),
* długość podłogi `L` (w centymetrach),
* szerokość podłogi `W` (w centymetrach).

Płytki układamy w prostokątną siatkę równolegle do ścian. Wzdłuż każdego wymiaru liczbę płytek zaokrąglamy **w górę** (ostatnią płytkę w rzędzie się docina, ale trzeba ją kupić w całości):

* $n_L = \lceil L / t \rceil$
* $n_W = \lceil W / t \rceil$
* liczba płytek: $n = n_L \cdot n_W$

Oblicz całkowity koszt zakupu płytek: $n \cdot p$.

### Wejście

4 liczby, każda w osobnej linii:

* 1. linia: `p` — liczba rzeczywista
* 2. linia: `t` — liczba całkowita
* 3. linia: `L` — liczba całkowita
* 4. linia: `W` — liczba całkowita

### Wyjście

Jedna linia: całkowity koszt do **2 miejsc po przecinku**.

### Ograniczenia

* $0 < p \le 1000$
* $1 \le t, L, W \le 10^4$

### Przykład

**Wejście:**

```
2
3
20
40
```

**Wyjście:**

```
196.00
```

$n_L = \lceil 20 / 3 \rceil = 7$, $n_W = \lceil 40 / 3 \rceil = 14$, więc potrzeba $7 \cdot 14 = 98$ płytek, które kosztują $98 \cdot 2 = 196$ zł.

### Uwagi

* Zaokrąglenie w górę daje funkcja `math.ceil`.

---

## ZAD-09 — Kalkulator kredytowy

**Poziom:** ★★☆
**Tagi:** `finanse`, `float`, `formatowanie`

### Treść

Wczytaj:

* roczną stopę procentową $R$ (w procentach),
* okres spłaty $Y$ (w latach),
* kwotę kredytu $P$.

Oblicz miesięczną ratę $M$ oraz całkowity koszt kredytu $C = M \cdot n$, gdzie $n = 12 \cdot Y$ to liczba rat.

Dla $R > 0$ użyj wzoru na ratę stałą (annuitetową):

$M = P \cdot \frac{r(1+r)^n}{(1+r)^n - 1}$

gdzie $r = \frac{R}{12 \cdot 100}$ to miesięczna stopa procentowa.

Dla $R = 0$ przyjmij $M = \frac{P}{n}$.

### Wejście

3 liczby, każda w osobnej linii:

* 1. linia: `R` — liczba rzeczywista, $R \ge 0$
* 2. linia: `Y` — liczba całkowita, $Y > 0$
* 3. linia: `P` — liczba rzeczywista, $P > 0$

### Wyjście

Dwie linie, obie do **2 miejsc po przecinku**:

1. miesięczna rata `M`,
2. całkowity koszt `C`.

### Ograniczenia

* $0 \le R \le 30$
* $1 \le Y \le 40$
* $0 < P \le 10^7$

### Przykład

**Wejście:**

```
3.5
8
12000
```

**Wyjście:**

```
143.50
13775.68
```

Niezaokrąglona rata to $M \approx 143.4966$, więc $C = 96 \cdot 143.4966\ldots \approx 13775.68$.

### Uwagi

* Koszt `C` obliczaj z **niezaokrąglonej** raty `M` (nie z wartości `143.50`). Zaokrąglaj dopiero przy wypisywaniu.

---

## ZAD-10 — Sekundy → format GG:MM:SS

**Poziom:** ★☆☆
**Tagi:** `dzielenie całkowite`, `modulo`, `formatowanie`

### Treść

Wczytaj liczbę sekund `s` i zapisz ją jako czas w formacie `GG:MM:SS`: pełne godziny, pozostałe pełne minuty (0–59) i pozostałe sekundy (0–59). Każdą część wypisz jako **dwie cyfry** — w razie potrzeby z zerem wiodącym (np. `07`).

### Wejście

* 1 linia: `s` — liczba całkowita, $0 \le s < 360000$

### Wyjście

Jedna linia: czas w formacie `GG:MM:SS`.

### Przykład

**Wejście:**

```
3725
```

**Wyjście:**

```
01:02:05
```

$3725 = 1 \cdot 3600 + 2 \cdot 60 + 5$, czyli 1 godzina, 2 minuty i 5 sekund.

### Uwagi

* Wbudowana funkcja `divmod(a, b)` zwraca naraz iloraz całkowity i resztę z dzielenia: `godziny, reszta = divmod(s, 3600)` daje to samo co `godziny = s // 3600` oraz `reszta = s % 3600`.
* Liczbę z zerem wiodącym wypiszesz formatowaniem `:02d`, np. `f"{5:02d}"` daje `05`, a `f"{12:02d}"` daje `12`.
* Ograniczenie $s < 360000$ gwarantuje, że godzin jest co najwyżej 99, czyli zawsze wystarczą dwie cyfry.
