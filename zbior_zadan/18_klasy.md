# Rozdział 18: Klasy

Zadania w tym rozdziale uczą projektowania **klas**: konstruktora `__init__`, atrybutów, metod, metod statycznych (`@staticmethod`) oraz metod specjalnych, dzięki którym obiekty można wypisywać (`__str__`), porównywać (`__eq__`) i łączyć operatorami (`__add__`, `__sub__`, `__mul__`, …). Ostatnie zadania wprowadzają też wyjątki (`raise`, `try`/`except`), klasy danych (`@dataclass`) i generatory (`yield`).

**Konwencje wspólne:**

* Każde zadanie to osobny program: czyta **standardowe wejście** i wypisuje wynik na **standardowe wyjście**.
* W każdym zadaniu dostajesz **kod startowy** ze szkieletem klasy, a zwykle także z gotowym wczytywaniem danych i wypisywaniem wyników. Twoim zadaniem jest przede wszystkim uzupełnienie metod klasy — wynik programu zależy od tego, jak działa Twoja klasa.
* Nazwy klas i metod podane w treści są obowiązkowe (kod startowy z nich korzysta). Nazwy w kodzie piszemy bez polskich znaków, np. `Kolo`, `Prostokat`.
* „Z dokładnością do 2 miejsc po przecinku” oznacza dokładnie dwie cyfry po kropce, np. `f"{x:.2f}"` (`3.00`, `-0.50`).
* Program nie wypisuje komunikatów typu „Podaj liczbę:”.

---

## ZAD-01 — Klasa Koło

**Poziom:** ★☆☆
**Tagi:** `class`, `metody`, `float`, `math`

### Treść

Zaprojektuj klasę `Kolo` opisującą koło:

1. Konstruktor `__init__(self, r=1)` zapamiętuje promień `r` (domyślnie 1).
2. Metoda `obwod()` zwraca obwód koła: $2\pi r$.
3. Metoda `pole()` zwraca pole koła: $\pi r^2$.
4. Metoda `wypisz()` wypisuje informacje o kole: promień, obwód i pole (format poniżej). Do obliczeń użyj metod `obwod()` i `pole()`.

Program wczytuje promień, tworzy obiekt `Kolo` i wywołuje jego metodę `wypisz()`.

### Wejście

* 1. linia: $r$ — liczba rzeczywista dodatnia (promień koła)

### Wyjście

Trzy linie:

```
Koło o promieniu: <r>
Obwód koła: <obwód>
Pole koła: <pole>
```

Wszystkie liczby wypisz z dokładnością do 2 miejsc po przecinku.

### Ograniczenia

* $0 < r \le 1000$

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
Koło o promieniu: 3.00
Obwód koła: 18.85
Pole koła: 28.27
```

Obwód: $2 \cdot \pi \cdot 3 \approx 18.8496$, pole: $\pi \cdot 3^2 \approx 28.2743$.

### Uwagi

* Wartość $\pi$ znajdziesz w module `math` jako `math.pi`.

### Kod startowy

```python
import math


class Kolo:
    def __init__(self, r=1):
        # Uzupełnij: zapamiętaj promień w atrybucie obiektu.
        pass

    def obwod(self):
        # Uzupełnij: zwróć obwód koła.
        pass

    def pole(self):
        # Uzupełnij: zwróć pole koła.
        pass

    def wypisz(self):
        # Uzupełnij: wypisz trzy linie z informacjami o kole.
        pass


r = float(input())
kolo = Kolo(r)
kolo.wypisz()
```

---

## ZAD-02 — Klasa Punkt

**Poziom:** ★★☆
**Tagi:** `class`, `static`, `porównania`, `math`

### Treść

Zaprojektuj klasę `Punkt` opisującą punkt na płaszczyźnie:

1. Konstruktor `__init__(self, x=0, y=0)` zapamiętuje współrzędne.
2. Metoda statyczna `odleglosc(p1, p2)` zwraca odległość między punktami `p1` i `p2`:
   $\sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$.
3. Metoda `__str__()` zwraca napis z współrzędnymi w postaci `(x, y)`, np. `(5, -3)`.
4. Metoda `__eq__(other)` sprawdza, czy dwa punkty są równe (obie współrzędne identyczne). Operator `!=` Python wyznaczy wtedy sam.

Program wczytuje współrzędne punktów $A$ i $B$, tworzy dwa obiekty `Punkt`, wypisuje je, podaje odległość między nimi i informuje, czy punkty są równe.

### Wejście

* 1. linia: dwie liczby całkowite $x_A$ i $y_A$ oddzielone spacją
* 2. linia: dwie liczby całkowite $x_B$ i $y_B$ oddzielone spacją

### Wyjście

Cztery linie:

```
Punkt A: (xA, yA)
Punkt B: (xB, yB)
Odległość między punktami A i B: <odległość>
Punkty są równe.
```

Odległość wypisz z dokładnością do 2 miejsc po przecinku. W ostatniej linii wypisz `Punkty są równe.` albo `Punkty są różne.`

### Ograniczenia

* $-1000 \le x, y \le 1000$

### Przykład

**Wejście:**

```
5 5
-3 -3
```

**Wyjście:**

```
Punkt A: (5, 5)
Punkt B: (-3, -3)
Odległość między punktami A i B: 11.31
Punkty są różne.
```

$\sqrt{8^2 + 8^2} = \sqrt{128} \approx 11.3137$.

### Kod startowy

```python
import math


class Punkt:
    def __init__(self, x=0, y=0):
        # Uzupełnij: zapamiętaj współrzędne.
        pass

    @staticmethod
    def odleglosc(p1, p2):
        # Uzupełnij: zwróć odległość między punktami p1 i p2.
        pass

    def __str__(self):
        # Uzupełnij: zwróć napis w postaci "(x, y)".
        pass

    def __eq__(self, other):
        # Uzupełnij: punkty są równe, gdy mają te same współrzędne.
        pass


