/*
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

*/
import java.util.Arrays;
import java.util.Scanner;

public class Main {

  // Macierz liczb całkowitych przechowywana jako tablica wierszy.
  // Operacje zwracają nową macierz albo null, gdy wymiary są niezgodne.
  private static class Macierz {
    private final int[][] wiersze;

    public Macierz(final int[][] wiersze) {
      this.wiersze = new int[wiersze.length][];

      for (int i = 0; i < wiersze.length; i++) {
        if (wiersze[i].length != wiersze[0].length) {
          throw new IllegalArgumentException("Wszystkie wiersze muszą mieć tę samą długość.");
        }
        this.wiersze[i] = wiersze[i].clone();
      }
    }

    public int liczbaWierszy() {
      return wiersze.length;
    }

    public int liczbaKolumn() {
      return wiersze.length == 0 ? 0 : wiersze[0].length;
    }

    private boolean takieSameWymiary(final Macierz inna) {
      return liczbaWierszy() == inna.liczbaWierszy() && liczbaKolumn() == inna.liczbaKolumn();
    }

    // Złożoność czasowa: O(n * m)
    // Złożoność pamięciowa: O(n * m)
    public Macierz dodaj(final Macierz inna) {
      if (!takieSameWymiary(inna)) {
        return null;
      }

      int[][] wynik = new int[liczbaWierszy()][liczbaKolumn()];
      for (int i = 0; i < liczbaWierszy(); i++) {
        for (int j = 0; j < liczbaKolumn(); j++) {
          wynik[i][j] = wiersze[i][j] + inna.wiersze[i][j];
        }
      }

      return new Macierz(wynik);
    }

    // Złożoność czasowa: O(n * m)
    // Złożoność pamięciowa: O(n * m)
    public Macierz odejmij(final Macierz inna) {
      if (!takieSameWymiary(inna)) {
        return null;
      }

      int[][] wynik = new int[liczbaWierszy()][liczbaKolumn()];
      for (int i = 0; i < liczbaWierszy(); i++) {
        for (int j = 0; j < liczbaKolumn(); j++) {
          wynik[i][j] = wiersze[i][j] - inna.wiersze[i][j];
        }
      }

      return new Macierz(wynik);
    }

    // c[i][j] = suma po k z a[i][k] * b[k][j]
    // Złożoność czasowa: O(n * m * q)
    // Złożoność pamięciowa: O(n * q)
    public Macierz pomnoz(final Macierz inna) {
      if (liczbaKolumn() != inna.liczbaWierszy()) {
        return null;
      }

      int[][] wynik = new int[liczbaWierszy()][inna.liczbaKolumn()];
      for (int i = 0; i < liczbaWierszy(); i++) {
        for (int j = 0; j < inna.liczbaKolumn(); j++) {
          for (int k = 0; k < liczbaKolumn(); k++) {
            wynik[i][j] += wiersze[i][k] * inna.wiersze[k][j];
          }
        }
      }

      return new Macierz(wynik);
    }

    @Override
    public boolean equals(final Object obiekt) {
      if (this == obiekt) {
        return true;
      }
      if (!(obiekt instanceof Macierz)) {
        return false;
      }
      return Arrays.deepEquals(wiersze, ((Macierz) obiekt).wiersze);
    }

    @Override
    public int hashCode() {
      return Arrays.deepHashCode(wiersze);
    }

    @Override
    public String toString() {
      StringBuilder napis = new StringBuilder();

      for (int i = 0; i < wiersze.length; i++) {
        if (i > 0) {
          napis.append('\n');
        }
        for (int j = 0; j < wiersze[i].length; j++) {
          if (j > 0) {
            napis.append(' ');
          }
          napis.append(wiersze[i][j]);
        }
      }

      return napis.toString();
    }
  }

  private static Macierz wczytajMacierz(final Scanner scanner) {
    int n = scanner.nextInt();
    int m = scanner.nextInt();
    int[][] wiersze = new int[n][m];

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        wiersze[i][j] = scanner.nextInt();
      }
    }

    return new Macierz(wiersze);
  }

  private static void wypiszBlok(final String naglowek, final Macierz macierz) {
    System.out.println(naglowek);
    System.out.println(macierz == null ? "Niezgodne wymiary." : macierz);
    System.out.println();
  }

  public static void testDzialania() {
    Macierz a = new Macierz(new int[][] {{1, 3}, {4, 2}});
    Macierz b = new Macierz(new int[][] {{5, 0}, {1, 3}});

    assert a.dodaj(b).equals(new Macierz(new int[][] {{6, 3}, {5, 5}}));
    assert a.odejmij(b).equals(new Macierz(new int[][] {{-4, 3}, {3, -1}}));
    assert a.pomnoz(b).equals(new Macierz(new int[][] {{8, 9}, {22, 6}}));
  }

  public static void testNiezgodneWymiary() {
    Macierz a = new Macierz(new int[][] {{1, 2}});
    Macierz b = new Macierz(new int[][] {{3, 4}});
    Macierz c = new Macierz(new int[][] {{1}, {2}});

    assert a.pomnoz(b) == null;
    assert a.dodaj(c) == null;
    assert a.odejmij(c) == null;
    assert a.pomnoz(c).equals(new Macierz(new int[][] {{5}}));
    assert c.pomnoz(a).equals(new Macierz(new int[][] {{1, 2}, {2, 4}}));
  }

  public static void testRownosc() {
    Macierz a = new Macierz(new int[][] {{1, 2}, {3, 4}});

    assert a.equals(new Macierz(new int[][] {{1, 2}, {3, 4}}));
    assert !a.equals(new Macierz(new int[][] {{1, 2}, {3, 5}}));
    assert !a.equals(new Macierz(new int[][] {{1, 2, 3, 4}}));
  }

  public static void testNapis() {
    Macierz a = new Macierz(new int[][] {{1, -3}, {4, 2}});

    assert a.toString().equals("1 -3\n4 2");
  }

  public static void main(String[] args) {
    testDzialania();
    testNiezgodneWymiary();
    testRownosc();
    testNapis();

    Scanner scanner = new Scanner(System.in);
    Macierz a = wczytajMacierz(scanner);
    Macierz b = wczytajMacierz(scanner);
    scanner.close();

    wypiszBlok("Macierz A:", a);
    wypiszBlok("Macierz B:", b);
    wypiszBlok("Suma macierzy:", a.dodaj(b));
    wypiszBlok("Różnica macierzy A - B:", a.odejmij(b));
    wypiszBlok("Iloczyn macierzy A * B:", a.pomnoz(b));

    if (a.equals(b)) {
      System.out.println("Macierze A i B są równe.");
    } else {
      System.out.println("Macierze A i B są różne.");
    }
  }
}
