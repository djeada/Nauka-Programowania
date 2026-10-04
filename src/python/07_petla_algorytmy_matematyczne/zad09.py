r"""
ZAD-09 — Rozkład na czynniki pierwsze

**Poziom:** ★★☆
**Tagi:** `pętle`, `pierwszość`, `dzielniki`, `złożoność`

### Treść

Napisz funkcję `wypisz_rozklad(n)`, która wypisuje rozkład liczby `n` na czynniki pierwsze: czynniki w kolejności niemalejącej, oddzielone znakiem `*`, bez spacji. Każdy czynnik powtarzamy tyle razy, ile razy dzieli `n`.

Program wczytuje `n` i wywołuje funkcję.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 2`)

### Wyjście

Jedna linia: czynniki pierwsze liczby `n` oddzielone znakiem `*`. Jeśli `n` jest liczbą pierwszą, wypisz samo `n`.

### Ograniczenia

* $2 \leq n \leq 10^{10}$

### Przykład

**Wejście:**

```
60
```

**Wyjście:**

```
2*2*3*5
```

$60 = 2 \cdot 2 \cdot 3 \cdot 5$.

### Uwagi

* Sprawdzaj kolejne dzielniki `d = 2, 3, 4, …`. Dopóki `d` dzieli `n`, wypisz `d` i podziel `n` przez `d`. Złożone `d` (np. `4`) nigdy nie podzielą `n`, bo ich czynniki pierwsze zostały już wcześniej „wydzielone”.
* **Wystarczy sprawdzać dzielniki `d`, dla których $d \cdot d \leq n$.** Gdyby liczba `n` była złożona, czyli $n = a \cdot b$ dla $2 \leq a \leq b$, to $a \cdot a \leq a \cdot b = n$ — miałaby więc dzielnik nie większy niż $\sqrt{n}$. Jeśli po zakończeniu pętli zostało `n > 1`, to pozostała liczba jest pierwsza i jest ostatnim czynnikiem.
* To ważna oszczędność: dla liczby pierwszej rzędu $10^{10}$ pętla aż do `n` wykonałaby ok. $10^{10}$ obrotów (zbyt długo), a pętla do $\sqrt{n}$ — tylko ok. $10^5$.
* Aby wypisać czynniki w jednej linii, użyj `print(d, end="")`, a znak `*` wypisuj przed każdym czynnikiem poza pierwszym.

### Kod startowy

```python
def wypisz_rozklad(n):
    pass


n = int(input())
wypisz_rozklad(n)
```

"""


def wypisz_czynnik(czynnik, pierwszy):
    if not pierwszy:
        print("*", end="")
    print(czynnik, end="")


def wypisz_rozklad(n):
    pierwszy = True
    d = 2
    while d * d <= n:
        while n % d == 0:
            wypisz_czynnik(d, pierwszy)
            pierwszy = False
            n //= d
        d += 1

    if n > 1:
        wypisz_czynnik(n, pierwszy)
    print()


if __name__ == "__main__":
    n = int(input())
    wypisz_rozklad(n)