x, y = input().split()
a = Punkt(int(x), int(y))
x, y = input().split()
b = Punkt(int(x), int(y))

print(f"Punkt A: {a}")
print(f"Punkt B: {b}")
print(f"Odległość między punktami A i B: {Punkt.odleglosc(a, b):.2f}")
if a == b:
    print("Punkty są równe.")
else:
    print("Punkty są różne.")
```

---

## ZAD-03 — Pole nałożenia się dwóch prostokątów

**Poziom:** ★★☆
**Tagi:** `class`, `static`, `geometria`

### Treść

Zaprojektuj klasę `Prostokat` opisującą prostokąt o bokach równoległych do osi układu współrzędnych. Prostokąt jest wyznaczony przez dwa przeciwległe wierzchołki: lewy dolny $(x_1, y_1)$ i prawy górny $(x_2, y_2)$.

Klasa ma mieć:

1. Konstruktor `__init__(self, x1, y1, x2, y2)`.
2. Metodę `__str__()` zwracającą napis `lewy dolny (x1, y1), prawy górny (x2, y2)`.
3. Metodę statyczną `pole_wspolne(a, b)` zwracającą pole części wspólnej prostokątów `a` i `b`. Jeśli prostokąty nie nachodzą na siebie (albo stykają się tylko bokiem lub wierzchołkiem), pole części wspólnej wynosi `0`.

Program wczytuje dwa prostokąty $A$ i $B$, wypisuje je i podaje pole ich części wspólnej.

### Wejście

* 1. linia: cztery liczby całkowite $x_1$, $y_1$, $x_2$, $y_2$ — prostokąt $A$
* 2. linia: cztery liczby całkowite $x_1$, $y_1$, $x_2$, $y_2$ — prostokąt $B$

### Wyjście

Trzy linie:

```
Prostokąt A: lewy dolny (x1, y1), prawy górny (x2, y2)
Prostokąt B: lewy dolny (x1, y1), prawy górny (x2, y2)
Pole części wspólnej: <pole>
```

Pole jest liczbą całkowitą.

### Ograniczenia

* $-1000 \le x_1 < x_2 \le 1000$, $-1000 \le y_1 < y_2 \le 1000$

### Przykład

**Wejście:**

```
3 4 9 6
2 2 7 5
```

**Wyjście:**

```
Prostokąt A: lewy dolny (3, 4), prawy górny (9, 6)
Prostokąt B: lewy dolny (2, 2), prawy górny (7, 5)
Pole części wspólnej: 4
```

Częścią wspólną jest prostokąt o wierzchołkach $(3, 4)$ i $(7, 5)$, czyli o wymiarach $4 \times 1$.

### Uwagi

* Część wspólna (jeśli istnieje) też jest prostokątem. Jej lewa krawędź leży na $\max$ z lewych krawędzi obu prostokątów, a prawa na $\min$ z prawych krawędzi — analogicznie w pionie.

### Kod startowy

```python
class Prostokat:
    def __init__(self, x1, y1, x2, y2):
        # Uzupełnij: zapamiętaj współrzędne wierzchołków.
        pass

    def __str__(self):
        # Uzupełnij: zwróć opis "lewy dolny (x1, y1), prawy górny (x2, y2)".
        pass

    @staticmethod
    def pole_wspolne(a, b):
        # Uzupełnij: zwróć pole części wspólnej prostokątów a i b.
        pass


x1, y1, x2, y2 = [int(x) for x in input().split()]
a = Prostokat(x1, y1, x2, y2)
x1, y1, x2, y2 = [int(x) for x in input().split()]
b = Prostokat(x1, y1, x2, y2)

print(f"Prostokąt A: {a}")
print(f"Prostokąt B: {b}")
print(f"Pole części wspólnej: {Prostokat.pole_wspolne(a, b)}")
```

---

## ZAD-04 — Klasy Wektor2D i Wektor3D

**Poziom:** ★★☆
**Tagi:** `class`, `operatory`, `math`

### Treść

Zaprojektuj klasy `Wektor2D` (wektor na płaszczyźnie) i `Wektor3D` (wektor w przestrzeni).

Obie klasy mają mieć:

* konstruktor z domyślnymi współrzędnymi równymi 0: `Wektor2D(x=0, y=0)`, `Wektor3D(x=0, y=0, z=0)`,
* dodawanie i odejmowanie wektorów operatorami `+` i `-` (metody `__add__` i `__sub__`) — wynikiem jest nowy wektor tej samej klasy,
* metodę `iloczyn_skalarny(other)` — np. dla 3D: $x_A x_B + y_A y_B + z_A z_B$,
* metodę `dlugosc()` zwracającą długość (moduł) wektora — np. dla 3D: $\sqrt{x^2 + y^2 + z^2}$,
* porównanie `==` (metoda `__eq__`) — wektory są równe, gdy wszystkie współrzędne są równe,
* metodę `__str__()` zwracającą współrzędne w nawiasach, np. `(1, -2)` albo `(1, -2, 3)`.

Dodatkowo klasa `Wektor3D` ma metodę `iloczyn_wektorowy(other)`, która zwraca nowy obiekt `Wektor3D`:
$A \times B = (y_A z_B - z_A y_B,\ z_A x_B - x_A z_B,\ x_A y_B - y_A x_B)$.

Program wczytuje dwa wektory. Jeśli linia zawiera dwie liczby, tworzony jest `Wektor2D`, a jeśli trzy — `Wektor3D`. Następnie wypisuje wyniki działań.

### Wejście

* 1. linia: współrzędne wektora $A$ — dwie albo trzy liczby całkowite oddzielone spacjami
* 2. linia: współrzędne wektora $B$ — tyle samo liczb całkowitych co dla $A$

### Wyjście

Kolejne linie:

```
Wektor A: <A>
Wektor B: <B>
Suma wektorów: <A + B>
Różnica wektorów A - B: <A - B>
Iloczyn skalarny: <A · B>
Iloczyn wektorowy: <A × B>
Długość wektora A: <|A|>
Wektory są równe.
```

* Linię `Iloczyn wektorowy: …` wypisz **tylko** dla wektorów trójwymiarowych.
* Długość wypisz z dokładnością do 2 miejsc po przecinku.
* W ostatniej linii wypisz `Wektory są równe.` albo `Wektory są różne.`

### Ograniczenia

* Współrzędne są liczbami całkowitymi z przedziału $[-100, 100]$.

### Przykład

**Wejście:**

```
-3 -3 -3
5 5 5
```

**Wyjście:**

```
Wektor A: (-3, -3, -3)
Wektor B: (5, 5, 5)
Suma wektorów: (2, 2, 2)
Różnica wektorów A - B: (-8, -8, -8)
Iloczyn skalarny: -45
Iloczyn wektorowy: (0, 0, 0)
Długość wektora A: 5.20
Wektory są różne.
```

### Przykład 2

**Wejście:**

```
3 4
1 -2
```

**Wyjście:**

```
Wektor A: (3, 4)
Wektor B: (1, -2)
Suma wektorów: (4, 2)
Różnica wektorów A - B: (2, 6)
Iloczyn skalarny: -5
Długość wektora A: 5.00
Wektory są różne.
```

### Kod startowy

```python
import math


