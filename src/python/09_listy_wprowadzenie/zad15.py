r"""
ZAD-15 — Element dominujący

**Poziom:** ★★☆
**Tagi:** `listy`, `zliczanie`, `pętle`

### Treść

Wczytaj listę `n` liczb naturalnych. Jeśli istnieje wartość, która występuje w liście **więcej niż** $\frac{n}{2}$ razy, wypisz ją. W przeciwnym razie wypisz `-1`.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb naturalnych oddzielonych spacjami

### Wyjście

Jedna liczba: element dominujący albo `-1`.

### Ograniczenia

* $n \ge 1$
* Elementy listy są nieujemne.

### Przykład

**Wejście:**

```
5
4 7 4 4 2
```

**Wyjście:**

```
4
```

Wartość $4$ występuje $3$ razy, a $3 > \frac{5}{2}$.

### Uwagi

* Wartość występująca dokładnie $\frac{n}{2}$ razy nie jest elementem dominującym.
* Wystarczy dla każdego elementu policzyć (pętlą albo metodą `lista.count(x)`), ile razy występuje w liście. Szybszy sposób, ze słownikiem, poznasz w rozdziale 17.

"""


def element_dominujacy(lista):
    for element in lista:
        if lista.count(element) > len(lista) / 2:
            return element
    return -1


if __name__ == "__main__":
    n = int(input())
    lista = [int(x) for x in input().split()]
    print(element_dominujacy(lista))
