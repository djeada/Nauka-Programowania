r"""
ZAD-10 — Znalezienie anagramów w tekście (grupy)

**Poziom:** ★★☆
**Tagi:** `dict`, `anagramy`, `string`

### Treść

Wczytaj tekst. Znajdź grupy różnych słów, które są swoimi **anagramami** (składają się z tych samych liter w tej samej liczbie, np. `absurd` i `brudas`), nie rozróżniając wielkości liter. Wypisz każdą grupę, która zawiera co najmniej dwa różne słowa.

### Wejście

* 1. linia: tekst

### Wyjście

* Każda grupa w osobnej linii: słowa małymi literami, oddzielone pojedynczą spacją, w kolejności pierwszego wystąpienia w tekście.
* Grupy w kolejności pierwszego wystąpienia ich pierwszego słowa.
* Jeśli nie ma żadnej grupy — jedna linia `Brak anagramów`.

### Ograniczenia

* tekst ma od 1 do 300 znaków

### Przykład

**Wejście:**

```
Tyran Brudas kupił narty. To absurd! Arbuz i burza.
```

**Wyjście:**

```
tyran narty
brudas absurd
arbuz burza
```

### Uwagi

* **Słowo** to najdłuższy ciąg kolejnych liter; pozostałe znaki rozdzielają słowa. Wielkość liter nie ma znaczenia (`Tyran` to `tyran`).
* Słowo powtórzone w tekście liczy się raz — `kot kot` nie jest grupą anagramów.
* Wskazówka: użyj słownika, w którym kluczem są posortowane litery słowa (`"".join(sorted(slowo))`), a wartością lista słów.

"""


def podziel_na_slowa(tekst):
    """Zwraca listę słów (ciągów liter) zapisanych małymi literami."""
    bez_innych_znakow = ""
    for znak in tekst:
        if znak.isalpha():
            bez_innych_znakow += znak.lower()
        else:
            bez_innych_znakow += " "
    return bez_innych_znakow.split()


def grupy_anagramow(tekst):
    """
    Zwraca listę grup anagramów (co najmniej dwa różne słowa w grupie).
    Kluczem słownika są posortowane litery słowa — wszystkie anagramy
    mają ten sam klucz.
    """
    grupy = {}
    for slowo in podziel_na_slowa(tekst):
        klucz = "".join(sorted(slowo))
        if klucz not in grupy:
            grupy[klucz] = []
        if slowo not in grupy[klucz]:
            grupy[klucz].append(slowo)

    wynik = []
    for grupa in grupy.values():
        if len(grupa) >= 2:
            wynik.append(grupa)
    return wynik


if __name__ == "__main__":
    grupy = grupy_anagramow(input())
    if not grupy:
        print("Brak anagramów")
    for grupa in grupy:
        print(" ".join(grupa))