class Wektor2D:
    def __init__(self, x=0, y=0):
        # Uzupełnij.
        pass

    def __add__(self, other):
        # Uzupełnij: zwróć nowy Wektor2D.
        pass

    def __sub__(self, other):
        # Uzupełnij: zwróć nowy Wektor2D.
        pass

    def iloczyn_skalarny(self, other):
        # Uzupełnij.
        pass

    def dlugosc(self):
        # Uzupełnij.
        pass

    def __eq__(self, other):
        # Uzupełnij.
        pass

    def __str__(self):
        # Uzupełnij: zwróć napis "(x, y)".
        pass


class Wektor3D:
    def __init__(self, x=0, y=0, z=0):
        # Uzupełnij.
        pass

    def __add__(self, other):
        # Uzupełnij: zwróć nowy Wektor3D.
        pass

    def __sub__(self, other):
        # Uzupełnij: zwróć nowy Wektor3D.
        pass

    def iloczyn_skalarny(self, other):
        # Uzupełnij.
        pass

    def iloczyn_wektorowy(self, other):
        # Uzupełnij: zwróć nowy Wektor3D.
        pass

    def dlugosc(self):
        # Uzupełnij.
        pass

    def __eq__(self, other):
        # Uzupełnij.
        pass

    def __str__(self):
        # Uzupełnij: zwróć napis "(x, y, z)".
        pass


def wczytaj_wektor():
    liczby = [int(x) for x in input().split()]
    if len(liczby) == 2:
        return Wektor2D(liczby[0], liczby[1])
    return Wektor3D(liczby[0], liczby[1], liczby[2])


a = wczytaj_wektor()
b = wczytaj_wektor()

print(f"Wektor A: {a}")
print(f"Wektor B: {b}")
print(f"Suma wektorów: {a + b}")
print(f"Różnica wektorów A - B: {a - b}")
print(f"Iloczyn skalarny: {a.iloczyn_skalarny(b)}")
if isinstance(a, Wektor3D):
    print(f"Iloczyn wektorowy: {a.iloczyn_wektorowy(b)}")
print(f"Długość wektora A: {a.dlugosc():.2f}")
if a == b:
    print("Wektory są równe.")
else:
    print("Wektory są różne.")
```

---

## ZAD-05 — Klasa Macierz

**Poziom:** ★★☆
**Tagi:** `class`, `macierze`, `operatory`

### Treść

Zaprojektuj klasę `Macierz`:

1. Konstruktor `__init__(self, wiersze)` przyjmuje listę wierszy (listę list liczb).
2. Operatory `+`, `-` i `*` (metody `__add__`, `__sub__`, `__mul__`) zwracają **nową** macierz — sumę, różnicę i iloczyn macierzy. Jeśli działania nie da się wykonać, metoda zwraca `None`:
   * dodawanie i odejmowanie wymagają macierzy o tych samych wymiarach,
   * iloczyn $A \cdot B$ wymaga, by liczba kolumn $A$ była równa liczbie wierszy $B$. Element wyniku to $c_{ij} = \sum_k a_{ik} b_{kj}$.
3. Porównanie `==` (metoda `__eq__`) — macierze są równe, gdy mają te same wymiary i te same elementy.
4. Metoda `__str__()` zwraca macierz jako napis: kolejne wiersze w osobnych liniach, elementy wiersza oddzielone pojedynczą spacją.

Program wczytuje macierze $A$ i $B$, wypisuje je, a potem wypisuje $A + B$, $A - B$, $A \cdot B$ i informację, czy macierze są równe.

### Wejście

* 1. linia: liczby $n$ i $m$ — liczba wierszy i kolumn macierzy $A$
* kolejne $n$ linii: wiersze macierzy $A$ ($m$ liczb całkowitych oddzielonych spacjami)
* następna linia: liczby $p$ i $q$ — liczba wierszy i kolumn macierzy $B$
* kolejne $p$ linii: wiersze macierzy $B$ ($q$ liczb całkowitych oddzielonych spacjami)

### Wyjście

Pięć bloków, każdy zakończony pustą linią, a po nich jedna linia z wynikiem porównania:

```
Macierz A:
<A>

