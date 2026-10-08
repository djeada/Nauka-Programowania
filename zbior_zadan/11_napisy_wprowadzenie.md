# Rozdział 11: Napisy — wprowadzenie

Zadania w tym rozdziale ćwiczą podstawowe operacje na napisach: indeksowanie, wycinanie, zamianę znaków, dzielenie zdania na słowa i składanie napisów z części.

**Konwencje wspólne:**

* Każde zadanie jest osobnym programem: czyta **standardowe wejście** i wypisuje wynik na **standardowe wyjście**.
* Program nie wypisuje komunikatów typu „Podaj napis:”.
* Napis lub zdanie wczytuj jako **całą linię** — może zawierać spacje.
* **Słowo** to fragment zdania oddzielony od innych spacjami. Znaki interpunkcyjne (np. `.` `,` `!` `?` `;` `:` `-` `(` `)` `"`) stojące na początku lub końcu fragmentu nie należą do słowa (`kota.` → `kota`), a fragment złożony wyłącznie z interpunkcji (np. samotny myślnik `-`) nie jest słowem. W Pythonie słowa uzyskasz tak: podziel zdanie metodą `split()`, z każdego fragmentu usuń interpunkcję metodą `strip(string.punctuation)` i pomiń puste wyniki.
* Gdy wynikiem jest lista, wypisz ją tak, jak robi to `print(lista)` w Pythonie, np. `['Ala', 'ma', 'kota']`. Pusta lista to `[]`.

---

## ZAD-01 — Odwróć napis

**Poziom:** ★☆☆
**Tagi:** `napisy`, `wycinanie`

### Treść

Wczytaj napis i wypisz go od tyłu — znak po znaku, od ostatniego do pierwszego.

### Wejście

* 1. linia: napis (może zawierać spacje)

### Wyjście

Jedna linia: odwrócony napis.

### Przykład 1

**Wejście:**

```
barszcz
```

**Wyjście:**

```
zczsrab
```

### Przykład 2

**Wejście:**

```
Ala ma kota
```

**Wyjście:**

```
atok am alA
```

Odwracamy kolejność wszystkich znaków (także spacji), a nie tylko kolejność słów.

---

## ZAD-02 — Policz wystąpienia znaku

**Poziom:** ★☆☆
**Tagi:** `napisy`, `zliczanie`

### Treść

Wczytaj napis oraz jeden znak. Wypisz, ile razy ten znak występuje w napisie.
Wielkość liter ma znaczenie: `A` i `a` to różne znaki.

### Wejście

* 1. linia: napis (może zawierać spacje)
* 2. linia: jeden znak (różny od spacji)

### Wyjście

Jedna linia: liczba wystąpień znaku (może być `0`).

### Przykład

**Wejście:**

```
klamra
a
```

**Wyjście:**

```
2
```

---

## ZAD-03 — Z ilu słów składa się zdanie?

**Poziom:** ★☆☆
**Tagi:** `napisy`, `split`, `słowa`

### Treść

Wczytaj zdanie i policz, z ilu słów się składa. Słowa wyznaczaj zgodnie z konwencją rozdziału: znaki interpunkcyjne nie są słowami.

### Wejście

* 1. linia: zdanie (zawiera co najmniej jedno słowo; słowa mogą być oddzielone kilkoma spacjami)

### Wyjście

Jedna linia: liczba słów.

### Przykład 1

**Wejście:**

```
gram na pianinie.
```

**Wyjście:**

```
3
```

### Przykład 2

**Wejście:**

```
Ala - jak co dzień - gra.
```

**Wyjście:**

```
5
```

Samotne myślniki nie są słowami, więc słowa to: `Ala`, `jak`, `co`, `dzień`, `gra`.

---

## ZAD-04 — Zamień wszystkie małe litery na duże

**Poziom:** ★☆☆
**Tagi:** `napisy`, `upper`

### Treść

Wczytaj napis i zamień w nim wszystkie małe litery (także polskie, np. `ż` → `Ż`) na wielkie. Pozostałe znaki pozostaw bez zmian.

### Wejście

* 1. linia: napis (może zawierać spacje)

### Wyjście

Jedna linia: napis po zamianie.

### Przykład

**Wejście:**

```
Rumcajs
```

**Wyjście:**

```
RUMCAJS
```

---

## ZAD-05 — Co k-ty znak poziomo i pionowo

**Poziom:** ★☆☆
**Tagi:** `napisy`, `wycinanie`, `pętle`

### Treść

Wczytaj napis i liczbę `k`. Wybierz co `k`-ty znak napisu, czyli znaki na pozycjach $k, 2k, 3k, \ldots$ (pozycje liczymy od 1).

a) Wypisz wybrane znaki w jednej linii, oddzielone pojedynczymi spacjami.
b) Wypisz wybrane znaki pionowo — każdy w osobnej linii.

