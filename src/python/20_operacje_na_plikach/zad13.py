r"""
ZAD-13 — Raport z pliku CSV

**Poziom:** ★★☆
**Tagi:** `files`, `csv`, `dict`

### Treść

Wczytaj ścieżkę pliku CSV z ocenami uczniów. Pierwszy wiersz pliku to nagłówek `imie,przedmiot,ocena`, a każdy kolejny wiersz opisuje jedną ocenę: imię ucznia, przedmiot i ocenę. Pola są oddzielone przecinkami, a pole zawierające przecinek jest ujęte w cudzysłów, np. `Adam,"WOS, rozszerzony",5`.

Dla każdego ucznia oblicz średnią wszystkich jego ocen (ze wszystkich przedmiotów razem) i wypisz wyniki uczniów w kolejności alfabetycznej imion.

### Wejście

* 1. linia: ścieżka pliku CSV

### Wyjście

* Dla każdego ucznia jedna linia `imię: średnia`, średnia z dokładnie 2 miejscami po przecinku. Uczniowie posortowani rosnąco po imieniu (tak jak sortuje `sorted()`).
* `Brak danych.` — jeśli plik zawiera tylko nagłówek.
* `Plik nie istnieje.` — jeśli podana ścieżka nie wskazuje istniejącego pliku.

### Ograniczenia

* Oceny to liczby od 1 do 6, całkowite albo z kropką dziesiętną (np. `4.5`).
* Plik nie zawiera pustych wierszy. Imiona porównujemy dokładnie — wielkość liter ma znaczenie.

### Przykład

**Pliki przed:**

```
oceny.csv
| imie,przedmiot,ocena
| Ola,matematyka,5
| Jan,fizyka,3
| Ola,"WOS, rozszerzony",4
| Jan,matematyka,4
| Ewa,historia,6
```

**Wejście:**

```
oceny.csv
```

**Wyjście:**

```
Ewa: 6.00
Jan: 3.50
Ola: 4.50
```

Ola ma oceny 5 i 4, więc jej średnia to $\frac{5 + 4}{2} = 4.5$.

### Uwagi

* Moduł `csv` dzieli wiersze na pola za Ciebie i poprawnie obsługuje cudzysłowy — zwykłe `split(",")` rozbiłoby `"WOS, rozszerzony"` na dwa pola. `csv.DictReader` pomija nagłówek i zwraca każdy kolejny wiersz jako słownik `{nazwa kolumny: wartość}`:

```python
import csv

with open("oceny.csv", encoding="utf-8", newline="") as plik:
    for wiersz in csv.DictReader(plik):
        print(wiersz["imie"], wiersz["przedmiot"], wiersz["ocena"])
```

* Wartości z pliku CSV są napisami — ocenę zamień na liczbę przez `float()`. Sumy i liczby ocen zbieraj w słownikach, których kluczem jest imię.

"""

import csv
import os


def srednie_uczniow(sciezka):
    """Zwraca słownik {imię: średnia ocen} na podstawie pliku CSV."""
    sumy = {}
    liczby = {}
    with open(sciezka, encoding="utf-8", newline="") as plik:
        for wiersz in csv.DictReader(plik):
            imie = wiersz["imie"]
            sumy[imie] = sumy.get(imie, 0) + float(wiersz["ocena"])
            liczby[imie] = liczby.get(imie, 0) + 1
    return {imie: sumy[imie] / liczby[imie] for imie in sumy}


if __name__ == "__main__":
    sciezka = input()

    if not os.path.isfile(sciezka):
        print("Plik nie istnieje.")
    else:
        srednie = srednie_uczniow(sciezka)
        if not srednie:
            print("Brak danych.")
        for imie in sorted(srednie):
            print(f"{imie}: {srednie[imie]:.2f}")