Macierz B:
<B>

Suma macierzy:
<A + B>

Różnica macierzy A - B:
<A - B>

Iloczyn macierzy A * B:
<A * B>

Macierze A i B są równe.
```

* Jeśli działania nie da się wykonać, zamiast macierzy wypisz w bloku jedną linię: `Niezgodne wymiary.`
* W ostatniej linii wypisz `Macierze A i B są równe.` albo `Macierze A i B są różne.`

### Ograniczenia

* $1 \le n, m, p, q \le 5$
* Elementy macierzy są liczbami całkowitymi z przedziału $[-100, 100]$.

### Przykład

**Wejście:**

```
2 2
1 3
4 2
2 2
5 0
1 3
```

**Wyjście:**

```
Macierz A:
1 3
4 2

Macierz B:
5 0
1 3

Suma macierzy:
6 3
5 5

Różnica macierzy A - B:
-4 3
3 -1

Iloczyn macierzy A * B:
8 9
22 6

Macierze A i B są różne.
```

Na przykład element w drugim wierszu i drugiej kolumnie iloczynu to $4 \cdot 0 + 2 \cdot 3 = 6$.

### Przykład 2

**Wejście:**

```
1 2
1 2
1 2
3 4
```

**Wyjście:**

```
Macierz A:
1 2

Macierz B:
3 4

Suma macierzy:
4 6

Różnica macierzy A - B:
-2 -2

Iloczyn macierzy A * B:
Niezgodne wymiary.

Macierze A i B są różne.
```

Macierz $1 \times 2$ można pomnożyć tylko przez macierz o 2 wierszach.

### Kod startowy

```python
class Macierz:
    def __init__(self, wiersze):
        # Uzupełnij: zapamiętaj wiersze (listę list liczb).
        pass

    def __add__(self, other):
        # Uzupełnij: zwróć nową Macierz albo None przy niezgodnych wymiarach.
        pass

    def __sub__(self, other):
        # Uzupełnij: zwróć nową Macierz albo None przy niezgodnych wymiarach.
        pass

    def __mul__(self, other):
        # Uzupełnij: zwróć nową Macierz albo None przy niezgodnych wymiarach.
        pass

    def __eq__(self, other):
        # Uzupełnij.
        pass

    def __str__(self):
        # Uzupełnij: wiersze w osobnych liniach, elementy oddzielone spacją.
        pass


def wczytaj_macierz():
    n, m = [int(x) for x in input().split()]
    wiersze = []
    for _ in range(n):
        wiersze.append([int(x) for x in input().split()])
    return Macierz(wiersze)


def wypisz_blok(naglowek, macierz):
    print(naglowek)
    if macierz is None:
        print("Niezgodne wymiary.")
    else:
        print(macierz)
    print()


a = wczytaj_macierz()
b = wczytaj_macierz()

wypisz_blok("Macierz A:", a)
wypisz_blok("Macierz B:", b)
wypisz_blok("Suma macierzy:", a + b)
wypisz_blok("Różnica macierzy A - B:", a - b)
wypisz_blok("Iloczyn macierzy A * B:", a * b)
if a == b:
    print("Macierze A i B są równe.")
else:
    print("Macierze A i B są różne.")
```

---

## ZAD-06 — Klasa LiczbaZespolona

**Poziom:** ★★☆
**Tagi:** `class`, `operatory`, `math`

### Treść

Zaprojektuj klasę `LiczbaZespolona` opisującą liczbę zespoloną $a + bi$:

* konstruktor `__init__(self, re=0, im=0)` — część rzeczywista i urojona,
* operatory `+`, `-`, `*`, `/` (metody `__add__`, `__sub__`, `__mul__`, `__truediv__`) zwracające nową liczbę zespoloną:
  * $(a + bi)(c + di) = (ac - bd) + (ad + bc)i$,
  * $\frac{a + bi}{c + di} = \frac{ac + bd}{c^2 + d^2} + \frac{bc - ad}{c^2 + d^2}i$ (dzielnik jest różny od zera),
* porównanie `==` (metoda `__eq__`) — liczby są równe, gdy mają równe części rzeczywiste i urojone,
* metodę `modul()` zwracającą moduł liczby: $|a + bi| = \sqrt{a^2 + b^2}$,
* metodę `__str__()` zwracającą napis `a + bi` albo `a - bi` (gdy część urojona jest ujemna, wypisz minus i jej wartość bezwzględną). Obie części wypisz z dokładnością do 2 miejsc po przecinku, np. `9.00 + 12.00i`, `-3.00 - 3.00i`.

Program wczytuje liczby $A$ i $B$ i wypisuje wyniki działań.

### Wejście

* 1. linia: dwie liczby całkowite — część rzeczywista i urojona liczby $A$
* 2. linia: dwie liczby całkowite — część rzeczywista i urojona liczby $B$

### Wyjście

Osiem linii:

```
Liczba A: <A>
Liczba B: <B>
Suma: <A + B>
Różnica A - B: <A - B>
Iloczyn: <A * B>
Iloraz A / B: <A / B>
Moduł liczby A: <|A|>
Liczby są równe.
```

* Jeśli $B = 0 + 0i$, zamiast ilorazu wypisz `Iloraz A / B: nie można dzielić przez zero`.
* Moduł wypisz z dokładnością do 2 miejsc po przecinku.
* W ostatniej linii wypisz `Liczby są równe.` albo `Liczby są różne.`

### Ograniczenia

* Części rzeczywiste i urojone są liczbami całkowitymi z przedziału $[-100, 100]$.

### Przykład

**Wejście:**

```
9 12
-3 -3
```

**Wyjście:**

```
Liczba A: 9.00 + 12.00i
Liczba B: -3.00 - 3.00i
Suma: 6.00 + 9.00i
Różnica A - B: 12.00 + 15.00i
Iloczyn: 9.00 - 63.00i
Iloraz A / B: -3.50 - 0.50i
Moduł liczby A: 15.00
Liczby są różne.
```

Iloczyn: $(9 + 12i)(-3 - 3i) = (-27 + 36) + (-27 - 36)i = 9 - 63i$.

### Kod startowy

```python
import math


