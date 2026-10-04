r"""
ZAD-07 — Algorytm Luhna (numer karty)

**Poziom:** ★★☆
**Tagi:** `pętle`, `modulo`, `suma kontrolna`

### Treść

Numery kart płatniczych mają ostatnią cyfrę kontrolną, dzięki której łatwo wykryć literówkę. Sprawdza się ją **algorytmem Luhna**:

1. Numeruj cyfry od prawej strony, zaczynając od `1` (ostatnia cyfra ma pozycję `1`, przedostatnia `2` itd.).
2. Każdą cyfrę na pozycji parzystej (`2`, `4`, `6`, …) pomnóż przez `2`. Jeśli wynik jest większy niż `9`, odejmij od niego `9`.
3. Zsumuj wszystkie otrzymane wartości: zmienione cyfry z pozycji parzystych i niezmienione cyfry z pozycji nieparzystych.
4. Numer jest poprawny, jeśli suma jest podzielna przez `10`.

Wczytaj numer jako liczbę całkowitą i sprawdź go algorytmem Luhna, wyznaczając cyfry za pomocą `% 10` i `// 10`.

### Wejście

* 1. linia: `n` — numer karty, liczba naturalna mająca od `1` do `19` cyfr

### Wyjście

Jedno słowo: `Poprawny`, jeśli numer przechodzi test Luhna, w przeciwnym razie `Niepoprawny`.

### Przykład

**Wejście:**

```
79927398713
```

**Wyjście:**

```
Poprawny
```

Cyfry od prawej: `3 1 7 8 9 3 7 2 9 9 7`. Cyfry z pozycji parzystych (`1`, `8`, `3`, `2`, `9`) po podwojeniu i ewentualnym odjęciu `9` dają `2`, `7`, `6`, `4`, `9` (suma `28`). Pozostałe cyfry (`3`, `7`, `9`, `7`, `9`, `7`) sumują się do `42`. Razem $28 + 42 = 70$, a `70` dzieli się przez `10`.

### Przykład 2

**Wejście:**

```
79927398710
```

**Wyjście:**

```
Niepoprawny
```

### Uwagi

* W każdym obrocie pętli weź ostatnią cyfrę (`n % 10`), a potem usuń ją z liczby (`n //= 10`). Dodatkowy licznik (albo zmienna przełączana na zmianę) powie Ci, czy bieżąca cyfra stoi na pozycji parzystej.
* Odjęcie `9` od podwojonej cyfry to to samo, co zsumowanie cyfr wyniku, np. $2 \cdot 8 = 16$, a $16 - 9 = 7 = 1 + 6$.

"""


def suma_luhna(n):
    suma = 0
    pozycja = 1
    while n > 0:
        cyfra = n % 10
        if pozycja % 2 == 0:
            cyfra *= 2
            if cyfra > 9:
                cyfra -= 9
        suma += cyfra
        n //= 10
        pozycja += 1
    return suma


def czy_poprawny_numer(n):
    return suma_luhna(n) % 10 == 0


if __name__ == "__main__":
    n = int(input())

    if czy_poprawny_numer(n):
        print("Poprawny")
    else:
        print("Niepoprawny")
