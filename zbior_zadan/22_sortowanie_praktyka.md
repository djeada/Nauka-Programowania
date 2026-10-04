# Rozdział 22: Sortowanie — praktyka

Zadania w tym rozdziale pokazują, jak sortować w praktyce: napisy, słowa, pary, obiekty — często według własnego kryterium. Tutaj **wolno** (a nawet warto) korzystać z wbudowanych narzędzi Pythona: `sorted()`, `list.sort()` i parametru `key=`.

**Konwencje wspólne:**

* Każde zadanie to osobny program: czyta **standardowe wejście** i wypisuje wynik na **standardowe wyjście**.
* Jeśli wejściem jest napis — wczytaj całą linię (łącznie ze spacjami).
* Jeśli wejściem jest lista — najpierw podana jest liczba elementów $N$, a potem elementy (w jednej linii albo w kolejnych liniach — zależnie od zadania).
* Napisy porównujemy tak jak Python, czyli według kodów znaków Unicode: wielkie litery są „mniejsze” od małych (`'Z' < 'a'`), a polskie litery są „większe” od wszystkich liter alfabetu łacińskiego (`'z' < 'ą'`).
* Sortowanie w Pythonie (`sorted()`, `list.sort()`) jest **stabilne**: elementy równe według kryterium sortowania zachowują kolejność z wejścia. Korzystają z tego zadania, w których mogą wystąpić remisy.
* Program nie wypisuje komunikatów typu „Podaj liczbę:”.

---

## ZAD-01 — Sortowanie znaków w napisie

**Poziom:** ★☆☆
**Tagi:** `sort`, `string`

### Treść

Wczytaj napis, posortuj rosnąco wszystkie jego znaki i wypisz napis złożony z posortowanych znaków.

### Wejście

* 1. linia: napis $s$ (co najmniej jeden znak)

### Wyjście

* 1. linia: znaki napisu $s$ posortowane rosnąco według kodów Unicode, sklejone w jeden napis

### Ograniczenia

* $1 \le |s| \le 100$

### Przykład

**Wejście:**

```
Ala ma kota
```

**Wyjście:**

```
  Aaaaklmot
```

### Uwagi

* Spacje też są znakami i biorą udział w sortowaniu. Spacja ma mniejszy kod niż litery i cyfry, dlatego w przykładzie wynik zaczyna się od **dwóch** spacji (napis `Ala ma kota` zawiera dwie spacje).
* `sorted(napis)` zwraca listę znaków — połącz ją w napis metodą `"".join(…)`.

---

## ZAD-02 — Sortowanie słów w zdaniu

**Poziom:** ★★☆
**Tagi:** `sort`, `string`, `split`

### Treść

Wczytaj zdanie i podziel je na słowa. Słowa oddzielają od siebie spacje oraz znaki interpunkcyjne: `.` `,` `!` `?` `;` `:` — te znaki nie należą do słów. Posortuj słowa rosnąco (według kodów Unicode, bez zmiany wielkości liter) i wypisz je.

### Wejście

* 1. linia: zdanie (zawiera co najmniej jedno słowo)

### Wyjście

* 1. linia: posortowane słowa oddzielone pojedynczymi spacjami

Jeśli słowo występuje w zdaniu kilka razy, wypisz je tyle samo razy.

### Ograniczenia

* Zdanie ma co najwyżej 200 znaków.

### Przykład

**Wejście:**

```
Lemur wygina śmiało ciało
```

**Wyjście:**

```
Lemur ciało wygina śmiało
```

### Przykład 2

**Wejście:**

```
Ala ma kota, a kot ma Alę.
```

**Wyjście:**

```
Ala Alę a kot kota ma ma
```

Wielkie litery są przed małymi, a `Ala` jest przed `Alę`, bo `'a' < 'ę'`.

### Uwagi

* Najprościej zamienić każdy znak interpunkcyjny na spację (`napis.replace(".", " ")` itd.), a potem użyć `split()`.

---

## ZAD-03 — Sortowanie listy par względem kryterium

**Poziom:** ★☆☆
**Tagi:** `sort`, `tuple`, `list`

### Treść

Wczytaj listę par `(napis, liczba)` i zapisz je jako krotki.

a) Posortuj pary rosnąco według liczby.
b) Posortuj pary rosnąco według długości napisu.

Przy remisie (ta sama liczba w a), ta sama długość napisu w b)) pary zachowują kolejność z wejścia.

### Wejście

* 1. linia: liczba par $N$
* kolejne $N$ linii: napis (bez spacji) i liczba całkowita, oddzielone spacją

### Wyjście

* 1. linia: lista par posortowana według podpunktu a)
* 2. linia: lista par posortowana według podpunktu b)

