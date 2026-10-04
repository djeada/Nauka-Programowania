r"""
ZAD-06 — Statystyki pliku tekstowego

**Poziom:** ★★☆
**Tagi:** `files`, `stats`, `dict`

### Treść

Wczytaj ścieżkę pliku tekstowego i oblicz:

1. liczbę wierszy,
2. łączną liczbę słów,
3. średnią długość wiersza (w znakach),
4. średnią liczbę słów w wierszu,
5. ile razy występuje każde słowo.

Definicje:

* **Wiersze** to fragmenty tekstu rozdzielone znakami nowej linii. Znak nowej linii na samym końcu pliku nie tworzy dodatkowego, pustego wiersza (tak działa `str.splitlines()`), ale puste wiersze w środku pliku się liczą.
* **Długość wiersza** to liczba jego znaków (bez znaku nowej linii), łącznie ze spacjami i interpunkcją.
* **Słowo** to najdłuższy ciąg kolejnych liter (także polskich). Wszystkie inne znaki — spacje, cyfry, interpunkcja, myślniki — rozdzielają słowa, np. `Mark-up 2024r.` zawiera słowa `Mark`, `up` i `r`.
* Licząc wystąpienia, nie rozróżniaj wielkości liter: `Ala` i `ala` to to samo słowo.

### Wejście

* 1. linia: ścieżka pliku

### Wyjście

* 1. linia: liczba wierszy,
* 2. linia: liczba słów,
* 3. linia: średnia długość wiersza z dokładnie 2 miejscami po przecinku,
* 4. linia: średnia liczba słów w wierszu z dokładnie 2 miejscami po przecinku,
* dalej: dla każdego różnego słowa jedna linia `słowo: liczba` — słowo małymi literami, w kolejności pierwszego wystąpienia w pliku. Jeśli plik nie zawiera słów, ta część jest pusta.

Przypadki szczególne (wypisz tylko komunikat):

* `Plik jest pusty.` — jeśli plik nie zawiera żadnego znaku,
* `Plik nie istnieje.` — jeśli podana ścieżka nie wskazuje istniejącego pliku.

### Przykład

**Pliki przed:**

```
tekst.txt
| Ala ma kota.
| Kot ma na imię Filemon.
| Filemon lubi mleko, Ala lubi
| kota Filemona!
```

**Wejście:**

```
tekst.txt
```

**Wyjście:**

```
4
15
19.25
3.75
ala: 2
ma: 2
kota: 2
kot: 1
na: 1
imię: 1
filemon: 2
lubi: 2
mleko: 1
filemona: 1
```

Wiersze mają 12, 23, 28 i 14 znaków, więc średnia długość to $\frac{77}{4} = 19.25$, a średnia liczba słów to $\frac{15}{4} = 3.75$.

### Uwagi

* Słowa łatwo wyodrębnić, zamieniając każdy znak, który nie jest literą (`znak.isalpha()`), na spację, a potem dzieląc wiersz metodą `split()`.
* Słownik w Pythonie pamięta kolejność dodawania kluczy.

"""

import os


def podziel_na_slowa(wiersz):
    """Zwraca listę słów (ciągów liter) z wiersza."""
    tylko_litery = ""
    for znak in wiersz:
        tylko_litery += znak if znak.isalpha() else " "
    return tylko_litery.split()


def czestosc_slow(wiersze):
    """Zwraca słownik {słowo małymi literami: liczba wystąpień}."""
    czestosc = {}
    for wiersz in wiersze:
        for slowo in podziel_na_slowa(wiersz):
            slowo = slowo.lower()
            czestosc[slowo] = czestosc.get(slowo, 0) + 1
    return czestosc


def statystyki(wiersze):
    """Zwraca (liczba wierszy, liczba słów, średnia długość wiersza, średnia liczba słów)."""
    liczba_wierszy = len(wiersze)
    liczba_slow = sum(len(podziel_na_slowa(wiersz)) for wiersz in wiersze)
    srednia_dlugosc = sum(len(wiersz) for wiersz in wiersze) / liczba_wierszy
    srednia_slow = liczba_slow / liczba_wierszy
    return liczba_wierszy, liczba_slow, srednia_dlugosc, srednia_slow


if __name__ == "__main__":
    sciezka = input()

    if not os.path.isfile(sciezka):
        print("Plik nie istnieje.")
    else:
        with open(sciezka, encoding="utf-8") as plik:
            wiersze = plik.read().splitlines()

        if not wiersze:
            print("Plik jest pusty.")
        else:
            liczba_wierszy, liczba_slow, srednia_dlugosc, srednia_slow = statystyki(
                wiersze
            )
            print(liczba_wierszy)
            print(liczba_slow)
            print(f"{srednia_dlugosc:.2f}")
            print(f"{srednia_slow:.2f}")
            for slowo, liczba in czestosc_slow(wiersze).items():
                print(f"{slowo}: {liczba}")
