# Rozdział 23: Wyrażenia regularne

Poniższe zadania polegają na wczytywaniu danych ze **standardowego wejścia** (stdin) i wypisywaniu wyniku na **standardowe wyjście** (stdout). Rozwiązuj je za pomocą wyrażeń regularnych (moduł `re`).
**Każde zadanie jest osobnym, niezależnym programem.**

**Konwencje wspólne:**

* Każda wartość wejściowa znajduje się w osobnej linii — wczytuj je dokładnie w podanej kolejności.
* Tekst wielowierszowy jest poprzedzony linią z liczbą jego wierszy `n` — wczytaj go, wywołując `input()` `n` razy.
* Dla wartości logicznych wypisuj dokładnie `Prawda` lub `Fałsz`.
* Wielkość liter ma znaczenie, chyba że zadanie mówi inaczej.
* **Słowo** to najdłuższy ciąg znaków dopasowywanych przez `\w`, czyli liter (także polskich), cyfr i znaku podkreślenia `_`. Każdy inny znak — spacja, interpunkcja, myślnik — rozdziela słowa, np. `biało-czerwona` to dwa słowa: `biało` i `czerwona`. Granicę słowa w wyrażeniu regularnym oznacza `\b`.
* Program nie wypisuje komunikatów typu „Podaj tekst:”. Tekst podany w `input("…")` jest ignorowany przez sprawdzarkę.

---

## ZAD-01 — Sprawdź poprawność adresu e-mail

**Poziom:** ★★☆
**Tagi:** `regex`, `string`, `walidacja`

### Treść

Wczytaj napis i sprawdź, czy jest poprawnym adresem e-mail według poniższych (uproszczonych) reguł.

* Adres ma postać `identyfikator@domena`: zawiera **dokładnie jeden** znak `@`, a identyfikator i domena są niepuste.
* **Identyfikator** składa się wyłącznie z:
  * liter `a–z` i `A–Z` (bez polskich znaków),
  * cyfr `0–9`,
  * znaków specjalnych `!` `#` `$` `%` `&` `'` `*` `+` `-` `/` `=` `?` `^` `_` `` ` `` `{` `|` `}` `~`,
  * kropek `.` — ale kropka nie może być pierwszym ani ostatnim znakiem identyfikatora i nie mogą stać dwie kropki obok siebie.
* **Domena** składa się wyłącznie z liter `a–z` i `A–Z`, cyfr `0–9`, kropek `.` i myślników `-`, przy czym:
  * zawiera co najmniej jedną kropkę,
  * nie zaczyna się ani nie kończy kropką ani myślnikiem,
  * żadne dwa znaki spośród `.` i `-` nie stoją obok siebie (niedozwolone są np. `..`, `--`, `.-`, `-.`).
* Żadne inne znaki (np. spacje) nie mogą wystąpić w adresie.

### Wejście

* 1. linia: napis do sprawdzenia

### Wyjście

* `Prawda` — jeśli napis jest poprawnym adresem e-mail,
* `Fałsz` — w przeciwnym razie.

### Przykład

**Wejście:**

```
adam@gmail.com
```

**Wyjście:**

```
Prawda
```

### Przykład 2

**Wejście:**

```
jan..nowak@poczta.pl
```

**Wyjście:**

```
Fałsz
```

W identyfikatorze stoją obok siebie dwie kropki.

### Uwagi

* Do sprawdzenia, czy **cały** napis pasuje do wzorca, służy `re.fullmatch(wzorzec, napis)`.
* Fragment „ciąg znaków bez kropek, a potem dowolnie wiele razy: kropka i znowu ciąg znaków” zapiszesz jako `X+(\.X+)*`, gdzie `X` to klasa dozwolonych znaków.
* W klasie znaków `[...]` myślnik umieść na końcu albo poprzedź go `\`, inaczej oznacza zakres (np. `+-/` to zakres od `+` do `/`).

---

## ZAD-02 — Sprawdź poprawność hasła

**Poziom:** ★★☆
**Tagi:** `regex`, `string`, `walidacja`

### Treść

Wczytaj hasło i sprawdź, czy spełnia **wszystkie** warunki:

1. ma od 8 do 20 znaków (włącznie),
2. zawiera co najmniej jedną małą literę `a–z`,
3. zawiera co najmniej jedną wielką literę `A–Z`,
4. zawiera co najmniej jedną cyfrę `0–9`,
5. zawiera co najmniej jeden znak specjalny spośród:
   `!` `#` `$` `%` `&` `'` `*` `+` `-` `/` `=` `?` `^` `_` `` ` `` `{` `|` `}` `~`.

