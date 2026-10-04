r"""
ZAD-01 — Podmiana słowa w zdaniu

**Poziom:** ★★☆
**Tagi:** `string`, `replace`, `substring`

### Treść

Otrzymujesz zdanie `S` oraz dwa napisy `A` i `B`. Zamień **wszystkie wystąpienia** napisu `A` w zdaniu na napis `B`. `A` może być częścią dłuższych słów — zamieniamy każde wystąpienie podnapisu.

Wystąpienia szukamy od lewej do prawej. Po każdej zamianie szukanie trwa dalej **za zamienionym fragmentem**, więc wystąpienia nie nakładają się na siebie, a wstawiony napis `B` nie jest ponownie przeszukiwany. Na przykład w `aaa` zamiana `aa` na `b` daje `ba`, a w `ab` zamiana `a` na `aa` daje `aab`.

### Wejście

* 1. linia: zdanie `S`
* 2. linia: napis `A` (szukany)
* 3. linia: napis `B` (wstawiany)

### Wyjście

Jedna linia: zdanie po zamianie.

### Ograniczenia

* `1 ≤ |S| ≤ 1000`
* `1 ≤ |A|, |B| ≤ 100` (żaden z napisów nie jest pusty)

### Przykład

**Wejście:**

```
Lezy jezy na wiezy
zy
rzy
```

**Wyjście:**

```
Lerzy jerzy na wierzy
```

### Uwagi

* Spróbuj nie używać metody `replace`: przechodź po zdaniu indeksem `i` i sprawdzaj, czy w tym miejscu zaczyna się `A` (np. porównując wycinek `S[i:i + len(A)]` z `A`). Jeśli tak — dopisz do wyniku `B` i przeskocz o `len(A)` znaków; jeśli nie — dopisz bieżący znak i przejdź o jeden dalej.

"""


def zamien_wszystkie(zdanie, stary, nowy):
    """Zamienia wszystkie (nienakładające się) wystąpienia napisu stary na nowy."""
    wynik = []
    i = 0

    while i < len(zdanie):
        if zdanie[i : i + len(stary)] == stary:
            wynik.append(nowy)
            i += len(stary)  # wstawionego tekstu nie przeszukujemy ponownie
        else:
            wynik.append(zdanie[i])
            i += 1

    return "".join(wynik)


if __name__ == "__main__":
    zdanie = input()
    stary = input()
    nowy = input()
    print(zamien_wszystkie(zdanie, stary, nowy))
