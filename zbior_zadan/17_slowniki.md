# Rozdział 17: Słowniki

Zadania w tym rozdziale ćwiczą pracę ze **słownikami** (`dict`): tworzenie, dodawanie i usuwanie par, zliczanie wystąpień oraz grupowanie danych według klucza.
**Każde zadanie (oraz każdy podpunkt) jest osobnym, niezależnym programem**: czyta **standardowe wejście** (stdin) i wypisuje wynik na **standardowe wyjście** (stdout).

**Konwencje wspólne:**

* Dane wczytuj dokładnie w kolejności podanej w sekcji **Wejście**; jeśli w jednej linii jest kilka wartości — rozbij ją po spacjach.
* Jeśli wynikiem jest słownik, wypisz go tak, jak robi to `print(slownik)` w Pythonie: `{klucz: wartość, klucz: wartość}` — pary oddzielone przecinkiem i spacją, po dwukropku spacja, klucze i wartości napisowe w apostrofach (np. `{'ala': 2, 'ma': 1}`), liczby bez apostrofów (np. `{1: 1, 2: 4}`), pusty słownik to `{}`.
* Kolejność par w wypisanym słowniku to kolejność, w jakiej klucze były do niego **dodawane** (tak zachowuje się słownik w Pythonie).
* Program nie wypisuje komunikatów typu „Podaj liczbę:”.

---

## ZAD-01 — Słownik: liczby i ich kwadraty

**Poziom:** ★☆☆
**Tagi:** `dict`, `pętla`

### Treść

Wczytaj liczbę `n`. Utwórz słownik, w którym kluczami są liczby od `1` do `n - 1`, a wartościami ich kwadraty, i wypisz go.

### Wejście

* 1. linia: `n`

### Wyjście

Słownik w postaci `{1: 1, 2: 4, …}` (klucze rosnąco). Dla `n = 1` słownik jest pusty: `{}`.

### Ograniczenia

* `1 ≤ n ≤ 30`

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

Wczytaj dwie listy liczb całkowitych. Jeśli mają tę samą długość, utwórz słownik, w którym `i`-ty element pierwszej listy jest kluczem, a `i`-ty element drugiej listy — jego wartością. Jeśli długości są różne, wynikiem jest pusty słownik.

### Wejście

* 1. linia: `n` — długość pierwszej listy
* 2. linia: `m` — długość drugiej listy
* 3. linia: `n` liczb całkowitych oddzielonych spacjami (klucze)
* 4. linia: `m` liczb całkowitych oddzielonych spacjami (wartości)

### Wyjście

Słownik w postaci `{klucz: wartość, …}` z kluczami w kolejności z wejścia albo `{}`, gdy `n ≠ m`.

### Ograniczenia

* `1 ≤ n, m ≤ 20`

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

### Uwagi

* Jeśli klucz powtarza się w pierwszej liście, obowiązuje jego **ostatnia** wartość, a klucz zostaje na miejscu swojego pierwszego wystąpienia — tak działa kolejne przypisanie `slownik[klucz] = wartość`. Na przykład klucze `1 2 1` i wartości `5 6 7` dają `{1: 7, 2: 6}`.

---

## ZAD-03 — Biblioteka: baza wypożyczeń

**Poziom:** ★☆☆
**Tagi:** `dict`, `list`, `pętle`, `string`

### Treść

Prowadź bazę wypożyczeń biblioteki jako słownik `imię → lista wypożyczonych tytułów`. Wczytuj komendy (każda w osobnej linii), aż do komendy `koniec`:

* `dodaj IMIĘ TYTUŁ` — czytelnik `IMIĘ` wypożycza książkę `TYTUŁ` (dopisz ją na koniec jego listy),
* `zwróć IMIĘ TYTUŁ` — czytelnik oddaje książkę (usuń ją z jego listy; jeśli jej tam nie ma, nic się nie dzieje),
* `lista IMIĘ` — wypisz książki wypożyczone przez czytelnika.

Po komendzie `lista IMIĘ` wypisz jedną linię:

* `Książki wypożyczone przez IMIĘ: t1, t2, …` — tytuły w kolejności wypożyczenia, oddzielone przecinkiem i spacją,
* `Książki wypożyczone przez IMIĘ: brak` — jeśli czytelnik nie ma żadnej książki albo nie występuje w bazie.