Hasło może zawierać także inne znaki (np. spację, `@` albo `ą`). Są one dozwolone, ale nie liczą się do warunków 2–5: `ą` nie jest literą z zakresu `a–z`, a `@` nie należy do listy znaków specjalnych.

### Wejście

* 1. linia: hasło

### Wyjście

* `Prawda` — jeśli hasło spełnia wszystkie warunki,
* `Fałsz` — w przeciwnym razie.

### Przykład

**Wejście:**

```
abc1234
```

**Wyjście:**

```
Fałsz
```

Hasło jest za krótkie, nie ma wielkiej litery ani znaku specjalnego.

### Przykład 2

**Wejście:**

```
Tajne_Haslo7
```

**Wyjście:**

```
Prawda
```

### Uwagi

* Każdy z warunków 2–5 sprawdzisz osobnym `re.search()`, np. `re.search(r"[a-z]", haslo)`.

---

## ZAD-03 — Sprawdź, czy napis składa się wyłącznie z cyfr

**Poziom:** ★☆☆
**Tagi:** `regex`, `string`

### Treść

Wczytaj napis i sprawdź, czy składa się **wyłącznie** z cyfr `0–9`. Każdy inny znak — spacja, minus, kropka, litera — sprawia, że odpowiedź to `Fałsz`.

### Wejście

* 1. linia: napis

### Wyjście

* `Prawda` — jeśli napis zawiera tylko cyfry `0–9`,
* `Fałsz` — w przeciwnym razie.

### Ograniczenia

* Napis ma od 1 do 100 znaków.

### Przykład

**Wejście:**

```
1234
```

**Wyjście:**

```
Prawda
```

### Przykład 2

**Wejście:**

```
12a
```

**Wyjście:**

```
Fałsz
```

### Uwagi

* Użyj `re.fullmatch()` — `re.match()` sprawdza tylko początek napisu.
* W Pythonie `\d` dopasowuje także cyfry innych pism, np. arabskie `٣` albo cyfry pełnej szerokości `３`. Aby dopuścić tylko `0–9`, użyj klasy `[0-9]` (albo flagi `re.ASCII`).

---

## ZAD-04 — Sprawdź, czy słowo występuje w zdaniu jako osobne słowo

**Poziom:** ★☆☆
**Tagi:** `regex`, `string`

### Treść

Wczytaj zdanie i słowo. Sprawdź, czy słowo występuje w zdaniu jako **całe słowo**, a nie tylko jako fragment innego słowa. Wielkość liter ma znaczenie.

Słowa rozumiemy jak w konwencjach rozdziału, więc np. w zdaniu `flaga biało-czerwona` występuje słowo `czerwona`, ale nie występuje słowo `flag`.

### Wejście

* 1. linia: zdanie
* 2. linia: słowo (tylko litery i cyfry)

### Wyjście

* `Prawda` — jeśli słowo występuje w zdaniu jako całe słowo,
* `Fałsz` — w przeciwnym razie.

### Przykład

**Wejście:**

```
Siała baba mak.
mak
```

**Wyjście:**

```
Prawda
```

### Przykład 2

**Wejście:**

```
Siała baba mak.
bab
```

**Wyjście:**

```
Fałsz
```

`bab` jest tylko fragmentem słowa `baba`.

### Uwagi

* Otocz słowo granicami `\b`: `re.search(r"\b" + re.escape(slowo) + r"\b", zdanie)`.

---

## ZAD-05 — Wyodrębnij cyfry z tekstu

