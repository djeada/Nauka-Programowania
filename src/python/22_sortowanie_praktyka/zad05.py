r"""
ZAD-05 — Sortowanie listy miast

**Poziom:** ★☆☆
**Tagi:** `class`, `sort`, `obiekty`

### Treść

Klasa `Miasto` ma atrybuty:

* `nazwa` (napis),
* `liczba_mieszkancow` (liczba naturalna).

Uzupełnij metodę `__repr__`, tak aby obiekt był wypisywany w postaci `Miasto("NAZWA", LICZBA)`, np. `Miasto("Berlin", 3800000)`. Dzięki temu `print(lista_miast)` wypisze całą listę w czytelnej postaci.

Wczytaj listę miast, a następnie:

a) posortuj miasta alfabetycznie według nazwy,
b) posortuj miasta rosnąco według liczby mieszkańców (miasta o tej samej liczbie mieszkańców zachowują kolejność z wejścia).

### Wejście

* 1. linia: liczba miast $N$
* kolejne $N$ linii: nazwa miasta (bez spacji) i liczba mieszkańców, oddzielone spacją

### Wyjście

* 1. linia: lista miast posortowana według podpunktu a)
* 2. linia: lista miast posortowana według podpunktu b)

Każdą listę wypisz przez `print(lista)` — w formacie `[Miasto("NAZWA", LICZBA), Miasto("NAZWA", LICZBA), …]`.

### Ograniczenia

* $1 \le N \le 20$
* Nazwy miast są różne.

### Przykład

**Wejście:**

```
3
Paris 2150000
Berlin 3800000
New_York 8400000
```

**Wyjście:**

```
[Miasto("Berlin", 3800000), Miasto("New_York", 8400000), Miasto("Paris", 2150000)]
[Miasto("Paris", 2150000), Miasto("Berlin", 3800000), Miasto("New_York", 8400000)]
```

### Kod startowy

```python
class Miasto:
    def __init__(self, nazwa, liczba_mieszkancow):
        self.nazwa = nazwa
        self.liczba_mieszkancow = liczba_mieszkancow

    def __repr__(self):
        pass


n = int(input())
miasta = []
for _ in range(n):
    nazwa, liczba = input().split()
    miasta.append(Miasto(nazwa, int(liczba)))

```

"""


class Miasto:
    def __init__(self, nazwa, liczba_mieszkancow):
        self.nazwa = nazwa
        self.liczba_mieszkancow = liczba_mieszkancow

    def __repr__(self):
        return f'Miasto("{self.nazwa}", {self.liczba_mieszkancow})'


def sortuj_wedlug_nazwy(miasta):
    return sorted(miasta, key=lambda miasto: miasto.nazwa)


def sortuj_wedlug_liczby_mieszkancow(miasta):
    return sorted(miasta, key=lambda miasto: miasto.liczba_mieszkancow)


if __name__ == "__main__":
    n = int(input())
    miasta = []
    for _ in range(n):
        nazwa, liczba = input().split()
        miasta.append(Miasto(nazwa, int(liczba)))

    print(sortuj_wedlug_nazwy(miasta))
    print(sortuj_wedlug_liczby_mieszkancow(miasta))
