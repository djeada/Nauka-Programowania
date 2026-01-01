"""
ZAD-16 — Odległość Hamminga

**Poziom:** ★★☆
**Tagi:** `string`, `porównanie`

### Treść

Wczytaj dwa napisy tej samej długości i policz, na ilu pozycjach różnią się znakami.

### Wejście

* 1. linia: napis `s1`
* 2. linia: napis `s2`  (ta sama długość)

### Wyjście

* 1. linia: odległość Hamminga

### Przykład

**Wejście:**

```
adam
axam
```

**Wyjście:**

```
1
```

"""


def odleglosc_hamminga(napis_a, napis_b):
    if len(napis_a) != len(napis_b):
        return -1

    licznik = 0
    for i in range(len(napis_a)):
        if napis_a[i] != napis_b[i]:
            licznik += 1
    return licznik


def test_odleglosc_hamminga():

    assert odleglosc_hamminga("abc", "abc") == 0
    assert odleglosc_hamminga("abc", "abd") == 1
    assert odleglosc_hamminga("abc", "abcd") == -1
    assert odleglosc_hamminga("xxx", "abc") == 3


if __name__ == "__main__":

    test_odleglosc_hamminga()
