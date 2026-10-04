r"""
ZAD-05 — Posortuj adresy IP z pliku

**Poziom:** ★☆☆
**Tagi:** `files`, `sort`, `list`

### Treść

Wczytaj ścieżkę pliku tekstowego, w którym każdy niepusty wiersz zawiera jeden adres IPv4 — cztery liczby od 0 do 255 oddzielone kropkami, np. `192.168.1.10`. Wypisz wszystkie adresy posortowane **rosnąco według wartości liczbowych**: najpierw według pierwszej liczby, przy równych — według drugiej, potem trzeciej i czwartej.

Zwykłe porównywanie napisów da złą kolejność: `"192.168.1.10" < "192.168.1.2"`, chociaż $10 > 2$.

### Wejście

* 1. linia: ścieżka pliku z adresami

### Wyjście

* Adresy w kolejności rosnącej, każdy w osobnej linii. Powtarzające się adresy wypisz tyle razy, ile razy występują w pliku.
* `Brak adresów.` — jeśli plik nie zawiera żadnego adresu.
* `Plik nie istnieje.` — jeśli podana ścieżka nie wskazuje istniejącego pliku.

### Ograniczenia

* Puste wiersze pomiń. Wiersze z adresami nie zawierają spacji ani innych znaków.

### Przykład

**Pliki przed:**

```
adresy_ip.txt
| 192.168.1.10
| 10.0.0.1
| 192.168.1.2
| 172.16.0.5
```

**Wejście:**

```
adresy_ip.txt
```

**Wyjście:**

```
10.0.0.1
172.16.0.5
192.168.1.2
192.168.1.10
```

### Uwagi

* Wygodnie jest sortować z kluczem: `sorted(adresy, key=...)`, gdzie klucz zamienia adres na krotkę czterech liczb całkowitych.

"""

import os


def wczytaj_adresy(sciezka):
    """Zwraca listę adresów IP z pliku (puste wiersze są pomijane)."""
    with open(sciezka, encoding="utf-8") as plik:
        return [wiersz.strip() for wiersz in plik if wiersz.strip()]


def klucz_adresu(adres):
    """Zamienia adres '192.168.1.10' na krotkę (192, 168, 1, 10)."""
    return tuple(int(liczba) for liczba in adres.split("."))


def sortuj_adresy_ip(adresy):
    return sorted(adresy, key=klucz_adresu)


if __name__ == "__main__":
    sciezka = input()

    if not os.path.isfile(sciezka):
        print("Plik nie istnieje.")
    else:
        adresy = sortuj_adresy_ip(wczytaj_adresy(sciezka))
        if adresy:
            print("\n".join(adresy))
        else:
            print("Brak adresów.")
