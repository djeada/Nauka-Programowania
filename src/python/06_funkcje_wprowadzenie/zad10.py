r"""
ZAD-10 — Średnia z dowolnej liczby argumentów

**Poziom:** ★★☆
**Tagi:** `funkcje`, `*args`, `krotka`, `float`

### Treść

Napisz funkcję `srednia(*liczby)`, którą można wywołać z **dowolną liczbą argumentów** — np. `srednia(2, 4)`, `srednia(1, 2, 3, 4, 5)` albo `srednia()`. Funkcja zwraca średnią arytmetyczną otrzymanych liczb, a jeśli nie dostała żadnego argumentu — zwraca `None`.

Program wczytuje linię z liczbami, przekazuje je do funkcji jako osobne argumenty (`srednia(*liczby)`) i wypisuje wynik.

### Wejście

Jedna linia: zero lub więcej liczb rzeczywistych oddzielonych spacjami. Pusta linia oznacza brak liczb.

### Wyjście

Jedna linia:

* średnia z dokładnością do **dwóch** miejsc po przecinku albo
* `Brak danych`, jeśli funkcja zwróciła `None`.

### Przykład

**Wejście:**

```
2 4 9
```

**Wyjście:**

```
5.00
```

$\frac{2 + 4 + 9}{3} = 5$.

### Uwagi

* Gwiazdka w nagłówku `def srednia(*liczby):` sprawia, że wszystkie argumenty wywołania trafiają do jednej **krotki** `liczby`. Np. po wywołaniu `srednia(2, 4, 9)` zmienna `liczby` to `(2, 4, 9)`, a po `srednia()` — pusta krotka `()`.
* Po krotce przejdziesz pętlą `for x in liczby:`, a liczbę jej elementów poda `len(liczby)`.
* Gwiazdka przy wywołaniu działa odwrotnie: `srednia(*liczby)` „rozpakowuje” listę `liczby` na osobne argumenty.
* Linia `liczby = [float(x) for x in input().split()]` w kodzie startowym zamienia wczytaną linię na listę liczb — listy poznasz dokładnie w rozdziale 9.
* `None` to specjalna wartość oznaczająca „brak wyniku”. Sprawdzamy ją warunkiem `wynik is None`.

### Kod startowy

```python
def srednia(*liczby):
    pass


liczby = [float(x) for x in input().split()]
wynik = srednia(*liczby)
if wynik is None:
    print("Brak danych")
else:
    print(f"{wynik:.2f}")
```

"""


def srednia(*liczby):
    """Zwraca średnią arytmetyczną argumentów albo None, gdy nie ma argumentów."""
    if len(liczby) == 0:
        return None
    suma = 0
    for liczba in liczby:
        suma += liczba
    return suma / len(liczby)


if __name__ == "__main__":
    liczby = [float(x) for x in input().split()]
    wynik = srednia(*liczby)
    if wynik is None:
        print("Brak danych")
    else:
        print(f"{wynik:.2f}")