### Wejście

* 1. linia: napis bez spacji
* 2. linia: liczba naturalna `k`

### Wyjście

* 1. linia: wynik podpunktu a)
* kolejne linie: wynik podpunktu b) — po jednym znaku w linii

### Ograniczenia

* $1 \le k \le$ długość napisu (wybrany zostanie więc co najmniej jeden znak).

### Przykład

**Wejście:**

```
Grzechotnik
3
```

**Wyjście:**

```
z h n
z
h
n
```

Znaki na pozycjach 3, 6 i 9 to `z`, `h` i `n`.

### Uwagi

* Pozycja $k$ to indeks `k - 1` w Pythonie, więc wybrane znaki to `napis[k - 1::k]`.

---

## ZAD-06 — Zamień litery „a” na „?”

**Poziom:** ★☆☆
**Tagi:** `napisy`, `replace`

### Treść

Wczytaj napis i zamień w nim wszystkie małe litery `a` na znak `?`. Wielkie `A` pozostaw bez zmian.

### Wejście

* 1. linia: napis (może zawierać spacje)

### Wyjście

Jedna linia: napis po zamianie.

### Przykład

**Wejście:**

```
Latarnik
```

**Wyjście:**

```
L?t?rnik
```

---

## ZAD-07 — Zamień znaki na kody ASCII

**Poziom:** ★☆☆
**Tagi:** `napisy`, `ASCII`, `ord`

### Treść

Wczytaj napis i wypisz kody ASCII wszystkich jego znaków (także spacji), w kolejności występowania.

### Wejście

* 1. linia: napis złożony ze znaków ASCII (bez polskich liter; może zawierać spacje)

### Wyjście

Jedna linia: kody ASCII oddzielone przecinkiem i spacją (`, `), bez separatora na końcu.

### Przykład

**Wejście:**

```
Robot
```

**Wyjście:**

```
82, 111, 98, 111, 116
```

### Uwagi

* Kod znaku zwraca funkcja `ord`, np. `ord("R")` to `82`.

---

## ZAD-08 — Wypisz pionowo słowa ze zdania

**Poziom:** ★☆☆
**Tagi:** `napisy`, `split`, `słowa`

### Treść

Wczytaj zdanie, podziel je na słowa (zgodnie z konwencją rozdziału — bez interpunkcji) i wypisz każde słowo w osobnej linii.

### Wejście

* 1. linia: zdanie (zawiera co najmniej jedno słowo)

### Wyjście

Słowa w kolejności występowania, każde w osobnej linii.

### Przykład

**Wejście:**

```
Ala ma kota, a kot ma Alę.
```

**Wyjście:**

```
Ala
ma
kota
a
kot
ma
Alę
```

---

## ZAD-09 — Rozdziel informacje o pracowniku

**Poziom:** ★☆☆
**Tagi:** `napisy`, `split`, `formatowanie`

### Treść

Wczytaj linię z danymi pracownika: imię, nazwisko, miejsce urodzenia, zawód i zarobki — w tej kolejności, oddzielone średnikami `;`.
Wypisz każdą informację w osobnej linii, poprzedzoną etykietą.

### Wejście

* 1. linia: dane w formacie `Imię; Nazwisko; Miejsce urodzenia; Zawód; Zarobki;`
  * przed średnikiem i po nim mogą (ale nie muszą) stać spacje,
  * linia zawsze kończy się średnikiem,
  * pojedyncze pole może zawierać spacje (np. `Nowy Sącz`).

### Wyjście

Pięć linii w formacie:

```
Imię: …
Nazwisko: …
Miejsce urodzenia: …
Zawód: …
Zarobki: …
```

Wartości wypisz bez spacji na początku i na końcu.

### Przykład

**Wejście:**

```
Jan; Kowalski; Warszawa; Programista; 1000;
```

**Wyjście:**

```
Imię: Jan
Nazwisko: Kowalski
Miejsce urodzenia: Warszawa
Zawód: Programista
Zarobki: 1000
```

### Uwagi

* Po `split(";")` usuń spacje z brzegów każdego pola metodą `strip()`.
* Końcowy średnik daje na końcu listy pusty element — pomiń go.

---

## ZAD-10 — Najdłuższe i najkrótsze słowo

**Poziom:** ★☆☆
**Tagi:** `napisy`, `słowa`, `min/max`

### Treść

Wczytaj zdanie i znajdź w nim (zgodnie z konwencją rozdziału — bez interpunkcji):

a) najdłuższe słowo,
b) najkrótsze słowo.

Jeśli kilka słów ma tę samą długość, wybierz to, które występuje w zdaniu **wcześniej**.

### Wejście

* 1. linia: zdanie (zawiera co najmniej jedno słowo)

