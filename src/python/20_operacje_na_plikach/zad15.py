r"""
ZAD-15 — Liczba wierszy z obsługą błędów

**Poziom:** ★☆☆
**Tagi:** `files`, `exceptions`, `try/except`

### Treść

Wczytaj `k` ścieżek. Dla każdej z nich wypisz w osobnej linii:

* liczbę wierszy pliku — jeśli ścieżka wskazuje istniejący plik,
* `To jest folder: X` — jeśli ścieżka wskazuje folder,
* `Brak pliku: X` — jeśli pod ścieżką nic nie ma,

gdzie `X` to ścieżka dokładnie w takiej postaci, w jakiej ją wczytano.

Wiersze liczymy jak w `str.splitlines()`: pusty plik ma 0 wierszy, a znak nowej linii na końcu pliku nie tworzy dodatkowego wiersza.

Rozwiąż zadanie w stylu „najpierw spróbuj, potem obsłuż błąd”: otwórz plik w bloku `try` i przechwyć wyjątki zgłaszane przez `open()` (zob. Uwagi).

### Wejście

* 1. linia: `k` — liczba ścieżek
* kolejne `k` linii: ścieżki

### Wyjście

`k` linii — wynik dla każdej ścieżki, w kolejności wczytywania.

### Ograniczenia

* $1 \le k \le 20$
* Żadna ścieżka nie prowadzi „przez” plik (np. `notatki.txt/a`).

### Przykład

**Pliki przed:**

```
notatki.txt
| kupić mleko
| zadzwonić do babci
dane/
```

**Wejście:**

```
3
notatki.txt
dane
raport.txt
```

**Wyjście:**

```
2
To jest folder: dane
Brak pliku: raport.txt
```

### Uwagi

* Gdy coś pójdzie nie tak, `open()` zgłasza **wyjątek**: `FileNotFoundError`, gdy pliku nie ma, i `IsADirectoryError`, gdy ścieżka wskazuje folder (na Windowsie zamiast niego pojawia się `PermissionError`). Wyjątek przechwytuje blok `try`/`except`:

```python
try:
    with open(sciezka, encoding="utf-8") as plik:
        tresc = plik.read()
except FileNotFoundError:
    print("Brak pliku:", sciezka)
```

* W ZAD-01 najpierw sprawdzaliśmy, co jest pod ścieżką (`os.path.isfile()`), a dopiero potem działaliśmy — to styl LBYL („patrz, zanim skoczysz”). Tutaj od razu próbujemy otworzyć plik i obsługujemy ewentualny błąd — to styl EAFP („łatwiej prosić o wybaczenie niż o pozwolenie”), typowy dla Pythona. Jest odporny na sytuację, w której plik zniknie między sprawdzeniem a otwarciem.

"""


def opis_sciezki(sciezka):
    """Zwraca liczbę wierszy pliku albo komunikat o błędzie."""
    try:
        with open(sciezka, encoding="utf-8") as plik:
            return str(len(plik.read().splitlines()))
    except FileNotFoundError:
        return f"Brak pliku: {sciezka}"
    except IsADirectoryError:
        return f"To jest folder: {sciezka}"


if __name__ == "__main__":
    k = int(input())
    for _ in range(k):
        print(opis_sciezki(input()))
