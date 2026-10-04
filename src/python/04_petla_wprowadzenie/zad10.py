r"""
ZAD-10 — Walidacja danych wejściowych

**Poziom:** ★★☆
**Tagi:** `while`, `break`, `continue`, `try/except`

### Treść

Program prosi o liczbę całkowitą z przedziału $[1, 100]$ i nie poddaje się, dopóki jej nie dostanie.

Wczytuj kolejne linie. Dla każdej linii:

* jeśli nie jest liczbą całkowitą — wypisz `To nie jest liczba całkowita.` i wczytaj następną linię,
* jeśli jest liczbą całkowitą spoza przedziału $[1, 100]$ — wypisz `Liczba spoza zakresu.` i wczytaj następną linię,
* jeśli jest liczbą całkowitą z przedziału $[1, 100]$ — zakończ wczytywanie i wypisz `Przyjęto: X`, gdzie `X` to ta liczba.

Linia jest liczbą całkowitą, jeśli funkcja `int()` potrafi ją zamienić na liczbę (np. `42`, `-7`). Napisy takie jak `abc`, `3.5` czy pusta linia nie są liczbami całkowitymi.

### Wejście

Kolejne linie tekstu.

### Wyjście

Jeden komunikat o błędzie dla każdej niepoprawnej linii (w kolejności wczytywania), a na końcu linia `Przyjęto: X`.

### Ograniczenia

* Wśród danych na pewno jest co najmniej jedna poprawna liczba.
* Po pierwszej poprawnej liczbie mogą występować kolejne linie — program ma je pominąć.

### Przykład

**Wejście:**

```
abc
150
3.5
42
```

**Wyjście:**

```
To nie jest liczba całkowita.
Liczba spoza zakresu.
To nie jest liczba całkowita.
Przyjęto: 42
```

### Uwagi

* Wywołanie `int("abc")` kończy się błędem `ValueError`. Taki błąd można „złapać” konstrukcją `try`/`except`: Python wykonuje instrukcje z bloku `try`, a jeśli w którejś z nich wystąpi `ValueError`, zamiast przerywać program przechodzi do bloku `except ValueError:`.

  ```python
  try:
      liczba = int("abc")
      print("To się nie wykona.")
  except ValueError:
      print("Nie udało się zamienić napisu na liczbę.")
  ```

* `continue` przerywa bieżący obrót pętli i od razu przechodzi do następnego, a `break` kończy całą pętlę.
* Pętla `while True:` kręci się „w nieskończoność” — kończy ją dopiero `break`.
* Granice przedziału należą do niego: `1` i `100` są poprawne.

### Kod startowy

```python
while True:
    linia = input()
    try:
        liczba = int(linia)
    except ValueError:
        pass


print(f"Przyjęto: {liczba}")
```

"""

DOLNA_GRANICA = 1
GORNA_GRANICA = 100


def wczytaj_liczbe_z_zakresu():
    while True:
        linia = input()
        try:
            liczba = int(linia)
        except ValueError:
            print("To nie jest liczba całkowita.")
            continue

        if liczba < DOLNA_GRANICA or liczba > GORNA_GRANICA:
            print("Liczba spoza zakresu.")
            continue

        break

    return liczba


if __name__ == "__main__":
    liczba = wczytaj_liczbe_z_zakresu()
    print(f"Przyjęto: {liczba}")
