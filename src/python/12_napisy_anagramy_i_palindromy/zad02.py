r"""
ZAD-02 — Wszystkie permutacje słowa

**Poziom:** ★★☆
**Tagi:** `napisy`, `permutacje`, `itertools`

### Treść

Wczytaj słowo złożone z **niepowtarzających się** liter i wypisz wszystkie jego permutacje (wszystkie słowa, które można ułożyć z jego liter, używając każdej dokładnie raz) — każdą w osobnej linii, w **kolejności alfabetycznej**.

### Wejście

* 1. linia: słowo złożone z małych liter alfabetu angielskiego (`a`–`z`), litery nie powtarzają się

### Wyjście

Wszystkie permutacje słowa w kolejności alfabetycznej, każda w osobnej linii. Słowo o długości $n$ ma $n!$ permutacji.

### Ograniczenia

* Długość słowa: od 1 do 6.

### Przykład 1

**Wejście:**

```
abc
```

**Wyjście:**

```
abc
acb
bac
bca
cab
cba
```

### Przykład 2

**Wejście:**

```
on
```

**Wyjście:**

```
no
on
```

### Uwagi

* Permutacje wygeneruje za Ciebie funkcja `permutations` z modułu `itertools` (biblioteka standardowa Pythona). Zwraca ona kolejne permutacje jako **krotki** liter — krotka to niezmienna lista zapisywana w nawiasach okrągłych:

  ```python
  from itertools import permutations

  for krotka in permutations("ab"):
      print(krotka)            # ('a', 'b'), a potem ('b', 'a')
      print("".join(krotka))   # ab, a potem ba
  ```

* `permutations` zachowuje kolejność liter z podanego ciągu, więc jeśli podasz mu litery posortowane alfabetycznie (`sorted(slowo)`), permutacje powstaną od razu w kolejności alfabetycznej. Możesz też posortować gotową listę wyników.
* Samodzielne generowanie permutacji (rekurencją) przećwiczysz w rozdziale o rekurencji.

"""

from itertools import permutations


def permutacje_alfabetycznie(slowo):
    """Zwraca listę wszystkich permutacji słowa w kolejności alfabetycznej."""
    wynik = []
    for krotka in permutations(sorted(slowo)):
        wynik.append("".join(krotka))
    return wynik


if __name__ == "__main__":
    slowo = input().strip()

    for permutacja in permutacje_alfabetycznie(slowo):
        print(permutacja)
