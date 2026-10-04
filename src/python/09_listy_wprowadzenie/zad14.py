r"""
ZAD-14 — Element bez pary

**Poziom:** ★★☆
**Tagi:** `listy`, `zliczanie`

### Treść

Wczytaj listę `n` liczb całkowitych. Każda wartość w liście poza jedną występuje **parzystą** liczbę razy (wszystkie jej wystąpienia da się połączyć w pary), a jedna wartość występuje **nieparzystą** liczbę razy. Znajdź i wypisz tę wartość.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb całkowitych oddzielonych spacjami

### Wyjście

Jedna liczba całkowita: wartość bez pary.

### Ograniczenia

* $n \ge 1$, `n` jest nieparzyste

### Przykład

**Wejście:**

```
7
1 3 1 7 3 1 1
```

**Wyjście:**

```
7
```

Wartość $1$ występuje 4 razy, $3$ — 2 razy, a $7$ — tylko raz.

### Uwagi

* Ciekawostka na później: w rozdziale 16 (operacje bitowe) zobaczysz, że to zadanie da się rozwiązać jednym przejściem po liście operatorem XOR (`^`), bo $x \oplus x = 0$ i $x \oplus 0 = x$.

"""


def element_bez_pary(lista):
    for element in lista:
        if lista.count(element) % 2 == 1:
            return element


if __name__ == "__main__":
    n = int(input())
    lista = [int(x) for x in input().split()]
    print(element_bez_pary(lista))
