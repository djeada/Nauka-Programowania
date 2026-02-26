# Rozdział: Klasy (stdin/stdout)

Poniższe zadania polegają na wczytywaniu danych ze **standardowego wejścia** (stdin) i wypisywaniu wyniku na **standardowe wyjście** (stdout).
**Każde zadanie (oraz każdy podpunkt w zadaniach wieloczęściowych) jest osobnym, niezależnym programem.**

**Konwencje wspólne:**

* Jeśli w danych wejściowych są liczby w osobnych liniach — wczytuj je dokładnie w tej kolejności.
* Jeśli format wyjścia zawiera kilka linii — wypisz je w tej samej kolejności.
* Dla liczb zmiennoprzecinkowych trzymaj stałą liczbę miejsc po przecinku (jak w przykładach).

---

## ZAD-01 — Klasa Koło

**Poziom:** ★★☆
**Tagi:** `class`, `metody`, `float`, `math`

### Treść

Zaprojektuj klasę **Koło**:

1. Konstruktor przyjmuje promień `r` (domyślnie 1).
2. Metoda licząca **obwód**: $2\pi r$
3. Metoda licząca **pole**: $\pi r^2$
4. Metoda wypisująca informacje: promień, obwód i pole.

Program ma utworzyć koło o promieniu wczytanym z wejścia (np. 3) i wypisać informacje.

### Wejście

* 1 linia: `r` (liczba rzeczywista)

### Wyjście

Trzy linie jak w przykładzie (obwód i pole do 4 miejsc po przecinku).

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
Koło o promieniu: 3
Obwód koła: 18.8496
Pole koła: 28.2743
```

---

## ZAD-02 — Klasa Punkt

**Poziom:** ★★☆
**Tagi:** `class`, `static`, `porównania`, `math`

### Treść

Zaprojektuj klasę **Punkt**:

1. Konstruktor `(x=0, y=0)`.
2. Metoda statyczna `odleglosc(p1, p2)` licząca odległość.
3. Metoda wypisująca współrzędne.
4. Porównania `==` i `!=` (równe, gdy oba współrzędne identyczne).

Program tworzy:

* A = (5, 5)
* B = (-3, -3)

Wypisuje oba punkty i odległość między nimi (4 miejsca po przecinku).

### Wejście

Brak.

### Wyjście

Jak w przykładzie.

### Przykład

**Wyjście:**

```
Punkt A: (5, 5)
Punkt B: (-3, -3)
Odległość między punktami A i B: 11.3137
```

---

## ZAD-03 — Pole nałożenia się dwóch prostokątów

**Poziom:** ★★☆
**Tagi:** `class`, `static`, `geometria`

### Treść

Zaprojektuj klasę **Prostokąt** opisaną przez dwa przeciwległe wierzchołki:

* lewy dolny `(x1, y1)`
* prawy górny `(x2, y2)`
  Boki równoległe do osi.

Klasa ma mieć:

1. Konstruktor `(x1, y1, x2, y2)`
2. Metodę statyczną `pole_wspolne(A, B)` zwracającą pole części wspólnej (albo 0).
3. Metodę wypisującą informacje o prostokącie.

Program tworzy:

* A: (3, 4) i (9, 6)
* B: (2, 2) i (7, 5)

Wypisuje oba i pole części wspólnej.

### Wejście

Brak.

### Wyjście

Jak w przykładzie.

### Przykład

**Wyjście:**

```
Prostokąt A: lewy dolny (3, 4), prawy górny (9, 6)
Prostokąt B: lewy dolny (2, 2), prawy górny (7, 5)
Pole części wspólnej: 6
```

---

## ZAD-04 — Klasy Wektor2D i Wektor3D

**Poziom:** ★★☆
**Tagi:** `class`, `operatory`, `math`

### Treść

Zaprojektuj klasy **Wektor2D** i **Wektor3D**:

Wspólne:

* konstruktor z domyślnymi współrzędnymi 0,
* dodawanie, odejmowanie,
* iloczyn skalarny,
* porównania `==` i `!=`,
* moduł (długość),
* metoda wypisująca wektor.

Dodatkowo dla **Wektor3D**:

* iloczyn wektorowy.

Program tworzy:

* A = (-3, -3, -3)
* B = (5, 5, 5)

Wypisuje A, B oraz:

* A + B
* A - B
* A · B
* A × B

### Wejście

Brak.

### Wyjście

Jak w przykładzie.

### Przykład

**Wyjście:**

```
Wektor A: (-3, -3, -3)
Wektor B: (5, 5, 5)
Suma wektorów: (2, 2, 2)
Różnica wektorów A - B: (-8, -8, -8)
Iloczyn skalarny: -45
Iloczyn wektorowy: (0, 0, 0)
```

---

## ZAD-05 — Klasa Macierz

**Poziom:** ★★☆
**Tagi:** `class`, `macierze`, `operacje`

### Treść

Zaprojektuj klasę **Macierz**:

1. Konstruktor przyjmuje listę list (domyślnie pusta).
2. Operacje: dodawanie, odejmowanie, mnożenie.
3. Metoda wypisująca macierz (wierszami).
4. Porównania `==` i `!=`.

(Operację odwracania możesz pominąć w tym zadaniu, jeśli nie jest wymagana w sprawdzarce; najczęściej w podstawowych zadaniach nie ma testów na odwracanie.)

Program tworzy:

* A = [[1, 3], [4, 2]]
* B = [[5, 0], [1, 3]]

Wypisuje A, B, a potem A+B, A-B, A*B.

### Wejście

Brak.

### Wyjście

Jak w przykładzie.

### Przykład

**Wyjście:**

```
Macierz A:
[1, 3]
[4, 2]

Macierz B:
[5, 0]
[1, 3]

Suma macierzy:
[6, 3]
[5, 5]

Różnica macierzy A - B:
[-4, 3]
[3, -1]

Iloczyn macierzy A * B:
[8, 9]
[22, 12]
```

---

## ZAD-06 — Klasa LiczbaZespolona

**Poziom:** ★★☆
**Tagi:** `class`, `operacje`, `math`

### Treść

Zaprojektuj klasę **LiczbaZespolona**:

* konstruktor `(re=0, im=0)`,
* dodawanie, odejmowanie, mnożenie, dzielenie,
* porównania,
* moduł,
* wypisywanie w formacie `a + bi` lub `a - bi` (z zachowaniem znaku).

Program tworzy:

* A = 9 + 12i
* B = -3 - 3i

Wypisuje A, B oraz: sumę, różnicę A-B, iloczyn i iloraz A/B.

### Wejście

Brak.

### Wyjście

Jak w przykładzie.

### Przykład

**Wyjście:**

```
Liczba A: 9 + 12i
Liczba B: -3 - 3i

Suma: 6 + 9i
Różnica A - B: 12 + 15i
Iloczyn: 27 + 63i
Iloraz A / B: -3.5 + 0.5i
```

---

## ZAD-07 — Zliczanie instancji klasy

**Poziom:** ★☆☆
**Tagi:** `class`, `static`

### Treść

Zaprojektuj klasę **MojaKlasa**, która zlicza ile instancji utworzono:

* prywatne pole statyczne licznik,
* konstruktor zwiększa licznik,
* metoda statyczna zwraca licznik.

Program tworzy np. 3 obiekty i wypisuje liczbę instancji.

### Wejście

Brak.

### Wyjście

Jedna linia.

### Przykład

**Wyjście:**

```
Liczba utworzonych instancji: 3
```

---
