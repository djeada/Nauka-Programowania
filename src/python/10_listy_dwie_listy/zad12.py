r"""
ZAD-12 — Sprawdzanie testu (zip, enumerate)

**Poziom:** ★☆☆
**Tagi:** `zip`, `enumerate`, `napisy`

### Treść

Uczeń rozwiązał test wyboru. Wczytaj klucz poprawnych odpowiedzi oraz odpowiedzi ucznia — oba jako napisy, w których znak na pozycji `i` to odpowiedź na pytanie `i + 1` (np. `ABCDA` oznacza: pytanie 1 — `A`, pytanie 2 — `B` itd.).

Dla każdego pytania wypisz, czy uczeń odpowiedział poprawnie, a na końcu podsumuj wynik.

### Wejście

* 1. linia: klucz odpowiedzi — napis z wielkich liter `A`–`E`, bez spacji
* 2. linia: odpowiedzi ucznia — napis tej samej długości co klucz, z wielkich liter `A`–`E`

### Wyjście

* Dla każdego pytania (numerowanych od 1) jedna linia:
  * `nr: OK` — gdy odpowiedź jest poprawna,
  * `nr: źle (poprawna: X)` — gdy jest błędna, gdzie `X` to poprawna odpowiedź z klucza.
* Ostatnia linia: `Wynik: p/n (q%)`, gdzie `p` to liczba poprawnych odpowiedzi, `n` — liczba pytań, a `q` — procent poprawnych odpowiedzi z **jedną cyfrą po przecinku** (np. `80.0`, `66.7`).

### Przykład

**Wejście:**

```
ABCDA
ACCDA
```

**Wyjście:**

```
1: OK
2: źle (poprawna: B)
3: OK
4: OK
5: OK
Wynik: 4/5 (80.0%)
```

### Uwagi

* `zip(a, b)` łączy dwa ciągi w pary kolejnych elementów: `zip("AB", "AC")` daje pary `("A", "A")` i `("B", "C")`.
* `enumerate(ciag, start=1)` dodaje do każdego elementu jego numer, licząc od 1: `enumerate("XY", start=1)` daje pary `(1, "X")` i `(2, "Y")`.
* Razem:

  ```python
  for nr, (poprawna, udzielona) in enumerate(zip(klucz, odpowiedzi), start=1):
      ...
  ```

* Procent sformatujesz tak: `f"{procent:.1f}"`.

"""


def sprawdz_test(klucz, odpowiedzi):
    poprawne = 0
    for nr, (poprawna, udzielona) in enumerate(zip(klucz, odpowiedzi), start=1):
        if poprawna == udzielona:
            print(f"{nr}: OK")
            poprawne += 1
        else:
            print(f"{nr}: źle (poprawna: {poprawna})")
    return poprawne


if __name__ == "__main__":
    klucz = input()
    odpowiedzi = input()

    poprawne = sprawdz_test(klucz, odpowiedzi)
    liczba_pytan = len(klucz)
    procent = poprawne / liczba_pytan * 100
    print(f"Wynik: {poprawne}/{liczba_pytan} ({procent:.1f}%)")