Listy wypisz w formacie Pythona — tak, jak robi to `print(lista)` dla listy krotek, np. `[('bca', 1), ('c', 2), ('ab', 3)]`.

### Ograniczenia

* $1 \le N \le 20$

### Przykład

**Wejście:**

```
3
ab 3
bca 1
c 2
```

**Wyjście:**

```
[('bca', 1), ('c', 2), ('ab', 3)]
[('c', 2), ('ab', 3), ('bca', 1)]
```

### Uwagi

* Kryterium sortowania podaj w parametrze `key`, np. `sorted(pary, key=lambda para: para[1])`.

---

## ZAD-04 — Sortowanie napisów według długości

**Poziom:** ★☆☆
**Tagi:** `sort`, `string`, `list`

### Treść

Wczytaj listę napisów i posortuj ją rosnąco według długości napisów. Napisy o tej samej długości zachowują kolejność z wejścia.

### Wejście

* 1. linia: liczba napisów $N$
* kolejne $N$ linii: napis (bez spacji)

### Wyjście

* 1. linia: posortowane napisy oddzielone pojedynczymi spacjami

### Ograniczenia

* $1 \le N \le 50$

### Przykład

**Wejście:**

```
4
abcd
ab
a
abc
```

**Wyjście:**

```
a ab abc abcd
```

### Uwagi

* Wystarczy `sorted(napisy, key=len)`.

---

## ZAD-05 — Sortowanie listy miast

**Poziom:** ★☆☆
**Tagi:** `class`, `sort`, `obiekty`

### Treść

Klasa `Miasto` ma atrybuty:

* `nazwa` (napis),
* `liczba_mieszkancow` (liczba naturalna).

Uzupełnij metodę `__repr__`, tak aby obiekt był wypisywany w postaci `Miasto("NAZWA", LICZBA)`, np. `Miasto("Berlin", 3800000)`. Dzięki temu `print(lista_miast)` wypisze całą listę w czytelnej postaci.

Wczytaj listę miast, a następnie:

a) posortuj miasta alfabetycznie według nazwy,
b) posortuj miasta rosnąco według liczby mieszkańców (miasta o tej samej liczbie mieszkańców zachowują kolejność z wejścia).

### Wejście

* 1. linia: liczba miast $N$
* kolejne $N$ linii: nazwa miasta (bez spacji) i liczba mieszkańców, oddzielone spacją

### Wyjście

* 1. linia: lista miast posortowana według podpunktu a)
* 2. linia: lista miast posortowana według podpunktu b)

Każdą listę wypisz przez `print(lista)` — w formacie `[Miasto("NAZWA", LICZBA), Miasto("NAZWA", LICZBA), …]`.

### Ograniczenia

* $1 \le N \le 20$
* Nazwy miast są różne.

### Przykład

**Wejście:**

```
3
Paris 2150000
Berlin 3800000
New_York 8400000
```

**Wyjście:**

```
[Miasto("Berlin", 3800000), Miasto("New_York", 8400000), Miasto("Paris", 2150000)]
[Miasto("Paris", 2150000), Miasto("Berlin", 3800000), Miasto("New_York", 8400000)]
```

### Kod startowy

```python
class Miasto:
    def __init__(self, nazwa, liczba_mieszkancow):
        self.nazwa = nazwa
        self.liczba_mieszkancow = liczba_mieszkancow

    def __repr__(self):
        # Uzupełnij: zwróć napis w postaci Miasto("NAZWA", LICZBA).
        pass


n = int(input())
miasta = []
for _ in range(n):
    nazwa, liczba = input().split()
    miasta.append(Miasto(nazwa, int(liczba)))

# Uzupełnij: wypisz listę miast posortowaną według nazwy,
# a potem według liczby mieszkańców.
```

---

## ZAD-07 — Sortowanie listy 0/1/2

**Poziom:** ★★☆
**Tagi:** `sort`, `counting`

### Treść

Wczytaj listę składającą się wyłącznie z liczb `0`, `1` i `2` i posortuj ją rosnąco.

### Wejście

* 1. linia: liczba elementów $N$
* 2. linia: $N$ liczb (każda to `0`, `1` albo `2`) oddzielonych spacjami

### Wyjście

* 1. linia: posortowana lista — liczby oddzielone pojedynczymi spacjami

### Ograniczenia

* $1 \le N \le 1000$

### Przykład

**Wejście:**

```
7
1 0 1 2 2 0 1
```

**Wyjście:**

```
0 0 1 1 1 2 2
```

### Uwagi

