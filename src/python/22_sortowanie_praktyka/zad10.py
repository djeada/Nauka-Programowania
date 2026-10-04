r"""
ZAD-10 — k najczęstszych słów

**Poziom:** ★★☆
**Tagi:** `sort`, `Counter`, `lambda`, `string`

### Treść

Wczytaj liczbę $k$ i tekst. Znajdź $k$ słów, które występują w tekście najczęściej.

Słowa wyznaczamy tak:

* wielkość liter nie ma znaczenia — cały tekst zamień na małe litery,
* słowo to ciąg kolejnych **liter** (znaków, dla których `znak.isalpha()` jest prawdą, także polskich); wszystkie inne znaki — spacje, cyfry, znaki interpunkcyjne — rozdzielają słowa.

Słowa uporządkuj według liczby wystąpień **malejąco**, a przy równej liczbie wystąpień — alfabetycznie (rosnąco, według kodów Unicode). Wypisz pierwsze $k$ słów z tej kolejności. Jeśli różnych słów jest mniej niż $k$, wypisz wszystkie.

### Wejście

* 1. linia: liczba całkowita $k$
* 2. linia: tekst (zawiera co najmniej jedno słowo)

### Wyjście

Co najwyżej $k$ linii, każda w postaci `<słowo> <liczba wystąpień>`.

### Ograniczenia

* $1 \le k \le 50$
* Tekst ma co najwyżej 1000 znaków.

### Przykład

**Wejście:**

```
3
Ala ma kota, a kot ma Alę. Ala ma też psa!
```

**Wyjście:**

```
ma 3
ala 2
a 1
```

Słowo `ma` występuje 3 razy, `ala` — 2 razy, a sześć słów występuje po razie: `a`, `alę`, `kot`, `kota`, `psa`, `też`. Spośród nich alfabetycznie pierwsze jest `a`.

### Uwagi

* Słowa wydzielisz bez wyrażeń regularnych: zamień każdy znak, który nie jest literą, na spację, a potem użyj `split()`.
* `Counter` z modułu `collections` zlicza wystąpienia: `Counter(["a", "b", "a"])` daje `Counter({'a': 2, 'b': 1})`, a `.items()` zwraca pary `(słowo, liczba)`.
* Metoda `most_common()` przy remisie zachowuje kolejność pierwszego wystąpienia, a nie alfabetyczną — dlatego posortuj pary samodzielnie: `sorted(licznik.items(), key=lambda p: (-p[1], p[0]))`.

"""

from collections import Counter


def podziel_na_slowa(tekst):
    znaki = []
    for znak in tekst.lower():
        if znak.isalpha():
            znaki.append(znak)
        else:
            znaki.append(" ")
    return "".join(znaki).split()


def najczestsze_slowa(tekst, k):
    licznik = Counter(podziel_na_slowa(tekst))
    pary = sorted(licznik.items(), key=lambda p: (-p[1], p[0]))
    return pary[:k]


if __name__ == "__main__":
    k = int(input())
    tekst = input()
    for slowo, liczba in najczestsze_slowa(tekst, k):
        print(slowo, liczba)
