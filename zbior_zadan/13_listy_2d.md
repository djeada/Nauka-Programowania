# Rozdział 13: Macierze i przedziały

Zadania w tym rozdziale ćwiczą pracę z **listami dwuwymiarowymi** (macierzami): tworzenie, wczytywanie, przechodzenie po wierszach i kolumnach oraz przekształcanie.
**Każde zadanie (oraz każdy podpunkt) jest osobnym, niezależnym programem**: czyta **standardowe wejście** (stdin) i wypisuje wynik na **standardowe wyjście** (stdout).

**Konwencje wspólne:**

* Dane wczytuj dokładnie w kolejności podanej w sekcji **Wejście**.
* Wiersz macierzy na wejściu to jedna linia z liczbami oddzielonymi spacjami — wczytaj całą linię i rozbij ją po spacjach (`input().split()`).
* W wyjściu macierzy: **każdy wiersz w osobnej linii**, elementy oddzielone **pojedynczą spacją**.
* Program nie wypisuje komunikatów typu „Podaj liczbę:”.

---

## ZAD-01 — Macierz z identycznymi wierszami 0..b

**Poziom:** ★☆☆
**Tagi:** `macierze`, `pętle`, `print`

### Treść

Wczytaj liczby `a` i `b`. Utwórz macierz złożoną z `a` identycznych wierszy, w których są kolejne liczby od `0` do `b` włącznie, i wypisz ją.

### Wejście

* 1. linia: `a` — liczba wierszy
* 2. linia: `b` — ostatnia liczba w wierszu

### Wyjście

`a` linii, w każdej liczby `0 1 2 … b` oddzielone spacjami.

### Ograniczenia

* `1 ≤ a ≤ 20`
* `0 ≤ b ≤ 20`

### Przykład

**Wejście:**

```
3
2
```

**Wyjście:**

```
0 1 2
0 1 2
0 1 2
```

---

## ZAD-02 — Macierz n×n: iloczyn indeksów

**Poziom:** ★☆☆
**Tagi:** `macierze`, `pętle zagnieżdżone`

### Treść

Wczytaj `n`. Utwórz macierz `n×n`, w której element w wierszu `i` i kolumnie `j` (indeksy od `0`) ma wartość $i \cdot j$, i wypisz ją.

### Wejście

* 1. linia: `n`

### Wyjście

`n` linii po `n` liczb oddzielonych spacjami.

### Ograniczenia

