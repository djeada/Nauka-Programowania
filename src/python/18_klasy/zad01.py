r"""
ZAD-01 — Klasa Koło

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
        pass

    def obwod(self):
        pass

    def pole(self):
        pass

    def wypisz(self):
        pass


r = float(input())
kolo = Kolo(r)
kolo.wypisz()
```

"""

import math


class Kolo:
    def __init__(self, r=1):
        self.r = r

    def obwod(self):
        return 2 * math.pi * self.r

    def pole(self):
        return math.pi * self.r**2

    def wypisz(self):
        print(f"Koło o promieniu: {self.r:.2f}")
        print(f"Obwód koła: {self.obwod():.2f}")
        print(f"Pole koła: {self.pole():.2f}")


if __name__ == "__main__":
    r = float(input())
    kolo = Kolo(r)
    kolo.wypisz()
