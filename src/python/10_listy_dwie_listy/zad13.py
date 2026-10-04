r"""
ZAD-13 — Poprawność numeru PESEL

**Poziom:** ★★☆
**Tagi:** `zip`, `cyfra kontrolna`, `napisy`

### Treść

Numer PESEL składa się z 11 cyfr $c_1 c_2 \ldots c_{11}$. Ostatnia cyfra $c_{11}$ jest **cyfrą kontrolną**: mnożymy pierwsze 10 cyfr przez wagi `1 3 7 9 1 3 7 9 1 3`, sumujemy iloczyny, a cyfra kontrolna to

$c_{11} = (10 - S \bmod 10) \bmod 10$, gdzie $S = 1 \cdot c_1 + 3 \cdot c_2 + 7 \cdot c_3 + 9 \cdot c_4 + 1 \cdot c_5 + 3 \cdot c_6 + 7 \cdot c_7 + 9 \cdot c_8 + 1 \cdot c_9 + 3 \cdot c_{10}$.

Dziesiąta cyfra $c_{10}$ oznacza płeć: parzysta — kobieta, nieparzysta — mężczyzna.

Wczytaj napis i sprawdź, czy jest poprawnym numerem PESEL, czyli czy:

* ma dokładnie 11 znaków,
* każdy znak jest cyfrą,
* cyfra kontrolna zgadza się z wyliczoną ze wzoru.

Dla poprawnego numeru wypisz dodatkowo płeć. **Nie sprawdzaj** poprawności daty urodzenia zapisanej w numerze (cyfry 1–6).

### Wejście

* 1. linia: napis bez spacji (może zawierać znaki niebędące cyframi i mieć dowolną długość)

### Wyjście

* Dla poprawnego numeru dwie linie: `Poprawny`, a w drugiej `kobieta` lub `mężczyzna`.
* W przeciwnym razie jedna linia: `Niepoprawny`.

### Przykład 1

**Wejście:**

```
44051401359
```

**Wyjście:**

```
Poprawny
mężczyzna
```

$S = 1 \cdot 4 + 3 \cdot 4 + 7 \cdot 0 + 9 \cdot 5 + 1 \cdot 1 + 3 \cdot 4 + 7 \cdot 0 + 9 \cdot 1 + 1 \cdot 3 + 3 \cdot 5 = 101$, więc cyfra kontrolna to $(10 - 1) \bmod 10 = 9$ — zgadza się. Dziesiąta cyfra `5` jest nieparzysta.

### Przykład 2

**Wejście:**

```
44051401358
```

**Wyjście:**

```
Niepoprawny
```

### Uwagi

* To, czy znak jest cyfrą, sprawdzisz warunkiem `znak in "0123456789"`, a cyfrę zamienisz na liczbę przez `int(znak)`.
* Wagi zapisz w liście `[1, 3, 7, 9, 1, 3, 7, 9, 1, 3]` i przejdź po parach (cyfra, waga) za pomocą `zip(numer, wagi)` — `zip` kończy na krótszym ciągu, więc weźmie tylko 10 pierwszych cyfr.

"""

WAGI = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]


def czy_poprawny_pesel(numer):
    if len(numer) != 11:
        return False
    for znak in numer:
        if znak not in "0123456789":
            return False

    suma = 0
    for cyfra, waga in zip(numer, WAGI):
        suma += int(cyfra) * waga
    cyfra_kontrolna = (10 - suma % 10) % 10
    return cyfra_kontrolna == int(numer[10])


def plec(numer):
    if int(numer[9]) % 2 == 0:
        return "kobieta"
    return "mężczyzna"


if __name__ == "__main__":
    numer = input()

    if czy_poprawny_pesel(numer):
        print("Poprawny")
        print(plec(numer))
    else:
        print("Niepoprawny")