class LiczbaZespolona:
    def __init__(self, re=0, im=0):
        # Uzupełnij.
        pass

    def __add__(self, other):
        # Uzupełnij.
        pass

    def __sub__(self, other):
        # Uzupełnij.
        pass

    def __mul__(self, other):
        # Uzupełnij.
        pass

    def __truediv__(self, other):
        # Uzupełnij.
        pass

    def __eq__(self, other):
        # Uzupełnij.
        pass

    def modul(self):
        # Uzupełnij.
        pass

    def __str__(self):
        # Uzupełnij: zwróć napis "a + bi" albo "a - bi".
        pass


re, im = input().split()
a = LiczbaZespolona(int(re), int(im))
re, im = input().split()
b = LiczbaZespolona(int(re), int(im))

print(f"Liczba A: {a}")
print(f"Liczba B: {b}")
print(f"Suma: {a + b}")
print(f"Różnica A - B: {a - b}")
print(f"Iloczyn: {a * b}")
if b == LiczbaZespolona(0, 0):
    print("Iloraz A / B: nie można dzielić przez zero")
else:
    print(f"Iloraz A / B: {a / b}")
print(f"Moduł liczby A: {a.modul():.2f}")
if a == b:
    print("Liczby są równe.")
else:
    print("Liczby są różne.")
```

---

## ZAD-07 — Zliczanie instancji klasy

**Poziom:** ★☆☆
**Tagi:** `class`, `static`

### Treść

Zaprojektuj klasę `MojaKlasa`, która sama zlicza, ile jej obiektów (instancji) utworzono:

* atrybut klasy (wspólny dla wszystkich obiektów) `_licznik`, początkowo równy 0 — podkreślenie na początku nazwy oznacza, że jest to pole „prywatne”, którego nie należy zmieniać spoza klasy,
* konstruktor zwiększa licznik o 1 i zapisuje w atrybucie obiektu `numer` numer nowego obiektu (pierwszy utworzony obiekt ma numer 1),
* metoda statyczna `liczba_instancji()` zwraca liczbę dotychczas utworzonych obiektów.

Program wykonuje polecenia:

* `nowy` — tworzy nowy obiekt `MojaKlasa` i wypisuje `Utworzono obiekt nr <numer>.`
* `ile` — wypisuje `Liczba utworzonych instancji: <liczba>`

### Wejście

* 1. linia: liczba poleceń $n$
* kolejne $n$ linii: polecenie `nowy` albo `ile`

### Wyjście

Po jednej linii dla każdego polecenia, w formacie opisanym w treści.

### Ograniczenia

* $1 \le n \le 100$

### Przykład

**Wejście:**

```
5
nowy
nowy
ile
nowy
ile
```

**Wyjście:**

```
Utworzono obiekt nr 1.
Utworzono obiekt nr 2.
Liczba utworzonych instancji: 2
Utworzono obiekt nr 3.
Liczba utworzonych instancji: 3
```

### Uwagi

* Do atrybutu klasy odwołuj się przez nazwę klasy: `MojaKlasa._licznik`. Zapis `self._licznik += 1` utworzyłby osobny atrybut w każdym obiekcie i licznik nie byłby wspólny.

### Kod startowy

```python
class MojaKlasa:
    _licznik = 0

    def __init__(self):
        # Uzupełnij: zwiększ licznik klasy i zapamiętaj numer obiektu w self.numer.
        pass

    @staticmethod
    def liczba_instancji():
        # Uzupełnij: zwróć liczbę utworzonych obiektów.
        pass


n = int(input())
obiekty = []
for _ in range(n):
    polecenie = input()
    if polecenie == "nowy":
        obiekt = MojaKlasa()
        obiekty.append(obiekt)
        print(f"Utworzono obiekt nr {obiekt.numer}.")
    elif polecenie == "ile":
        print(f"Liczba utworzonych instancji: {MojaKlasa.liczba_instancji()}")
