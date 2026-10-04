r"""
ZAD-08 — Połącz posortowane listy w posortowaną listę bez duplikatów

**Poziom:** ★★☆
**Tagi:** `listy`, `scalanie`, `sortowanie`

### Treść

Wczytaj dwie listy liczb całkowitych, każdą **posortowaną niemalejąco**, i scal je w jedną listę, która:

* jest posortowana rosnąco,
* zawiera każdą wartość **tylko raz** (bez duplikatów — także tych, które powtarzają się w obrębie jednej listy).

Wykorzystaj to, że listy wejściowe są już posortowane: przechodź jednocześnie po obu listach i za każdym razem dobieraj mniejszy z dwóch bieżących elementów.

### Wejście

* 1. linia: lista 1 (posortowana niemalejąco) — liczby całkowite oddzielone spacjami
* 2. linia: lista 2 (posortowana niemalejąco) — liczby całkowite oddzielone spacjami

### Wyjście

Jedna linia: scalona, posortowana lista bez duplikatów.

### Przykład

**Wejście:**

```
2 4 7
3 5 9
```

**Wyjście:**

```
[2, 3, 4, 5, 7, 9]
```

"""


def dodaj_bez_powtorzen(lista, element):
    if not lista or lista[-1] != element:
        lista.append(element)


def scal_bez_duplikatow(lista_a, lista_b):
    wynik = []
    i = 0
    j = 0
    while i < len(lista_a) and j < len(lista_b):
        if lista_a[i] <= lista_b[j]:
            dodaj_bez_powtorzen(wynik, lista_a[i])
            i += 1
        else:
            dodaj_bez_powtorzen(wynik, lista_b[j])
            j += 1
    for element in lista_a[i:] + lista_b[j:]:
        dodaj_bez_powtorzen(wynik, element)
    return wynik


if __name__ == "__main__":
    lista_a = [int(x) for x in input().split()]
    lista_b = [int(x) for x in input().split()]

    print(scal_bez_duplikatow(lista_a, lista_b))
