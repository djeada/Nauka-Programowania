r"""
ZAD-09 — Dni między datami (moduł datetime)

**Poziom:** ★★☆
**Tagi:** `datetime`, `daty`, `biblioteka standardowa`

### Treść

Wczytaj dwie daty i za pomocą modułu `datetime` z biblioteki standardowej Pythona oblicz:

1. liczbę dni między tymi datami — jako wartość bezwzględną różnicy, więc kolejność dat nie ma znaczenia,
2. nazwę dnia tygodnia **pierwszej** daty.

### Wejście

6 liczb całkowitych, każda w osobnej linii:

1. `d1` — dzień pierwszej daty
2. `m1` — miesiąc pierwszej daty
3. `y1` — rok pierwszej daty
4. `d2` — dzień drugiej daty
5. `m2` — miesiąc drugiej daty
6. `y2` — rok drugiej daty

### Wyjście

Dwie linie:

1. liczba dni między datami (liczba całkowita, $\ge 0$),
2. nazwa dnia tygodnia pierwszej daty — dokładnie jedna z: `Poniedziałek`, `Wtorek`, `Środa`, `Czwartek`, `Piątek`, `Sobota`, `Niedziela`.

### Ograniczenia

* Obie daty są poprawne (nie musisz ich sprawdzać).
* $1 \le y1, y2 \le 9999$

### Przykład

**Wejście:**

```
9
10
2020
1
1
2021
```

**Wyjście:**

```
84
Piątek
```

Od 9 października 2020 do 1 stycznia 2021 mijają 84 dni: 22 do końca października, 30 w listopadzie, 31 w grudniu i 1 w styczniu.

### Uwagi

* Moduł `datetime` udostępnia typ `date`, który reprezentuje jedną datę. Tworząc ją, podaj kolejno **rok, miesiąc, dzień**:

  ```python
  from datetime import date

  pierwsza = date(2020, 10, 9)
  druga = date(2021, 1, 1)
  print((druga - pierwsza).days)   # 84
  print((pierwsza - druga).days)   # -84
  print(pierwsza.weekday())        # 4
  ```

* Różnica dwóch dat to odcinek czasu (`timedelta`); liczbę dni odczytasz z jego pola `.days`. Może być ujemna, więc użyj `abs(...)`.
* Metoda `weekday()` zwraca 0 dla poniedziałku, 1 dla wtorku, …, 6 dla niedzieli — to inna numeracja niż `h` w kongruencji Zellera z ZAD-08 (tam 0 oznacza sobotę).
* Moduł sam uwzględnia lata przestępne. Porównaj go z ZAD-07 i ZAD-08: `(data - date(rok, 1, 1)).days + 1` to numer dnia w roku, a `weekday()` zastępuje wzór Zellera — dobry sposób na sprawdzenie swoich wcześniejszych rozwiązań.

### Kod startowy

```python
from datetime import date

d1 = int(input())
m1 = int(input())
y1 = int(input())
d2 = int(input())
m2 = int(input())
y2 = int(input())

```

"""

from datetime import date


def nazwa_dnia(numer):
    if numer == 0:
        return "Poniedziałek"
    elif numer == 1:
        return "Wtorek"
    elif numer == 2:
        return "Środa"
    elif numer == 3:
        return "Czwartek"
    elif numer == 4:
        return "Piątek"
    elif numer == 5:
        return "Sobota"
    else:
        return "Niedziela"


if __name__ == "__main__":
    d1 = int(input())
    m1 = int(input())
    y1 = int(input())
    d2 = int(input())
    m2 = int(input())
    y2 = int(input())

    pierwsza = date(y1, m1, d1)
    druga = date(y2, m2, d2)

    print(abs((druga - pierwsza).days))
    print(nazwa_dnia(pierwsza.weekday()))
