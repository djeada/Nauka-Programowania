r"""
ZAD-02 — Usuń podnapis

**Poziom:** ★★☆
**Tagi:** `string`, `replace`, `substring`

### Treść

Otrzymujesz napis `S` i napis `T`. Usuń z `S` **wszystkie wystąpienia** podnapisu `T`.

Wystąpienia szukamy od lewej do prawej, a usuwanie wykonujemy **jednokrotnie** (jednym przejściem): fragmenty, które dopiero po usunięciu „skleją się” w nowe wystąpienie `T`, zostają. Na przykład usunięcie `ab` z `aabb` daje `ab`, a usunięcie `aa` z `aaa` daje `a`.

### Wejście

* 1. linia: napis `S`
* 2. linia: napis `T` (do usunięcia)

### Wyjście

Jedna linia: napis po usunięciu wszystkich wystąpień `T`. Jeśli nic nie zostało, wypisz pustą linię.

### Ograniczenia

* `1 ≤ |S| ≤ 1000`
* `1 ≤ |T| ≤ 100`

### Przykład

**Wejście:**

```
Lezy jezy na wiezy
zy
```

**Wyjście:**

```
Le je na wie
```

### Uwagi

* To samo przejście co w poprzednim zadaniu, tylko zamiast wstawiać nowy napis — po prostu przeskakujesz znalezione wystąpienie.

"""


def usun_wszystkie(napis, fragment):
    """Usuwa wszystkie (nienakładające się) wystąpienia fragmentu w jednym przejściu."""
    wynik = []
    i = 0

    while i < len(napis):
        if napis[i : i + len(fragment)] == fragment:
            i += len(fragment)
        else:
            wynik.append(napis[i])
            i += 1

    return "".join(wynik)


if __name__ == "__main__":
    napis = input()
    fragment = input()
    print(usun_wszystkie(napis, fragment))
