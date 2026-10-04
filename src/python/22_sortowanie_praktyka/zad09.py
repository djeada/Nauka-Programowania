r"""
ZAD-09 — Ranking zawodników

**Poziom:** ★★☆
**Tagi:** `sort`, `key`, `lambda`, `tuple`

### Treść

Wczytaj wyniki zawodów: dla każdego zawodnika jego imię, liczbę zdobytych punktów i czas (w sekundach). Ułóż ranking według następujących zasad:

1. więcej punktów — wyższe miejsce (punkty **malejąco**),
2. przy równej liczbie punktów: krótszy czas — wyższe miejsce (czas **rosnąco**),
3. przy równych punktach i czasie zawodnicy dzielą miejsce, a w rankingu wypisujemy ich alfabetycznie według imienia (imię **rosnąco**).

Zawodnicy, którzy mają te same punkty i ten sam czas, zajmują **to samo miejsce**, a kolejne miejsca są pomijane — tak jak w sporcie: np. `1, 2, 2, 4`. Miejsce zawodnika to $1 +$ liczba zawodników, którzy mają od niego lepszy wynik.

### Wejście

* 1. linia: liczba zawodników $N$
* kolejne $N$ linii: `imię punkty czas` — imię (jedno słowo), punkty i czas (liczby całkowite $\ge 0$), oddzielone spacjami

### Wyjście

$N$ linii w kolejności rankingu, każda w postaci:

```
<miejsce>. <imię> <punkty> <czas>
```

### Ograniczenia

* $1 \le N \le 100$
* Imiona są różne.

### Przykład

**Wejście:**

```
5
Ola 90 300
Adam 95 320
Ewa 90 300
Kuba 90 280
Zosia 70 250
```

**Wyjście:**

```
1. Adam 95 320
2. Kuba 90 280
3. Ewa 90 300
3. Ola 90 300
5. Zosia 70 250
```

Ewa i Ola mają te same punkty i ten sam czas, więc dzielą 3. miejsce (wypisujemy je alfabetycznie), a następna zawodniczka zajmuje miejsce 5.

### Uwagi

* Kilka kryteriów naraz zapiszesz jako **krotkę** zwracaną przez funkcję `key` — Python porównuje krotki element po elemencie: najpierw pierwsze elementy, a przy remisie kolejne.
* Żeby posortować liczby **malejąco** w kluczu, który poza tym sortuje rosnąco, wystarczy je zanegować:
  `sorted(zawodnicy, key=lambda z: (-z[1], z[2], z[0]))` (dla krotek `(imię, punkty, czas)`).
* Po posortowaniu miejsce zawodnika jest równe miejscu poprzednika, jeśli ma on te same punkty i czas, a w przeciwnym razie — jego pozycji w rankingu (licząc od 1).

"""


def ranking(zawodnicy):
    """Zwraca listę par (miejsce, zawodnik) dla krotek (imię, punkty, czas)."""
    posortowani = sorted(zawodnicy, key=lambda z: (-z[1], z[2], z[0]))
    wynik = []
    for i, zawodnik in enumerate(posortowani):
        if i > 0 and zawodnik[1:] == posortowani[i - 1][1:]:
            miejsce = wynik[-1][0]
        else:
            miejsce = i + 1
        wynik.append((miejsce, zawodnik))
    return wynik


if __name__ == "__main__":
    n = int(input())
    zawodnicy = []
    for _ in range(n):
        imie, punkty, czas = input().split()
        zawodnicy.append((imie, int(punkty), int(czas)))

    for miejsce, (imie, punkty, czas) in ranking(zawodnicy):
        print(f"{miejsce}. {imie} {punkty} {czas}")
