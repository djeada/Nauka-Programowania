r"""
ZAD-02 — Klasa Kształt oraz klasy Koło i Kwadrat

**Poziom:** ★★☆
**Tagi:** `dziedziczenie`, `polimorfizm`, `math`

### Treść

Zaprojektuj hierarchię klas:

* `Ksztalt` — klasa bazowa dla wszystkich kształtów. Ma metodę `wypisz()`, która wypisuje informacje o kształcie w trzech liniach:

  ```
  Kształt: <nazwa>
  <parametr>
  Pole powierzchni: <pole>
  ```

  Metoda `wypisz()` jest napisana **tylko raz**, w klasie `Ksztalt` — korzysta z metod `nazwa()`, `parametr()` i `pole()`, które nadpisują klasy potomne.
* `Kolo(r)` — dziedziczy po `Ksztalt`. Metoda `nazwa()` zwraca `Koło`, `parametr()` zwraca napis `Promień: <r>`, a `pole()` zwraca $\pi r^2$.
* `Kwadrat(a)` — dziedziczy po `Ksztalt`. Metoda `nazwa()` zwraca `Kwadrat`, `parametr()` zwraca napis `Długość boku: <a>`, a `pole()` zwraca $a^2$.

Program wczytuje listę kształtów, wypisuje informacje o każdym z nich (bloki oddzielone pustą linią), a na końcu — po pustej linii — sumę pól wszystkich kształtów.

### Wejście

* 1. linia: liczba kształtów $n$
* kolejne $n$ linii: `kolo r` albo `kwadrat a`, gdzie $r$ i $a$ są dodatnimi liczbami rzeczywistymi

### Wyjście

* Dla każdego kształtu blok trzech linii opisany w treści; po każdym bloku pusta linia.
* Ostatnia linia: `Suma pól: <suma>`.

Wszystkie liczby (promień, bok, pola i suma) wypisz z dokładnością do 2 miejsc po przecinku.

### Ograniczenia

* $1 \le n \le 20$
* $0 < r, a \le 1000$

### Przykład

**Wejście:**

```
2
kolo 5
kwadrat 4
```

**Wyjście:**

```
Kształt: Koło
Promień: 5.00
Pole powierzchni: 78.54

Kształt: Kwadrat
Długość boku: 4.00
Pole powierzchni: 16.00

Suma pól: 94.54
```

### Uwagi

* Metody `nazwa()`, `parametr()` i `pole()` w klasie `Ksztalt` mogą zgłaszać wyjątek `NotImplementedError` — w ten sposób zaznaczamy, że każda klasa potomna musi je nadpisać.

### Kod startowy

```python
import math


class Ksztalt:
    def nazwa(self):
        raise NotImplementedError

    def parametr(self):
        raise NotImplementedError

    def pole(self):
        raise NotImplementedError

    def wypisz(self):
        pass


class Kolo(Ksztalt):
    def __init__(self, r):
        pass



class Kwadrat(Ksztalt):
    def __init__(self, a):
        pass



n = int(input())
ksztalty = []
for _ in range(n):
    rodzaj, wartosc = input().split()
    if rodzaj == "kolo":
        ksztalty.append(Kolo(float(wartosc)))
    else:
        ksztalty.append(Kwadrat(float(wartosc)))

suma = 0
for ksztalt in ksztalty:
    ksztalt.wypisz()
    print()
    suma += ksztalt.pole()
print(f"Suma pól: {suma:.2f}")
```

"""

import math


class Ksztalt:
    def nazwa(self):
        raise NotImplementedError

    def parametr(self):
        raise NotImplementedError

    def pole(self):
        raise NotImplementedError

    def wypisz(self):
        print(f"Kształt: {self.nazwa()}")
        print(self.parametr())
        print(f"Pole powierzchni: {self.pole():.2f}")


class Kolo(Ksztalt):
    def __init__(self, r):
        self.r = r

    def nazwa(self):
        return "Koło"

    def parametr(self):
        return f"Promień: {self.r:.2f}"

    def pole(self):
        return math.pi * self.r**2


class Kwadrat(Ksztalt):
    def __init__(self, a):
        self.a = a

    def nazwa(self):
        return "Kwadrat"

    def parametr(self):
        return f"Długość boku: {self.a:.2f}"

    def pole(self):
        return self.a**2


if __name__ == "__main__":
    n = int(input())
    ksztalty = []
    for _ in range(n):
        rodzaj, wartosc = input().split()
        if rodzaj == "kolo":
            ksztalty.append(Kolo(float(wartosc)))
        else:
            ksztalty.append(Kwadrat(float(wartosc)))

    suma = 0
    for ksztalt in ksztalty:
        ksztalt.wypisz()
        print()
        suma += ksztalt.pole()
    print(f"Suma pól: {suma:.2f}")
