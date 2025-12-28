# Rozdział 1: Interakcja z konsolą (stdin/stdout)

Poniższe zadania polegają na wczytywaniu danych ze **standardowego wejścia** (stdin) i wypisywaniu wyniku na **standardowe wyjście** (stdout).
**Każde zadanie (oraz każdy podpunkt w zadaniach wieloczęściowych) jest osobnym, niezależnym programem.**

**Konwencje wspólne:**

* Jeśli w danych wejściowych są liczby w osobnych liniach — wczytuj je dokładnie w tej kolejności.
* Jeśli w danych wyjściowych jest „każda w oddzielnej linii” — po każdym wyniku wypisz znak nowej linii.
* Dla liczb zmiennoprzecinkowych stosuj formatowanie zgodne z poleceniem (np. `%.3f`, `format(x, ".3f")`).

## ZAD-01 — Wypisywanie tekstu na ekran

**Poziom:** ★☆☆
**Tagi:** `I/O`, `print`, `string`

### Treść

Napisz program, który wypisze dokładnie:
`Witaj, świecie!`

### Wejście

Brak.

### Wyjście

Jedna linia:

* `Witaj, świecie!`

### Przykład

**Wyjście:**

```
Witaj, świecie!
```

### Uwagi o formatowaniu

* Tekst musi być identyczny (łącznie z przecinkiem, spacją i wykrzyknikiem).

---

## ZAD-02 — Zamiana kolejności liczb

**Poziom:** ★☆☆
**Tagi:** `I/O`, `zmienne`

### Treść

Wczytaj dwie liczby całkowite i wypisz je w odwrotnej kolejności (każda w osobnej linii).

### Wejście

Dwie liczby całkowite:

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Dwie linie:

* 1. linia: `b`
* 2. linia: `a`

### Ograniczenia / gwarancje

* `a`, `b` mieszczą się w typowym zakresie int (np. 32-bit).

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
**Tagi:** `print`, `formatowanie`, `pętle`, `string`

### Treść

Wypisz na wyjście trzy kształty:

1. **Kwadrat 2×2** z liter `x`
2. **Trójkąt liczbowy** z 3 linii: w linii `i` wypisz `i` razy cyfrę `i` (dla i=1..3)
3. **Romb z jedynek** o maksymalnej szerokości 5 znaków

Każdy kształt ma być oddzielony **jedną pustą linią**.

### Wejście

Brak.

### Wyjście

Dokładnie:

* 2 linie kwadratu,
* pusta linia,
* 3 linie trójkąta,
* pusta linia,
* 5 linii rombu.

### Przykład (oczekiwane wyjście)

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

### Uwagi o formatowaniu

* W rombie spacje na początku linii są istotne.
* Nie dodawaj dodatkowych pustych linii na początku; jedna na końcu jest zwykle akceptowalna, ale trzymaj się przykładu.

---

## ZAD-04 — Podstawowe operacje arytmetyczne

**Poziom:** ★☆☆
**Tagi:** `arytmetyka`, `I/O`

### Treść

Wczytaj dwie liczby naturalne `a` i `b` i wypisz kolejno:

1. `a + b`
2. `a - b`
3. `a * b`
4. `a // b` (dzielenie całkowite)
5. `a % b`
6. `a^b`

### Wejście

* 1. linia: `a` (liczba całkowita)
* 2. linia: `b` (liczba całkowita)

### Wyjście

6 linii — wyniki działań w kolejności 1–6.

### Ograniczenia / gwarancje

* `a ≥ 0`
* `b > 0` (żeby dzielenie i modulo były poprawne)

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

# Funkcje — zadania niezależne (ZAD-05A … ZAD-05E)

## ZAD-05A — Funkcja liniowa: y = 3x + 10

**Poziom:** ★★☆
**Tagi:** `arytmetyka`, `float`, `formatowanie`

### Wejście

1 liczba: `x` (może być całkowita lub zmiennoprzecinkowa)

### Wyjście

1 liczba: `y` wypisana z dokładnością do **3 miejsc po przecinku**.

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

**Poziom:** ★★☆
**Tagi:** `arytmetyka`, `float`

### Wejście

3 liczby (każda w osobnej linii): `a`, `b`, `x`

### Wyjście

`y` do 3 miejsc po przecinku.

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

**Poziom:** ★★☆
**Tagi:** `potęgi`, `float`

### Treść

Oblicz: `y = x^3 + 22 - 20`, czyli równoważnie `y = x^3 + 2`.

### Wejście

1 liczba: `x`

### Wyjście

`y` do 3 miejsc po przecinku.

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

**Poziom:** ★★☆
**Tagi:** `potęgi`, `float`

### Wejście

6 liczb (w osobnych liniach): `a`, `b`, `c`, `m`, `n`, `x`

### Wyjście

`y` do 3 miejsc po przecinku.

### Ograniczenia / gwarancje

* `m` i `n` są liczbami całkowitymi (np. nieujemnymi), aby potęgowanie było jednoznaczne w typowych językach.

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

---

## ZAD-05E — Funkcja z trygonometrią, wykładniczą i logarytmem

**Poziom:** ★★★☆
**Tagi:** `math`, `trygonometria`, `log`, `exp`, `float`

### Treść

Dla `x` (w radianach) oblicz:
[
y=\sin^3(x)\cdot\cos^2(x)+e^{x^2}+\ln(x^3+2x^2-x-3)
]

### Wejście

1 liczba zmiennoprzecinkowa: `x` (w radianach)

### Wyjście

