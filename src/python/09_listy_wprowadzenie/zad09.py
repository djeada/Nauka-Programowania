"""
ZAD-09 — Usuń duplikaty (z zachowaniem kolejności)

**Poziom:** ★☆☆
**Tagi:** `listy`, `duplikaty`, `set`

### Treść

Wczytaj listę liczb naturalnych i usuń duplikaty tak, aby każda liczba występowała tylko raz — **zachowując kolejność pierwszego wystąpienia**.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby naturalne

### Wyjście

Jedna linia: lista bez duplikatów, elementy oddzielone przecinkami.

### Przykład

**Wejście:**

```
6
3
2
1
3
2
2
```

**Wyjście:**

```
3,2,1
```

"""


def usun_duplikaty_v1(lista):
    lista_nowa = []
    for i in lista:
        if i not in lista_nowa:
            lista_nowa.append(i)
    return lista_nowa


def usun_duplikaty_v2(lista):
    return list(set(lista))


def test_usun_duplikaty_v1():
    assert usun_duplikaty_v1([]) == []
    assert usun_duplikaty_v1([1, 1, 1, 1, 1]) == [1]
    assert usun_duplikaty_v1([3, 5, 3, 3, 2]) == [3, 5, 2]


if __name__ == "__main__":

    test_usun_duplikaty_v1()
