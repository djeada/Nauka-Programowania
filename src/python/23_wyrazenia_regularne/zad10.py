r"""
ZAD-10 — Podmień napisy z listy A na napisy z listy B

**Poziom:** ★★☆
**Tagi:** `regex`, `string`, `zamiana`

### Treść

Wczytaj tekst wielowierszowy oraz dwie listy słów tej samej długości: A i B. Zastąp w tekście każde wystąpienie słowa `A[i]` słowem `B[i]` (ten sam indeks).

* Zamieniaj tylko **całe słowa** (zob. konwencje rozdziału), np. słowo `kot` nie zmienia się wewnątrz `kota` ani `kot_1`. Wielkość liter ma znaczenie.
* Wszystkie zamiany wykonaj **jednocześnie**, na podstawie oryginalnego tekstu — wstawione słowo nie jest już ponownie zamieniane. Dla A = `kot pies` i B = `pies kot` tekst `kot i pies` zmienia się w `pies i kot`.

### Wejście

* 1. linia: `n` — liczba wierszy tekstu
* kolejne `n` linii: tekst
* następna linia: słowa listy A oddzielone spacjami
* ostatnia linia: słowa listy B oddzielone spacjami (tyle samo co w A)

### Wyjście

Tekst po zamianach (tyle samo wierszy co na wejściu).

### Ograniczenia

* $1 \le n \le 100$
* Listy mają co najmniej jedno słowo, słowa w liście A się nie powtarzają, a każde słowo składa się tylko z liter i cyfr.

### Przykład

**Wejście:**

```
1
Ala ma kota, a kot ma Alę.
kot Ala
pies Ola
```

**Wyjście:**

```
Ola ma kota, a pies ma Alę.
```

Słowa `kota` i `Alę` się nie zmieniają — to inne słowa niż `kot` i `Ala`.

### Uwagi

* Zbuduj jeden wzorzec z alternatywą, np. `\b(kot|Ala)\b`, i użyj `re.sub()` z funkcją, która dla dopasowanego słowa zwraca jego zamiennik ze słownika.

"""

import re


def zamien_slowa(tekst, lista_a, lista_b):
    """Zamienia jednocześnie całe słowa z listy A na odpowiadające im słowa z listy B."""
    zamiany = dict(zip(lista_a, lista_b))
    wzorzec = r"\b(" + "|".join(re.escape(slowo) for slowo in lista_a) + r")\b"
    return re.sub(wzorzec, lambda dopasowanie: zamiany[dopasowanie.group(1)], tekst)


if __name__ == "__main__":
    n = int(input())
    tekst = "\n".join(input() for _ in range(n))
    lista_a = input().split()
    lista_b = input().split()

    print(zamien_slowa(tekst, lista_a, lista_b))
