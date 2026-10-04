r"""
ZAD-10 — Koszyk zakupów (dataclass)

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
        pass


@dataclass
class Koszyk:
    produkty: list = field(default_factory=list)

    def dodaj(self, produkt):
        pass

    def suma(self):
        pass

    def wypisz_paragon(self):
        pass


koszyk = Koszyk()
n = int(input())
for _ in range(n):
    nazwa, cena, ilosc = input().split()
    koszyk.dodaj(Produkt(nazwa, float(cena), int(ilosc)))
koszyk.wypisz_paragon()
```

"""

from dataclasses import dataclass, field


@dataclass
class Produkt:
    nazwa: str
    cena: float
    ilosc: int

    def wartosc(self):
        return self.cena * self.ilosc


@dataclass
class Koszyk:
    produkty: list = field(default_factory=list)

    def dodaj(self, produkt):
        for p in self.produkty:
            if p.nazwa == produkt.nazwa:
                p.ilosc += produkt.ilosc
                return
        self.produkty.append(produkt)

    def suma(self):
        return sum(p.wartosc() for p in self.produkty)

    def wypisz_paragon(self):
        for p in self.produkty:
            print(f"{p.nazwa:<10} {p.ilosc:>3} x {p.cena:>7.2f} = {p.wartosc():>8.2f}")
        print("-" * 35)
        print(f"Razem: {self.suma():.2f}")


if __name__ == "__main__":
    koszyk = Koszyk()
    n = int(input())
    for _ in range(n):
        nazwa, cena, ilosc = input().split()
        koszyk.dodaj(Produkt(nazwa, float(cena), int(ilosc)))
    koszyk.wypisz_paragon()
