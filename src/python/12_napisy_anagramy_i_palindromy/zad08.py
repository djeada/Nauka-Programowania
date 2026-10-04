r"""
ZAD-08 — Wyjątkowe palindromy (podciągi bez zmiany kolejności)

**Poziom:** ★★★
**Tagi:** `napisy`, `palindrom`, `podnapisy`

### Treść

Wczytaj słowo i znajdź wszystkie **różne** wyjątkowe palindromy, które są jego **spójnymi fragmentami** (podnapisami, czyli kolejnymi znakami słowa, np. `slowo[i:j]`).

Fragment jest **wyjątkowym palindromem**, jeśli:

1. wszystkie jego znaki są identyczne (np. `a`, `aaa`), **albo**
2. ma nieparzystą długość, a wszystkie jego znaki poza środkowym są identyczne (np. `cbc`, `aabaa`).

### Wejście

* 1. linia: słowo złożone z małych liter

### Wyjście

Każdy wyjątkowy palindrom w osobnej linii, bez powtórzeń. Kolejność: od najkrótszych do najdłuższych, a palindromy tej samej długości — alfabetycznie.

### Przykład

**Wejście:**

```
xxyxx
```

**Wyjście:**

```
x
y
xx
xyx
xxyxx
```

Fragmenty `xxy`, `xyxx` itp. nie są wyjątkowymi palindromami. Palindrom `xx` występuje w słowie dwa razy, ale wypisujemy go raz.

### Uwagi

* Sprawdź wszystkie fragmenty `slowo[i:j]`, a pasujące zbierz w zbiorze (`set`), żeby usunąć powtórzenia.
* Wymaganą kolejność uzyskasz, przechodząc po długościach od 1 do długości słowa i dla każdej długości wypisując alfabetycznie (`sorted`) znalezione palindromy tej długości.

"""


def czy_wyjatkowy_palindrom(fragment):
    """
    Sprawdza, czy fragment jest wyjątkowym palindromem:
    wszystkie znaki są identyczne albo (przy nieparzystej długości)
    identyczne są wszystkie znaki poza środkowym.
    """
    srodek = len(fragment) // 2
    bez_srodka = fragment[:srodek] + fragment[srodek + 1 :]

    if fragment == fragment[0] * len(fragment):
        return True
    if len(fragment) % 2 == 1 and bez_srodka == fragment[0] * len(bez_srodka):
        return True
    return False


def wyjatkowe_palindromy(slowo):
    """Zwraca różne wyjątkowe palindromy: od najkrótszych, a w obrębie długości alfabetycznie."""
    wynik = []
    for dlugosc in range(1, len(slowo) + 1):
        znalezione = set()
        for poczatek in range(len(slowo) - dlugosc + 1):
            fragment = slowo[poczatek : poczatek + dlugosc]
            if czy_wyjatkowy_palindrom(fragment):
                znalezione.add(fragment)
        wynik.extend(sorted(znalezione))
    return wynik


if __name__ == "__main__":
    slowo = input().strip()

    for palindrom in wyjatkowe_palindromy(slowo):
        print(palindrom)
