r"""
ZAD-06C — Sekundy → pełne godziny

**Poziom:** ★☆☆
**Tagi:** `dzielenie całkowite`

### Treść

Wczytaj liczbę sekund `s` i wypisz, ile **pełnych godzin** się w niej mieści (godzina ma 3600 sekund).

### Wejście

* 1 linia: `s` — liczba całkowita, $0 \le s \le 10^9$

### Wyjście

Jedna linia: liczba pełnych godzin, czyli $\lfloor s / 3600 \rfloor$ (w Pythonie `s // 3600`).

### Przykład

**Wejście:**

```
8639
```

**Wyjście:**

```
2
```

8639 sekund to 2 godziny i 1439 sekund, więc pełne godziny są 2.

"""


def pelne_godziny(sekundy):
    return sekundy // 3600


if __name__ == "__main__":
    sekundy = int(input())
    print(pelne_godziny(sekundy))
