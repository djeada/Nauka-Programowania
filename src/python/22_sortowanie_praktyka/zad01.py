"""
ZAD-01 — Sortowanie znaków w napisie

**Poziom:** ★☆☆
**Tagi:** `sort`, `string`

### Treść

Otrzymujesz napis. Posortuj alfabetycznie wszystkie jego znaki i wypisz wynikowy napis.

### Wejście

* 1 linia: napis `s`

### Wyjście

* 1 linia: napis `s` po posortowaniu znaków rosnąco (porównanie znaków jak w Pythonie / Unicode)

### Przykład

**Wejście:**

```
Ala ma kota
```

**Wyjście:**

```
 Aaaaklmot
```

### Uwagi o formatowaniu

* Spacje też są znakami i biorą udział w sortowaniu (dlatego w przykładzie wyjście zaczyna się od spacji).

"""


def sortuj_napis(napis):
    return "".join(sorted(napis))


def test_sortuj_napis():
    assert sortuj_napis("Ala ma kota") == "  Aaaaklmot"
    assert sortuj_napis("kot ma Ale") == "  Aaeklmot"


if __name__ == "__main__":
    test_sortuj_napis()
