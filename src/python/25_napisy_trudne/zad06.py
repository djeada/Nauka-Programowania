r"""
ZAD-06 — Rotacje napisów

**Poziom:** ★★☆
**Tagi:** `string`, `rotation`, `substring`

### Treść

Otrzymujesz dwa napisy `A` i `B`. Sprawdź, czy `B` jest **rotacją** (przesunięciem cyklicznym) napisu `A`, czyli czy da się go otrzymać, przenosząc pewną liczbę początkowych znaków `A` (być może zero) na koniec. Na przykład rotacjami napisu `abcd` są `abcd`, `bcda`, `cdab` i `dabc`.

Napisy różnej długości nigdy nie są swoimi rotacjami, a każdy napis jest rotacją samego siebie.

### Wejście

* 1. linia: napis `A`
* 2. linia: napis `B`

### Wyjście

`Prawda`, jeśli `B` jest rotacją `A`, w przeciwnym razie `Fałsz`.

### Ograniczenia

* `1 ≤ |A|, |B| ≤ 1000`

### Przykład

**Wejście:**

```
malpka
pkamal
```

**Wyjście:**

```
Prawda
```

`pkamal` powstaje z `malpka` przez przeniesienie początkowych `mal` na koniec.

### Uwagi

* Każda rotacja `A` jest podnapisem napisu `A + A`. Wystarczy więc porównać długości i sprawdzić, czy `B` występuje w `A + A`.

"""


def czy_rotacja(napis_a, napis_b):
    """Sprawdza, czy napis_b jest przesunięciem cyklicznym napisu_a."""
    if len(napis_a) != len(napis_b):
        return False

    # Każda rotacja napisu A jest fragmentem napisu A + A.
    return napis_b in napis_a + napis_a


if __name__ == "__main__":
    napis_a = input()
    napis_b = input()
    print("Prawda" if czy_rotacja(napis_a, napis_b) else "Fałsz")