* `1 ≤ n ≤ 20`

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
0 0 0
0 1 2
0 2 4
```

---

## ZAD-03 — Macierz 2-kolumnowa z dwóch list

**Poziom:** ★☆☆
**Tagi:** `listy`, `macierze`

### Treść

Wczytaj dwie listy liczb całkowitych. Jeśli mają tę samą długość, utwórz macierz o dwóch kolumnach, w której wiersz `i` to `lista1[i] lista2[i]`, i wypisz ją.
Jeśli długości list są różne, wypisz `Pusta macierz`.

### Wejście

* 1. linia: `n` — długość pierwszej listy
* 2. linia: `m` — długość drugiej listy
* następnie `n` linii, w każdej jedna liczba całkowita (pierwsza lista)
* następnie `m` linii, w każdej jedna liczba całkowita (druga lista)

### Wyjście

* Jeśli `n = m`: `n` linii postaci `x y`, gdzie `x` pochodzi z pierwszej listy, a `y` z drugiej.
* Jeśli `n ≠ m`: jedna linia `Pusta macierz`.

### Ograniczenia

* `1 ≤ n, m ≤ 100`

### Przykład

**Wejście:**

```
3
3
3
5
2
2
8
1
```

**Wyjście:**

```
3 2
5 8
2 1
```

---

## ZAD-04 — Dodawanie i odejmowanie macierzy

**Poziom:** ★☆☆
**Tagi:** `macierze`, `arytmetyka`

### Treść

Wczytaj dwie macierze `A` i `B` o wymiarach `n×m`.

a) Wypisz ich sumę $A + B$.

b) Wypisz ich różnicę $A - B$ (pierwsza minus druga).

Element wyniku w wierszu `i` i kolumnie `j` to odpowiednio $A_{ij} + B_{ij}$ oraz $A_{ij} - B_{ij}$.

### Wejście

* 1. linia: `n` — liczba wierszy
* 2. linia: `m` — liczba kolumn
* następnie `n` linii macierzy `A` (po `m` liczb całkowitych)
* następnie `n` linii macierzy `B` (po `m` liczb całkowitych)

### Wyjście

Najpierw `n` linii sumy, zaraz po nich `n` linii różnicy (bez pustej linii i dodatkowych napisów między nimi).

### Ograniczenia

* `1 ≤ n, m ≤ 20`

### Przykład

**Wejście:**

```
2
2
1 2
-2 0
5 -3
1 7
```

**Wyjście:**

```
6 -1
-1 7
-4 5
-3 -7
```

---

## ZAD-05 — Czy macierz jest magiczna?

**Poziom:** ★★☆
**Tagi:** `macierze`, `suma`, `warunki`

### Treść

Wczytaj macierz kwadratową `n×n` z dodatnimi liczbami całkowitymi. Sprawdź, czy jest **kwadratem magicznym**, czyli czy suma każdego wiersza, każdej kolumny oraz obu przekątnych jest taka sama.

### Wejście

* 1. linia: `n`
* następnie `n` linii po `n` liczb oddzielonych spacjami

### Wyjście

Jedno słowo: `Prawda`, jeśli macierz jest kwadratem magicznym, w przeciwnym razie `Fałsz`.

### Ograniczenia

* `1 ≤ n ≤ 10`

### Przykład

**Wejście:**

```
3
6 7 2
1 5 9
8 3 4
```

**Wyjście:**

```
Prawda
```

### Uwagi

* Sprawdzamy wyłącznie sumy — liczby w macierzy **nie muszą** być różne (np. macierz `2×2` z samymi dwójkami jest kwadratem magicznym).
* Pamiętaj o drugiej przekątnej (od prawego górnego do lewego dolnego rogu) — macierz może mieć równe sumy wierszy, kolumn i jednej przekątnej, a mimo to nie być magiczna.
* Macierz `1×1` jest kwadratem magicznym.

---

## ZAD-06 — Scalanie przedziałów

**Poziom:** ★★☆
**Tagi:** `sortowanie`, `przedziały`, `algorytmy`

### Treść

Wczytaj `n` przedziałów domkniętych $[a_i, b_i]$. Scal wszystkie przedziały, które na siebie nachodzą, i wypisz otrzymane rozłączne przedziały w kolejności rosnącej według początku.

### Wejście

* 1. linia: `n`
* następnie `n` linii, w każdej dwie liczby całkowite `a_i b_i` (`a_i ≤ b_i`)

### Wyjście

Każdy scalony przedział w osobnej linii w postaci `a b`, posortowane rosnąco według `a`.

### Ograniczenia

* `1 ≤ n ≤ 1000`
* $-10^6 \le a_i \le b_i \le 10^6$

### Przykład

**Wejście:**

```
7
23 67
23 53
45 88
77 88
10 22
11 12
42 45
```

**Wyjście:**

```
10 22
23 88
```

### Uwagi

* Przedziały na wejściu mogą być podane w dowolnej kolejności — najpierw je posortuj.
* Dwa przedziały (po posortowaniu) nachodzą na siebie, gdy początek następnego jest **mniejszy lub równy** końcowi bieżącego. Przedziały stykające się końcami, np. `1 3` i `3 5`, scalamy w `1 5`, natomiast `10 22` i `23 88` pozostają osobno.

---

## ZAD-07 — Zerowanie macierzy

**Poziom:** ★★☆
**Tagi:** `macierze`, `indeksy`

### Treść

Wczytaj macierz `n×m`. Dla każdego zera w **wejściowej** macierzy wyzeruj cały jego wiersz i całą jego kolumnę. Zera powstałe w trakcie zerowania nie powodują dalszego zerowania.

### Wejście

* 1. linia: `n m` — liczba wierszy i kolumn (w jednej linii)
* następnie `n` linii po `m` liczb całkowitych

### Wyjście

`n` linii zmodyfikowanej macierzy.

### Ograniczenia

* `1 ≤ n, m ≤ 20`

### Przykład

**Wejście:**

```
3 3
1 2 3
4 0 6
7 8 9
```

**Wyjście:**

```
1 0 3
0 0 0
7 0 9
```

### Uwagi

* Najpierw zapamiętaj, które wiersze i kolumny zawierają zero, a dopiero potem zeruj — inaczej wyzerujesz całą macierz.

---

## ZAD-08 — Wypisanie elementów macierzy spiralnie

**Poziom:** ★★☆
**Tagi:** `macierze`, `spirala`

### Treść

Wczytaj macierz `n×m` i wypisz jej elementy spiralnie, zgodnie z ruchem wskazówek zegara: zacznij od lewego górnego rogu, idź w prawo po pierwszym wierszu, potem w dół po ostatniej kolumnie, w lewo po ostatnim wierszu, w górę po pierwszej kolumnie i tak dalej, aż do odczytania wszystkich elementów.

### Wejście

* 1. linia: `n m` — liczba wierszy i kolumn (w jednej linii)
* następnie `n` linii po `m` liczb całkowitych

### Wyjście

Jedna linia: wszystkie elementy w kolejności spiralnej, oddzielone spacjami.

### Ograniczenia

* `1 ≤ n, m ≤ 20`

### Przykład

**Wejście:**

```
3 3
1 2 3
4 5 6
7 8 9
```

**Wyjście:**

```
1 2 3 6 9 8 7 4 5
```

### Uwagi

* Macierz nie musi być kwadratowa — sprawdź swój program także dla jednego wiersza i dla jednej kolumny.

---

## ZAD-09 — Klepsydra o największej sumie

**Poziom:** ★★☆
**Tagi:** `macierze`, `przeszukiwanie`

### Treść

Wczytaj macierz `n×m`. **Klepsydra** to 7 pól wyciętych z dowolnego kwadratu `3×3` macierzy: cały górny wiersz, środkowe pole i cały dolny wiersz.

```
a b c
  d
