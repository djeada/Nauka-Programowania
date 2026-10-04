r"""
ZAD-10 — Prosty kalkulator

**Poziom:** ★★☆
**Tagi:** `if-elif-else`, `arytmetyka`, `string`, `float`

### Treść

Wczytaj liczbę `a`, operator i liczbę `b`, a następnie wypisz wynik działania `a <operator> b`.
Obsługiwane operatory to: `+` (dodawanie), `-` (odejmowanie), `*` (mnożenie), `/` (dzielenie).

Przypadki szczególne:

* jeśli operator to `/`, a $b = 0$, wypisz `Nie można dzielić przez zero.`
* jeśli operator nie jest jednym z czterech powyższych, wypisz `Nieznany operator.` (niezależnie od wartości `b`).

### Wejście

* 1. linia: `a` — liczba rzeczywista
* 2. linia: operator — jeden znak
* 3. linia: `b` — liczba rzeczywista

### Wyjście

Jedna linia: wynik do **2 miejsc po przecinku** (np. `f"{wynik:.2f}"`) albo jeden z komunikatów.

### Ograniczenia

* $-10^6 \le a, b \le 10^6$

### Przykład 1

**Wejście:**

```
7
/
2
```

**Wyjście:**

```
3.50
```

### Przykład 2

**Wejście:**

```
5
/
0
```

**Wyjście:**

```
Nie można dzielić przez zero.
```

### Uwagi

* Operator wczytaj jako napis (`dzialanie = input()`) i porównuj go z napisami, np. `if dzialanie == "+":`.

"""


def oblicz(a, dzialanie, b):
    if dzialanie == "+":
        return f"{a + b:.2f}"
    elif dzialanie == "-":
        return f"{a - b:.2f}"
    elif dzialanie == "*":
        return f"{a * b:.2f}"
    elif dzialanie == "/":
        if b == 0:
            return "Nie można dzielić przez zero."
        return f"{a / b:.2f}"
    else:
        return "Nieznany operator."


if __name__ == "__main__":
    a = float(input())
    dzialanie = input()
    b = float(input())
    print(oblicz(a, dzialanie, b))
