r"""
ZAD-20 — Wyrażenia listowe

**Poziom:** ★☆☆
**Tagi:** `listy`, `wyrażenia listowe`, `list comprehension`

### Treść

Wczytaj listę `n` liczb całkowitych i utwórz z niej trzy nowe listy — każdą **jednym wyrażeniem listowym**:

1. `kwadraty` — kwadraty wszystkich elementów (w tej samej kolejności),
2. `ujemne` — tylko elementy ujemne (w kolejności występowania),
3. `etykiety` — dla każdego elementu napis `"P"`, jeśli jest parzysty, albo `"N"`, jeśli jest nieparzysty.

Wypisz te trzy listy.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb całkowitych oddzielonych spacjami

### Wyjście

Trzy linie — listy `kwadraty`, `ujemne` i `etykiety` w formacie `print(lista)`. Lista napisów wypisuje się z apostrofami, np. `['N', 'P']`. Jeśli nie ma elementów ujemnych, druga linia to `[]`.

### Ograniczenia

* $n \ge 1$

### Przykład

**Wejście:**

```
5
3 -2 0 -7 4
```

**Wyjście:**

```
[9, 4, 0, 49, 16]
[-2, -7]
['N', 'P', 'P', 'N', 'P']
```

### Uwagi

* Wyrażenie listowe buduje listę w jednej linii: `[wyrażenie for x in lista]`, np. `[x + 1 for x in [1, 2, 3]]` daje `[2, 3, 4]`. Takiego wyrażenia używa już linia wczytująca listę: `[int(x) for x in input().split()]`.
* **Filtrowanie** — warunek na końcu zostawia tylko pasujące elementy: `[x for x in lista if x > 2]`; dla `[1, 2, 3, 4]` daje `[3, 4]`.
* **Wybór wartości** — wyrażenie `a if warunek else b` na początku wybiera wartość dla każdego elementu: `["duża" if x > 2 else "mała" for x in lista]`; dla `[1, 3]` daje `['mała', 'duża']`.
* Zwróć uwagę na różnicę: `if` na końcu (bez `else`) **usuwa** elementy, a `if … else …` na początku **zamienia** każdy element — lista wynikowa ma wtedy tyle samo elementów co wejściowa.
* `0` jest liczbą parzystą.

### Kod startowy

```python
n = int(input())
lista = [int(x) for x in input().split()]

kwadraty = [...]  # Uzupełnij: kwadraty wszystkich elementów.
ujemne = [...]  # Uzupełnij: tylko elementy ujemne.
etykiety = [...]  # Uzupełnij: "P" dla parzystych, "N" dla nieparzystych.

print(kwadraty)
print(ujemne)
print(etykiety)
```

"""


def zbuduj_listy(lista):
    """Zwraca listy: kwadratów, elementów ujemnych i etykiet "P"/"N"."""
    kwadraty = [x**2 for x in lista]
    ujemne = [x for x in lista if x < 0]
    etykiety = ["P" if x % 2 == 0 else "N" for x in lista]
    return kwadraty, ujemne, etykiety


if __name__ == "__main__":
    n = int(input())
    lista = [int(x) for x in input().split()]
    kwadraty, ujemne, etykiety = zbuduj_listy(lista)
    print(kwadraty)
    print(ujemne)
    print(etykiety)
