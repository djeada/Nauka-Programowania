r"""
ZAD-03 — Czy napis A jest początkiem napisu B?

**Poziom:** ★☆☆
**Tagi:** `string`, `prefix`

### Treść

Otrzymujesz napisy `A` i `B`. Sprawdź, czy `B` **zaczyna się** od `A`, czyli czy `A` jest przedrostkiem `B`. Każdy napis jest swoim własnym przedrostkiem, a napis dłuższy od `B` nie może być jego przedrostkiem.

### Wejście

* 1. linia: napis `A`
* 2. linia: napis `B`

### Wyjście

`Prawda`, jeśli `B` zaczyna się od `A`, w przeciwnym razie `Fałsz`.

### Ograniczenia

* `1 ≤ |A|, |B| ≤ 1000`

### Przykład

**Wejście:**

```
Dino
Dinozaur jest zly
```

**Wyjście:**

```
Prawda
```

### Uwagi

* Spróbuj porównywać znaki w pętli, bez metody `startswith`. Pamiętaj, żeby najpierw sprawdzić długości — inaczej przy `A` dłuższym od `B` wyjdziesz poza zakres napisu.

"""


def czy_przedrostek(przedrostek, napis):
    """Sprawdza znak po znaku, czy napis zaczyna się od przedrostka."""
    if len(przedrostek) > len(napis):
        return False

    for i in range(len(przedrostek)):
        if przedrostek[i] != napis[i]:
            return False

    return True


if __name__ == "__main__":
    przedrostek = input()
    napis = input()
    print("Prawda" if czy_przedrostek(przedrostek, napis) else "Fałsz")
