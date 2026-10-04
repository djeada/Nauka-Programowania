r"""
ZAD-13 — Odwrócenie słownika

**Poziom:** ★☆☆
**Tagi:** `dict`, `setdefault`, `wyrażenie słownikowe`

### Treść

Wczytaj `n` par `osoba miasto` — słownik, który każdej osobie przypisuje miasto, w którym mieszka. „Odwróć” go: zbuduj słownik `miasto → lista osób` mieszkających w tym mieście.

Wypisz:

1. dla każdego miasta (w kolejności alfabetycznej) linię `miasto: osoba1, osoba2, …` z osobami posortowanymi alfabetycznie,
2. w ostatniej linii słownik `{miasto: liczba osób}` z miastami w kolejności alfabetycznej, zbudowany **wyrażeniem słownikowym** i wypisany przez `print(slownik)`.

### Wejście

* 1. linia: `n`
* następnie `n` linii: `osoba miasto` — dwa słowa oddzielone spacją

### Wyjście

* Po jednej linii dla każdego miasta: nazwa miasta, dwukropek, spacja i osoby oddzielone przecinkiem ze spacją.
* Ostatnia linia: słownik w postaci `{'Miasto': liczba, …}`.

### Ograniczenia

* `1 ≤ n ≤ 50`
* osoby są różne; imiona i nazwy miast składają się z liter alfabetu łacińskiego bez polskich znaków i zaczynają się wielką literą

### Przykład

**Wejście:**

```
5
Anna Warszawa
Jan Lublin
Ewa Warszawa
Adam Gdynia
Bartek Lublin
```

**Wyjście:**

```
Gdynia: Adam
Lublin: Bartek, Jan
Warszawa: Anna, Ewa
{'Gdynia': 1, 'Lublin': 2, 'Warszawa': 2}
```

### Uwagi

* `slownik.setdefault(klucz, domyslna)` zwraca wartość dla klucza, a jeśli klucza jeszcze nie ma — najpierw wstawia `domyslna` i zwraca ją. Dzięki temu dopisanie osoby do listy miasta to jedna linia:

  ```python
  miasta = {}
  miasta.setdefault("Lublin", []).append("Jan")
  miasta.setdefault("Lublin", []).append("Bartek")
  print(miasta)  # {'Lublin': ['Jan', 'Bartek']}
  ```

* **Wyrażenie słownikowe** (*dict comprehension*) buduje słownik w jednej linii, podobnie jak wyrażenie listowe buduje listę: `{x: x * x for x in range(1, 4)}` daje `{1: 1, 2: 4, 3: 9}`.
* `sorted(slownik)` zwraca posortowaną listę kluczy słownika.

"""


def odwroc(osoba_miasto):
    """Zamienia słownik osoba -> miasto na słownik miasto -> lista osób."""
    miasta = {}
    for osoba, miasto in osoba_miasto.items():
        # setdefault zwraca listę dla miasta, a gdy jej jeszcze nie ma — najpierw wstawia []
        miasta.setdefault(miasto, []).append(osoba)
    return miasta


if __name__ == "__main__":
    n = int(input())
    osoba_miasto = {}
    for _ in range(n):
        osoba, miasto = input().split()
        osoba_miasto[osoba] = miasto

    miasta = odwroc(osoba_miasto)
    for miasto in sorted(miasta):
        print(f"{miasto}: {', '.join(sorted(miasta[miasto]))}")

    liczba_osob = {miasto: len(miasta[miasto]) for miasto in sorted(miasta)}
    print(liczba_osob)
