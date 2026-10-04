r"""
ZAD-09 — Usuń z pierwszej listy część wspólną obu list

**Poziom:** ★★☆
**Tagi:** `listy`, `filtrowanie`

### Treść

Wczytaj dwie listy liczb całkowitych. Usuń z listy 1 **wszystkie** elementy (także powtórzenia), które występują w liście 2.

* Zachowaj kolejność pozostałych elementów listy 1.
* Jeśli usunięte zostaną wszystkie elementy, wypisz `[]`.

### Wejście

* 1. linia: lista 1 — liczby całkowite oddzielone spacjami
* 2. linia: lista 2 — liczby całkowite oddzielone spacjami

### Wyjście

Jedna linia: lista 1 po usunięciu elementów występujących w liście 2.

### Przykład

**Wejście:**

```
9 2 5 4
4 2 1
```

**Wyjście:**

```
[9, 5]
```

### Uwagi

* Uważaj na usuwanie elementów z listy podczas przechodzenia po niej pętlą `for` — łatwo wtedy pominąć element. Bezpieczniej zbudować nową listę z elementów, które zostają.

"""


def usun_czesc_wspolna(lista_a, lista_b):
    wynik = []
    for element in lista_a:
        if element not in lista_b:
            wynik.append(element)
    return wynik


if __name__ == "__main__":
    lista_a = [int(x) for x in input().split()]
    lista_b = [int(x) for x in input().split()]

    print(usun_czesc_wspolna(lista_a, lista_b))
