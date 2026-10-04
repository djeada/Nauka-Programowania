r"""
ZAD-15 — Robot na siatce

**Poziom:** ★★☆
**Tagi:** `dict`, `krotki`, `zbiory`

### Treść

Robot stoi na polu $(0, 0)$ nieskończonej kratkowanej płaszczyzny i wykonuje ciąg ruchów:

* `N` — o jedno pole na północ: $y$ rośnie o 1,
* `S` — na południe: $y$ maleje o 1,
* `E` — na wschód: $x$ rośnie o 1,
* `W` — na zachód: $x$ maleje o 1.

Pole startowe liczy się jako odwiedzone raz, a każdy ruch to jedno odwiedzenie pola, na które robot wchodzi. Wypisz:

1. liczbę różnych odwiedzonych pól (razem z polem startowym),
2. najczęściej odwiedzane pole i liczbę jego odwiedzin; przy remisie — to z nich, które robot odwiedził po raz pierwszy najwcześniej,
3. `Tak`, jeśli po wykonaniu wszystkich ruchów robot stoi na polu startowym, w przeciwnym razie `Nie`.

### Wejście

* 1. linia: ciąg ruchów złożony z liter `N`, `S`, `E`, `W` (bez spacji)

### Wyjście

* 1. linia: liczba różnych odwiedzonych pól
* 2. linia: `x y k` — współrzędne najczęściej odwiedzanego pola i liczba jego odwiedzin
* 3. linia: `Tak` albo `Nie`

### Ograniczenia

* ciąg ma od 1 do 1000 ruchów

### Przykład

**Wejście:**

```
NESW
```

**Wyjście:**

```
4
0 0 2
Tak
```

Robot odwiedza kolejno pola $(0, 0)$, $(0, 1)$, $(1, 1)$, $(1, 0)$ i znowu $(0, 0)$ — to pole odwiedził dwa razy.

### Uwagi

* Pozycję trzymaj jako krotkę `(x, y)`. Krotki — w przeciwieństwie do list — mogą być kluczami słownika i elementami zbioru, np. `odwiedziny[(0, 0)] = 1`.
* Krotkę łatwo „rozpakować” do zmiennych: `x, y = pozycja`. Przesunięcia też można trzymać w słowniku: `RUCHY = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}`, a potem `dx, dy = RUCHY[ruch]`.
* Liczba różnych pól to liczba kluczy słownika odwiedzin — albo rozmiar zbioru (`set`) odwiedzonych pozycji.
* Kolejność kluczy w słowniku to kolejność pierwszego wstawienia, co ułatwia rozstrzygnięcie remisu.

"""

RUCHY = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}


def przejdz(ruchy):
    """
    Zwraca słownik pole -> liczba odwiedzin (pola to krotki (x, y), w kolejności
    pierwszego odwiedzenia) oraz pole, na którym robot kończy.
    """
    pozycja = (0, 0)
    odwiedziny = {pozycja: 1}
    for ruch in ruchy:
        dx, dy = RUCHY[ruch]
        x, y = pozycja
        pozycja = (x + dx, y + dy)
        odwiedziny[pozycja] = odwiedziny.get(pozycja, 0) + 1
    return odwiedziny, pozycja


def najczesciej_odwiedzane(odwiedziny):
    """Przy remisie wygrywa pole odwiedzone po raz pierwszy najwcześniej."""
    najlepsze = None
    for pole in odwiedziny:
        if najlepsze is None or odwiedziny[pole] > odwiedziny[najlepsze]:
            najlepsze = pole
    return najlepsze


if __name__ == "__main__":
    ruchy = input().strip()
    odwiedziny, koniec = przejdz(ruchy)

    print(len(odwiedziny))
    x, y = najczesciej_odwiedzane(odwiedziny)
    print(x, y, odwiedziny[(x, y)])
    print("Tak" if koniec == (0, 0) else "Nie")
