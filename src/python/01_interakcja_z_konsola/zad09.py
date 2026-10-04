r"""
ZAD-09 — Kalkulator kredytowy

**Poziom:** ★★☆
**Tagi:** `finanse`, `float`, `formatowanie`

### Treść

Wczytaj:

* roczną stopę procentową $R$ (w procentach),
* okres spłaty $Y$ (w latach),
* kwotę kredytu $P$.

Oblicz miesięczną ratę $M$ oraz całkowity koszt kredytu $C = M \cdot n$, gdzie $n = 12 \cdot Y$ to liczba rat.

Dla $R > 0$ użyj wzoru na ratę stałą (annuitetową):

$M = P \cdot \frac{r(1+r)^n}{(1+r)^n - 1}$

gdzie $r = \frac{R}{12 \cdot 100}$ to miesięczna stopa procentowa.

Dla $R = 0$ przyjmij $M = \frac{P}{n}$.

### Wejście

3 liczby, każda w osobnej linii:

* 1. linia: `R` — liczba rzeczywista, $R \ge 0$
* 2. linia: `Y` — liczba całkowita, $Y > 0$
* 3. linia: `P` — liczba rzeczywista, $P > 0$

### Wyjście

Dwie linie, obie do **2 miejsc po przecinku**:

1. miesięczna rata `M`,
2. całkowity koszt `C`.

### Ograniczenia

* $0 \le R \le 30$
* $1 \le Y \le 40$
* $0 < P \le 10^7$

### Przykład

**Wejście:**

```
3.5
8
12000
```

**Wyjście:**

```
143.50
13775.68
```

Niezaokrąglona rata to $M \approx 143.4966$, więc $C = 96 \cdot 143.4966\ldots \approx 13775.68$.

### Uwagi

* Koszt `C` obliczaj z **niezaokrąglonej** raty `M` (nie z wartości `143.50`). Zaokrąglaj dopiero przy wypisywaniu.

"""


def rata_miesieczna(stopa_roczna, liczba_rat, kwota):
    if stopa_roczna == 0:
        return kwota / liczba_rat
    r = stopa_roczna / (12 * 100)
    czynnik = (1 + r) ** liczba_rat
    return kwota * r * czynnik / (czynnik - 1)


if __name__ == "__main__":
    stopa_roczna = float(input())
    lata = int(input())
    kwota = float(input())

    liczba_rat = 12 * lata
    rata = rata_miesieczna(stopa_roczna, liczba_rat, kwota)
    koszt = rata * liczba_rat

    print(f"{rata:.2f}")
    print(f"{koszt:.2f}")
