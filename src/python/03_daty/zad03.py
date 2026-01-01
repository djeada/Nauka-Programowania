"""
ZAD-03 — Rok przestępny

**Poziom:** ★☆☆
**Tagi:** `modulo`, `if`, `kalendarz`

### Treść

Wczytaj rok `y` i sprawdź, czy jest przestępny w kalendarzu gregoriańskim.

Wypisz:

* `Rok jest przestępny.`
* `Rok nie jest przestępny.`

### Wejście

* 1 linia: `y` (liczba całkowita, `y ≥ 0`)

### Wyjście

Jedna linia — odpowiedni komunikat.

### Definicja

Rok jest przestępny, gdy:

* jest podzielny przez 400 **lub**
* jest podzielny przez 4 i **nie** jest podzielny przez 100.

### Przykład

**Wejście:**

```
2100
```

**Wyjście:**

```
Rok nie jest przestępny.
```

"""

if __name__ == "__main__":

    print("Podaj rok: ")
    rok = int(input())

    if rok % 4 == 0 and rok % 100 != 0 or rok % 400 == 0:
        print("Rok jest przestepny.")
    else:
        print("Rok nie jest przestepny.")
