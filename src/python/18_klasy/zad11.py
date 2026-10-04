r"""
ZAD-11 — Własny zakres iterowalny

**Poziom:** ★★★
**Tagi:** `class`, `iterator`, `generator`, `yield`

### Treść

Zaprojektuj klasę `Zakres` — własny odpowiednik wbudowanej funkcji `range()` — po której obiektach można iterować pętlą `for`:

* Konstruktor `__init__(self, start, stop, krok=1)` zapamiętuje parametry. Jeśli `krok` jest równy 0, zgłasza wyjątek `ValueError("Krok nie może być równy 0.")`.
* Metoda `__iter__()` jest **generatorem** — kolejne elementy zwraca instrukcją `yield`:
  * dla kroku dodatniego: $start, start + krok, start + 2 \cdot krok, \dots$ — dopóki element jest **mniejszy** od $stop$,
  * dla kroku ujemnego: $start, start + krok, \dots$ — dopóki element jest **większy** od $stop$.

Nie używaj w klasie wbudowanej funkcji `range()` — kolejne elementy wylicz samodzielnie.

Program dla każdego zapytania `start stop krok` tworzy obiekt `Zakres` i wypisuje jego elementy oraz ich sumę. Każde przejście pętlą `for` (a także wywołanie `sum()`) uruchamia generator od nowa, więc po jednym obiekcie można iterować wiele razy.

### Wejście

* 1. linia: liczba zapytań $q$
* kolejne $q$ linii: trzy liczby całkowite `start stop krok` oddzielone spacjami

### Wyjście

Dla każdego zapytania jedna linia:

* `<elementy oddzielone spacjami> (suma: <suma>)`,
* `pusty (suma: 0)` — jeśli zakres nie zawiera żadnego elementu,
* `Błąd: Krok nie może być równy 0.` — jeśli konstruktor zgłosił wyjątek.

### Ograniczenia

* $1 \le q \le 20$
* $-1000 \le start, stop, krok \le 1000$

### Przykład

**Wejście:**

```
4
1 10 2
10 0 -3
5 5 1
0 5 0
```

**Wyjście:**

```
1 3 5 7 9 (suma: 25)
10 7 4 1 (suma: 22)
pusty (suma: 0)
Błąd: Krok nie może być równy 0.
```

### Uwagi

* Pętla `for x in obiekt:` wywołuje najpierw `iter(obiekt)`, czyli metodę `obiekt.__iter__()`, a potem pobiera z otrzymanego iteratora kolejne elementy.
* Funkcja (lub metoda), która zawiera `yield`, jest **generatorem**: jej wywołanie nie wykonuje od razu kodu, tylko zwraca iterator. Każde `yield` „oddaje” jeden element i wstrzymuje funkcję do czasu, aż pętla poprosi o następny:

  ```python
  def odliczanie(n):
      while n > 0:
          yield n
          n -= 1


  for x in odliczanie(3):
      print(x)        # 3, 2, 1 (w osobnych liniach)
  ```

* Wyjątek zgłoszony w konstruktorze przechwytuje program główny w bloku `try`/`except` (zob. zadanie „Konto bankowe”).

### Kod startowy

```python
class Zakres:
    def __init__(self, start, stop, krok=1):
        pass

    def __iter__(self):
        pass


q = int(input())
for _ in range(q):
    start, stop, krok = [int(x) for x in input().split()]
    try:
        zakres = Zakres(start, stop, krok)
    except ValueError as e:
        print(f"Błąd: {e}")
        continue
    elementy = [str(x) for x in zakres]
    if elementy:
        tekst = " ".join(elementy)
    else:
        tekst = "pusty"
    print(f"{tekst} (suma: {sum(zakres)})")
```

"""


class Zakres:
    def __init__(self, start, stop, krok=1):
        if krok == 0:
            raise ValueError("Krok nie może być równy 0.")
        self.start = start
        self.stop = stop
        self.krok = krok

    def __iter__(self):
        x = self.start
        if self.krok > 0:
            while x < self.stop:
                yield x
                x += self.krok
        else:
            while x > self.stop:
                yield x
                x += self.krok


if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        start, stop, krok = [int(x) for x in input().split()]
        try:
            zakres = Zakres(start, stop, krok)
        except ValueError as e:
            print(f"Błąd: {e}")
            continue
        elementy = [str(x) for x in zakres]
        if elementy:
            tekst = " ".join(elementy)
        else:
            tekst = "pusty"
        print(f"{tekst} (suma: {sum(zakres)})")
