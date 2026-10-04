r"""
ZAD-05 — Kodowanie długości serii (RLE)

**Poziom:** ★★☆
**Tagi:** `string`, `compress`, `run-length`

### Treść

**Kodowanie długości serii** (ang. *run-length encoding*, RLE) to prosta metoda kompresji. Każdą **serię** jednakowych znaków stojących bezpośrednio obok siebie zapisujemy jako ten znak, a zaraz po nim liczbę jego powtórzeń (w zapisie dziesiętnym, więc może mieć kilka cyfr). Na przykład `aaabcc` koduje się jako `a3b1c2`, a dwanaście liter `x` pod rząd — jako `x12`.

Zakoduj podany napis metodą RLE. Ten sam znak może tworzyć kilka oddzielnych serii — każdą kodujemy osobno.

### Wejście

Jedna linia: napis `S` złożony wyłącznie z liter alfabetu angielskiego (wielkość liter ma znaczenie).

### Wyjście

Jedna linia: zakodowany napis.

### Ograniczenia

* `1 ≤ |S| ≤ 1000`

### Przykład

**Wejście:**

```
AAAAAAAAAABBBBBBBBA
```

**Wyjście:**

```
A10B8A1
```

Napis składa się z trzech serii: dziesięciu liter `A`, ośmiu liter `B` i jednej litery `A`.

### Uwagi

* Przechodź po napisie i licz, ile razy z rzędu powtarza się bieżący znak. Gdy seria się kończy (następny znak jest inny albo napis się skończył), dopisz do wyniku znak i licznik zamieniony na napis (`str(licznik)`).

"""


def koduj_rle(napis):
    """Koduje napis metodą RLE: każdą serię zapisuje jako znak i długość serii."""
    wynik = []
    i = 0

    while i < len(napis):
        znak = napis[i]
        dlugosc = 0
        while i < len(napis) and napis[i] == znak:
            dlugosc += 1
            i += 1
        wynik.append(znak + str(dlugosc))

    return "".join(wynik)


if __name__ == "__main__":
    napis = input()
    print(koduj_rle(napis))
