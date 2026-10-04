r"""
ZAD-07 — Pierwiastek metodą Newtona (Herona)

**Poziom:** ★★☆
**Tagi:** `Newton`, `float`, `pętle`, `dokładność`

### Treść

Napisz funkcję `pierwiastek(n)`, która zwraca przybliżenie $\sqrt{n}$ obliczone metodą Newtona (Herona), bez użycia `math.sqrt()` ani potęgowania.

Zacznij od $x_0 = n$ i obliczaj kolejne przybliżenia ze wzoru $x_{k+1} = \frac{1}{2}\left(x_k + \frac{n}{x_k}\right)$, aż dwa kolejne przybliżenia będą różnić się o mniej niż $0.0001$, czyli $|x_{k+1} - x_k| < 0.0001$. Zwróć ostatnie obliczone przybliżenie $x_{k+1}$.

Program wczytuje `n`, wywołuje funkcję i wypisuje wynik z dokładnością do **czterech miejsc po przecinku**.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Jedna liczba — przybliżenie $\sqrt{n}$ zaokrąglone do czterech miejsc po przecinku.

### Przykład

**Wejście:**

```
16
```

**Wyjście:**

```
4.0000
```

### Uwagi

* Dla `n = 0` funkcja ma zwrócić `0.0` (wzór wymagałby dzielenia przez zero).
* Wartość bezwzględną obliczysz funkcją `abs()`.

### Kod startowy

```python
def pierwiastek(n):
    pass


n = int(input())
print(f"{pierwiastek(n):.4f}")
```

"""

DOKLADNOSC = 0.0001


def pierwiastek(n):
    if n == 0:
        return 0.0

    x = n
    while True:
        nastepne = (x + n / x) / 2
        if abs(nastepne - x) < DOKLADNOSC:
            return nastepne
        x = nastepne


if __name__ == "__main__":
    n = int(input())
    print(f"{pierwiastek(n):.4f}")
