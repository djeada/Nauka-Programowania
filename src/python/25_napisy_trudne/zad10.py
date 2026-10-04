r"""
ZAD-10 — Poprawność nawiasów

**Poziom:** ★★☆
**Tagi:** `string`, `stack`, `nawiasy`

### Treść

Otrzymujesz napis, który oprócz dowolnych innych znaków może zawierać nawiasy trzech rodzajów: okrągłe `()`, kwadratowe `[]` i klamrowe `{}`. Pozostałe znaki pomijamy. Nawiasy są **poprawne**, jeśli każdy nawias zamykający zamyka nawias otwierający tego samego rodzaju, który został otwarty najpóźniej i jeszcze nie jest zamknięty, a na końcu napisu żaden nawias nie zostaje otwarty. Na przykład `{[()()]}` i `a(b)[c]` są poprawne, a `([)]`, `(()` i `())` — nie.

Sprawdź napis, czytając go od lewej do prawej:

* jeśli trafisz na nawias zamykający, dla którego nie ma żadnego otwartego nawiasu albo ostatnio otwarty nawias jest innego rodzaju — **błąd jest na pozycji tego nawiasu zamykającego** (dalszej części napisu już nie sprawdzamy),
* jeśli dojdziesz do końca bez takiego błędu, ale niektóre nawiasy pozostały otwarte — **błąd jest na pozycji pierwszego (najbardziej na lewo) niezamkniętego nawiasu otwierającego**.

### Wejście

Jedna linia: napis `S`.

### Wyjście

`Tak`, jeśli nawiasy są poprawne; w przeciwnym razie pozycja (indeks liczony od `0`) pierwszego błędu.

### Ograniczenia

* `1 ≤ |S| ≤ 1000`

### Przykład

**Wejście:**

```
a(b[c]{d}e)f
```

**Wyjście:**

```
Tak
```

### Przykład 2

**Wejście:**

```
(a[b)c]
```

**Wyjście:**

```
4
```

Nawias `)` na pozycji 4 zamyka ostatnio otwarty nawias `[`, czyli nawias innego rodzaju.

### Przykład 3

**Wejście:**

```
((x)(
```

**Wyjście:**

```
0
```

Na końcu otwarte zostają nawiasy z pozycji 0 i 4 — pierwszy z nich jest na pozycji 0.

### Uwagi

* Do tego zadania służy **stos**: struktura, do której dokładamy elementy na wierzch i zdejmujemy je z wierzchu (ostatni włożony wychodzi pierwszy). W Pythonie stosem jest zwykła lista: `append` kładzie element na wierzch, `stos[-1]` podgląda wierzch, a `pop()` go zdejmuje:

  ```python
  stos = []
  stos.append(3)   # stos: [3]
  stos.append(7)   # stos: [3, 7]
  print(stos[-1])  # 7 — wierzch stosu
  stos.pop()       # zdejmuje 7, stos: [3]
  print(len(stos)) # 1
  ```

* Każdy nawias otwierający odkładaj na stos (najlepiej jego **indeks** — przyda się do zgłoszenia błędu). Przy nawiasie zamykającym sprawdź, czy stos nie jest pusty i czy na wierzchu leży nawias pasującego rodzaju; jeśli tak — zdejmij go. Pary nawiasów wygodnie trzymać w słowniku, np. `{")": "(", "]": "[", "}": "{"}`.
* Po przejściu całego napisu niezamknięte nawiasy zostają na stosie — pierwszy z nich leży na samym dole (`stos[0]`).

### Kod startowy

```python
def pierwszy_blad(napis):
    return -1


napis = input()
blad = pierwszy_blad(napis)
if blad == -1:
    print("Tak")
else:
    print(blad)
```

"""

PARY = {")": "(", "]": "[", "}": "{"}


def pierwszy_blad(napis):
    """Zwraca indeks pierwszego błędu w nawiasach albo -1, gdy nawiasy są poprawne."""
    stos = []  # indeksy nawiasów otwierających, które jeszcze nie zostały zamknięte

    for i, znak in enumerate(napis):
        if znak in "([{":
            stos.append(i)
        elif znak in PARY:
            if not stos or napis[stos[-1]] != PARY[znak]:
                return i
            stos.pop()

    if stos:
        return stos[0]  # najwcześniejszy niezamknięty nawias otwierający

    return -1


if __name__ == "__main__":
    napis = input()
    blad = pierwszy_blad(napis)
    print("Tak" if blad == -1 else blad)