e f g
```

Suma klepsydry to $a + b + c + d + e + f + g$. Wypisz największą sumę spośród wszystkich klepsydr w macierzy.

### Wejście

* 1. linia: `n m` — liczba wierszy i kolumn (w jednej linii)
* następnie `n` linii po `m` liczb całkowitych (mogą być ujemne)

### Wyjście

Jedna liczba całkowita: największa suma klepsydry.

### Ograniczenia

* `3 ≤ n, m ≤ 20`

### Przykład

**Wejście:**

```
4 4
7 4 2 0
4 8 10 8
3 6 7 6
3 9 19 14
```

**Wyjście:**

```
75
```

Największą sumę ma klepsydra ze środkiem w polu o wartości `7`: $8 + 10 + 8 + 7 + 9 + 19 + 14 = 75$.

### Uwagi

* Gdy wszystkie liczby są ujemne, wynik też jest ujemny — nie zaczynaj szukania maksimum od `0`.

---

## ZAD-10 — Obróć macierz o 90° w prawo

**Poziom:** ★★☆
**Tagi:** `macierze`, `transpozycja`

### Treść

Wczytaj kwadratową macierz `n×n` i wypisz ją po obrocie o 90° zgodnie z ruchem wskazówek zegara.

### Wejście

* 1. linia: `n`
* następnie `n` linii po `n` liczb całkowitych

### Wyjście

`n` linii obróconej macierzy.

### Ograniczenia

* `1 ≤ n ≤ 20`

### Przykład

**Wejście:**

```
3
1 2 3
4 5 6
7 8 9
```

**Wyjście:**

```
7 4 1
8 5 2
9 6 3
```

### Uwagi

* Pierwszy wiersz wyniku to pierwsza kolumna macierzy czytana od dołu do góry. Obrót można też uzyskać, transponując macierz i odwracając każdy jej wiersz.

---

## ZAD-11 — Gra w statki

**Poziom:** ★★★
**Tagi:** `macierze`, `gra`, `pętle`, `symulacja`

### Treść

Wczytaj planszę `10×10` do gry w statki, a potem kolejne strzały gracza i rozstrzygnij każdy z nich.

Na planszy `.` oznacza wodę, a `#` pole statku. Każdy statek to poziomy albo pionowy odcinek złożony z jednego lub kilku pól `#`; statki nie stykają się ze sobą ani bokami, ani rogami.

Strzał to para `r c` — numer wiersza i numer kolumny, **liczone od 1** (lewy górny róg to `1 1`). Dla każdego strzału wypisz jedną linię:

* `Niepoprawny strzał` — linia nie składa się z dokładnie dwóch liczb całkowitych z zakresu od 1 do 10,
* `Pole już ostrzelane` — w to pole już wcześniej strzelano (niezależnie od wyniku tamtego strzału),
* `Pudło` — w polu jest woda,
* `Trafiony` — w polu jest statek, ale ma on jeszcze nietrafione pola,
* `Trafiony, zatopiony` — trafiono ostatnie nietrafione pole statku.

Gdy zatopiony zostanie ostatni statek, wypisz dodatkowo `Wygrana po X strzałach` i zakończ program — pozostałe linie wejścia pomiń. `X` to liczba wczytanych linii ze strzałami aż do tego strzału włącznie (liczą się wszystkie strzały, także niepoprawne i powtórzone).

