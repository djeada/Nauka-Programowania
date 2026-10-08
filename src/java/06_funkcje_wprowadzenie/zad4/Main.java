/*
ZAD-04A — Minimum z dwóch liczb

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
    pass


a = int(input())
b = int(input())
print(min_z_dwoch(a, b))
```

ZAD-04B — Ograniczenie liczby do przedziału

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
    pass


x = int(input())
dolna = int(input())
gorna = int(input())
print(ogranicz(x, dolna, gorna))
```

ZAD-04C — Środkowa z trzech liczb

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
    pass


a = int(input())
b = int(input())
c = int(input())
print(srodkowa_z_trzech(a, b, c))
```

ZAD-04D — Maksimum z trzech liczb

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
    pass


a = int(input())
b = int(input())
c = int(input())
print(max_z_trzech(a, b, c))
```

*/
public class Main {
  // ZAD-04A: minimum z dwóch liczb, ZAD-04B: ograniczenie do przedziału,
  // ZAD-04C: środkowa z trzech liczb, ZAD-04D: maksimum z trzech liczb

  public static int min2(int a, int b) {
    return a < b ? a : b;
  }

  public static int max2(int a, int b) {
    return a > b ? a : b;
  }

  public static int ogranicz(int x, int dolna, int gorna) {
    return min2(max2(x, dolna), gorna);
  }

  public static int srodkowa3(int a, int b, int c) {
    if ((b <= a && a <= c) || (c <= a && a <= b)) {
      return a;
    }
    if ((a <= b && b <= c) || (c <= b && b <= a)) {
      return b;
    }
    return c;
  }

  public static int max3(int a, int b, int c) {
    return Math.max(Math.max(a, b), c);
  }

  public static void main(String[] args) {
    System.out.println(min2(3, 1));
    System.out.println(ogranicz(15, 0, 10));
    System.out.println(srodkowa3(3, 1, 2));
    System.out.println(max3(3, 2, 1));
  }
}
