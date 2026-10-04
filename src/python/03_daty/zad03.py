r"""
ZAD-03 — Rok przestępny

**Poziom:** ★☆☆
**Tagi:** `modulo`, `if`, `kalendarz`

### Treść

Wczytaj rok `y` i sprawdź, czy jest przestępny w kalendarzu gregoriańskim.

Rok jest przestępny, gdy:

* jest podzielny przez 400 **lub**
* jest podzielny przez 4 i **nie** jest podzielny przez 100.

Wypisz:

* `Rok jest przestępny.` — jeśli rok jest przestępny,
* `Rok nie jest przestępny.` — w przeciwnym razie.

### Wejście

* 1 linia: `y` — liczba całkowita, $1 \le y \le 9999$

### Wyjście

Jedna linia — odpowiedni komunikat.

### Przykład

**Wejście:**

```
2100
```

**Wyjście:**

```
Rok nie jest przestępny.
```

Rok 2100 jest podzielny przez 4 i przez 100, ale nie przez 400.

"""


def czy_przestepny(rok):
    return rok % 400 == 0 or (rok % 4 == 0 and rok % 100 != 0)


if __name__ == "__main__":
    rok = int(input())

    if czy_przestepny(rok):
        print("Rok jest przestępny.")
    else:
        print("Rok nie jest przestępny.")
