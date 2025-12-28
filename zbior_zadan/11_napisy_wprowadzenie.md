# Rozdział: Napisy — operacje podstawowe (stdin/stdout)

Poniższe zadania polegają na wczytywaniu danych ze **standardowego wejścia** (stdin) i wypisywaniu wyniku na **standardowe wyjście** (stdout).
**Każde zadanie (oraz każdy podpunkt) jest osobnym, niezależnym programem.**

**Konwencje wspólne:**

* Wczytuj dane dokładnie w kolejności podanej w sekcji **Wejście**.
* Jeśli w danych jest „jeden napis” — wczytaj **całą linię** (może zawierać spacje).
* Jeśli w wyjściu ma być lista w stylu `["Ala", "ma"]` albo `['o', 'ń']`, wypisz ją dokładnie w tej postaci.

---

## ZAD-01 — Odwróć napis

**Poziom:** ★☆☆
**Tagi:** `string`, `I/O`

### Treść

Wczytaj napis i wypisz go od tyłu.

### Wejście

* 1. linia: napis

### Wyjście

* 1. linia: odwrócony napis

### Przykład

**Wejście:**

```
barszcz
```

**Wyjście:**

```
zczsrab
```

---

## ZAD-02 — Policz wystąpienia znaku

**Poziom:** ★☆☆
**Tagi:** `string`, `count`

### Treść

Wczytaj napis oraz jeden znak. Wypisz, ile razy ten znak występuje w napisie.

### Wejście

* 1. linia: napis
* 2. linia: pojedynczy znak

### Wyjście

* 1. linia: liczba wystąpień

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
**Tagi:** `string`, `split`

### Treść

Wczytaj zdanie i policz, z ilu słów się składa. Znaki interpunkcyjne nie są słowami.

### Wejście

* 1. linia: zdanie

### Wyjście

* 1. linia: liczba słów

### Przykład

**Wejście:**

```
gram na pianinie.
```

**Wyjście:**

```
3
```

### Uwagi o formatowaniu

* Najprościej: podziel po białych znakach, a z końców słów usuń interpunkcję.

---

## ZAD-04 — Zamień wszystkie małe litery na duże

**Poziom:** ★☆☆
**Tagi:** `string`, `upper`

### Treść

Wczytaj napis i zamień wszystkie litery na wielkie.

### Wejście

* 1. linia: napis

### Wyjście

* 1. linia: napis po konwersji

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
**Tagi:** `string`, `slicing`, `pętle`

### Treść

Wczytaj napis i liczbę `k`.

a) Wypisz co `k`-ty znak w jednym wierszu, oddzielając znaki spacjami.
b) Wypisz co `k`-ty znak pionowo (każdy w osobnej linii).

### Wejście

* 1. linia: napis
* 2. linia: liczba naturalna `k` (k ≥ 1)

### Wyjście

* (a) 1 linia: znaki oddzielone spacjami
* (b) wiele linii: każdy znak osobno

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

### Uwagi o formatowaniu

* Dokładnie jedna spacja między znakami w punkcie (a), bez spacji na końcu linii.

---

## ZAD-06 — Zamień litery „a” na „?”

**Poziom:** ★☆☆
**Tagi:** `string`, `replace`

### Treść

Wczytaj napis i zamień wszystkie wystąpienia litery `a` na znak `?`.

### Wejście

* 1. linia: napis

### Wyjście

* 1. linia: napis po zamianie

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
**Tagi:** `ASCII`, `ord`, `string`

### Treść

Wczytaj napis i wypisz kody ASCII wszystkich jego znaków, oddzielone przecinkiem i spacją `", "`.

### Wejście

* 1. linia: napis

### Wyjście

* 1. linia: kody ASCII oddzielone `, `

### Przykład

**Wejście:**

```
Robot
```

**Wyjście:**

```
82, 111, 98, 111, 116
```

---

## ZAD-08 — Wypisz pionowo słowa ze zdania

**Poziom:** ★☆☆
**Tagi:** `split`, `string`

### Treść

Wczytaj zdanie, podziel na słowa i wypisz każde słowo w osobnej linii. Interpunkcja nie jest słowem.

### Wejście

* 1. linia: zdanie

### Wyjście

* wiele linii: słowa w kolejności występowania

### Przykład

**Wejście:**

```
Ala ma kota
```

**Wyjście:**

```
Ala
ma
kota
```

---

## ZAD-09 — Rozdziel informacje o pracowniku

**Poziom:** ★☆☆
**Tagi:** `split`, `formatowanie`

### Treść

Wczytaj linię z danymi pracownika rozdzielonymi średnikami `;`:

1. Imię, 2) Nazwisko, 3) Miejsce urodzenia, 4) Stanowisko, 5) Zarobki

Wypisz każdą informację w osobnej linii z etykietą.

### Wejście

* 1. linia: dane w formacie `Imię; Nazwisko; Miasto; Zawód; Zarobki;`