**Poziom:** ★☆☆
**Tagi:** `regex`, `string`

### Treść

Wczytaj tekst i wypisz wszystkie występujące w nim cyfry `0–9` sklejone w jeden napis, w kolejności występowania. Pozostałe znaki (także kropki i minusy w liczbach) pomiń.

### Wejście

* 1. linia: tekst

### Wyjście

* Jedna linia: cyfry z tekstu (z zachowaniem kolejności i zer na początku),
* `Brak cyfr.` — jeśli w tekście nie ma żadnej cyfry.

### Przykład

**Wejście:**

```
Terminator2001
```

**Wyjście:**

```
2001
```

### Uwagi

* Przydadzą się `re.findall(r"[0-9]", tekst)` albo `re.sub(r"[^0-9]", "", tekst)`.

---

## ZAD-06 — Wiersze kończące się określonym napisem

**Poziom:** ★☆☆
**Tagi:** `regex`, `string`, `linijki`

### Treść

Wczytaj tekst wielowierszowy i końcówkę (np. `da`). Wypisz wszystkie wiersze tekstu, które **kończą się** podaną końcówką. Wiersz może mieć po końcówce znaki interpunkcyjne `.` `,` `;` `:` `!` `?` oraz spacje — w dowolnej liczbie — i nadal się liczy.

Końcówka nie musi być całym słowem: wiersz `Folgujmy paniom nie sobie, ma rada;` kończy się na `da`. Wielkość liter ma znaczenie. Wiersze wypisuj w niezmienionej postaci (razem z interpunkcją).

### Wejście

* 1. linia: `n` — liczba wierszy tekstu
* kolejne `n` linii: tekst
* ostatnia linia: końcówka (same litery)

### Wyjście

* Pasujące wiersze, każdy w osobnej linii, w kolejności występowania w tekście,
* `Brak wierszy.` — jeśli żaden wiersz nie pasuje.

### Ograniczenia

* $1 \le n \le 100$

### Przykład

**Wejście:**

```
4
Folgujmy paniom nie sobie, ma rada;
Milujmy wiernie nie jest w nich przysada.
Godności trzeba nie za nic tu cnota,
Miłości pragną nie pragną tu złota.
da
```

**Wyjście:**

```
Folgujmy paniom nie sobie, ma rada;
Milujmy wiernie nie jest w nich przysada.
```

### Uwagi

* Kotwica `$` oznacza koniec napisu, np. wzorzec `da[.,;:!? ]*$` pasuje do `rada;` i `przysada.`, ale nie do `dama`. Pamiętaj o `re.escape()` dla wczytanej końcówki.

---

## ZAD-07 — Podziel tekst względem znaków interpunkcyjnych

**Poziom:** ★☆☆
**Tagi:** `regex`, `string`

### Treść

Wczytaj tekst (jedno lub kilka zdań) i podziel go na fragmenty w miejscach występowania znaków interpunkcyjnych `,` `.` `!` `?` `;` `:`. Inne znaki (np. myślnik czy cudzysłów) nie dzielą tekstu.

Z każdego fragmentu usuń spacje z początku i końca. Puste fragmenty (np. między `?` a `!` w `?!` albo po kropce na końcu tekstu) pomiń.

### Wejście

* 1. linia: tekst

### Wyjście

Każdy niepusty fragment w osobnej linii, w kolejności występowania.

### Ograniczenia

* Tekst zawiera co najmniej jedną literę, więc zawsze jest co najmniej jeden fragment.

### Przykład

**Wejście:**

```
Ani nie poszedł do kina, ani nie wybrał się do teatru.
```

**Wyjście:**

```
Ani nie poszedł do kina
ani nie wybrał się do teatru
```

### Uwagi

* Podział zrobi `re.split(r"[,.!?;:]", tekst)`.

---

## ZAD-08 — Cyfry w słowach

**Poziom:** ★★☆
**Tagi:** `regex`, `string`

### Treść

