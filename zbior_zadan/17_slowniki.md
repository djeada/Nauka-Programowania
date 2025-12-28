# Rozdział: Słowniki (stdin/stdout)

Poniższe zadania polegają na wczytywaniu danych ze **standardowego wejścia** (stdin) i wypisywaniu wyniku na **standardowe wyjście** (stdout).
**Każde zadanie (oraz każdy podpunkt) jest osobnym, niezależnym programem.**

**Konwencje wspólne:**

* Jeśli w danych wejściowych liczby/napisy są w osobnych liniach — wczytuj je dokładnie w tej kolejności.
* Jeśli w danych wejściowych w jednej linii jest kilka wartości — rozbij linię po spacjach.
* Wypisuj wynik dokładnie w formacie z treści (np. słownik w postaci `{...}`, listy jak `[...]`).

---

## ZAD-01 — Słownik: liczby i ich kwadraty

**Poziom:** ★☆☆
**Tagi:** `dict`, `pętla`

### Treść

Wczytaj liczbę `n`. Utwórz słownik, gdzie klucze to liczby od `1` do `n-1`, a wartości to ich kwadraty.

### Wejście

* 1 linia: `n` (n ≥ 1)

### Wyjście

* Słownik w postaci: `{1: 1, 2: 4, ...}`

### Przykład

**Wejście:**

```
5
```

**Wyjście:**

```
{1: 1, 2: 4, 3: 9, 4: 16}
```

---

## ZAD-02 — Słownik z dwóch list (klucze i wartości)

**Poziom:** ★☆☆
**Tagi:** `dict`, `listy`

### Treść

Wczytaj dwie listy. Jeśli mają tę samą długość, utwórz słownik: klucz z pierwszej listy → wartość z drugiej listy.
Jeśli długości są różne, wypisz pusty słownik `{}`.

### Wejście

* 1 linia: `n`
* 2 linia: `m`
* następnie `n` liczb (pierwsza lista)
* następnie `m` liczb (druga lista)

### Wyjście

* Słownik albo `{}`

### Przykład

**Wejście:**

```
3
3
3 5 8
1 2 -1
```

**Wyjście:**

```
{3: 1, 5: 2, 8: -1}
```

---

## ZAD-03 — Biblioteka: baza wypożyczeń

**Poziom:** ★☆☆
**Tagi:** `dict`, `list`, `pętle`, `string`

### Treść

Utrzymuj słownik: `imię -> lista wypożyczonych książek`.
Obsługuj komendy (każda w osobnej linii) aż do `koniec`:

* `dodaj [imię] [tytuł]`
* `zwróć [imię] [tytuł]`
* `lista [imię]`

Po `lista [imię]` wypisz:

* jeśli lista niepusta: `Książki wypożyczone przez [imię]: t1, t2, ...`
* jeśli brak książek (lub brak czytelnika): `Książki wypożyczone przez [imię]: brak`

### Wejście

Wiele linii z komendami, koniec po słowie `koniec`.

### Wyjście

Tylko po komendach `lista ...`.

### Przykład

**Wejście:**

```
dodaj Jan Hobbit
dodaj Anna "Duma i uprzedzenie"
dodaj Jan "Władca Pierścieni"
lista Jan
zwróć Jan Hobbit
lista Jan
lista Anna
koniec
```

**Wyjście:**

```
Książki wypożyczone przez Jan: Hobbit, Władca Pierścieni
Książki wypożyczone przez Jan: Władca Pierścieni
Książki wypożyczone przez Anna: Duma i uprzedzenie
```

---

## ZAD-04 — Usuń pary ze słownika na podstawie wartości

**Poziom:** ★☆☆
**Tagi:** `dict`, `filtrowanie`

### Treść

Wczytaj słownik (`n` par: klucz-napis, wartość-liczba) oraz liczbę `k`. Usuń wszystkie pary, gdzie wartość == `k`. Wypisz wynikowy słownik.

### Wejście

* 1 linia: `n`
* następnie `n` linii: `klucz wartość`
* ostatnia linia: `k`

### Wyjście

* Słownik po usunięciu par

### Przykład

**Wejście:**

```
4
aaa 5
abc 1
xxx 5
cba 3
5
```

**Wyjście:**

```
{'abc': 1, 'cba': 3}
```

---

## ZAD-05 — Pracownik z największym sumarycznym zyskiem

**Poziom:** ★☆☆
**Tagi:** `dict`, `sumowanie`

### Treść

Wczytaj `n` wpisów: `pracownik zysk`. Zsumuj zyski per pracownik i wypisz nazwę pracownika z największą sumą.
(Jeśli remis, wybierz tego, który pierwszy osiągnął tę maksymalną sumę podczas przetwarzania.)

### Wejście

* 1 linia: `n`
* następnie `n` linii: `imie_i_nazwisko zysk`

### Wyjście

* Jedna linia: `imie_i_nazwisko`

### Przykład

**Wejście:**

```
5
Barnaba_Barabash 120
Jon_Snow 100
Kira_Summer 300
Barnaba_Barabash 200
Bob_Marley 110
```