### Wyjście

Pięć linii w formacie:

* `Imię: ...`
* `Nazwisko: ...`
* `Miejsce urodzenia: ...`
* `Zawód: ...`
* `Zarobki: ...`

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

* Po `split(';')` usuń ewentualne spacje z brzegów pól (np. `strip()`).
* Ostatni średnik może powodować pusty element na końcu — zignoruj go.

---

## ZAD-10 — Najdłuższe i najkrótsze słowo

**Poziom:** ★☆☆
**Tagi:** `string`, `min/max`, `len`

### Treść

Wczytaj zdanie i znajdź:

a) najdłuższe słowo,
b) najkrótsze słowo.

Jeśli jest remis, wybierz słowo, które występuje wcześniej.

### Wejście

* 1. linia: zdanie

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

---

## ZAD-11 — Średnia długość słów

**Poziom:** ★☆☆
**Tagi:** `string`, `arytmetyka`

### Treść

Wczytaj zdanie i oblicz średnią długość słów. Wynik ma być liczbą całkowitą.

### Wejście

* 1. linia: zdanie

### Wyjście

* 1. linia: średnia długość słów (liczba całkowita)

### Przykład

**Wejście:**

```
Zepsuty rower.
```

**Wyjście:**

```
6
```

### Uwagi

* Licz jako: `suma_dlugosci // liczba_slow` (dzielenie całkowite).

---

## ZAD-12 — Usuń spacje ze zdania

**Poziom:** ★☆☆
**Tagi:** `replace`, `string`

### Treść

Wczytaj zdanie i usuń z niego wszystkie spacje.

### Wejście

* 1. linia: zdanie

### Wyjście

* 1. linia: zdanie bez spacji

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
**Tagi:** `liczby pierwsze`, `indeksy`, `string`

### Treść

Wczytaj napis. Zbierz znaki, których **indeksy (od 0)** są liczbami pierwszymi (2, 3, 5, 7, ...). Wypisz wynik jako listę w stylu Pythona.

### Wejście

* 1. linia: napis

### Wyjście

* 1. linia: lista znaków, np. `['o', 'ń']`

### Przykład

**Wejście:**

```
Słoń
```

**Wyjście:**

```
['o', 'ń']
```

### Uwagi

* Indeksy: `S(0) ł(1) o(2) ń(3)` → bierz 2 i 3.

---

## ZAD-14 — Napis z liczb od 1 do n

**Poziom:** ★☆☆
**Tagi:** `pętle`, `string`

### Treść

Wczytaj `n` i wypisz napis złożony z kolejnych liczb od 1 do `n`, bez separatorów.

### Wejście

* 1. linia: liczba naturalna `n` (n ≥ 1)

### Wyjście

* 1. linia: ciąg `1..n` bez spacji

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
123
```

---

## ZAD-15 — Słowa jako lista

**Poziom:** ★☆☆
**Tagi:** `split`, `list`

### Treść

Wczytaj zdanie i wypisz listę słów w formacie `["Ala", "ma", "kota"]`.

### Wejście

* 1. linia: zdanie

### Wyjście

* 1. linia: lista słów (jak w przykładzie)

### Przykład

**Wejście:**

```
Ala ma kota
```

**Wyjście:**

```
["Ala", "ma", "kota"]
```

---

## ZAD-16 — Odległość Hamminga

**Poziom:** ★★☆
**Tagi:** `string`, `porównanie`

### Treść

Wczytaj dwa napisy tej samej długości i policz, na ilu pozycjach różnią się znakami.

### Wejście

* 1. linia: napis `s1`
* 2. linia: napis `s2`  (ta sama długość)

### Wyjście

* 1. linia: odległość Hamminga

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
**Tagi:** `list`, `string`

### Treść

Otrzymujesz listę liczb naturalnych w zapisie tekstowym (np. `[2, 4, 7]`). Połącz liczby bez separatorów i wypisz jako napis.

### Wejście

* 1. linia: lista w formacie podobnym do Pythona, np. `[2, 4, 7]`

### Wyjście

* 1. linia: napis z połączonych liczb, np. `247`

### Przykład

**Wejście:**

```
[2, 4, 7]
```

**Wyjście:**

```
247
```

### Uwagi

* Najprościej: usuń nawiasy `[` `]`, rozdziel po przecinkach, `strip()`, potem sklej.

---

## ZAD-18 — Odwróć słowa w zdaniu

**Poziom:** ★★☆
**Tagi:** `split`, `string`, `pętle`

### Treść

Wczytaj zdanie i odwróć litery **w każdym słowie osobno**, zachowując kolejność słów.

### Wejście

* 1. linia: zdanie

### Wyjście

* 1. linia: zdanie z odwróconymi słowami

### Przykład

**Wejście:**

```
Ala ma kota
```

**Wyjście:**

```
alA am atok
```
