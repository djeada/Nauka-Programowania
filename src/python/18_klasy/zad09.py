r"""
ZAD-09 — Klasa Ułamek

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
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __eq__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __str__(self):
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

"""

import math


class Ulamek:
    def __init__(self, licznik, mianownik=1):
        if mianownik < 0:
            licznik, mianownik = -licznik, -mianownik
        nwd = math.gcd(licznik, mianownik)
        self.licznik = licznik // nwd
        self.mianownik = mianownik // nwd

    def __add__(self, other):
        return Ulamek(
            self.licznik * other.mianownik + other.licznik * self.mianownik,
            self.mianownik * other.mianownik,
        )

    def __sub__(self, other):
        return Ulamek(
            self.licznik * other.mianownik - other.licznik * self.mianownik,
            self.mianownik * other.mianownik,
        )

    def __mul__(self, other):
        return Ulamek(self.licznik * other.licznik, self.mianownik * other.mianownik)

    def __truediv__(self, other):
        return Ulamek(self.licznik * other.mianownik, self.mianownik * other.licznik)

    def __eq__(self, other):
        return self.licznik == other.licznik and self.mianownik == other.mianownik

    def __lt__(self, other):
        return self.licznik * other.mianownik < other.licznik * self.mianownik

    def __str__(self):
        if self.mianownik == 1:
            return str(self.licznik)
        return f"{self.licznik}/{self.mianownik}"


if __name__ == "__main__":
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
