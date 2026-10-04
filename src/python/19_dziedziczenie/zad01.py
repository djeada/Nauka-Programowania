r"""
ZAD-01 — Wywołanie metody klasy bazowej w klasie potomnej

**Poziom:** ★☆☆
**Tagi:** `dziedziczenie`, `override`, `super`

### Treść

Zaprojektuj dwie klasy:

1. `Bazowa` — konstruktor `__init__(self, nazwa)` zapamiętuje nazwę obiektu, a metoda `przedstaw_sie()` wypisuje linię
   `Jestem klasą bazową. Nazywam się <nazwa>.`
2. `Potomna` — dziedziczy po `Bazowa` i **nadpisuje** metodę `przedstaw_sie()`. Nowa wersja:
   * najpierw **wywołuje** wersję metody z klasy bazowej (przez `super()`),
   * potem wypisuje linię `A ja jestem klasą potomną.`

Klasa `Potomna` nie potrzebuje własnego konstruktora — dziedziczy go po `Bazowa`.

Program wczytuje opis kilku obiektów, tworzy je, a następnie dla każdego z nich (w kolejności z wejścia) wywołuje metodę `przedstaw_sie()`.

### Wejście

* 1. linia: liczba obiektów $n$
* kolejne $n$ linii: rodzaj obiektu (`bazowa` albo `potomna`) i jego nazwa (jedno słowo), oddzielone spacją

### Wyjście

Komunikaty wypisane przez kolejne wywołania `przedstaw_sie()`: jedna linia dla obiektu klasy `Bazowa` i dwie linie dla obiektu klasy `Potomna`.

### Ograniczenia

* $1 \le n \le 20$

### Przykład

**Wejście:**

```
3
bazowa Ala
potomna Ola
bazowa Jan
```

**Wyjście:**

```
Jestem klasą bazową. Nazywam się Ala.
Jestem klasą bazową. Nazywam się Ola.
A ja jestem klasą potomną.
Jestem klasą bazową. Nazywam się Jan.
```

### Kod startowy

```python
class Bazowa:
    def __init__(self, nazwa):
        pass

    def przedstaw_sie(self):
        pass


class Potomna(Bazowa):
    def przedstaw_sie(self):
        pass


n = int(input())
obiekty = []
for _ in range(n):
    rodzaj, nazwa = input().split()
    if rodzaj == "bazowa":
        obiekty.append(Bazowa(nazwa))
    else:
        obiekty.append(Potomna(nazwa))

for obiekt in obiekty:
    obiekt.przedstaw_sie()
```

"""


class Bazowa:
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def przedstaw_sie(self):
        print(f"Jestem klasą bazową. Nazywam się {self.nazwa}.")


class Potomna(Bazowa):
    def przedstaw_sie(self):
        super().przedstaw_sie()
        print("A ja jestem klasą potomną.")


if __name__ == "__main__":
    n = int(input())
    obiekty = []
    for _ in range(n):
        rodzaj, nazwa = input().split()
        if rodzaj == "bazowa":
            obiekty.append(Bazowa(nazwa))
        else:
            obiekty.append(Potomna(nazwa))

    for obiekt in obiekty:
        obiekt.przedstaw_sie()