```

---

## ZAD-08 — Konto bankowe

**Poziom:** ★★☆
**Tagi:** `class`, `wyjątki`, `try-except`

### Treść

Zaprojektuj klasę `KontoBankowe`:

* konstruktor `__init__(self, saldo=0)` zapamiętuje saldo początkowe w atrybucie `saldo`,
* metoda `wplac(kwota)` zwiększa saldo o `kwota`. Jeśli $kwota \le 0$, metoda zgłasza wyjątek `ValueError("Kwota musi być dodatnia.")` i nie zmienia salda,
* metoda `wyplac(kwota)` zmniejsza saldo o `kwota`. Najpierw sprawdza, czy $kwota \le 0$ — wtedy zgłasza `ValueError("Kwota musi być dodatnia.")`, a następnie, czy kwota nie przekracza salda — jeśli przekracza, zgłasza `ValueError("Brak środków na koncie.")`. W obu przypadkach saldo się nie zmienia.

Metody **nie wypisują** komunikatów o błędach — tylko zgłaszają wyjątki. Wyjątki przechwytuje program główny (`try`/`except`) i wypisuje komunikat błędu.

Program tworzy konto z podanym saldem początkowym i wykonuje kolejne polecenia:

* `wplac K` — wpłaca kwotę $K$ i wypisuje `Wpłacono K. Saldo: S`,
* `wyplac K` — wypłaca kwotę $K$ i wypisuje `Wypłacono K. Saldo: S`,
* `saldo` — wypisuje `Saldo: S`,

gdzie $S$ to saldo po wykonaniu polecenia. Jeśli metoda zgłosi wyjątek, program zamiast tego wypisuje `Błąd: <komunikat wyjątku>`.

### Wejście

* 1. linia: saldo początkowe — liczba całkowita $\ge 0$
* 2. linia: liczba poleceń $n$
* kolejne $n$ linii: polecenie `wplac K`, `wyplac K` albo `saldo` ($K$ — liczba całkowita, może być ujemna lub równa 0)

### Wyjście

$n$ linii — po jednej dla każdego polecenia, w formacie opisanym w treści.

### Ograniczenia

* $1 \le n \le 100$
* $-10^6 \le K \le 10^6$, saldo początkowe nie przekracza $10^6$

### Przykład

**Wejście:**

```
100
5
wplac 50
wyplac 30
wyplac 500
wplac -20
saldo
```

**Wyjście:**

```
Wpłacono 50. Saldo: 150
Wypłacono 30. Saldo: 120
Błąd: Brak środków na koncie.
Błąd: Kwota musi być dodatnia.
Saldo: 120
```

### Uwagi

* Instrukcja `raise` zgłasza wyjątek i natychmiast przerywa działanie metody. Kod, który wywołał metodę, może wyjątek przechwycić w bloku `try`/`except`; zapis `except ValueError as e` daje dostęp do obiektu wyjątku, a `str(e)` (lub `{e}` w f-stringu) to jego komunikat:

  ```python
  def pierwiastek(x):
      if x < 0:
          raise ValueError("Liczba nie może być ujemna.")
      return x ** 0.5


  try:
      print(pierwiastek(-4))
  except ValueError as e:
      print(f"Błąd: {e}")      # Błąd: Liczba nie może być ujemna.
  ```

* Dzięki temu klasa tylko **sygnalizuje** problem, a o tym, co z nim zrobić (wypisać komunikat, zapytać ponownie, przerwać program), decyduje kod, który z niej korzysta.

### Kod startowy

```python
class KontoBankowe:
    def __init__(self, saldo=0):
        # Uzupełnij.
        pass

    def wplac(self, kwota):
        # Uzupełnij: dla kwoty <= 0 zgłoś ValueError("Kwota musi być dodatnia.").
        pass

    def wyplac(self, kwota):
        # Uzupełnij: zgłoś ValueError przy kwocie <= 0 albo przy braku środków.
        pass


konto = KontoBankowe(int(input()))
n = int(input())
for _ in range(n):
    czesci = input().split()
    polecenie = czesci[0]
    # Uzupełnij: wykonaj polecenie i wypisz wynik.
    # Wywołania wplac/wyplac umieść w bloku try, a błąd obsłuż w except ValueError.
```

---

## ZAD-09 — Klasa Ułamek

**Poziom:** ★★☆
**Tagi:** `class`, `operatory`, `NWD`, `sortowanie`

### Treść

Zaprojektuj klasę `Ulamek` opisującą ułamek zwykły $\frac{a}{b}$:

* Konstruktor `__init__(self, licznik, mianownik=1)` od razu **normalizuje** ułamek:
  * skraca go przez $\text{NWD}(|a|, |b|)$ (funkcja `math.gcd`),
  * przenosi znak do licznika — mianownik jest zawsze dodatni (np. $\frac{3}{-6}$ zapisujemy jako $-\frac{1}{2}$),
  * zero zapisujemy jako $\frac{0}{1}$.
* Operatory `+`, `-`, `*`, `/` (metody `__add__`, `__sub__`, `__mul__`, `__truediv__`) zwracają nowy, znormalizowany ułamek (dzielnik w `/` jest różny od zera):
  $\frac{a}{b} + \frac{c}{d} = \frac{ad + cb}{bd}$, $\frac{a}{b} \cdot \frac{c}{d} = \frac{ac}{bd}$, $\frac{a}{b} : \frac{c}{d} = \frac{ad}{bc}$.
* Porównania `==` (`__eq__`) i `<` (`__lt__`): $\frac{a}{b} < \frac{c}{d}$ wtedy i tylko wtedy, gdy $ad < cb$ (mianowniki są dodatnie).
* Metoda `__str__()` zwraca `a/b`, np. `-3/4`, a gdy mianownik jest równy 1 — samą liczbę całkowitą, np. `3`, `-2`, `0`.

Program wczytuje listę ułamków i wypisuje:

1. ułamki posortowane rosnąco (`sorted()` porównuje elementy operatorem `<`, czyli Twoją metodą `__lt__`),
2. ich sumę,
3. ich iloczyn,
4. ich średnią arytmetyczną (sumę podzieloną przez `Ulamek(n)`),
5. różnicę między największym a najmniejszym ułamkiem,
6. liczbę różnych wartości (operator `in` porównuje elementy operatorem `==`, czyli Twoją metodą `__eq__`).

### Wejście

* 1. linia: liczba ułamków $n$
* 2. linia: $n$ ułamków w postaci `a/b` oddzielonych spacjami ($a$, $b$ — liczby całkowite, $b \ne 0$, mogą być ujemne)

### Wyjście

Sześć linii:

```
Posortowane: <ułamki oddzielone spacjami>
Suma: <suma>
Iloczyn: <iloczyn>
Średnia: <średnia>
Największy - najmniejszy: <różnica>
Liczba różnych wartości: <liczba>
```

Wszystkie ułamki wypisz w postaci znormalizowanej (jak w metodzie `__str__`).

### Ograniczenia

* $1 \le n \le 10$
* $-100 \le a, b \le 100$, $b \ne 0$

### Przykład

**Wejście:**

```
5
1/2 3/4 -2/8 6/4 2/4
```

**Wyjście:**

```
Posortowane: -1/4 1/2 1/2 3/4 3/2
Suma: 3
Iloczyn: -9/128
Średnia: 3/5
Największy - najmniejszy: 7/4
Liczba różnych wartości: 4
```

Po normalizacji ułamki to $\frac{1}{2}, \frac{3}{4}, -\frac{1}{4}, \frac{3}{2}, \frac{1}{2}$. Ich suma to $3$, a średnia $\frac{3}{5}$. Ułamki $\frac{1}{2}$ i $\frac{2}{4}$ są równe, więc różnych wartości są 4.

### Uwagi

* `math.gcd(a, b)` zwraca NWD wartości bezwzględnych argumentów, np. `math.gcd(-6, 9) == 3`, `math.gcd(0, 5) == 5`.
* Używaj dzielenia całkowitego `//` — licznik i mianownik mają pozostać liczbami całkowitymi.

