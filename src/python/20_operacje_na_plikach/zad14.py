r"""
ZAD-14 — Edycja konfiguracji JSON

**Poziom:** ★★☆
**Tagi:** `files`, `json`, `dict`

### Treść

Plik konfiguracyjny w formacie JSON zawiera obiekt (w Pythonie: słownik), w którym mogą być zagnieżdżone kolejne obiekty. Wczytaj ścieżkę pliku, klucz i nową wartość. Klucz jest zapisany w **notacji kropkowej**: `baza.port` oznacza klucz `port` wewnątrz obiektu zapisanego pod kluczem `baza`.

Klucz **istnieje**, jeśli każda jego część poza ostatnią prowadzi do obiektu, a ostatnia część jest kluczem w tym obiekcie. Jeśli klucz istnieje:

1. wypisz jego dotychczasową wartość,
2. ustaw nową wartość — jako **liczbę całkowitą**, jeśli wczytany napis składa się z samych cyfr, ewentualnie poprzedzonych znakiem `-` (np. `8080`, `-5`); w przeciwnym razie jako **napis** (np. `3.5`, `true`, `localhost`),
3. zapisz cały plik od nowa poleceniem `json.dump(dane, plik, indent=2, ensure_ascii=False)`.

Dzięki takiemu zapisowi plik ma wcięcia po 2 spacje, klucze zostają w dotychczasowej kolejności, a polskie litery nie są zamieniane na kody `\u…`. Sprawdzarka porównuje plik po zmianie dokładnie z tym formatem (ignoruje tylko końcowe spacje i puste wiersze).

### Wejście

* 1. linia: ścieżka pliku
* 2. linia: klucz w notacji kropkowej
* 3. linia: nowa wartość

### Wyjście

* Dotychczasowa wartość klucza: napis bez cudzysłowów, liczba jako liczba.
* `Brak klucza: K` — gdzie `K` to wczytany klucz — jeśli klucz nie istnieje. Plik pozostaje wtedy bez zmian.
* `Plik nie istnieje.` — jeśli podana ścieżka nie wskazuje istniejącego pliku.

### Ograniczenia

* Plik zawiera poprawny JSON, którego główną wartością jest obiekt.
* Wartość pod istniejącym kluczem jest napisem albo liczbą całkowitą. Pozostałe wartości w pliku mogą być dowolne (listy, `true`, `null` …).
* Części klucza nie zawierają kropek.

### Przykład

**Pliki przed:**

```
config.json
| {
|   "nazwa": "Sklep",
|   "baza": {
|     "host": "localhost",
|     "port": 5432
|   },
|   "wersja": "1.0"
| }
```

**Wejście:**

```
config.json
baza.port
6543
```

**Wyjście:**

```
5432
```

**Pliki po:**

```
config.json
| {
|   "nazwa": "Sklep",
|   "baza": {
|     "host": "localhost",
|     "port": 6543
|   },
|   "wersja": "1.0"
| }
```

### Przykład 2

**Pliki przed:**

```
config.json
| {"nazwa": "Sklep", "baza": {"host": "localhost"}}
```

**Wejście:**

```
config.json
baza.port
6543
```

**Wyjście:**

```
Brak klucza: baza.port
```

**Pliki po:**

```
config.json
| {"nazwa": "Sklep", "baza": {"host": "localhost"}}
```

W obiekcie `baza` nie ma klucza `port`, więc plik się nie zmienia.

### Uwagi

* Moduł `json` zamienia tekst JSON na słowniki, listy, napisy i liczby Pythona i z powrotem:

```python
import json

with open("config.json", encoding="utf-8") as plik:
    dane = json.load(plik)          # np. {"baza": {"port": 5432}}

dane["baza"]["port"] = 6543

with open("config.json", "w", encoding="utf-8") as plik:
    json.dump(dane, plik, indent=2, ensure_ascii=False)
```

* Do zagnieżdżonego obiektu dojdziesz pętlą po `klucz.split(".")`: w każdym kroku sprawdź, czy bieżąca wartość jest słownikiem (`isinstance(obiekt, dict)`) i czy zawiera kolejną część klucza.

"""

import json
import os


def zamien_na_wartosc(napis):
    """'8080' -> 8080, '-5' -> -5, każdy inny napis zostaje napisem."""
    cyfry = napis[1:] if napis.startswith("-") else napis
    if cyfry.isdigit():
        return int(napis)
    return napis


def znajdz_obiekt(dane, czesci):
    """Zwraca obiekt zawierający ostatnią część klucza albo None, jeśli klucz nie istnieje."""
    obiekt = dane
    for czesc in czesci[:-1]:
        if not isinstance(obiekt, dict) or czesc not in obiekt:
            return None
        obiekt = obiekt[czesc]
    if not isinstance(obiekt, dict) or czesci[-1] not in obiekt:
        return None
    return obiekt


if __name__ == "__main__":
    sciezka = input()
    klucz = input()
    nowa_wartosc = input()

    if not os.path.isfile(sciezka):
        print("Plik nie istnieje.")
    else:
        with open(sciezka, encoding="utf-8") as plik:
            dane = json.load(plik)

        czesci = klucz.split(".")
        obiekt = znajdz_obiekt(dane, czesci)
        if obiekt is None:
            print(f"Brak klucza: {klucz}")
        else:
            print(obiekt[czesci[-1]])
            obiekt[czesci[-1]] = zamien_na_wartosc(nowa_wartosc)
            with open(sciezka, "w", encoding="utf-8") as plik:
                json.dump(dane, plik, indent=2, ensure_ascii=False)