### Wyjście

* 1. linia: najdłuższe słowo
* 2. linia: najkrótsze słowo

### Przykład

**Wejście:**

```
Kaczka lubi wiosnę.
```

**Wyjście:**

```
Kaczka
lubi
```

Słowa `Kaczka` i `wiosnę` mają po 6 liter — wygrywa wcześniejsze `Kaczka`.

---

## ZAD-11 — Średnia długość słów

**Poziom:** ★☆☆
**Tagi:** `napisy`, `słowa`, `arytmetyka`

### Treść

Wczytaj zdanie i oblicz średnią długość jego słów (zgodnie z konwencją rozdziału — interpunkcja nie wlicza się do długości słowa).
Wynikiem jest **część całkowita** średniej, czyli `suma_długości // liczba_słów`.

### Wejście

* 1. linia: zdanie (zawiera co najmniej jedno słowo)

### Wyjście

Jedna linia: część całkowita średniej długości słów.

### Przykład

**Wejście:**

```
Zepsuty rower.
```

**Wyjście:**

```
6
```

Słowa `Zepsuty` i `rower` mają razem $7 + 5 = 12$ liter, a `12 // 2` to `6`.

---

## ZAD-12 — Usuń spacje ze zdania

**Poziom:** ★☆☆
**Tagi:** `napisy`, `replace`

### Treść

Wczytaj zdanie i usuń z niego wszystkie spacje. Pozostałe znaki (także interpunkcję) pozostaw bez zmian.

### Wejście

* 1. linia: zdanie (zawiera co najmniej jeden znak różny od spacji)

### Wyjście

Jedna linia: zdanie bez spacji.

### Przykład

**Wejście:**

```
Ala ma kota
```

**Wyjście:**

```
Alamakota
```

---

## ZAD-13 — Znaki na indeksach będących liczbami pierwszymi

**Poziom:** ★☆☆
**Tagi:** `napisy`, `indeksy`, `liczby pierwsze`

### Treść

Wczytaj napis i zbierz do listy znaki, których **indeksy** (liczone od 0) są liczbami pierwszymi: 2, 3, 5, 7, 11, … Wypisz tę listę.

### Wejście

* 1. linia: napis (może zawierać spacje)

### Wyjście

Jedna linia: lista znaków wypisana tak jak przez `print(lista)`, np. `['o', 'ń']`. Jeśli napis ma mniej niż 3 znaki, wypisz `[]`.

### Przykład

**Wejście:**

```
Słoń
```

**Wyjście:**

```
['o', 'ń']
```

Indeksy: `S` — 0, `ł` — 1, `o` — 2, `ń` — 3. Liczbami pierwszymi są 2 i 3.

---

## ZAD-14 — Napis z liczb od 1 do n

**Poziom:** ★☆☆
**Tagi:** `napisy`, `pętle`, `konkatenacja`

### Treść

Wczytaj liczbę `n` i zbuduj napis złożony z kolejnych liczb od 1 do `n` zapisanych jedna za drugą, bez separatorów. Wypisz ten napis.

### Wejście

* 1. linia: liczba naturalna `n` ($n \ge 1$)

### Wyjście

Jedna linia: napis `123…n`.

### Przykład

**Wejście:**

```
11
```

**Wyjście:**

```
1234567891011
```

---

## ZAD-15 — Akronim ze zdania

**Poziom:** ★☆☆
**Tagi:** `napisy`, `słowa`, `upper`

### Treść

**Akronim** to skrót utworzony z pierwszych liter kolejnych słów, np. „Polska Akademia Nauk” → `PAN`.

Wczytaj zdanie i wypisz jego akronim: pierwsze znaki wszystkich słów (zgodnie z konwencją rozdziału — bez interpunkcji), zapisane jeden za drugim **wielkimi** literami.

### Wejście

* 1. linia: zdanie (zawiera co najmniej jedno słowo; może zawierać polskie litery)

### Wyjście

Jedna linia: akronim.

### Przykład

**Wejście:**

```
Polska Akademia Nauk
```

**Wyjście:**

```
PAN
```

### Uwagi

* Słowa mogą być rozdzielone kilkoma spacjami, a zdanie może zaczynać się lub kończyć spacjami — `split()` bez argumentu poradzi sobie z tym.
* Interpunkcja nie należy do słowa: w zdaniu `(Unia Europejska)` słowami są `Unia` i `Europejska`, więc akronim to `UE`. Samotny myślnik `-` nie jest słowem.
* Zamiana na wielką literę dotyczy także polskich liter: `żółta łódź` → `ŻŁ`.

---

## ZAD-16 — Odległość Hamminga

**Poziom:** ★★☆
**Tagi:** `napisy`, `porównywanie`, `pętle`

### Treść

