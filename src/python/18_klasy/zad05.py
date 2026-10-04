r"""
ZAD-05 — Klasa Macierz

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
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __eq__(self, other):
        pass

    def __str__(self):
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

"""


class Macierz:
    def __init__(self, wiersze):
        self.wiersze = wiersze
        self.n = len(wiersze)
        self.m = len(wiersze[0])

    def __add__(self, other):
        if self.n != other.n or self.m != other.m:
            return None
        wynik = []
        for i in range(self.n):
            wiersz = []
            for j in range(self.m):
                wiersz.append(self.wiersze[i][j] + other.wiersze[i][j])
            wynik.append(wiersz)
        return Macierz(wynik)

    def __sub__(self, other):
        if self.n != other.n or self.m != other.m:
            return None
        wynik = []
        for i in range(self.n):
            wiersz = []
            for j in range(self.m):
                wiersz.append(self.wiersze[i][j] - other.wiersze[i][j])
            wynik.append(wiersz)
        return Macierz(wynik)

    def __mul__(self, other):
        if self.m != other.n:
            return None
        wynik = []
        for i in range(self.n):
            wiersz = []
            for j in range(other.m):
                suma = 0
                for k in range(self.m):
                    suma += self.wiersze[i][k] * other.wiersze[k][j]
                wiersz.append(suma)
            wynik.append(wiersz)
        return Macierz(wynik)

    def __eq__(self, other):
        return self.wiersze == other.wiersze

    def __str__(self):
        linie = []
        for wiersz in self.wiersze:
            linie.append(" ".join(str(x) for x in wiersz))
        return "\n".join(linie)


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


if __name__ == "__main__":
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
