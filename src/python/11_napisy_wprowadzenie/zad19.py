r"""
ZAD-19 — Szyfr Cezara

**Poziom:** ★★☆
**Tagi:** `napisy`, `ord/chr`, `modulo`

### Treść

Szyfr Cezara zastępuje każdą literę literą położoną `k` miejsc dalej w alfabecie. Alfabet jest „zawinięty”: po `z` następuje znowu `a`. Przy `k = 3` litera `a` przechodzi w `d`, `x` w `a`, a `Z` w `C`.

Wczytaj przesunięcie `k` oraz tekst i wypisz zaszyfrowany tekst:

* przesuwaj tylko litery alfabetu łacińskiego `A`–`Z` i `a`–`z`, zachowując ich wielkość (wielka litera pozostaje wielką, mała — małą),
* pozostałe znaki (spacje, cyfry, interpunkcję, polskie litery takie jak `ą` czy `Ż`) przepisz bez zmian.

Przesunięcie może być ujemne (przesunięcie w lewo, np. przy `k = -1` litera `a` przechodzi w `z`) lub większe niż 26.

### Wejście

* 1. linia: liczba całkowita `k`
* 2. linia: tekst (może zawierać spacje)

### Wyjście

Jedna linia: zaszyfrowany tekst.

### Przykład 1

**Wejście:**

```
3
Ala ma kota!
```

**Wyjście:**

```
Dod pd nrwd!
```

### Przykład 2

**Wejście:**

```
-1
Zebra
```

**Wyjście:**

```
Ydaqz
```

### Uwagi

* `ord(znak)` zwraca kod znaku, a `chr(kod)` — znak o danym kodzie, np. `ord("a")` to `97`, a `chr(100)` to `"d"`.
* Numer małej litery w alfabecie (od 0) to `ord(znak) - ord("a")`. Nowy numer to `(numer + k) % 26` — w Pythonie wynik `%` dla dodatniego dzielnika jest zawsze z przedziału 0–25, także dla ujemnego `k`. Z powrotem na literę: `chr(nowy_numer + ord("a"))`. Wielkie litery obsłuż tak samo, z `ord("A")`.
* To, czy znak jest małą literą łacińską, sprawdzisz warunkiem `"a" <= znak <= "z"`.

"""


def przesun_litere(znak, k):
    if "a" <= znak <= "z":
        poczatek = ord("a")
    elif "A" <= znak <= "Z":
        poczatek = ord("A")
    else:
        return znak
    numer = ord(znak) - poczatek
    return chr((numer + k) % 26 + poczatek)


def szyfr_cezara(tekst, k):
    wynik = ""
    for znak in tekst:
        wynik += przesun_litere(znak, k)
    return wynik


if __name__ == "__main__":
    k = int(input())
    tekst = input()
    print(szyfr_cezara(tekst, k))