### Kod startowy

```python
import math


class Ulamek:
    def __init__(self, licznik, mianownik=1):
        # Uzupełnij: zapamiętaj ułamek w postaci znormalizowanej.
        pass

    def __add__(self, other):
        # Uzupełnij.
        pass

    def __sub__(self, other):
        # Uzupełnij.
        pass

    def __mul__(self, other):
        # Uzupełnij.
        pass

    def __truediv__(self, other):
        # Uzupełnij.
        pass

    def __eq__(self, other):
        # Uzupełnij.
        pass

    def __lt__(self, other):
        # Uzupełnij.
        pass

    def __str__(self):
        # Uzupełnij: "a/b" albo sama liczba całkowita, gdy mianownik == 1.
        pass


n = int(input())
ulamki = []
for tekst in input().split():
    a, b = tekst.split("/")
    ulamki.append(Ulamek(int(a), int(b)))

posortowane = sorted(ulamki)
suma = Ulamek(0)
iloczyn = Ulamek(1)
for u in ulamki:
    suma = suma + u
    iloczyn = iloczyn * u
rozne = []
for u in ulamki:
    if u not in rozne:
        rozne.append(u)

print("Posortowane:", " ".join(str(u) for u in posortowane))
print(f"Suma: {suma}")
print(f"Iloczyn: {iloczyn}")
print(f"Średnia: {suma / Ulamek(n)}")
print(f"Największy - najmniejszy: {posortowane[-1] - posortowane[0]}")
print(f"Liczba różnych wartości: {len(rozne)}")
```

---

## ZAD-10 — Koszyk zakupów (dataclass)

**Poziom:** ★★☆
**Tagi:** `dataclass`, `class`, `formatowanie`

### Treść

Zaprojektuj dwie **klasy danych** (`@dataclass`):

* `Produkt` z polami `nazwa: str`, `cena: float`, `ilosc: int` oraz metodą `wartosc()`, która zwraca $cena \cdot ilosc$.
* `Koszyk` z polem `produkty: list`, które domyślnie jest pustą listą (`field(default_factory=list)`), oraz metodami:
  * `dodaj(produkt)` — jeśli w koszyku jest już produkt o tej samej nazwie, zwiększa jego ilość o `produkt.ilosc`; w przeciwnym razie dopisuje produkt na koniec listy,
  * `suma()` — zwraca łączną wartość wszystkich produktów,
  * `wypisz_paragon()` — wypisuje paragon (format poniżej).

Program wczytuje kolejne pozycje zakupów, dodaje je do koszyka i wypisuje paragon.

### Wejście

* 1. linia: liczba pozycji $n$
* kolejne $n$ linii: `nazwa cena ilosc` — nazwa produktu (bez spacji), cena (liczba rzeczywista z co najwyżej 2 miejscami po przecinku) i ilość (liczba całkowita), oddzielone spacjami

### Wyjście

* Dla każdego produktu w koszyku (w kolejności pierwszego pojawienia się na wejściu) jedna linia, w której kolejno:
  * nazwa wyrównana do **lewej** w polu o szerokości 10 znaków,
  * spacja i ilość wyrównana do **prawej** w polu o szerokości 3,
  * ` x ` i cena z 2 miejscami po przecinku, wyrównana do prawej w polu o szerokości 7,
  * ` = ` i wartość z 2 miejscami po przecinku, wyrównana do prawej w polu o szerokości 8.
* Linia złożona z 35 znaków `-`.
* Linia `Razem: <suma>` (suma z 2 miejscami po przecinku).

### Ograniczenia

* $1 \le n \le 20$
* Nazwa ma od 1 do 10 znaków. Produkty o tej samej nazwie mają zawsze tę samą cenę.
* $0.01 \le cena \le 999.99$, $1 \le ilosc$, a łączna ilość każdego produktu w koszyku nie przekracza 99.

### Przykład

**Wejście:**

```
5
chleb 3.50 2
mleko 2.99 3
ser 12.00 1
chleb 3.50 1
jajka 0.89 10
```

**Wyjście:**

```
chleb        3 x    3.50 =    10.50
mleko        3 x    2.99 =     8.97
ser          1 x   12.00 =    12.00
jajka       10 x    0.89 =     8.90
-----------------------------------
Razem: 40.37
```

Dwie pozycje `chleb` zostały scalone w jedną (2 + 1 = 3 sztuki).

### Uwagi

