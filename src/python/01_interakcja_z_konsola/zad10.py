r"""
ZAD-10 — Sekundy → format GG:MM:SS

**Poziom:** ★☆☆
**Tagi:** `dzielenie całkowite`, `modulo`, `formatowanie`

### Treść

Wczytaj liczbę sekund `s` i zapisz ją jako czas w formacie `GG:MM:SS`: pełne godziny, pozostałe pełne minuty (0–59) i pozostałe sekundy (0–59). Każdą część wypisz jako **dwie cyfry** — w razie potrzeby z zerem wiodącym (np. `07`).

### Wejście

* 1 linia: `s` — liczba całkowita, $0 \le s < 360000$

### Wyjście

Jedna linia: czas w formacie `GG:MM:SS`.

### Przykład

**Wejście:**

```
3725
```

**Wyjście:**

```
01:02:05
```

$3725 = 1 \cdot 3600 + 2 \cdot 60 + 5$, czyli 1 godzina, 2 minuty i 5 sekund.

### Uwagi

* Wbudowana funkcja `divmod(a, b)` zwraca naraz iloraz całkowity i resztę z dzielenia: `godziny, reszta = divmod(s, 3600)` daje to samo co `godziny = s // 3600` oraz `reszta = s % 3600`.
* Liczbę z zerem wiodącym wypiszesz formatowaniem `:02d`, np. `f"{5:02d}"` daje `05`, a `f"{12:02d}"` daje `12`.
* Ograniczenie $s < 360000$ gwarantuje, że godzin jest co najwyżej 99, czyli zawsze wystarczą dwie cyfry.

"""


def format_czasu(sekundy):
    godziny, reszta = divmod(sekundy, 3600)
    minuty, sekundy = divmod(reszta, 60)
    return f"{godziny:02d}:{minuty:02d}:{sekundy:02d}"


if __name__ == "__main__":
    s = int(input())
    print(format_czasu(s))
