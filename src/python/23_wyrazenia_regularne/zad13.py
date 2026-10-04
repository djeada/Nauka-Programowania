r"""
ZAD-13 — Analiza logów serwera

**Poziom:** ★★☆
**Tagi:** `regex`, `string`, `grupy`, `słowniki`

### Treść

Serwer WWW zapisuje każde żądanie w jednym wierszu dziennika (logu), np.:

```
192.168.0.1 - - [10/Oct/2024:13:55:36 +0200] "GET /index.html HTTP/1.1" 200 2326
```

Wiersz jest **poprawny**, jeśli w całości ma postać `IP - - [DATA] "METODA ŚCIEŻKA HTTP/W" KOD ROZMIAR`, gdzie poszczególne elementy oddziela dokładnie jedna spacja, a:

* `IP` — cztery liczby (każda z 1–3 cyfr) oddzielone kropkami,
* `- -` — dosłownie dwa myślniki oddzielone spacją,
* `[DATA]` — nawias kwadratowy, co najmniej jeden dowolny znak różny od `]`, nawias zamykający,
* `METODA` — co najmniej jedna wielka litera `A–Z` (np. `GET`, `POST`),
* `ŚCIEŻKA` — zaczyna się od `/` i nie zawiera spacji,
* `W` — wersja protokołu: cyfra, kropka, cyfra (np. `1.1`),
* `KOD` — kod odpowiedzi: dokładnie 3 cyfry,
* `ROZMIAR` — liczba bajtów (same cyfry) albo `-`.

Wczytaj wiersze logu. Dla poprawnych wierszy policz, ile razy wystąpił każdy kod odpowiedzi, i znajdź najczęściej odwiedzaną ścieżkę. Policz też wiersze niepoprawne.

### Wejście

* 1. linia: `n` — liczba wierszy logu
* kolejne `n` linii: wiersze logu

### Wyjście

* Dla każdego kodu, który wystąpił: linia `KOD: liczba`, kody rosnąco.
* Linia `Najczęstsza ścieżka: ŚCIEŻKA (liczba)`. Jeśli kilka ścieżek ma tę samą największą liczbę wystąpień, wybierz najmniejszą z nich w porządku `sorted()`.
* Ostatnia linia: `Błędne wiersze: liczba`.

Jeśli nie ma żadnego poprawnego wiersza, zamiast pierwszych dwóch części wypisz `Brak poprawnych wpisów.` (a potem linię z liczbą błędnych wierszy).

### Ograniczenia

* $1 \le n \le 1000$

### Przykład

**Wejście:**

```
5
192.168.0.1 - - [10/Oct/2024:13:55:36 +0200] "GET /index.html HTTP/1.1" 200 2326
10.0.0.7 - - [10/Oct/2024:13:56:01 +0200] "GET /logo.png HTTP/1.1" 404 -
192.168.0.1 - - [10/Oct/2024:13:57:12 +0200] "POST /login HTTP/1.1" 302 512
to nie jest wpis logu
10.0.0.7 - - [10/Oct/2024:13:58:40 +0200] "GET /index.html HTTP/1.1" 200 2326
```

**Wyjście:**

```
200: 2
302: 1
404: 1
Najczęstsza ścieżka: /index.html (2)
Błędne wiersze: 1
```

### Uwagi

* **Grupy nazwane** `(?P<nazwa>...)` pozwalają odczytać fragment dopasowania po nazwie zamiast po numerze:

```python
m = re.fullmatch(r"(?P<imie>\w+) ma (?P<lat>[0-9]+) lat", "Ola ma 12 lat")
print(m.group("imie"), m.group("lat"))   # Ola 12
```

* `re.fullmatch()` zwraca `None`, gdy wiersz nie pasuje w całości — to właśnie wiersz błędny.
* W klasie znaków `[^\]]` oznacza „dowolny znak oprócz `]`”, a `\S` — „dowolny znak oprócz białych znaków”.

"""

import re

WIERSZ_LOGU = re.compile(
    r"(?P<ip>[0-9]{1,3}(?:\.[0-9]{1,3}){3}) - - "
    r"\[(?P<data>[^\]]+)\] "
    r'"(?P<metoda>[A-Z]+) (?P<sciezka>/\S*) HTTP/[0-9]\.[0-9]" '
    r"(?P<kod>[0-9]{3}) "
    r"(?P<rozmiar>[0-9]+|-)"
)


def analizuj_log(wiersze):
    """Zwraca (liczności kodów, liczności ścieżek, liczba błędnych wierszy)."""
    kody = {}
    sciezki = {}
    bledne = 0
    for wiersz in wiersze:
        dopasowanie = WIERSZ_LOGU.fullmatch(wiersz)
        if dopasowanie is None:
            bledne += 1
            continue
        kod = dopasowanie.group("kod")
        sciezka = dopasowanie.group("sciezka")
        kody[kod] = kody.get(kod, 0) + 1
        sciezki[sciezka] = sciezki.get(sciezka, 0) + 1
    return kody, sciezki, bledne


def najczestsza(licznosci):
    """Klucz o największej liczności; przy remisie — najmniejszy w porządku sorted()."""
    return min(licznosci, key=lambda klucz: (-licznosci[klucz], klucz))


if __name__ == "__main__":
    n = int(input())
    wiersze = [input() for _ in range(n)]

    kody, sciezki, bledne = analizuj_log(wiersze)
    if kody:
        for kod in sorted(kody):
            print(f"{kod}: {kody[kod]}")
        sciezka = najczestsza(sciezki)
        print(f"Najczęstsza ścieżka: {sciezka} ({sciezki[sciezka]})")
    else:
        print("Brak poprawnych wpisów.")
    print(f"Błędne wiersze: {bledne}")
