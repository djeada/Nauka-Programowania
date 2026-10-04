r"""
ZAD-12 — Zamiana formatu dat

**Poziom:** ★★☆
**Tagi:** `regex`, `string`, `grupy`

### Treść

Wczytaj tekst i zamień w nim każdą datę zapisaną w formacie `DD.MM.RRRR` na format `RRRR-MM-DD`, np. `05.03.2024` → `2024-03-05`. Resztę tekstu pozostaw bez zmian.

**Data** to dokładnie: 2 cyfry, kropka, 2 cyfry, kropka, 4 cyfry (cyfry `0–9`). Data nie może być częścią dłuższego słowa — tuż przed nią i tuż po niej nie może stać litera, cyfra ani `_` (zob. `\b` w konwencjach rozdziału). Nie sprawdzaj, czy taki dzień istnieje: `31.02.2023` też zamieniamy.

Nie są więc datami np. `1.02.2024` (jednocyfrowy dzień), `01.02.20245` (pięciocyfrowy rok) ani `x01.02.2024` (data przyklejona do litery).

### Wejście

* 1. linia: tekst

### Wyjście

Jedna linia: tekst po zamianie (bez zmian, jeśli nie zawiera żadnej daty).

### Przykład

**Wejście:**

```
Spotkanie przeniesiono z 05.03.2024 na 12.03.2024.
```

**Wyjście:**

```
Spotkanie przeniesiono z 2024-03-05 na 2024-03-12.
```

### Uwagi

* Fragmenty wzorca ujęte w nawiasy `( )` to **grupy** — są numerowane od 1 w kolejności nawiasów otwierających. W napisie zastępczym `re.sub()` odwołujesz się do nich przez `\1`, `\2`… albo `\g<1>`, `\g<2>`…:

```python
re.sub(r"(\w+) (\w+)", r"\2 \1", "Ala Kowalska")   # 'Kowalska Ala'
```

* Postać `\g<1>` przydaje się, gdy zaraz po odwołaniu stoi cyfra: `\g<1>0` to grupa 1 i znak `0`, a `\10` oznaczałoby grupę 10.

"""

import re

DATA = r"\b([0-9]{2})\.([0-9]{2})\.([0-9]{4})\b"


def zamien_daty(tekst):
    """Zamienia daty DD.MM.RRRR na RRRR-MM-DD."""
    return re.sub(DATA, r"\g<3>-\g<2>-\g<1>", tekst)


if __name__ == "__main__":
    tekst = input()
    print(zamien_daty(tekst))