### Wejście

Kolejne linie z komendami; ostatnia linia to `koniec`.

* `IMIĘ` to jedno słowo (bez spacji).
* `TYTUŁ` to cała reszta linii po imieniu — może zawierać spacje (bez cudzysłowów).

### Wyjście

Po jednej linii dla każdej komendy `lista`; pozostałe komendy niczego nie wypisują.

### Ograniczenia

* co najwyżej 100 komend

### Przykład

**Wejście:**

```
dodaj Jan Hobbit
dodaj Anna Duma i uprzedzenie
dodaj Jan Władca Pierścieni
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

### Uwagi

* Linię komendy rozbij na co najwyżej trzy części: `linia.split(maxsplit=2)`.
* Czytelnik może wypożyczyć kilka egzemplarzy tego samego tytułu — wtedy tytuł występuje na liście kilka razy, a `zwróć` usuwa tylko jeden egzemplarz (pierwsze wystąpienie).

---

## ZAD-04 — Usuń pary ze słownika na podstawie wartości

**Poziom:** ★☆☆
**Tagi:** `dict`, `filtrowanie`

### Treść

Wczytaj słownik złożony z `n` par (klucz — słowo, wartość — liczba całkowita) oraz liczbę `k`. Usuń ze słownika wszystkie pary, których wartość jest równa `k`, i wypisz wynikowy słownik.

### Wejście

* 1. linia: `n`
* następnie `n` linii: `klucz wartość` (klucze są różne i składają się z małych liter)
* ostatnia linia: `k`

### Wyjście

Słownik po usunięciu par, w postaci `{'klucz': wartość, …}`, z parami w kolejności z wejścia; jeśli usunięto wszystkie pary — `{}`.

### Ograniczenia

* `1 ≤ n ≤ 50`

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

### Uwagi

* Nie usuwaj elementów ze słownika, po którym właśnie iterujesz — przejdź po kopii kluczy (`list(slownik)`) albo zbuduj nowy słownik.

---

## ZAD-05 — Pracownik z największym sumarycznym zyskiem

**Poziom:** ★☆☆
**Tagi:** `dict`, `sumowanie`

### Treść

Wczytaj `n` wpisów postaci `pracownik zysk`. Ten sam pracownik może mieć wiele wpisów. Zsumuj zyski każdego pracownika i wypisz pracownika z największą sumą.

### Wejście

* 1. linia: `n`
* następnie `n` linii: `imie_i_nazwisko zysk` — identyfikator pracownika bez spacji (np. `Jon_Snow`) i liczba całkowita (może być ujemna — strata)

### Wyjście

Jedna linia: identyfikator pracownika z największym sumarycznym zyskiem.

### Ograniczenia

* `1 ≤ n ≤ 100`

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

Barnaba_Barabash ma łącznie $120 + 200 = 320$, czyli więcej niż Kira_Summer (300).

### Uwagi

* Przy remisie wypisz tego pracownika, który **wcześniej pojawił się na wejściu** (jego pierwszy wpis jest wcześniej).

---

## ZAD-06 — Histogram znaków w słowie

**Poziom:** ★☆☆
**Tagi:** `dict`, `string`

### Treść

Wczytaj napis. Utwórz słownik, w którym kluczami są znaki napisu, a wartościami liczby ich wystąpień, i wypisz go.

### Wejście

* 1. linia: napis

### Wyjście

Słownik w postaci `{'znak': liczba, …}` — znaki w kolejności pierwszego wystąpienia w napisie.

### Ograniczenia

* napis ma od 1 do 100 znaków, nie zaczyna się ani nie kończy spacją i nie zawiera apostrofów, cudzysłowów ani znaku `\`

### Przykład

**Wejście:**

```
klasa
```

**Wyjście:**

```
{'k': 1, 'l': 1, 'a': 2, 's': 1}
```

### Uwagi

* Liczą się wszystkie znaki, także spacje (klucz `' '`) i cyfry.
* Wielkość liter ma znaczenie: `a` i `A` to różne znaki.

---

## ZAD-07 — Histogram słów w tekście (ignoruj wielkość liter)

**Poziom:** ★☆☆
**Tagi:** `dict`, `string`, `tekst`

### Treść

Wczytaj tekst. Policz, ile razy występuje w nim każde słowo, nie rozróżniając wielkości liter. Wypisz słownik: słowo (małymi literami) → liczba wystąpień.

### Wejście

* 1. linia: tekst

### Wyjście

Słownik w postaci `{'słowo': liczba, …}` — słowa zapisane małymi literami, w kolejności pierwszego wystąpienia w tekście. Jeśli w tekście nie ma żadnego słowa — `{}`.

### Ograniczenia

* tekst ma od 1 do 300 znaków

### Przykład

**Wejście:**

```
Ala ma kota. Ala lubi koty.
```

**Wyjście:**

```
{'ala': 2, 'ma': 1, 'kota': 1, 'lubi': 1, 'koty': 1}
```

### Uwagi

* **Słowo** to najdłuższy ciąg kolejnych liter (także polskich, np. `ż`, `ó`). Wszystkie inne znaki — spacje, cyfry, znaki interpunkcyjne — rozdzielają słowa.
* `Kot`, `KOT` i `kot` to to samo słowo `kot`.

---

## ZAD-08 — Najczęstsza litera w zdaniu

**Poziom:** ★☆☆
**Tagi:** `dict`, `string`

### Treść

Wczytaj zdanie. Policz wystąpienia liter, pomijając spacje, cyfry i znaki interpunkcyjne oraz nie rozróżniając wielkości liter. Wypisz literę, która występuje najczęściej.
Jeśli kilka liter występuje tyle samo razy, wybierz tę, która **pojawia się w zdaniu jako pierwsza**.

### Wejście

* 1. linia: zdanie (zawiera co najmniej jedną literę)

### Wyjście

Jedna linia: najczęstsza litera, zapisana jako mała litera.

### Ograniczenia

* zdanie ma od 1 do 300 znaków

### Przykład

**Wejście:**

```
lezy jerzy na wiezy
```

**Wyjście:**

```
e
```

Litery `e`, `z` i `y` występują po 3 razy; najwcześniej w zdaniu pojawia się `e`.

### Uwagi

* `A` i `a` to ta sama litera — w zdaniu `Ala ma Asa` litera `a` występuje 5 razy.
* Zliczanie można powierzyć klasie `Counter` z modułu `collections` (`from collections import Counter`). `Counter` to słownik element → liczba wystąpień, np. `Counter("abca")` daje `Counter({'a': 2, 'b': 1, 'c': 1})`, a metoda `most_common(1)` zwraca listę z jedną parą `(element, liczba)` o największej liczbie wystąpień: `Counter("abca").most_common(1)` to `[('a', 2)]`.
* Przy remisie `most_common` zachowuje kolejność pierwszego wystąpienia, więc spełnia regułę z treści: `Counter("baab").most_common(1)` to `[('b', 2)]`.

---

## ZAD-09 — Znaki występujące co najmniej dwa razy

**Poziom:** ★☆☆
**Tagi:** `dict`, `string`

### Treść

Wczytaj napis. Wypisz napis złożony z tych znaków, które występują w nim **co najmniej 2 razy** — każdy taki znak tylko raz, w kolejności pierwszego wystąpienia w napisie.

### Wejście

* 1. linia: napis bez spacji

### Wyjście

Jedna linia: wynikowy napis. Jeśli żaden znak się nie powtarza — pusta linia (albo brak wyjścia).

### Ograniczenia

* napis ma od 1 do 100 znaków

### Przykład

**Wejście:**

```
aaabbbccc
```

**Wyjście:**

```
abc
```

### Uwagi

* Wielkość liter ma znaczenie: `A` i `a` to różne znaki.
* Policz wystąpienia znaków w słowniku — kolejność kluczy w słowniku to kolejność pierwszego wystąpienia.

---

## ZAD-10 — Znalezienie anagramów w tekście (grupy)

**Poziom:** ★★☆
**Tagi:** `dict`, `anagramy`, `string`

### Treść

Wczytaj tekst. Znajdź grupy różnych słów, które są swoimi **anagramami** (składają się z tych samych liter w tej samej liczbie, np. `absurd` i `brudas`), nie rozróżniając wielkości liter. Wypisz każdą grupę, która zawiera co najmniej dwa różne słowa.

### Wejście

* 1. linia: tekst

### Wyjście

* Każda grupa w osobnej linii: słowa małymi literami, oddzielone pojedynczą spacją, w kolejności pierwszego wystąpienia w tekście.
* Grupy w kolejności pierwszego wystąpienia ich pierwszego słowa.
* Jeśli nie ma żadnej grupy — jedna linia `Brak anagramów`.

### Ograniczenia

* tekst ma od 1 do 300 znaków

### Przykład

**Wejście:**

```
Tyran Brudas kupił narty. To absurd! Arbuz i burza.
```

**Wyjście:**

```
tyran narty
brudas absurd
arbuz burza
```

### Uwagi

* **Słowo** to najdłuższy ciąg kolejnych liter; pozostałe znaki rozdzielają słowa. Wielkość liter nie ma znaczenia (`Tyran` to `tyran`).
* Słowo powtórzone w tekście liczy się raz — `kot kot` nie jest grupą anagramów.
* Wskazówka: użyj słownika, w którym kluczem są posortowane litery słowa (`"".join(sorted(slowo))`), a wartością lista słów.

---

## ZAD-11 — Sortowanie „słownika” po kluczach i po wartościach

**Poziom:** ★☆☆
**Tagi:** `sort`, `dict`

### Treść

Wczytaj `n` par `klucz wartość` do słownika.

a) Wypisz pary posortowane rosnąco według kluczy.

b) Wypisz pary posortowane rosnąco według wartości; pary o równych wartościach uporządkuj rosnąco według kluczy.

### Wejście

* 1. linia: `n`
* następnie `n` linii: `klucz wartość` — klucz to słowo z małych liter (klucze są różne), wartość to liczba całkowita

### Wyjście

* 1. linia: pary dla a)
* 2. linia: pary dla b)

Każdą parę wypisz jako `klucz:wartość` (bez spacji wokół dwukropka), a pary oddziel pojedynczą spacją.

### Ograniczenia

* `1 ≤ n ≤ 50`

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
a:-2 b:4 c:3 x:5
a:-2 c:3 b:4 x:5
```