* Zadanie da się rozwiązać w czasie $O(N)$, bez sortowania. Najprościej policzyć zera, jedynki i dwójki, a potem wypisać odpowiednio wiele zer, jedynek i dwójek (to sortowanie przez zliczanie z rozdziału 21).
* Ambitniejszy wariant działa w miejscu, w jednym przejściu po liście: trzymaj trzy indeksy — koniec obszaru zer, bieżący element i początek obszaru dwójek — i zamieniaj elementy miejscami (tzw. problem flagi holenderskiej).

---

## ZAD-08 — Indeks klucza w cyklicznie posortowanej liście

**Poziom:** ★★☆
**Tagi:** `binary search`, `rotacja`, `list`

### Treść

Lista liczb całkowitych była posortowana rosnąco, a następnie została **cyklicznie przesunięta** (jej początkowy fragment przeniesiono na koniec), np. `1 2 3 4 5 6` → `3 4 5 6 1 2`. Znajdź indeks (liczony od 0), pod którym w tej liście znajduje się podany klucz. Jeśli klucza nie ma w liście, wypisz `-1`.

### Wejście

* 1. linia: liczba elementów $N$
* 2. linia: $N$ liczb całkowitych oddzielonych spacjami — cyklicznie przesunięta lista rosnąca
* 3. linia: liczba całkowita $x$ — szukany klucz

### Wyjście

* 1. linia: indeks elementu równego $x$ albo `-1`

### Ograniczenia

* $1 \le N \le 1000$
* Wszystkie elementy listy są różne.
* Przesunięcie może wynosić 0 (lista jest wtedy po prostu posortowana).

### Przykład

**Wejście:**

```
6
3 4 5 6 1 2
4
```

**Wyjście:**

```
1
```

### Uwagi

* Zadanie da się rozwiązać w czasie $O(\log N)$ zmodyfikowanym wyszukiwaniem binarnym: po podziale przedziału na pół **co najmniej jedna** z połówek jest posortowana rosnąco — sprawdź, czy klucz mieści się w jej zakresie, i na tej podstawie wybierz połowę do dalszego przeszukiwania.
* To rozwinięcie zwykłego wyszukiwania binarnego — zob. zadanie „Wyszukiwanie binarne” z rozdziału 21.

---

## ZAD-09 — Ranking zawodników

**Poziom:** ★★☆
**Tagi:** `sort`, `key`, `lambda`, `tuple`

### Treść

Wczytaj wyniki zawodów: dla każdego zawodnika jego imię, liczbę zdobytych punktów i czas (w sekundach). Ułóż ranking według następujących zasad:

1. więcej punktów — wyższe miejsce (punkty **malejąco**),
2. przy równej liczbie punktów: krótszy czas — wyższe miejsce (czas **rosnąco**),
3. przy równych punktach i czasie zawodnicy dzielą miejsce, a w rankingu wypisujemy ich alfabetycznie według imienia (imię **rosnąco**).

Zawodnicy, którzy mają te same punkty i ten sam czas, zajmują **to samo miejsce**, a kolejne miejsca są pomijane — tak jak w sporcie: np. `1, 2, 2, 4`. Miejsce zawodnika to $1 +$ liczba zawodników, którzy mają od niego lepszy wynik.

### Wejście

* 1. linia: liczba zawodników $N$
* kolejne $N$ linii: `imię punkty czas` — imię (jedno słowo), punkty i czas (liczby całkowite $\ge 0$), oddzielone spacjami

### Wyjście

$N$ linii w kolejności rankingu, każda w postaci:

```
<miejsce>. <imię> <punkty> <czas>
```

### Ograniczenia

* $1 \le N \le 100$
* Imiona są różne.

### Przykład

**Wejście:**

```
5
Ola 90 300
Adam 95 320
Ewa 90 300
Kuba 90 280
Zosia 70 250
```

**Wyjście:**

```
1. Adam 95 320
2. Kuba 90 280
3. Ewa 90 300
3. Ola 90 300
5. Zosia 70 250
```

Ewa i Ola mają te same punkty i ten sam czas, więc dzielą 3. miejsce (wypisujemy je alfabetycznie), a następna zawodniczka zajmuje miejsce 5.

### Uwagi

* Kilka kryteriów naraz zapiszesz jako **krotkę** zwracaną przez funkcję `key` — Python porównuje krotki element po elemencie: najpierw pierwsze elementy, a przy remisie kolejne.
* Żeby posortować liczby **malejąco** w kluczu, który poza tym sortuje rosnąco, wystarczy je zanegować:
  `sorted(zawodnicy, key=lambda z: (-z[1], z[2], z[0]))` (dla krotek `(imię, punkty, czas)`).
* Po posortowaniu miejsce zawodnika jest równe miejscu poprzednika, jeśli ma on te same punkty i czas, a w przeciwnym razie — jego pozycji w rankingu (licząc od 1).

---

## ZAD-10 — k najczęstszych słów

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