Jeśli strzały się skończą, zanim wszystkie statki zostaną zatopione, wypisz na końcu `Pozostało statków: Y`, gdzie `Y` to liczba niezatopionych statków.

### Wejście

* 10 linii po 10 znaków `.` lub `#` — plansza
* następnie dowolnie wiele linii (także zero) — strzały `r c`, aż do końca danych

### Wyjście

* Po jednej linii z wynikiem dla każdego rozpatrzonego strzału.
* Na końcu `Wygrana po X strzałach` albo `Pozostało statków: Y`.

### Ograniczenia

* na planszy jest co najmniej jeden statek, a pól `#` jest łącznie co najmniej 2
* co najwyżej 200 strzałów

### Przykład

**Wejście:**

```
#.........
#.........
..........
....###...
..........
..........
.........#
..........
.##.......
..........
1 1
5 5
2 1
1 1
11 3
7 10
```

**Wyjście:**

```
Trafiony
Pudło
Trafiony, zatopiony
Pole już ostrzelane
Niepoprawny strzał
Trafiony, zatopiony
Pozostało statków: 2
```

Na planszy są 4 statki: pionowy w kolumnie 1 (wiersze 1–2), poziomy w wierszu 4 (kolumny 5–7), jednomasztowiec w polu `7 10` i poziomy w wierszu 9 (kolumny 2–3). Zatopiono dwa z nich.

### Uwagi

* Planszę trzymaj jako listę list znaków (`list(input())`) i zaznaczaj na niej strzały, np. `X` — trafione pole statku, `o` — pudło. Wtedy „pole już ostrzelane” to pole z `X` albo `o`.
* Aby sprawdzić zatopienie, od trafionego pola idź w każdą z czterech stron, dopóki trafiasz na pola statku (`#` lub `X`). Statek jest zatopiony, gdy żadne z jego pól nie jest już `#`.
* Liczbę statków na początku policzysz, zliczając pola statków, które nie mają pola statku ani nad sobą, ani po lewej stronie — każdy statek ma dokładnie jedno takie pole.
* Kod startowy wczytuje wszystkie strzały do listy. Gdy dane wejściowe się skończą, `input()` zgłasza błąd `EOFError`; konstrukcja `try` / `except EOFError` przechwytuje go i kończy pętlę.

### Kod startowy

```python
plansza = [list(input()) for _ in range(10)]

strzaly = []
while True:
    try:
        strzaly.append(input())
    except EOFError:  # dane wejściowe się skończyły
        break

# Uzupełnij: rozstrzygnij kolejne strzały z listy strzaly.
```

---

## ZAD-12 — Transpozycja i mnożenie macierzy

**Poziom:** ★★☆
**Tagi:** `macierze`, `pętle zagnieżdżone`, `algebra`

### Treść

Wczytaj macierz `A` o wymiarach `n×m` i macierz `B` o wymiarach `r×p`.

a) Wypisz macierz transponowaną $A^T$ o wymiarach `m×n`: jej wiersz `j` to kolumna `j` macierzy `A`, czyli $A^T_{ji} = A_{ij}$.

b) Wypisz iloczyn $A \cdot B$ o wymiarach `n×p`, w którym $(A \cdot B)_{ij} = \sum_{k} A_{ik} \cdot B_{kj}$ — element w wierszu `i` i kolumnie `j` to suma iloczynów kolejnych elementów wiersza `i` macierzy `A` i kolumny `j` macierzy `B`. Iloczyn istnieje tylko wtedy, gdy liczba kolumn `A` jest równa liczbie wierszy `B` ($m = r$); w przeciwnym razie zamiast iloczynu wypisz `Niezgodne wymiary.`

### Wejście

* 1. linia: `n m` — wymiary macierzy `A`
* następnie `n` linii po `m` liczb całkowitych
* następnie linia `r p` — wymiary macierzy `B`
* następnie `r` linii po `p` liczb całkowitych

### Wyjście

Najpierw `m` linii macierzy $A^T$, zaraz po nich `n` linii iloczynu $A \cdot B$ albo jedna linia `Niezgodne wymiary.` (bez pustych linii między częściami).

### Ograniczenia

* `1 ≤ n, m, r, p ≤ 10`
* elementy macierzy mają wartość bezwzględną nie większą niż 100

### Przykład

**Wejście:**

```
2 3
1 2 3
4 5 6
3 2
7 8
9 10
11 12
```

**Wyjście:**

```
1 4
2 5
3 6
58 64
139 154
```

Na przykład $58 = 1 \cdot 7 + 2 \cdot 9 + 3 \cdot 11$ (pierwszy wiersz `A` i pierwsza kolumna `B`).

