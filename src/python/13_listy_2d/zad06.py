"""
ZAD-06 — Scalanie przedziałów

**Poziom:** ★★☆
**Tagi:** `sortowanie`, `przedziały`, `algorytmy`

### Treść

Wczytaj `n` przedziałów `[a_i, b_i]` (a_i ≤ b_i). Scal przedziały nachodzące na siebie i wypisz wynik w kolejności rosnącej po początku.

### Wejście

* 1. linia: `n`
* następnie `n` linii: `a_i b_i`

### Wyjście

* Każdy scalony przedział w osobnej linii: `a b`

### Przykład

**Wejście:**

```
7
23 67
23 53
45 88
77 88
10 22
11 12
42 45
```

**Wyjście:**

```
10 22
23 88
```

### Uwagi

* Przedziały uznajemy za nachodzące, gdy `next_start <= current_end`.

"""


def polacz_pokrywajace_sie_przedzialy(lista_przedzialow):
    """
    Funkcja zwraca liste niepokrywajacych sie przedzialow.
    """
    # sortujemy liste przedzialow
    lista_przedzialow.sort()

    lista_napotkanych_przedzialow = []
    lista_napotkanych_przedzialow.append(lista_przedzialow[0])

    # przechodzimy po wszystkich przedzialach i sprawdzamy czy nie nachodza na siebie
    # jesli nie to dodajemy do listy napotkanych przedzialow
    # jesli tak to sprawdzamy czy to zmieniamy poczatek przedzialu na koniec poprzedniego przedzialu

    for przedzial in lista_przedzialow:
        if przedzial[0] <= lista_napotkanych_przedzialow[-1][1]:
            lista_napotkanych_przedzialow[-1][1] = max(
                przedzial[1], lista_napotkanych_przedzialow[-1][1]
            )
        else:
            lista_napotkanych_przedzialow.append(przedzial)
    return lista_napotkanych_przedzialow


def test_polacz_pokrywajace_sie_przedzialy():
    lista_przedzialow = [
        [23, 67],
        [23, 53],
        [45, 88],
        [77, 88],
        [10, 22],
        [11, 12],
        [42, 45],
    ]
    wynik = [[10, 22], [23, 88]]
    assert polacz_pokrywajace_sie_przedzialy(lista_przedzialow) == wynik


if __name__ == "__main__":
    test_polacz_pokrywajace_sie_przedzialy()
