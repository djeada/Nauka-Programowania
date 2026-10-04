r"""
ZAD-05 — Sprawdzanie, czy liczba jest palindromem

**Poziom:** ★★☆
**Tagi:** `pętle`, `modulo`, `palindrom`

### Treść

Wczytaj liczbę naturalną `n` i sprawdź, czy jest palindromem, czyli czy czytana od końca jest taka sama (np. `1221`, `7`). Wypisz odpowiedni komunikat.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Dokładnie jeden z komunikatów:

* `Liczba jest palindromem.`
* `Liczba nie jest palindromem.`

### Przykład

**Wejście:**

```
13231
```

**Wyjście:**

```
Liczba jest palindromem.
```

### Przykład 2

**Wejście:**

```
1231
```

**Wyjście:**

```
Liczba nie jest palindromem.
```

### Uwagi

* Każda liczba jednocyfrowa (także `0`) jest palindromem.
* Liczba zakończona zerem (np. `10`, `120`) nie jest palindromem, bo zapis liczby nie zaczyna się od `0`.
* Wskazówka: zbuduj w pętli liczbę o odwróconych cyfrach i porównaj ją z `n`.

"""


def odwroc_liczbe(n):
    odwrocona = 0
    while n > 0:
        odwrocona = odwrocona * 10 + n % 10
        n //= 10
    return odwrocona


def czy_palindrom(n):
    return n == odwroc_liczbe(n)


if __name__ == "__main__":
    n = int(input())

    if czy_palindrom(n):
        print("Liczba jest palindromem.")
    else:
        print("Liczba nie jest palindromem.")