Wczytaj zdanie i wypisz wszystkie ciągi cyfr, które są „przyklejone” do liter. Chodzi o najdłuższe ciągi kolejnych cyfr `0–9`, bezpośrednio przed którymi **lub** bezpośrednio po których stoi litera (także polska).

Cyfry oddzielone od liter spacją, interpunkcją czy myślnikiem się nie liczą. Na przykład w `s3łuchali91` są dwa ciągi: `3` i `91`, w `3.5kg` tylko `5`, a samodzielna liczba `22` nie jest wynikiem.

### Wejście

* 1. linia: zdanie

### Wyjście

* Znalezione ciągi cyfr, każdy w osobnej linii, w kolejności występowania (z zerami na początku, jeśli są),
* `Brak ciągów cyfr.` — jeśli nie ma żadnego takiego ciągu.

### Przykład

**Wejście:**

```
Jerzy29 i An37a s3łuchali91 lekcji 22 z języka polskiego
```

**Wyjście:**

```
29
37
3
91
```

### Uwagi

* Przydadzą się asercje: `(?<=...)` sprawdza, co stoi tuż przed dopasowaniem, a `(?=...)` — co stoi tuż po nim. Dowolną literę (także polską) opisuje klasa `[^\W\d_]` („znak słowa, który nie jest cyfrą ani `_`”).

---

## ZAD-09 — Usuń fragment napisu od pierwszego wystąpienia słowa klucz

**Poziom:** ★★☆
**Tagi:** `regex`, `string`

### Treść

Wczytaj tekst wielowierszowy i słowo klucz. Znajdź **pierwsze** wystąpienie słowa klucz w tekście jako **całego słowa** (zob. konwencje rozdziału; wielkość liter ma znaczenie). Usuń wszystko od początku tego wystąpienia do **końca tekstu** — także wszystkie dalsze wiersze — i wypisz to, co zostało.

Jeśli słowo klucz nie występuje w tekście, wypisz tekst bez zmian. Jeśli słowo klucz jest pierwszym słowem tekstu, nic nie wypisuj.

### Wejście

* 1. linia: `n` — liczba wierszy tekstu
* kolejne `n` linii: tekst
* ostatnia linia: słowo klucz (tylko litery i cyfry)

### Wyjście

Pozostała część tekstu: wiersze przed wierszem z wystąpieniem słowa klucz w całości, a z tego wiersza — tylko fragment przed słowem klucz.

### Ograniczenia

* $1 \le n \le 100$

### Przykład

**Wejście:**

```
3
Ala ma kota, a kot ma Alę.
Kot lubi mleko i spać.
Mleko jest białe.
mleko
```

**Wyjście:**

```
Ala ma kota, a kot ma Alę.
Kot lubi
```

Słowo `Mleko` w trzecim wierszu nie pasuje (wielka litera), a pierwsze `mleko` jest w drugim wierszu.

### Uwagi

* Złącz wiersze w jeden napis (`"\n".join(...)`) i znajdź wystąpienie przez `re.search()` — metoda `start()` dopasowania poda jego pozycję.
* Sprawdzarka ignoruje spacje na końcu wierszy i puste wiersze na końcu wyjścia.

---

## ZAD-10 — Podmień napisy z listy A na napisy z listy B

**Poziom:** ★★☆
**Tagi:** `regex`, `string`, `zamiana`

### Treść

Wczytaj tekst wielowierszowy oraz dwie listy słów tej samej długości: A i B. Zastąp w tekście każde wystąpienie słowa `A[i]` słowem `B[i]` (ten sam indeks).

* Zamieniaj tylko **całe słowa** (zob. konwencje rozdziału), np. słowo `kot` nie zmienia się wewnątrz `kota` ani `kot_1`. Wielkość liter ma znaczenie.
* Wszystkie zamiany wykonaj **jednocześnie**, na podstawie oryginalnego tekstu — wstawione słowo nie jest już ponownie zamieniane. Dla A = `kot pies` i B = `pies kot` tekst `kot i pies` zmienia się w `pies i kot`.

### Wejście

