r"""
ZAD-06 — Czy średnia elementów znajduje się w liście?

**Poziom:** ★☆☆
**Tagi:** `listy`, `średnia`, `wyszukiwanie`

### Treść

Wczytaj listę `n` liczb całkowitych. Oblicz średnią arytmetyczną jej elementów i sprawdź, czy ta średnia jest **dokładnie** równa któremuś z elementów listy.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb całkowitych oddzielonych spacjami

### Wyjście

Jedno słowo: `Tak`, jeśli średnia występuje w liście, albo `Nie` w przeciwnym razie.

### Ograniczenia

* $n \ge 1$

### Przykład

**Wejście:**

```
5
6 2 1 4 27
```

**Wyjście:**

```
Nie
```

Średnia wynosi $\frac{40}{5} = 8$, a liczby $8$ nie ma w liście.

### Uwagi

* Średnia może być ułamkiem (np. $1.5$) — wtedy na pewno nie jest elementem listy liczb całkowitych. Nie zaokrąglaj jej.

"""


def czy_srednia_w_liscie(lista):
    srednia = sum(lista) / len(lista)
    return srednia in lista


if __name__ == "__main__":
    n = int(input())
    lista = [int(x) for x in input().split()]
    print("Tak" if czy_srednia_w_liscie(lista) else "Nie")