`y` do 3 miejsc po przecinku.

### Ograniczenia / gwarancje

* Dane testowe spełniają warunek dziedziny logarytmu:

  * (x^3+2x^2-x-3 > 0)

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
57.179
```

---

# Konwersje — zadania niezależne (ZAD-06A … ZAD-06F)

## ZAD-06A — Kilogramy → gramy

**Poziom:** ★☆☆ | **Tagi:** `konwersje`

* Wejście: `kg`
* Wyjście: `g` jako liczba całkowita (`g = kg * 1000`)
* Gwarancja: `kg` jest liczbą całkowitą lub taką, że wynik w gramach jest całkowity.

---

## ZAD-06B — Cale → centymetry

**Poziom:** ★☆☆ | **Tagi:** `konwersje`, `float`

* Wejście: `inch`
* Wyjście: `cm = inch * 2.54` do **2 miejsc po przecinku**

---

## ZAD-06C — Sekundy → pełne godziny

**Poziom:** ★☆☆ | **Tagi:** `dzielenie całkowite`

* Wejście: `s` (liczba całkowita, `s ≥ 0`)
* Wyjście: `s // 3600`

---

## ZAD-06D — Euro → złotówki (kurs stały)

**Poziom:** ★☆☆ | **Tagi:** `konwersje`, `float`

* Wejście: `eur`
* Wyjście: `pln = eur * 4.4` do **2 miejsc po przecinku**

---

## ZAD-06E — Stopnie → radiany

**Poziom:** ★☆☆ | **Tagi:** `pi`, `float`

* Wejście: `deg`
* Wyjście: `rad = deg * π / 180` do **3 miejsc po przecinku**
* Przyjmij `π` z biblioteki (np. `math.pi`) lub `π = 3.141592653589793`.

---

## ZAD-06F — Fahrenheit → Celsius i Kelviny

**Poziom:** ★☆☆ | **Tagi:** `konwersje`, `float`

* Wejście: `F`
* Wyjście:

  1. `C = (5/9) * (F - 32)` do **3 miejsc**
  2. `K = C + 273.15` do **3 miejsc**
* Każdy wynik w osobnej linii.

---

# Geometria — zadania niezależne (ZAD-07A … ZAD-07F)

**Wspólna zasada:** wszystkie wyniki wypisz do **3 miejsc po przecinku**.
**Tagi:** `geometria`, `pi`, `float`

## ZAD-07A — Pole trójkąta: (P = \frac{1}{2}ah)

Wejście: `a`, `h` (2 linie) → Wyjście: `P`

## ZAD-07B — Pole prostokąta: (P = ab)

Wejście: `a`, `b` → Wyjście: `P`

## ZAD-07C — Pole rombu: (P = \frac{1}{2}d_1d_2)

Wejście: `d1`, `d2` → Wyjście: `P`

## ZAD-07D — Objętość kuli: (V = \frac{4}{3}\pi r^3)

Wejście: `r` → Wyjście: `V`

## ZAD-07E — Objętość stożka: (V = \frac{1}{3}\pi r^2 h)

Wejście: `r`, `h` → Wyjście: `V`

## ZAD-07F — Objętość prostopadłościanu: (V = abc)

Wejście: `a`, `b`, `c` (3 linie) → Wyjście: `V`

**Ograniczenia / gwarancje (dla wszystkich):**

* Wszystkie długości są dodatnie.

---

## ZAD-08 — Koszt pokrycia podłogi płytkami

**Poziom:** ★★☆
**Tagi:** `ceil`, `arytmetyka`, `formatowanie`, `geometria`

### Treść

Dane są:

* cena jednej płytki `p`,
* bok płytki `t` (płytka kwadratowa),
* długość podłogi `L`,
* szerokość podłogi `W`.

Oblicz liczbę płytek potrzebnych do pokrycia całej podłogi, zakładając układ bez docinania „na styk” (czyli wzdłuż każdego wymiaru zaokrąglasz w górę), a następnie podaj koszt całkowity.

### Wejście

4 liczby (każda w osobnej linii): `p`, `t`, `L`, `W`

### Wyjście

Jedna liczba: całkowity koszt do **2 miejsc po przecinku**.

### Ograniczenia / gwarancje

* `p > 0`, `t > 0`, `L > 0`, `W > 0`
* Liczba płytek:

  * `nL = ceil(L / t)`
  * `nW = ceil(W / t)`
  * `n = nL * nW`
* Koszt: `n * p`

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

---

## ZAD-09 — Kalkulator kredytowy (rata annuitetowa)

**Poziom:** ★★☆
**Tagi:** `finanse`, `float`, `formatowanie`

### Treść

Wczytaj:

* roczną stopę procentową `R` (w %),
* okres spłaty `Y` (w latach),
* kwotę kredytu `P`.

Oblicz miesięczną ratę `M` oraz całkowity koszt `C = M * n`, gdzie `n = 12 * Y`.

Dla `R > 0` użyj wzoru:
[
M = P \cdot \frac{r(1+r)^n}{(1+r)^n-1}
]
gdzie `r = R / (12*100)`.

Dla `R = 0` przyjmij:

* `M = P / n`.

### Wejście

3 liczby (w osobnych liniach):

1. `R` (float, `R ≥ 0`)
2. `Y` (int, `Y > 0`)
3. `P` (float, `P > 0`)

### Wyjście

Dwie linie (do **2 miejsc po przecinku**):

1. miesięczna rata `M`
2. całkowity koszt `C`

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
13776.00
```