### Uwagi

* Klucze porównujemy jak napisy (alfabetycznie), np. `ab` jest przed `b`.
* `sorted(slownik.items())` sortuje pary według kluczy — pary (krotki) porównywane są najpierw po pierwszym elemencie.
* Aby sortować według czegoś innego, przekaż w parametrze `key` **nazwę funkcji** (bez nawiasów). `sorted` wywoła tę funkcję dla każdego elementu i ułoży elementy rosnąco według zwróconych wartości:

  ```python
  def dlugosc_napisu(napis):
      return len(napis)

  print(sorted(["kot", "żyrafa", "pies"], key=dlugosc_napisu))  # ['kot', 'pies', 'żyrafa']
  ```

* Funkcja klucza może zwracać krotkę. Krotki porównywane są element po elemencie, więc dla pary `(klucz, wartość)` zwrócenie `(wartość, klucz)` sortuje po wartości, a przy równych wartościach — po kluczu.

### Kod startowy

```python
def wartosc_potem_klucz(para):
    # para to krotka (klucz, wartość) — zwróć to, według czego sortować
    pass


def wypisz_pary(pary):
    print(" ".join(f"{klucz}:{wartosc}" for klucz, wartosc in pary))


n = int(input())
slownik = {}
for _ in range(n):
    klucz, wartosc = input().split()
    slownik[klucz] = int(wartosc)

po_kluczach = []  # TODO: posortuj pary według kluczy
po_wartosciach = []  # TODO: posortuj pary, używając key=wartosc_potem_klucz

wypisz_pary(po_kluczach)
wypisz_pary(po_wartosciach)
```

