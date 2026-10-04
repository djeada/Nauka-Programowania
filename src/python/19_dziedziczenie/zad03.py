r"""
ZAD-03 — Polimorfizm: Zwierz, Pies i Kot

**Poziom:** ★★☆
**Tagi:** `dziedziczenie`, `polimorfizm`, `override`

### Treść

Zaprojektuj klasy:

* `Zwierz` — konstruktor `__init__(self, imie)` zapamiętuje imię zwierzęcia. Metoda `odglos()` zwraca napis `...` (ogólny, nieokreślony dźwięk). Metoda `przedstaw_sie()` wypisuje linię:

  ```
  <NazwaKlasy> <imię> wydaje odgłos: <odgłos>
  ```

  gdzie `<NazwaKlasy>` to nazwa klasy obiektu (`Zwierz`, `Pies` albo `Kot`), a `<odgłos>` to wynik metody `odglos()`.
* `Pies` — dziedziczy po `Zwierz` i nadpisuje `odglos()`, która zwraca `Hau!`.
* `Kot` — dziedziczy po `Zwierz` i nadpisuje `odglos()`, która zwraca `Miau!`.

Klasy `Pies` i `Kot` **nie** definiują własnej metody `przedstaw_sie()` — korzystają z odziedziczonej. Dzięki polimorfizmowi wywołanie `self.odglos()` wewnątrz `przedstaw_sie()` uruchomi wersję metody właściwą dla klasy obiektu.

Program wczytuje listę zwierząt, umieszcza je w jednej liście i dla każdego (w kolejności z wejścia) wywołuje `przedstaw_sie()`.

### Wejście

* 1. linia: liczba zwierząt $n$
* kolejne $n$ linii: rodzaj zwierzęcia (`zwierz`, `pies` albo `kot`) i jego imię (jedno słowo), oddzielone spacją

### Wyjście

$n$ linii — po jednej dla każdego zwierzęcia, w formacie podanym w treści.

### Ograniczenia

* $1 \le n \le 20$

### Przykład

**Wejście:**

```
3
zwierz Gucio
pies Burek
kot Mruczek
```

**Wyjście:**

```
Zwierz Gucio wydaje odgłos: ...
Pies Burek wydaje odgłos: Hau!
Kot Mruczek wydaje odgłos: Miau!
```

### Uwagi

* Nazwę klasy obiektu można odczytać wyrażeniem `type(self).__name__`.

### Kod startowy

```python
class Zwierz:
    def __init__(self, imie):
        pass

    def odglos(self):
        pass

    def przedstaw_sie(self):
        pass


class Pies(Zwierz):
    pass


class Kot(Zwierz):
    pass


n = int(input())
zwierzeta = []
for _ in range(n):
    rodzaj, imie = input().split()
    if rodzaj == "pies":
        zwierzeta.append(Pies(imie))
    elif rodzaj == "kot":
        zwierzeta.append(Kot(imie))
    else:
        zwierzeta.append(Zwierz(imie))

for zwierze in zwierzeta:
    zwierze.przedstaw_sie()
```

"""


class Zwierz:
    def __init__(self, imie):
        self.imie = imie

    def odglos(self):
        return "..."

    def przedstaw_sie(self):
        nazwa_klasy = type(self).__name__
        print(f"{nazwa_klasy} {self.imie} wydaje odgłos: {self.odglos()}")


class Pies(Zwierz):
    def odglos(self):
        return "Hau!"


class Kot(Zwierz):
    def odglos(self):
        return "Miau!"


if __name__ == "__main__":
    n = int(input())
    zwierzeta = []
    for _ in range(n):
        rodzaj, imie = input().split()
        if rodzaj == "pies":
            zwierzeta.append(Pies(imie))
        elif rodzaj == "kot":
            zwierzeta.append(Kot(imie))
        else:
            zwierzeta.append(Zwierz(imie))

    for zwierze in zwierzeta:
        zwierze.przedstaw_sie()
