r"""
ZAD-07 — Zamień znaki na kody ASCII

**Poziom:** ★☆☆
**Tagi:** `napisy`, `ASCII`, `ord`

### Treść

Wczytaj napis i wypisz kody ASCII wszystkich jego znaków (także spacji), w kolejności występowania.

### Wejście

* 1. linia: napis złożony ze znaków ASCII (bez polskich liter; może zawierać spacje)

### Wyjście

Jedna linia: kody ASCII oddzielone przecinkiem i spacją (`, `), bez separatora na końcu.

### Przykład

**Wejście:**

```
Robot
```

**Wyjście:**

```
82, 111, 98, 111, 116
```

### Uwagi

* Kod znaku zwraca funkcja `ord`, np. `ord("R")` to `82`.

"""


def kody_ascii(napis):
    kody = []
    for znak in napis:
        kody.append(str(ord(znak)))
    return kody


if __name__ == "__main__":
    napis = input()
    print(", ".join(kody_ascii(napis)))
