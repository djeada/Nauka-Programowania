r"""
ZAD-11 — Sortowanie „słownika” po kluczach i po wartościach

**Poziom:** ★☆☆
**Tagi:** `sort`, `dict`

### Treść

Wczytaj `n` par `klucz wartość` do słownika.

a) Wypisz pary posortowane rosnąco według kluczy.

b) Wypisz pary posortowane rosnąco według wartości; pary o równych wartościach uporządkuj rosnąco według kluczy.

### Wejście

* 1. linia: `n`
* następnie `n` linii: `klucz wartość` — klucz to słowo z małych liter (klucze są różne), wartość to liczba całkowita

### Wyjście

* 1. linia: pary dla a)
* 2. linia: pary dla b)

Każdą parę wypisz jako `klucz:wartość` (bez spacji wokół dwukropka), a pary oddziel pojedynczą spacją.

### Ograniczenia

* `1 ≤ n ≤ 50`

### Przykład

**Wejście:**

```
4
c 3
x 5
a -2
b 4
```

**Wyjście:**

```
a:-2 b:4 c:3 x:5
a:-2 c:3 b:4 x:5
```

### Uwagi

* Klucze porównujemy jak napisy (alfabetycznie), np. `ab` jest przed `b`.
* `sorted(slownik.items())` sortuje pary według kluczy — pary (krotki) porównywane są najpierw po pierwszym elemencie.
* Aby sortować według czegoś innego, przekaż w parametrze `key` **nazwę funkcji** (bez nawiasów). `sorted` wywoła tę funkcję dla każdego elementu i ułoży elementy rosnąco według zwróconych wartości:

  ```python
  def dlugosc_napisu(napis):
      return len(napis)

  print(sorted(["kot", "żyrafa", "pies"], key=dlugosc_napisu))  # ['kot', 'pies', 'żyrafa']
  ```

* Funkcja klucza może zwracać krotkę. Krotki porównywane są element po elemencie, więc dla pary `(klucz, wartość)` zwrócenie `(wartość, klucz)` sortuje po wartości, a przy równych wartościach — po kluczu.

### Kod startowy

```python
def wartosc_potem_klucz(para):
    pass


def wypisz_pary(pary):
    print(" ".join(f"{klucz}:{wartosc}" for klucz, wartosc in pary))


n = int(input())
slownik = {}
for _ in range(n):
    klucz, wartosc = input().split()
    slownik[klucz] = int(wartosc)

po_kluczach = []  # TODO: posortuj pary według kluczy
po_wartosciach = []  # TODO: posortuj pary, używając key=wartosc_potem_klucz

wypisz_pary(po_kluczach)
wypisz_pary(po_wartosciach)
```

"""


def wartosc_potem_klucz(para):
    """Klucz sortowania: najpierw wartość, przy remisie klucz."""
    klucz, wartosc = para
    return (wartosc, klucz)


def sortuj_po_kluczach(slownik):
    """Zwraca listę par (klucz, wartość) posortowaną rosnąco po kluczach."""
    return sorted(slownik.items())


def sortuj_po_wartosciach(slownik):
    """Zwraca listę par posortowaną rosnąco po wartościach (przy remisie — po kluczach)."""
    return sorted(slownik.items(), key=wartosc_potem_klucz)


def wypisz_pary(pary):
    print(" ".join(f"{klucz}:{wartosc}" for klucz, wartosc in pary))


if __name__ == "__main__":
    n = int(input())
    slownik = {}
    for _ in range(n):
        klucz, wartosc = input().split()
        slownik[klucz] = int(wartosc)

    wypisz_pary(sortuj_po_kluczach(slownik))
    wypisz_pary(sortuj_po_wartosciach(slownik))