**Wyjście:**

```
Barnaba_Barabash
```

---

## ZAD-06 — Histogram znaków w słowie

**Poziom:** ★☆☆
**Tagi:** `dict`, `string`

### Treść

Wczytaj napis. Zwróć słownik: znak → liczba wystąpień.

### Wejście

* 1 linia: napis

### Wyjście

* Słownik, np. `{'k': 1, 'l': 1, 'a': 2, 's': 1}`

### Przykład

**Wejście:**

```
klasa
```

**Wyjście:**

```
{'k': 1, 'l': 1, 'a': 2, 's': 1}
```

---

## ZAD-07 — Histogram słów w tekście (ignoruj wielkość liter)

**Poziom:** ★☆☆
**Tagi:** `dict`, `string`, `tekst`

### Treść

Wczytaj tekst. Policz częstość występowania słów (tylko litery), ignorując wielkość liter. Wypisz słownik: słowo (małe litery) → liczba wystąpień.

### Wejście

* 1 linia: tekst

### Wyjście

* Słownik

### Przykład

**Wejście:**

```
Ala ma kota. Ala lubi koty.
```

**Wyjście:**

```
{'ala': 2, 'ma': 1, 'kota': 1, 'lubi': 1, 'koty': 1}
```

---

## ZAD-08 — Najczęstsza litera w zdaniu

**Poziom:** ★☆☆
**Tagi:** `dict`, `string`

### Treść

Wczytaj zdanie. Zignoruj spacje i znaki interpunkcyjne. Znajdź literę występującą najczęściej.
Jeśli jest kilka, wybierz tę, która **pojawia się jako pierwsza w zdaniu**.

### Wejście

* 1 linia: zdanie

### Wyjście

* 1 znak

### Przykład

**Wejście:**

```
lezy jerzy na wiezy
```

**Wyjście:**

```
e
```

---

## ZAD-09 — Znaki występujące co najmniej dwa razy

**Poziom:** ★☆☆
**Tagi:** `dict`, `string`

### Treść

Wczytaj napis. Wypisz napis złożony z **unikalnych** znaków, które występują co najmniej 2 razy, w kolejności pierwszego pojawienia się w wejściu.

### Wejście

* 1 linia: napis

### Wyjście

* 1 linia: wynikowy napis

### Przykład

**Wejście:**

```
aaabbbccc
```

**Wyjście:**

```
abc
```

---

## ZAD-10 — Znalezienie anagramów w tekście (grupy)

**Poziom:** ★★☆
**Tagi:** `dict`, `anagramy`, `string`

### Treść

Wczytaj tekst. Znajdź grupy słów będących anagramami (ignoruj wielkość liter, słowa to tylko litery).
Wypisz wynik jako listę list, np. `[['absurd', 'brudas'], ...]`.
Do grup wypisuj tylko te klucze, które mają co najmniej 2 słowa.

### Wejście

* 1 linia: tekst

### Wyjście

* Lista list słów

### Przykład

Wejście jak w treści zadania → wyjście:

```
[["absurd", "brudas"], ["tyran", "narty"], ["bandzior", "zbrodnia"], ["burza", "arbuz"], ["galeria", "alergia"]]
```

---

## ZAD-11 — Sortowanie „słownika” po kluczach i po wartościach

**Poziom:** ★☆☆
**Tagi:** `sort`, `dict`

### Treść

Wczytaj `n` par `klucz wartość`.
a) Wypisz listę par posortowaną rosnąco po kluczach.
b) Wypisz listę par posortowaną rosnąco po wartościach.

### Wejście

* 1 linia: `n`
* następnie `n` linii: `klucz wartość`

### Wyjście

* 1 linia: lista par dla a)
* 2 linia: lista par dla b)

### Przykład

**Wejście:**

```
4
c 3
x 5
a -2
b 4
```

**Wyjście:**

```
[('a', -2), ('b', 4), ('c', 3), ('x', 5)]
[('a', -2), ('c', 3), ('b', 4), ('x', 5)]
```

---

## ZAD-12 — Porównanie dwóch słowników z listami (kolejność list bez znaczenia)

**Poziom:** ★★☆
**Tagi:** `dict`, `porównanie`, `list`

### Treść

Wczytaj dwa „słowniki” (opis w wejściu). Dla każdego klucza wartościami są listy liczb całkowitych, ale **kolejność w listach nie ma znaczenia**.
Wypisz `Prawda` jeśli słowniki są identyczne (te same klucze i te same wielozbiory wartości), w przeciwnym razie `Fałsz`.

### Wejście

* Najpierw:

  * 1 linia: `n`
  * następnie `n` linii: `klucz v1 v2 v3 ...` (co najmniej jedna wartość)
* Potem:

  * 1 linia: `m`
  * następnie `m` linii: `klucz v1 v2 v3 ...`

### Wyjście

* `Prawda` lub `Fałsz`

### Przykład

**Wejście:**

```
2
a 1 2 3
b 4 5
2
a 3 2 1
b 5 4
```

**Wyjście:**

```
Prawda
```

---