---

## ZAD-12 — Porównanie dwóch słowników z listami (kolejność list bez znaczenia)

**Poziom:** ★★☆
**Tagi:** `dict`, `porównanie`, `list`

### Treść

Wczytaj dwa słowniki, w których kluczami są słowa, a wartościami listy liczb całkowitych. Sprawdź, czy słowniki są identyczne, przy czym **kolejność liczb w listach nie ma znaczenia**: oba słowniki muszą mieć ten sam zbiór kluczy, a pod każdym kluczem te same liczby, występujące tyle samo razy.

### Wejście

* 1. linia: `n` — liczba kluczy pierwszego słownika
* następnie `n` linii: `klucz v1 v2 v3 …` (co najmniej jedna liczba)
* następnie linia z `m` — liczbą kluczy drugiego słownika
* następnie `m` linii: `klucz v1 v2 v3 …`

W obrębie jednego słownika klucze są różne.

### Wyjście

Jedno słowo: `Prawda`, jeśli słowniki są identyczne, w przeciwnym razie `Fałsz`.

### Ograniczenia

* `1 ≤ n, m ≤ 20`
* każda lista ma od 1 do 20 liczb

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

### Przykład 2

**Wejście:**

```
1
a 1 2
1
a 2 1 1
```

**Wyjście:**

