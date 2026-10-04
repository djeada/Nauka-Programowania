r"""
ZAD-11 — Gra w statki

**Poziom:** ★★★
**Tagi:** `macierze`, `gra`, `pętle`, `symulacja`

### Treść

Wczytaj planszę `10×10` do gry w statki, a potem kolejne strzały gracza i rozstrzygnij każdy z nich.

Na planszy `.` oznacza wodę, a `#` pole statku. Każdy statek to poziomy albo pionowy odcinek złożony z jednego lub kilku pól `#`; statki nie stykają się ze sobą ani bokami, ani rogami.

Strzał to para `r c` — numer wiersza i numer kolumny, **liczone od 1** (lewy górny róg to `1 1`). Dla każdego strzału wypisz jedną linię:

* `Niepoprawny strzał` — linia nie składa się z dokładnie dwóch liczb całkowitych z zakresu od 1 do 10,
* `Pole już ostrzelane` — w to pole już wcześniej strzelano (niezależnie od wyniku tamtego strzału),
* `Pudło` — w polu jest woda,
* `Trafiony` — w polu jest statek, ale ma on jeszcze nietrafione pola,
* `Trafiony, zatopiony` — trafiono ostatnie nietrafione pole statku.

Gdy zatopiony zostanie ostatni statek, wypisz dodatkowo `Wygrana po X strzałach` i zakończ program — pozostałe linie wejścia pomiń. `X` to liczba wczytanych linii ze strzałami aż do tego strzału włącznie (liczą się wszystkie strzały, także niepoprawne i powtórzone).

Jeśli strzały się skończą, zanim wszystkie statki zostaną zatopione, wypisz na końcu `Pozostało statków: Y`, gdzie `Y` to liczba niezatopionych statków.

### Wejście

* 10 linii po 10 znaków `.` lub `#` — plansza
* następnie dowolnie wiele linii (także zero) — strzały `r c`, aż do końca danych

### Wyjście

* Po jednej linii z wynikiem dla każdego rozpatrzonego strzału.
* Na końcu `Wygrana po X strzałach` albo `Pozostało statków: Y`.

### Ograniczenia

* na planszy jest co najmniej jeden statek, a pól `#` jest łącznie co najmniej 2
* co najwyżej 200 strzałów

### Przykład

**Wejście:**

```
#.........
#.........
..........
....###...
..........
..........
.........#
..........
.##.......
..........
1 1
5 5
2 1
1 1
11 3
7 10
```

**Wyjście:**

```
Trafiony
Pudło
Trafiony, zatopiony
Pole już ostrzelane
Niepoprawny strzał
Trafiony, zatopiony
Pozostało statków: 2
```

Na planszy są 4 statki: pionowy w kolumnie 1 (wiersze 1–2), poziomy w wierszu 4 (kolumny 5–7), jednomasztowiec w polu `7 10` i poziomy w wierszu 9 (kolumny 2–3). Zatopiono dwa z nich.

### Uwagi

* Planszę trzymaj jako listę list znaków (`list(input())`) i zaznaczaj na niej strzały, np. `X` — trafione pole statku, `o` — pudło. Wtedy „pole już ostrzelane” to pole z `X` albo `o`.
* Aby sprawdzić zatopienie, od trafionego pola idź w każdą z czterech stron, dopóki trafiasz na pola statku (`#` lub `X`). Statek jest zatopiony, gdy żadne z jego pól nie jest już `#`.
* Liczbę statków na początku policzysz, zliczając pola statków, które nie mają pola statku ani nad sobą, ani po lewej stronie — każdy statek ma dokładnie jedno takie pole.
* Kod startowy wczytuje wszystkie strzały do listy. Gdy dane wejściowe się skończą, `input()` zgłasza błąd `EOFError`; konstrukcja `try` / `except EOFError` przechwytuje go i kończy pętlę.

### Kod startowy

```python
plansza = [list(input()) for _ in range(10)]

strzaly = []
while True:
    try:
        strzaly.append(input())
    except EOFError:  # dane wejściowe się skończyły
        break

```

"""

ROZMIAR = 10
KIERUNKI = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Znaki na planszy: "." woda, "#" nietrafione pole statku,
# "X" trafione pole statku, "o" woda, w którą już strzelano.


def czy_statek(plansza, wiersz, kolumna):
    return (
        0 <= wiersz < ROZMIAR
        and 0 <= kolumna < ROZMIAR
        and plansza[wiersz][kolumna] in "#X"
    )


def pola_statku(plansza, wiersz, kolumna):
    """Zwraca listę pól statku, do którego należy pole [wiersz][kolumna]."""
    pola = [(wiersz, kolumna)]
    for dw, dk in KIERUNKI:
        w, k = wiersz + dw, kolumna + dk
        while czy_statek(plansza, w, k):
            pola.append((w, k))
            w, k = w + dw, k + dk
    return pola


def policz_statki(plansza):
    """Każdy statek liczymy raz — po jego lewym górnym polu."""
    liczba = 0
    for w in range(ROZMIAR):
        for k in range(ROZMIAR):
            if (
                czy_statek(plansza, w, k)
                and not czy_statek(plansza, w - 1, k)
                and not czy_statek(plansza, w, k - 1)
            ):
                liczba += 1
    return liczba


def odczytaj_strzal(linia):
    """Zwraca indeksy (wiersz, kolumna) liczone od 0 albo None dla niepoprawnej linii."""
    czesci = linia.split()
    if len(czesci) != 2 or not czesci[0].isdigit() or not czesci[1].isdigit():
        return None
    wiersz, kolumna = int(czesci[0]), int(czesci[1])
    if not (1 <= wiersz <= ROZMIAR and 1 <= kolumna <= ROZMIAR):
        return None
    return wiersz - 1, kolumna - 1


def rozegraj(plansza, strzaly):
    pozostale_statki = policz_statki(plansza)
    for numer, linia in enumerate(strzaly, start=1):
        strzal = odczytaj_strzal(linia)
        if strzal is None:
            print("Niepoprawny strzał")
            continue

        w, k = strzal
        if plansza[w][k] in "Xo":
            print("Pole już ostrzelane")
        elif plansza[w][k] == ".":
            plansza[w][k] = "o"
            print("Pudło")
        else:
            plansza[w][k] = "X"
            zatopiony = True
            for a, b in pola_statku(plansza, w, k):
                if plansza[a][b] == "#":
                    zatopiony = False
            if not zatopiony:
                print("Trafiony")
            else:
                print("Trafiony, zatopiony")
                pozostale_statki -= 1
                if pozostale_statki == 0:
                    print(f"Wygrana po {numer} strzałach")
                    return
    print(f"Pozostało statków: {pozostale_statki}")


if __name__ == "__main__":
    plansza = [list(input()) for _ in range(ROZMIAR)]

    strzaly = []
    while True:
        try:
            strzaly.append(input())
        except EOFError:  # dane wejściowe się skończyły
            break

    rozegraj(plansza, strzaly)
