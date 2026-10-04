r"""
ZAD-05 — Pracownik z największym sumarycznym zyskiem

**Poziom:** ★☆☆
**Tagi:** `dict`, `sumowanie`

### Treść

Wczytaj `n` wpisów postaci `pracownik zysk`. Ten sam pracownik może mieć wiele wpisów. Zsumuj zyski każdego pracownika i wypisz pracownika z największą sumą.

### Wejście

* 1. linia: `n`
* następnie `n` linii: `imie_i_nazwisko zysk` — identyfikator pracownika bez spacji (np. `Jon_Snow`) i liczba całkowita (może być ujemna — strata)

### Wyjście

Jedna linia: identyfikator pracownika z największym sumarycznym zyskiem.

### Ograniczenia

* `1 ≤ n ≤ 100`

### Przykład

**Wejście:**

```
5
Barnaba_Barabash 120
Jon_Snow 100
Kira_Summer 300
Barnaba_Barabash 200
Bob_Marley 110
```

**Wyjście:**

```
Barnaba_Barabash
```

Barnaba_Barabash ma łącznie $120 + 200 = 320$, czyli więcej niż Kira_Summer (300).

### Uwagi

* Przy remisie wypisz tego pracownika, który **wcześniej pojawił się na wejściu** (jego pierwszy wpis jest wcześniej).

"""


def pracownik_z_najwiekszym_zyskiem(wpisy):
    """
    Sumuje zyski każdego pracownika i zwraca tego z największą sumą.
    Przy remisie wygrywa pracownik, który wcześniej pojawił się w danych.
    """
    zyski = {}
    for pracownik, zysk in wpisy:
        zyski[pracownik] = zyski.get(pracownik, 0) + zysk

    najlepszy = None
    for pracownik in zyski:  # kolejność pierwszego pojawienia się
        if najlepszy is None or zyski[pracownik] > zyski[najlepszy]:
            najlepszy = pracownik
    return najlepszy


if __name__ == "__main__":
    n = int(input())
    wpisy = []
    for _ in range(n):
        pracownik, zysk = input().split()
        wpisy.append((pracownik, int(zysk)))

    print(pracownik_z_najwiekszym_zyskiem(wpisy))