```
Fałsz
```

Lista `2 1 1` zawiera liczbę `1` dwa razy, a lista `1 2` — tylko raz.

### Uwagi

* Kolejność kluczy na wejściu też nie ma znaczenia.
* Porównanie zbiorów (`set`) nie wystarczy, bo gubi powtórzenia — porównaj posortowane listy.

---

## ZAD-13 — Odwrócenie słownika

**Poziom:** ★☆☆
**Tagi:** `dict`, `setdefault`, `wyrażenie słownikowe`

### Treść

Wczytaj `n` par `osoba miasto` — słownik, który każdej osobie przypisuje miasto, w którym mieszka. „Odwróć” go: zbuduj słownik `miasto → lista osób` mieszkających w tym mieście.

Wypisz:

1. dla każdego miasta (w kolejności alfabetycznej) linię `miasto: osoba1, osoba2, …` z osobami posortowanymi alfabetycznie,
2. w ostatniej linii słownik `{miasto: liczba osób}` z miastami w kolejności alfabetycznej, zbudowany **wyrażeniem słownikowym** i wypisany przez `print(slownik)`.

### Wejście

* 1. linia: `n`
* następnie `n` linii: `osoba miasto` — dwa słowa oddzielone spacją

### Wyjście

* Po jednej linii dla każdego miasta: nazwa miasta, dwukropek, spacja i osoby oddzielone przecinkiem ze spacją.
* Ostatnia linia: słownik w postaci `{'Miasto': liczba, …}`.

### Ograniczenia

* `1 ≤ n ≤ 50`
* osoby są różne; imiona i nazwy miast składają się z liter alfabetu łacińskiego bez polskich znaków i zaczynają się wielką literą

### Przykład

**Wejście:**

```
5
Anna Warszawa
Jan Lublin
Ewa Warszawa
Adam Gdynia
Bartek Lublin
```

**Wyjście:**

```
Gdynia: Adam
Lublin: Bartek, Jan
Warszawa: Anna, Ewa
{'Gdynia': 1, 'Lublin': 2, 'Warszawa': 2}
```

### Uwagi

* `slownik.setdefault(klucz, domyslna)` zwraca wartość dla klucza, a jeśli klucza jeszcze nie ma — najpierw wstawia `domyslna` i zwraca ją. Dzięki temu dopisanie osoby do listy miasta to jedna linia:

  ```python
  miasta = {}
  miasta.setdefault("Lublin", []).append("Jan")
  miasta.setdefault("Lublin", []).append("Bartek")
  print(miasta)  # {'Lublin': ['Jan', 'Bartek']}
  ```

* **Wyrażenie słownikowe** (*dict comprehension*) buduje słownik w jednej linii, podobnie jak wyrażenie listowe buduje listę: `{x: x * x for x in range(1, 4)}` daje `{1: 1, 2: 4, 3: 9}`.
* `sorted(slownik)` zwraca posortowaną listę kluczy słownika.

---

## ZAD-14 — Para o danej sumie — szybko

**Poziom:** ★★☆
**Tagi:** `dict`, `2-sum`, `złożoność`

### Treść

Wczytaj listę `n` liczb całkowitych oraz liczbę `x`. Znajdź indeksy `i`, `j` (gdzie $i < j$) takie, że `lista[i] + lista[j] == x`.

Jeśli takich par jest kilka, wybierz tę o najmniejszym `i`, a przy równym `i` — o najmniejszym `j`. Jeśli nie ma żadnej — wypisz `-1 -1`.