Wczytaj dwa napisy tej samej długości i policz, na ilu pozycjach mają różne znaki (tzw. odległość Hamminga). Wielkość liter ma znaczenie.

### Wejście

* 1. linia: napis `s1` (bez spacji)
* 2. linia: napis `s2` (bez spacji, tej samej długości co `s1`)

### Wyjście

Jedna linia: odległość Hamminga.

### Przykład

**Wejście:**

```
adam
axam
```

**Wyjście:**

```
1
```

---

## ZAD-17 — Konwersja listy na napis

**Poziom:** ★☆☆
**Tagi:** `napisy`, `listy`, `str`

### Treść

Napisz funkcję `lista_na_napis(liczby)`, która otrzymuje listę liczb naturalnych i zwraca napis powstały przez zapisanie tych liczb jedna za drugą, bez separatorów (każdą liczbę zamień na napis funkcją `str`).

Program wczytuje listę liczb, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: liczby naturalne oddzielone spacjami (co najmniej jedna)

### Wyjście

Jedna linia: napis z połączonych liczb.

### Przykład

**Wejście:**

```
2 4 7
```

**Wyjście:**

```
247
```

### Kod startowy

```python
def lista_na_napis(liczby):
    # Uzupełnij funkcję: zamień każdą liczbę na napis i połącz wyniki.
    pass


liczby = [int(x) for x in input().split()]
print(lista_na_napis(liczby))
```

---

## ZAD-18 — Odwróć słowa w zdaniu

**Poziom:** ★★☆
**Tagi:** `napisy`, `split`, `pętle`

### Treść

Wczytaj zdanie i odwróć kolejność liter **w każdym słowie osobno**, zachowując kolejność słów w zdaniu.
Znaki interpunkcyjne na początku i na końcu słowa zostają na swoim miejscu (np. `kota,` → `atok,`).

### Wejście

* 1. linia: zdanie, w którym słowa są oddzielone pojedynczymi spacjami

### Wyjście

Jedna linia: zdanie z odwróconymi słowami (słowa oddzielone pojedynczymi spacjami).

### Przykład 1

**Wejście:**

```
Ala ma kota
```

**Wyjście:**

```
alA am atok
```

### Przykład 2

**Wejście:**

```
Ala ma kota, a kot ma Alę.
```

**Wyjście:**

```
alA am atok, a tok am ęlA.
```

---

## ZAD-19 — Szyfr Cezara

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

---

## ZAD-20 — Numerowanie wierszy do końca danych

**Poziom:** ★☆☆
**Tagi:** `napisy`, `sys.stdin`, `formatowanie`

### Treść

Wczytuj wiersze tekstu aż do **końca danych wejściowych** — nie wiadomo z góry, ile ich będzie. Wypisz wszystkie niepuste wiersze, poprzedzając każdy jego numerem w wejściu, a na końcu podaj, ile było wszystkich wierszy i ile niepustych.

Wiersz jest **pusty**, jeśli nie zawiera żadnych znaków albo zawiera same spacje. Puste wiersze nie są wypisywane, ale liczą się do numeracji.

### Wejście

* dowolna liczba wierszy tekstu (także zero)

### Wyjście

* Dla każdego niepustego wiersza jedna linia w formacie `nr | wiersz`, gdzie `nr` to numer wiersza w wejściu (od 1) wyrównany do prawej na szerokości 3 znaków, np. `  1 | Ala`, ` 12 | kot`. Wiersz wypisz bez zmian (z ewentualnymi spacjami na początku).
* Ostatnia linia: `Wierszy: X, niepustych: Y`.

### Przykład

**Wejście:**

```
Ala ma kota

Kot ma Alę
```

**Wyjście:**

```
  1 | Ala ma kota
  3 | Kot ma Alę
Wierszy: 3, niepustych: 2
```

### Uwagi

* Wszystkie wiersze aż do końca danych wczytasz za pomocą modułu `sys`: `sys.stdin.read().splitlines()` zwraca listę wierszy (bez znaków końca linii). Można też przejść po wierszach pętlą `for wiersz in sys.stdin:` — wtedy każdy wiersz kończy się znakiem `"\n"`, który usuniesz przez `wiersz.rstrip("\n")`.
* Wpisując dane ręcznie w konsoli, koniec danych zasygnalizujesz skrótem `Ctrl+D` (Linux, macOS) albo `Ctrl+Z` i `Enter` (Windows).
* Liczbę wyrównasz do prawej na szerokości 3 znaków w f-stringu: `f"{nr:>3}"`.
* Numerować wiersze pomoże `enumerate(wiersze, start=1)`.

### Kod startowy

```python
import sys

wiersze = sys.stdin.read().splitlines()

# Uzupełnij: wypisz ponumerowane niepuste wiersze i podsumowanie.
```
