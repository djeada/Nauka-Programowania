r"""
ZAD-08 — Koszt pokrycia podłogi płytkami

**Poziom:** ★★☆
**Tagi:** `ceil`, `arytmetyka`, `formatowanie`, `geometria`

### Treść

Dane są:

* cena jednej płytki `p` (w złotych),
* bok kwadratowej płytki `t` (w centymetrach),
* długość podłogi `L` (w centymetrach),
* szerokość podłogi `W` (w centymetrach).

Płytki układamy w prostokątną siatkę równolegle do ścian. Wzdłuż każdego wymiaru liczbę płytek zaokrąglamy **w górę** (ostatnią płytkę w rzędzie się docina, ale trzeba ją kupić w całości):

* $n_L = \lceil L / t \rceil$
* $n_W = \lceil W / t \rceil$
* liczba płytek: $n = n_L \cdot n_W$

Oblicz całkowity koszt zakupu płytek: $n \cdot p$.

### Wejście

4 liczby, każda w osobnej linii:

* 1. linia: `p` — liczba rzeczywista
* 2. linia: `t` — liczba całkowita
* 3. linia: `L` — liczba całkowita
* 4. linia: `W` — liczba całkowita

### Wyjście

Jedna linia: całkowity koszt do **2 miejsc po przecinku**.

### Ograniczenia

* $0 < p \le 1000$
* $1 \le t, L, W \le 10^4$

### Przykład

**Wejście:**

```
2
3
20
40
```

**Wyjście:**

```
196.00
```

$n_L = \lceil 20 / 3 \rceil = 7$, $n_W = \lceil 40 / 3 \rceil = 14$, więc potrzeba $7 \cdot 14 = 98$ płytek, które kosztują $98 \cdot 2 = 196$ zł.

### Uwagi

* Zaokrąglenie w górę daje funkcja `math.ceil`.

"""

import math


def koszt_plytek(cena, bok, dlugosc, szerokosc):
    plytki_wzdluz = math.ceil(dlugosc / bok)
    plytki_wszerz = math.ceil(szerokosc / bok)
    return plytki_wzdluz * plytki_wszerz * cena


if __name__ == "__main__":
    cena = float(input())
    bok = int(input())
    dlugosc = int(input())
    szerokosc = int(input())
    print(f"{koszt_plytek(cena, bok, dlugosc, szerokosc):.2f}")
