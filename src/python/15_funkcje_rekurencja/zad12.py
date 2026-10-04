r"""
ZAD-12 — Szybkie potęgowanie modulo

**Poziom:** ★★☆
**Tagi:** `rekurencja`, `potęgowanie`, `modulo`

### Treść

Oblicz $a^b \bmod m$, czyli resztę z dzielenia $a^b$ przez $m$, dla wykładnika $b$ nawet rzędu $10^{18}$.

Napisz rekurencyjną funkcję `potega_modulo(a, b, m)`, która **połowi wykładnik**:

* $a^0 = 1$,
* jeśli $b$ jest parzyste: $a^b = \left(a^{b/2}\right)^2$,
* jeśli $b$ jest nieparzyste: $a^b = a \cdot \left(a^{(b-1)/2}\right)^2$,

a po każdym mnożeniu bierze resztę z dzielenia przez $m$.

### Wejście

Jedna linia: trzy liczby całkowite `a b m` oddzielone spacjami.

### Wyjście

Jedna liczba całkowita — wartość $a^b \bmod m$ (z zakresu `0 … m-1`). Przyjmujemy $a^0 = 1$, także dla $a = 0$.

### Ograniczenia

* `0 ≤ a ≤ 10^9`
* `0 ≤ b ≤ 10^18`
* `1 ≤ m ≤ 10^9`

### Przykład

**Wejście:**

```
2 10 1000
```

**Wyjście:**

```
24
```

$2^{10} = 1024$, a $1024 \bmod 1000 = 24$.

### Uwagi

* Nie używaj `pow(a, b, m)`, `pow(a, b)` ani operatora `**` — potęgowanie ma wykonać Twoja funkcja.
* W ZAD-03 wykładnik malał o 1, więc potrzeba było $b$ wywołań — dla $b = 10^{18}$ to niewykonalne (a głębokość rekurencji przekroczyłaby limit). Połowienie wykładnika daje tylko około $\log_2 b$ wywołań: dla $b = 10^{18}$ to około $60$.
* Wywołaj funkcję dla połowy wykładnika **raz**, zapisz wynik w zmiennej i dopiero ją podnieś do kwadratu (`x * x`). Dwa osobne wywołania dla tej samej połowy znów dałyby około $b$ wywołań.
* Reszta z iloczynu nie zmieni się, jeśli czynniki wcześniej zastąpimy ich resztami: $(x \cdot y) \bmod m = ((x \bmod m) \cdot (y \bmod m)) \bmod m$. Dzięki temu liczby w obliczeniach pozostają małe.
* Pamiętaj o przypadku $m = 1$: każda liczba daje resztę `0`, więc dla $b = 0$ wynikiem jest `1 % m`, a nie `1`.

### Kod startowy

```python
def potega_modulo(a, b, m):
    pass


a, b, m = [int(s) for s in input().split()]
print(potega_modulo(a, b, m))
```

"""


def potega_modulo(a, b, m):
    """Zwraca a^b mod m, połowiąc wykładnik (około log2(b) wywołań)."""
    if b == 0:
        return 1 % m
    polowa = potega_modulo(a, b // 2, m)
    wynik = polowa * polowa % m
    if b % 2 == 1:
        wynik = wynik * a % m
    return wynik


if __name__ == "__main__":
    a, b, m = [int(s) for s in input().split()]
    print(potega_modulo(a, b, m))
