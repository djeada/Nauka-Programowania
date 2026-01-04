"""
ZAD-01 — Podmiana słowa w zdaniu

**Poziom:** ★★☆
**Tagi:** `string`, `replace`, `substring`

### Treść

Masz trzy napisy:

1. Zdanie (tekst do modyfikacji),
2. Słowo A (podnapis do znalezienia),
3. Słowo B (podnapis zastępujący).

Zamień **wszystkie wystąpienia** słowa/podnapisu **A** na **B** w podanym zdaniu.

> Uwaga: A może być częścią innych słów — zamiana dotyczy **każdego wystąpienia podnapisu**.

### Wejście

* 1 linia: zdanie `S`
* 2 linia: napis `A`
* 3 linia: napis `B`

### Wyjście

* 1 linia: zdanie po zamianie

### Przykład

**Wejście:**

```
Lezy jezy na wiezy
zy
rzy
```

**Wyjście:**

```
Lerzy jerzy na wierzy
```

"""


def zamien_wszystkoV1(zdanie, napis_a, napis_b):
    return zdanie.replace(napis_a, napis_b)


# Testy Poprawnosci
def test_1():
    zdanie = "Lezy jezy na wiezy"
    napis_a = "zy"
    napis_b = "rzy"
    wynik = "Lerzy jerzy na wierzy"

    assert zamien_wszystkoV1(zdanie, napis_a, napis_b) == wynik


def main():
    test_1()


if __name__ == "__main__":
    main()