To samo zadanie rozwiązywaliśmy w rozdziale o listach (ZAD-16), ale tym razem lista może mieć nawet $2 \cdot 10^5$ elementów, więc sprawdzanie wszystkich par dwiema pętlami (około $2 \cdot 10^{10}$ porównań) jest zbyt wolne. Użyj słownika, który pozwala w jednym kroku sprawdzić, czy i gdzie w liście wystąpiła potrzebna wartość.

### Wejście

* 1. linia: liczba elementów `n`
* 2. linia: `n` liczb całkowitych oddzielonych spacjami
* 3. linia: liczba całkowita `x`

### Wyjście

Jedna linia: dwie liczby `i j` oddzielone spacją albo `-1 -1`.

### Ograniczenia

* $2 \le n \le 2 \cdot 10^5$
* $-10^9 \le$ `lista[i]`, `x` $\le 10^9$

### Przykład

**Wejście:**

```
4
3 1 4 2
5
```

**Wyjście:**

```
0 3
```

Sumę $5$ dają pary indeksów $(0, 3)$: $3 + 2$ oraz $(1, 2)$: $1 + 4$. Para $(1, 2)$ kończy się wcześniej, ale wybieramy $(0, 3)$, bo ma mniejsze `i`.

### Uwagi

* Para składa się z dwóch **różnych** pozycji w liście — elementu nie można dodać do samego siebie, ale dwie równe liczby na różnych pozycjach już tak.
* Wskazówka: przechodź po liście indeksem `j` i trzymaj słownik `wartość → indeks jej pierwszego wystąpienia` dla elementów przed `j`. Wtedy najmniejsze `i` do pary z `j` to `slownik[x - lista[j]]` (o ile taki klucz istnieje). Spośród znalezionych par zapamiętaj tę o najmniejszym `i`.
* Uważaj: pierwsza znaleziona w ten sposób para ma najmniejsze `j`, a niekoniecznie najmniejsze `i` (patrz przykład).

---

## ZAD-15 — Robot na siatce

**Poziom:** ★★☆
**Tagi:** `dict`, `krotki`, `zbiory`

### Treść

Robot stoi na polu $(0, 0)$ nieskończonej kratkowanej płaszczyzny i wykonuje ciąg ruchów:

* `N` — o jedno pole na północ: $y$ rośnie o 1,
* `S` — na południe: $y$ maleje o 1,
* `E` — na wschód: $x$ rośnie o 1,
* `W` — na zachód: $x$ maleje o 1.

Pole startowe liczy się jako odwiedzone raz, a każdy ruch to jedno odwiedzenie pola, na które robot wchodzi. Wypisz:

1. liczbę różnych odwiedzonych pól (razem z polem startowym),
2. najczęściej odwiedzane pole i liczbę jego odwiedzin; przy remisie — to z nich, które robot odwiedził po raz pierwszy najwcześniej,
3. `Tak`, jeśli po wykonaniu wszystkich ruchów robot stoi na polu startowym, w przeciwnym razie `Nie`.

### Wejście

* 1. linia: ciąg ruchów złożony z liter `N`, `S`, `E`, `W` (bez spacji)

### Wyjście

* 1. linia: liczba różnych odwiedzonych pól
* 2. linia: `x y k` — współrzędne najczęściej odwiedzanego pola i liczba jego odwiedzin
* 3. linia: `Tak` albo `Nie`

### Ograniczenia

* ciąg ma od 1 do 1000 ruchów

### Przykład

**Wejście:**

```
NESW
```

**Wyjście:**

```
4
0 0 2
Tak
```

Robot odwiedza kolejno pola $(0, 0)$, $(0, 1)$, $(1, 1)$, $(1, 0)$ i znowu $(0, 0)$ — to pole odwiedził dwa razy.

### Uwagi

* Pozycję trzymaj jako krotkę `(x, y)`. Krotki — w przeciwieństwie do list — mogą być kluczami słownika i elementami zbioru, np. `odwiedziny[(0, 0)] = 1`.
* Krotkę łatwo „rozpakować” do zmiennych: `x, y = pozycja`. Przesunięcia też można trzymać w słowniku: `RUCHY = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}`, a potem `dx, dy = RUCHY[ruch]`.
* Liczba różnych pól to liczba kluczy słownika odwiedzin — albo rozmiar zbioru (`set`) odwiedzonych pozycji.
* Kolejność kluczy w słowniku to kolejność pierwszego wstawienia, co ułatwia rozstrzygnięcie remisu.