* Dekorator `@dataclass` (z modułu `dataclasses`) sam tworzy konstruktor `__init__`, metodę `__repr__` i porównanie `__eq__` na podstawie pól zapisanych z adnotacją typu:

  ```python
  from dataclasses import dataclass


  @dataclass
  class Punkt:
      x: int
      y: int = 0


  p = Punkt(3)
  print(p)                  # Punkt(x=3, y=0)
  print(p == Punkt(3, 0))   # True
  ```

* Pole z listą nie może mieć wartości domyślnej `[]` — taka jedna lista byłaby **wspólna** dla wszystkich obiektów klasy (dlatego `@dataclass` zgłasza wtedy błąd). `field(default_factory=list)` sprawia, że każdy nowy obiekt dostaje **własną**, nową pustą listę.
* Szerokość pola i wyrównanie ustawisz w f-stringu: `f"{tekst:<10}"` (do lewej, 10 znaków), `f"{liczba:>3}"` (do prawej, 3 znaki), `f"{x:>8.2f}"` (do prawej, 8 znaków, 2 miejsca po przecinku).

### Kod startowy

```python
from dataclasses import dataclass, field


@dataclass
class Produkt:
    nazwa: str
    cena: float
    ilosc: int

    def wartosc(self):
        # Uzupełnij.
        pass


@dataclass
class Koszyk:
    produkty: list = field(default_factory=list)

    def dodaj(self, produkt):
        # Uzupełnij: scal z produktem o tej samej nazwie albo dopisz na koniec.
        pass

    def suma(self):
        # Uzupełnij.
        pass

    def wypisz_paragon(self):
        # Uzupełnij.
        pass


koszyk = Koszyk()
n = int(input())
for _ in range(n):
    nazwa, cena, ilosc = input().split()
    koszyk.dodaj(Produkt(nazwa, float(cena), int(ilosc)))
koszyk.wypisz_paragon()
```

---

## ZAD-11 — Własny zakres iterowalny

**Poziom:** ★★★
**Tagi:** `class`, `iterator`, `generator`, `yield`

### Treść

Zaprojektuj klasę `Zakres` — własny odpowiednik wbudowanej funkcji `range()` — po której obiektach można iterować pętlą `for`:

* Konstruktor `__init__(self, start, stop, krok=1)` zapamiętuje parametry. Jeśli `krok` jest równy 0, zgłasza wyjątek `ValueError("Krok nie może być równy 0.")`.
* Metoda `__iter__()` jest **generatorem** — kolejne elementy zwraca instrukcją `yield`:
  * dla kroku dodatniego: $start, start + krok, start + 2 \cdot krok, \dots$ — dopóki element jest **mniejszy** od $stop$,
  * dla kroku ujemnego: $start, start + krok, \dots$ — dopóki element jest **większy** od $stop$.

Nie używaj w klasie wbudowanej funkcji `range()` — kolejne elementy wylicz samodzielnie.

Program dla każdego zapytania `start stop krok` tworzy obiekt `Zakres` i wypisuje jego elementy oraz ich sumę. Każde przejście pętlą `for` (a także wywołanie `sum()`) uruchamia generator od nowa, więc po jednym obiekcie można iterować wiele razy.

### Wejście

* 1. linia: liczba zapytań $q$
* kolejne $q$ linii: trzy liczby całkowite `start stop krok` oddzielone spacjami

### Wyjście

Dla każdego zapytania jedna linia:

* `<elementy oddzielone spacjami> (suma: <suma>)`,
* `pusty (suma: 0)` — jeśli zakres nie zawiera żadnego elementu,
* `Błąd: Krok nie może być równy 0.` — jeśli konstruktor zgłosił wyjątek.

### Ograniczenia

* $1 \le q \le 20$
* $-1000 \le start, stop, krok \le 1000$

### Przykład

**Wejście:**

```
4
1 10 2
10 0 -3
5 5 1
0 5 0
```

**Wyjście:**

```
1 3 5 7 9 (suma: 25)
10 7 4 1 (suma: 22)
pusty (suma: 0)
Błąd: Krok nie może być równy 0.
```

### Uwagi

* Pętla `for x in obiekt:` wywołuje najpierw `iter(obiekt)`, czyli metodę `obiekt.__iter__()`, a potem pobiera z otrzymanego iteratora kolejne elementy.
* Funkcja (lub metoda), która zawiera `yield`, jest **generatorem**: jej wywołanie nie wykonuje od razu kodu, tylko zwraca iterator. Każde `yield` „oddaje” jeden element i wstrzymuje funkcję do czasu, aż pętla poprosi o następny:

  ```python
  def odliczanie(n):
      while n > 0:
          yield n
          n -= 1


  for x in odliczanie(3):
      print(x)        # 3, 2, 1 (w osobnych liniach)
  ```

* Wyjątek zgłoszony w konstruktorze przechwytuje program główny w bloku `try`/`except` (zob. zadanie „Konto bankowe”).

### Kod startowy

```python
class Zakres:
    def __init__(self, start, stop, krok=1):
        # Uzupełnij: dla krok == 0 zgłoś ValueError("Krok nie może być równy 0.").
        pass

    def __iter__(self):
        # Uzupełnij: zwracaj kolejne elementy instrukcją yield.
        pass


q = int(input())
for _ in range(q):
    start, stop, krok = [int(x) for x in input().split()]
    try:
        zakres = Zakres(start, stop, krok)
    except ValueError as e:
        print(f"Błąd: {e}")
        continue
    elementy = [str(x) for x in zakres]
    if elementy:
        tekst = " ".join(elementy)
    else:
        tekst = "pusty"
    print(f"{tekst} (suma: {sum(zakres)})")
```
