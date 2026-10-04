r"""
ZAD-08 — Dzień tygodnia dla daty (Zeller)

**Poziom:** ★★☆
**Tagi:** `algorytmy`, `Zeller`, `mapowanie`, `daty`

### Treść

Wczytaj datę `d`, `m`, `y` i wyznacz nazwę dnia tygodnia, używając **kongruencji Zellera** dla kalendarza gregoriańskiego.

Kroki:

1. Jeśli $m \le 2$, potraktuj styczeń i luty jako 13. i 14. miesiąc poprzedniego roku: $m = m + 12$, $y = y - 1$.
2. Oblicz:
   * $K = y \bmod 100$ (rok w stuleciu),
   * $J = \lfloor y / 100 \rfloor$ (stulecie),
   * $h = \left(d + \left\lfloor \frac{13(m+1)}{5} \right\rfloor + K + \left\lfloor \frac{K}{4} \right\rfloor + \left\lfloor \frac{J}{4} \right\rfloor + 5J\right) \bmod 7$.
3. Zamień `h` na dzień tygodnia:
   * 0 → `Sobota`
   * 1 → `Niedziela`
   * 2 → `Poniedziałek`
   * 3 → `Wtorek`
   * 4 → `Środa`
   * 5 → `Czwartek`
   * 6 → `Piątek`

### Wejście

3 liczby całkowite, każda w osobnej linii: `d`, `m`, `y`.

### Wyjście

Jedna linia: nazwa dnia tygodnia — dokładnie jedna z: `Poniedziałek`, `Wtorek`, `Środa`, `Czwartek`, `Piątek`, `Sobota`, `Niedziela`.

### Ograniczenia

* Podana data jest poprawna (nie musisz jej sprawdzać).
* $1 \le y \le 9999$

### Przykład

**Wejście:**

```
9
10
2020
```

**Wyjście:**

```
Piątek
```

$m = 10$, $y = 2020$, więc $K = 20$, $J = 20$, $h = (9 + 28 + 20 + 5 + 5 + 100) \bmod 7 = 167 \bmod 7 = 6$, czyli piątek.

### Uwagi

* W Pythonie $\lfloor a / b \rfloor$ to `a // b`, a $a \bmod b$ to `a % b`.

"""


def nazwa_dnia_zeller(h):
    if h == 0:
        return "Sobota"
    elif h == 1:
        return "Niedziela"
    elif h == 2:
        return "Poniedziałek"
    elif h == 3:
        return "Wtorek"
    elif h == 4:
        return "Środa"
    elif h == 5:
        return "Czwartek"
    else:
        return "Piątek"


def dzien_tygodnia(dzien, miesiac, rok):
    if miesiac <= 2:
        miesiac += 12
        rok -= 1

    k = rok % 100
    j = rok // 100
    h = (dzien + 13 * (miesiac + 1) // 5 + k + k // 4 + j // 4 + 5 * j) % 7
    return nazwa_dnia_zeller(h)


if __name__ == "__main__":
    dzien = int(input())
    miesiac = int(input())
    rok = int(input())
    print(dzien_tygodnia(dzien, miesiac, rok))
