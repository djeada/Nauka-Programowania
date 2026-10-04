r"""
ZAD-07 — Zliczanie instancji klasy

**Poziom:** ★☆☆
**Tagi:** `class`, `static`

### Treść

Zaprojektuj klasę `MojaKlasa`, która sama zlicza, ile jej obiektów (instancji) utworzono:

* atrybut klasy (wspólny dla wszystkich obiektów) `_licznik`, początkowo równy 0 — podkreślenie na początku nazwy oznacza, że jest to pole „prywatne”, którego nie należy zmieniać spoza klasy,
* konstruktor zwiększa licznik o 1 i zapisuje w atrybucie obiektu `numer` numer nowego obiektu (pierwszy utworzony obiekt ma numer 1),
* metoda statyczna `liczba_instancji()` zwraca liczbę dotychczas utworzonych obiektów.

Program wykonuje polecenia:

* `nowy` — tworzy nowy obiekt `MojaKlasa` i wypisuje `Utworzono obiekt nr <numer>.`
* `ile` — wypisuje `Liczba utworzonych instancji: <liczba>`

### Wejście

* 1. linia: liczba poleceń $n$
* kolejne $n$ linii: polecenie `nowy` albo `ile`

### Wyjście

Po jednej linii dla każdego polecenia, w formacie opisanym w treści.

### Ograniczenia

* $1 \le n \le 100$

### Przykład

**Wejście:**

```
5
nowy
nowy
ile
nowy
ile
```

**Wyjście:**

```
Utworzono obiekt nr 1.
Utworzono obiekt nr 2.
Liczba utworzonych instancji: 2
Utworzono obiekt nr 3.
Liczba utworzonych instancji: 3
```

### Uwagi

* Do atrybutu klasy odwołuj się przez nazwę klasy: `MojaKlasa._licznik`. Zapis `self._licznik += 1` utworzyłby osobny atrybut w każdym obiekcie i licznik nie byłby wspólny.

### Kod startowy

```python
class MojaKlasa:
    _licznik = 0

    def __init__(self):
        pass

    @staticmethod
    def liczba_instancji():
        pass


n = int(input())
obiekty = []
for _ in range(n):
    polecenie = input()
    if polecenie == "nowy":
        obiekt = MojaKlasa()
        obiekty.append(obiekt)
        print(f"Utworzono obiekt nr {obiekt.numer}.")
    elif polecenie == "ile":
        print(f"Liczba utworzonych instancji: {MojaKlasa.liczba_instancji()}")
```

"""


class MojaKlasa:
    _licznik = 0

    def __init__(self):
        MojaKlasa._licznik += 1
        self.numer = MojaKlasa._licznik

    @staticmethod
    def liczba_instancji():
        return MojaKlasa._licznik


if __name__ == "__main__":
    n = int(input())
    obiekty = []
    for _ in range(n):
        polecenie = input()
        if polecenie == "nowy":
            obiekt = MojaKlasa()
            obiekty.append(obiekt)
            print(f"Utworzono obiekt nr {obiekt.numer}.")
        elif polecenie == "ile":
            print(f"Liczba utworzonych instancji: {MojaKlasa.liczba_instancji()}")