* 1. linia: `n` — liczba wierszy tekstu
* kolejne `n` linii: tekst
* następna linia: słowa listy A oddzielone spacjami
* ostatnia linia: słowa listy B oddzielone spacjami (tyle samo co w A)

### Wyjście

Tekst po zamianach (tyle samo wierszy co na wejściu).

### Ograniczenia

* $1 \le n \le 100$
* Listy mają co najmniej jedno słowo, słowa w liście A się nie powtarzają, a każde słowo składa się tylko z liter i cyfr.

### Przykład

**Wejście:**

```
1
Ala ma kota, a kot ma Alę.
kot Ala
pies Ola
```

**Wyjście:**

```
Ola ma kota, a pies ma Alę.
```

Słowa `kota` i `Alę` się nie zmieniają — to inne słowa niż `kot` i `Ala`.

### Uwagi

* Zbuduj jeden wzorzec z alternatywą, np. `\b(kot|Ala)\b`, i użyj `re.sub()` z funkcją, która dla dopasowanego słowa zwraca jego zamiennik ze słownika.

---

## ZAD-11 — Nazwa pliku bez rozszerzenia

**Poziom:** ★★☆
**Tagi:** `regex`, `string`, `ścieżki`

### Treść

Wczytaj ścieżkę do pliku. Wyodrębnij z niej nazwę pliku (część po ostatnim separatorze `/` lub `\`; ścieżka może mieszać oba separatory) i usuń z niej rozszerzenie.

**Rozszerzenie** to ostatnia kropka w nazwie pliku razem ze wszystkimi znakami po niej — chyba że ta kropka jest pierwszym znakiem nazwy (np. `.bashrc` nie ma rozszerzenia). Kropki w nazwach folderów nie mają znaczenia. Nazwa bez kropki zostaje bez zmian.

### Wejście

* 1. linia: ścieżka (nie kończy się separatorem)

### Wyjście

Jedna linia: nazwa pliku bez rozszerzenia.

### Przykład

**Wejście:**

```
C:\my-long\path_directory\file.html
```

**Wyjście:**

```
file
```

### Przykład 2

**Wejście:**

```
backup/archiwum.tar.gz
```

**Wyjście:**

```
archiwum.tar
```

### Uwagi

* Nazwę pliku dopasuje wzorzec `[^\\/]+$` („znaki inne niż ukośniki aż do końca napisu”).

---

## ZAD-12 — Zamiana formatu dat

**Poziom:** ★★☆
**Tagi:** `regex`, `string`, `grupy`

### Treść

Wczytaj tekst i zamień w nim każdą datę zapisaną w formacie `DD.MM.RRRR` na format `RRRR-MM-DD`, np. `05.03.2024` → `2024-03-05`. Resztę tekstu pozostaw bez zmian.

**Data** to dokładnie: 2 cyfry, kropka, 2 cyfry, kropka, 4 cyfry (cyfry `0–9`). Data nie może być częścią dłuższego słowa — tuż przed nią i tuż po niej nie może stać litera, cyfra ani `_` (zob. `\b` w konwencjach rozdziału). Nie sprawdzaj, czy taki dzień istnieje: `31.02.2023` też zamieniamy.

Nie są więc datami np. `1.02.2024` (jednocyfrowy dzień), `01.02.20245` (pięciocyfrowy rok) ani `x01.02.2024` (data przyklejona do litery).

### Wejście

* 1. linia: tekst

### Wyjście

Jedna linia: tekst po zamianie (bez zmian, jeśli nie zawiera żadnej daty).

### Przykład

**Wejście:**

```
Spotkanie przeniesiono z 05.03.2024 na 12.03.2024.
```

**Wyjście:**

```
Spotkanie przeniesiono z 2024-03-05 na 2024-03-12.
```

### Uwagi

* Fragmenty wzorca ujęte w nawiasy `( )` to **grupy** — są numerowane od 1 w kolejności nawiasów otwierających. W napisie zastępczym `re.sub()` odwołujesz się do nich przez `\1`, `\2`… albo `\g<1>`, `\g<2>`…:

```python
re.sub(r"(\w+) (\w+)", r"\2 \1", "Ala Kowalska")   # 'Kowalska Ala'
```

* Postać `\g<1>` przydaje się, gdy zaraz po odwołaniu stoi cyfra: `\g<1>0` to grupa 1 i znak `0`, a `\10` oznaczałoby grupę 10.

---

## ZAD-13 — Analiza logów serwera

**Poziom:** ★★☆
**Tagi:** `regex`, `string`, `grupy`, `słowniki`

### Treść

Serwer WWW zapisuje każde żądanie w jednym wierszu dziennika (logu), np.:

```
192.168.0.1 - - [10/Oct/2024:13:55:36 +0200] "GET /index.html HTTP/1.1" 200 2326
```

Wiersz jest **poprawny**, jeśli w całości ma postać `IP - - [DATA] "METODA ŚCIEŻKA HTTP/W" KOD ROZMIAR`, gdzie poszczególne elementy oddziela dokładnie jedna spacja, a:

* `IP` — cztery liczby (każda z 1–3 cyfr) oddzielone kropkami,
* `- -` — dosłownie dwa myślniki oddzielone spacją,
* `[DATA]` — nawias kwadratowy, co najmniej jeden dowolny znak różny od `]`, nawias zamykający,
* `METODA` — co najmniej jedna wielka litera `A–Z` (np. `GET`, `POST`),
* `ŚCIEŻKA` — zaczyna się od `/` i nie zawiera spacji,
* `W` — wersja protokołu: cyfra, kropka, cyfra (np. `1.1`),
* `KOD` — kod odpowiedzi: dokładnie 3 cyfry,
* `ROZMIAR` — liczba bajtów (same cyfry) albo `-`.

Wczytaj wiersze logu. Dla poprawnych wierszy policz, ile razy wystąpił każdy kod odpowiedzi, i znajdź najczęściej odwiedzaną ścieżkę. Policz też wiersze niepoprawne.

### Wejście

* 1. linia: `n` — liczba wierszy logu
* kolejne `n` linii: wiersze logu

### Wyjście

* Dla każdego kodu, który wystąpił: linia `KOD: liczba`, kody rosnąco.
* Linia `Najczęstsza ścieżka: ŚCIEŻKA (liczba)`. Jeśli kilka ścieżek ma tę samą największą liczbę wystąpień, wybierz najmniejszą z nich w porządku `sorted()`.
* Ostatnia linia: `Błędne wiersze: liczba`.

Jeśli nie ma żadnego poprawnego wiersza, zamiast pierwszych dwóch części wypisz `Brak poprawnych wpisów.` (a potem linię z liczbą błędnych wierszy).

### Ograniczenia

* $1 \le n \le 1000$

### Przykład

**Wejście:**

```
5
192.168.0.1 - - [10/Oct/2024:13:55:36 +0200] "GET /index.html HTTP/1.1" 200 2326
10.0.0.7 - - [10/Oct/2024:13:56:01 +0200] "GET /logo.png HTTP/1.1" 404 -
192.168.0.1 - - [10/Oct/2024:13:57:12 +0200] "POST /login HTTP/1.1" 302 512
to nie jest wpis logu
10.0.0.7 - - [10/Oct/2024:13:58:40 +0200] "GET /index.html HTTP/1.1" 200 2326
```

**Wyjście:**

```
200: 2
302: 1
404: 1
Najczęstsza ścieżka: /index.html (2)
Błędne wiersze: 1
```

### Uwagi

* **Grupy nazwane** `(?P<nazwa>...)` pozwalają odczytać fragment dopasowania po nazwie zamiast po numerze:

```python
m = re.fullmatch(r"(?P<imie>\w+) ma (?P<lat>[0-9]+) lat", "Ola ma 12 lat")
print(m.group("imie"), m.group("lat"))   # Ola 12
```

* `re.fullmatch()` zwraca `None`, gdy wiersz nie pasuje w całości — to właśnie wiersz błędny.
* W klasie znaków `[^\]]` oznacza „dowolny znak oprócz `]`”, a `\S` — „dowolny znak oprócz białych znaków”.