### Uwagi

* Mnożenie macierzy wymaga trzech zagnieżdżonych pętli: po wierszach `A`, po kolumnach `B` i po sumowanych elementach.
* Mnożenie macierzy nie jest przemienne — $A \cdot B$ zwykle różni się od $B \cdot A$, a jeden z tych iloczynów może w ogóle nie istnieć.

---

## ZAD-13 — Gra w życie: k pokoleń

**Poziom:** ★★☆
**Tagi:** `macierze`, `symulacja`, `sąsiedzi`

### Treść

**Gra w życie** Conwaya to plansza komórek, z których każda jest żywa (`#`) albo martwa (`.`). Sąsiadami komórki jest 8 komórek stykających się z nią bokiem lub rogiem. W każdym kroku (pokoleniu) wszystkie komórki zmieniają się **jednocześnie** według reguł:

* żywa komórka z 2 lub 3 żywymi sąsiadami przeżywa, w przeciwnym razie umiera,
* martwa komórka z dokładnie 3 żywymi sąsiadami ożywa, w przeciwnym razie pozostaje martwa.

Komórki poza planszą są zawsze martwe. Wczytaj planszę i liczbę `k`, a następnie wypisz stan planszy po `k` krokach.

### Wejście

* 1. linia: `n m k` — liczba wierszy, liczba kolumn i liczba kroków
* następnie `n` linii po `m` znaków `.` lub `#`

### Wyjście

`n` linii po `m` znaków `.` lub `#` — plansza po `k` krokach (bez spacji między znakami).

### Ograniczenia

* `1 ≤ n, m ≤ 20`
* `0 ≤ k ≤ 10`

### Przykład

**Wejście:**

```
5 5 1
.....
..#..
..#..
..#..
.....
```

**Wyjście:**

```
.....
.....
.###.
.....
.....
```

Środkowa komórka ma 2 żywych sąsiadów, więc przeżywa; skrajne komórki pionowej kreski mają po 1 sąsiedzie i umierają, a komórki obok środka mają po 3 żywych sąsiadów i ożywają.

### Uwagi

* W każdym kroku buduj **nową** macierz i wypełniaj ją na podstawie starej. Jeśli zmieniasz komórki w miejscu, kolejne komórki policzą sąsiadów z już zmienionej planszy i wynik będzie błędny.
* Przy liczeniu sąsiadów sprawdzaj, czy indeksy mieszczą się w planszy (pamiętaj, że w Pythonie indeks `-1` oznacza ostatni element, a nie „poza planszą”).
* Dla `k = 0` wypisz planszę bez zmian.

---

## ZAD-14 — Znajdź błąd: wspólne wiersze

**Poziom:** ★★☆
**Tagi:** `macierze`, `debugowanie`, `listy`

### Treść

Program z sekcji **Kod startowy** miał tworzyć planszę `n×m` wypełnioną zerami, a następnie wpisywać `1` w `k` pól podanych na wejściu. Niestety wypisuje zły wynik. Dla przykładu poniżej zamiast oczekiwanej planszy wypisuje:

```
1 1 0
1 1 0
1 1 0
```

Znajdź błąd i popraw program tak, aby działał zgodnie z opisem.

### Wejście

* 1. linia: `n m` — liczba wierszy i kolumn
* 2. linia: `k` — liczba pól do zaznaczenia
* następnie `k` linii: `r c` — numer wiersza i kolumny pola, **liczone od 0**

### Wyjście

`n` linii po `m` liczb `0` lub `1` oddzielonych spacjami — plansza po zaznaczeniu pól.

### Ograniczenia

* `1 ≤ n, m ≤ 10`
* `0 ≤ k ≤ 20`; to samo pole może zostać podane kilka razy

### Przykład

**Wejście:**

```
3 3
2
0 0
2 1
```

**Wyjście:**

```
1 0 0
0 0 0
0 1 0
```

### Uwagi

* Uruchom program i sprawdź, które pola zmieniają się po zaznaczeniu tylko jednego pola. Przyjrzyj się linii, która tworzy planszę.
* Pomocne może być wypisanie `plansza[0] is plansza[1]` — operator `is` sprawdza, czy dwie nazwy wskazują na **ten sam** obiekt w pamięci.

### Kod startowy

```python
n, m = [int(x) for x in input().split()]
k = int(input())

plansza = [[0] * m] * n

for _ in range(k):
    r, c = [int(x) for x in input().split()]
    plansza[r][c] = 1

for wiersz in plansza:
    print(" ".join(str(x) for x in wiersz))
```
