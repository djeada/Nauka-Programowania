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
    
    Złożoność czasowa: O(n log n), gdzie n to liczba przedziałów (sortowanie)
    Złożoność pamięciowa: O(n) dla wyniku
    """
    if not lista_przedzialow:
        return []
    
    # sortujemy liste przedzialow
    lista_przedzialow.sort()

    lista_napotkanych_przedzialow = []
    lista_napotkanych_przedzialow.append(lista_przedzialow[0])

    # przechodzimy po wszystkich przedzialach i sprawdzamy czy nie nachodza na siebie
    # jesli nie to dodajemy do listy napotkanych przedzialow
    # jesli tak to zmieniamy koniec przedzialu na maksimum z konca obecnego i poprzedniego

    for przedzial in lista_przedzialow[1:]:
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
    # Wczytanie liczby przedziałów
    n = int(input().strip())
    
    # Wczytanie przedziałów
    przedzialy = []
    for _ in range(n):
        a, b = map(int, input().strip().split())
        przedzialy.append([a, b])
    
    # Scalenie przedziałów
    # Złożoność czasowa: O(n log n)
    # Złożoność pamięciowa: O(n)
    scalone = polacz_pokrywajace_sie_przedzialy(przedzialy)
    
    # Wypisanie wyniku
    for przedzial in scalone:
        print(f"{przedzial[0]} {przedzial[1]}")
