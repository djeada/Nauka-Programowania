r"""
ZAD-06 — Wypłaty pracowników

**Poziom:** ★★☆
**Tagi:** `dziedziczenie`, `polimorfizm`, `fabryka`

### Treść

Zaprojektuj hierarchię klas pracowników:

* `Pracownik` — klasa bazowa. Konstruktor `__init__(self, imie)` zapamiętuje imię. Metoda `wyplata()` zgłasza wyjątek `NotImplementedError` (każda klasa potomna musi ją nadpisać). Metoda `opis()` zwraca napis
  `<imię> (<rodzaj>): <wypłata>`, gdzie `<rodzaj>` to atrybut klasy `rodzaj`, a wypłata jest wypisana z dokładnością do 2 miejsc po przecinku. Metoda `opis()` jest zdefiniowana **tylko** w klasie `Pracownik`.
* `Etatowy(imie, pensja)` — `rodzaj = "etatowy"`; wypłata to stała miesięczna pensja.
* `Godzinowy(imie, stawka, godziny)` — `rodzaj = "godzinowy"`; za pierwsze 160 godzin płacimy zwykłą stawkę, a za każdą godzinę powyżej 160 (nadgodziny) — stawkę 1,5 razy wyższą:
  $w = s \cdot g$ dla $g \le 160$ oraz $w = 160 s + 1.5 s (g - 160)$ dla $g > 160$.
* `Stazysta(imie)` — `rodzaj = "stażysta"`; wypłata to stałe stypendium 1500 zł, takie samo dla każdego stażysty.

Napisz też funkcję-fabrykę `utworz_pracownika(linia)`, która na podstawie jednej linii wejścia tworzy i zwraca obiekt odpowiedniej klasy.

Program wczytuje listę pracowników, wypisuje opis każdego z nich (w kolejności z wejścia) i sumę wszystkich wypłat.

### Wejście

* 1. linia: liczba pracowników $n$
* kolejne $n$ linii, każda w jednej z postaci:
  * `etatowy IMIĘ PENSJA`
  * `godzinowy IMIĘ STAWKA GODZINY`
  * `stazysta IMIĘ`

Imię to jedno słowo, pensja i stawka to liczby rzeczywiste, a liczba godzin to liczba całkowita $\ge 0$.

### Wyjście

* $n$ linii — wynik metody `opis()` dla kolejnych pracowników,
* ostatnia linia: `Suma wypłat: <suma>` (z dokładnością do 2 miejsc po przecinku).

### Ograniczenia

* $1 \le n \le 50$
* $0 \le pensja \le 100000$, $0 \le stawka \le 1000$, $0 \le godziny \le 400$

### Przykład

**Wejście:**

```
4
etatowy Anna 5200
godzinowy Bartek 40 170
stazysta Celina
godzinowy Darek 35.5 100
```

**Wyjście:**

```
Anna (etatowy): 5200.00
Bartek (godzinowy): 7000.00
Celina (stażysta): 1500.00
Darek (godzinowy): 3550.00
Suma wypłat: 17250.00
```

Bartek przepracował 10 nadgodzin: $160 \cdot 40 + 10 \cdot 1.5 \cdot 40 = 6400 + 600 = 7000$.

### Uwagi

* **Funkcja-fabryka** ukrywa przed resztą programu, jak powstają obiekty: program tylko woła `utworz_pracownika(linia)` i dostaje gotowy obiekt, a dalej korzysta wyłącznie z metod wspólnych dla wszystkich pracowników (`opis()`, `wyplata()`). Dodanie nowego rodzaju pracownika wymaga wtedy zmian tylko w nowej klasie i w fabryce.
* `raise NotImplementedError` w klasie bazowej to umowny sposób zapisania: „ta metoda musi zostać nadpisana w klasie potomnej”.

### Kod startowy

```python
class Pracownik:
    rodzaj = "pracownik"

    def __init__(self, imie):
        self.imie = imie

    def wyplata(self):
        raise NotImplementedError

    def opis(self):
        pass


class Etatowy(Pracownik):
    rodzaj = "etatowy"


class Godzinowy(Pracownik):
    rodzaj = "godzinowy"


class Stazysta(Pracownik):
    rodzaj = "stażysta"


def utworz_pracownika(linia):
    pass


n = int(input())
pracownicy = []
for _ in range(n):
    pracownicy.append(utworz_pracownika(input()))

suma = 0
for pracownik in pracownicy:
    print(pracownik.opis())
    suma += pracownik.wyplata()
print(f"Suma wypłat: {suma:.2f}")
```

"""


class Pracownik:
    rodzaj = "pracownik"

    def __init__(self, imie):
        self.imie = imie

    def wyplata(self):
        raise NotImplementedError

    def opis(self):
        return f"{self.imie} ({self.rodzaj}): {self.wyplata():.2f}"


class Etatowy(Pracownik):
    rodzaj = "etatowy"

    def __init__(self, imie, pensja):
        super().__init__(imie)
        self.pensja = pensja

    def wyplata(self):
        return self.pensja


class Godzinowy(Pracownik):
    rodzaj = "godzinowy"
    NORMA_GODZIN = 160
    MNOZNIK_NADGODZIN = 1.5

    def __init__(self, imie, stawka, godziny):
        super().__init__(imie)
        self.stawka = stawka
        self.godziny = godziny

    def wyplata(self):
        if self.godziny <= self.NORMA_GODZIN:
            return self.stawka * self.godziny
        nadgodziny = self.godziny - self.NORMA_GODZIN
        return (
            self.stawka * self.NORMA_GODZIN
            + self.MNOZNIK_NADGODZIN * self.stawka * nadgodziny
        )


class Stazysta(Pracownik):
    rodzaj = "stażysta"
    STYPENDIUM = 1500

    def wyplata(self):
        return self.STYPENDIUM


def utworz_pracownika(linia):
    czesci = linia.split()
    rodzaj, imie = czesci[0], czesci[1]
    if rodzaj == "etatowy":
        return Etatowy(imie, float(czesci[2]))
    if rodzaj == "godzinowy":
        return Godzinowy(imie, float(czesci[2]), int(czesci[3]))
    return Stazysta(imie)


if __name__ == "__main__":
    n = int(input())
    pracownicy = [utworz_pracownika(input()) for _ in range(n)]

    suma = 0
    for pracownik in pracownicy:
        print(pracownik.opis())
        suma += pracownik.wyplata()
    print(f"Suma wypłat: {suma:.2f}")
