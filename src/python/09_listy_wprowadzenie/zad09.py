r"""
ZAD-09 — Usuń duplikaty (z zachowaniem kolejności)

**Poziom:** ★☆☆
**Tagi:** `listy`, `duplikaty`

### Treść

Wczytaj listę `n` liczb naturalnych i usuń z niej duplikaty tak, aby każda liczba występowała tylko raz — **zachowując kolejność pierwszych wystąpień**.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb naturalnych oddzielonych spacjami

### Wyjście

Jedna linia: lista bez duplikatów, w formacie `print(lista)`.

### Ograniczenia

* $n \ge 1$

### Przykład

**Wejście:**

```
6
3 2 1 3 2 2
```

**Wyjście:**

```
[3, 2, 1]
```

### Uwagi

* W rozdziale 10 poznasz zbiory (`set`) — też usuwają duplikaty, ale nie zachowują kolejności elementów, dlatego tutaj ich nie używaj.

"""


def usun_duplikaty(lista):
    bez_duplikatow = []
    for element in lista:
        if element not in bez_duplikatow:
            bez_duplikatow.append(element)
    return bez_duplikatow


if __name__ == "__main__":
    n = int(input())
    lista = [int(x) for x in input().split()]
    print(usun_duplikaty(lista))
