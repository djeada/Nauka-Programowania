r"""
ZAD-21 — Rzuty kostką z ziarnem

**Poziom:** ★☆☆
**Tagi:** `listy`, `random`, `zliczanie`

### Treść

Zasymuluj `n` rzutów sześcienną kostką do gry i policz, ile razy wypadła każda liczba oczek.

Wczytaj `ziarno` i `n`. Ustaw ziarno generatora liczb losowych instrukcją `random.seed(ziarno)`, a następnie wykonaj `n` rzutów — każdy to jedno wywołanie `random.randint(1, 6)`. Wyniki zliczaj w liście sześciu liczników.

### Wejście

* 1. linia: liczba całkowita `ziarno`
* 2. linia: liczba rzutów `n`

### Wyjście

Sześć linii w formacie `oczka: liczba`, dla oczek od `1` do `6` po kolei — np. `3: 1` oznacza, że trójka wypadła raz.

### Ograniczenia

* $n \ge 0$

### Przykład

**Wejście:**

```
42
10
```

**Wyjście:**

```
1: 3
2: 3
3: 1
4: 0
5: 0
6: 3
```

Dla ziarna `42` kolejne rzuty to: 6, 1, 1, 6, 3, 2, 2, 2, 6, 1.

### Uwagi

* Moduł `random` (dołączany instrukcją `import random`) losuje liczby. `random.randint(a, b)` zwraca losową liczbę całkowitą od `a` do `b` **włącznie**.
* Liczby z komputera są tak naprawdę **pseudolosowe**: wylicza je wzór, który zaczyna od pewnej wartości początkowej — **ziarna**. Po `random.seed(ziarno)` z tym samym ziarnem zawsze otrzymasz ten sam ciąg liczb. Dzięki temu wynik programu da się sprawdzić automatycznie.
* Aby otrzymać dokładnie te same wyniki co sprawdzarka, wywołaj `random.randint(1, 6)` dokładnie `n` razy, po jednym razie na rzut, i nie losuj nic innego.
* `[0] * 6` tworzy listę sześciu zer `[0, 0, 0, 0, 0, 0]`. Wygodnie jest liczyć `k` oczek w elemencie o indeksie `k - 1`.

### Kod startowy

```python
import random

ziarno = int(input())
n = int(input())
random.seed(ziarno)

liczniki = [0] * 6  # liczniki[0] — liczba jedynek, …, liczniki[5] — liczba szóstek

for oczka in range(1, 7):
    print(f"{oczka}: {liczniki[oczka - 1]}")
```

"""

import random


def rzuty_kostka(n):
    """Wykonuje n rzutów kostką i zwraca listę liczników oczek 1-6."""
    liczniki = [0] * 6
    for _ in range(n):
        oczka = random.randint(1, 6)
        liczniki[oczka - 1] += 1
    return liczniki


if __name__ == "__main__":
    ziarno = int(input())
    n = int(input())
    random.seed(ziarno)
    liczniki = rzuty_kostka(n)
    for oczka in range(1, 7):
        print(f"{oczka}: {liczniki[oczka - 1]}")
