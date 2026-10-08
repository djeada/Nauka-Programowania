# Rozdział 16: Bity i systemy liczbowe

Zadania w tym rozdziale ćwiczą zamianę liczb między systemami liczbowymi oraz operatory bitowe: `&` (AND), `|` (OR), `^` (XOR), `~` (NOT) i przesunięcia `<<`, `>>`.
**Każde zadanie (oraz każdy podpunkt w zadaniach wieloczęściowych) jest osobnym, niezależnym programem**: czyta **standardowe wejście** (stdin) i wypisuje wynik na **standardowe wyjście** (stdout).

**Konwencje wspólne:**

* Każda liczba na wejściu jest w osobnej linii, w kolejności podanej w sekcji **Wejście**.
* Liczby na wejściu są **nieujemne** (`0` jest dozwolone), chyba że zadanie wprost mówi inaczej.
* Zapis binarny wypisuj jako ciąg znaków `0` i `1` **bez spacji, bez prefiksu `0b` i bez zer wiodących**; zapis binarny liczby `0` to `0`.
* Dla systemów o podstawie większej niż 10 używaj cyfr `0–9` oraz wielkich liter `A–Z`.
* Jeśli zadanie mówi „nie wypisuj nic” — program nie wypisuje nawet pustej linii.
* Program nie wypisuje komunikatów typu „Podaj liczbę:”.

---

## ZAD-01A — Dziesiętny → binarny

**Poziom:** ★☆☆
**Tagi:** `konwersja`, `binarne`, `pętle`

### Treść

Wczytaj liczbę naturalną `n` zapisaną w systemie dziesiętnym i wypisz jej zapis w systemie binarnym.

### Wejście

* 1. linia: `n` — liczba naturalna

### Wyjście

Jedna linia: zapis binarny liczby `n`.

### Ograniczenia

* $0 \le n \le 10^9$

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
11
```

### Uwagi

* Dla `n = 0` wypisz `0`.
* Spróbuj obejść się bez wbudowanej funkcji `bin()`: kolejne cyfry binarne to reszty z dzielenia przez 2 (od najmniej znaczącej).

---

## ZAD-01B — Binarny → dziesiętny

**Poziom:** ★☆☆
**Tagi:** `konwersja`, `string`, `binarne`

### Treść

Wczytaj liczbę naturalną zapisaną w systemie binarnym (ciąg znaków `0` i `1`) i wypisz jej wartość w systemie dziesiętnym.

### Wejście

* 1. linia: `b` — niepusty ciąg znaków `0` i `1` (może zaczynać się od zer)

### Wyjście

Jedna linia: wartość liczby w systemie dziesiętnym.

### Ograniczenia

* długość `b` od 1 do 30 znaków

### Przykład

**Wejście:**

```
101
```

**Wyjście:**

```
5
```

### Uwagi

* Zera wiodące nie zmieniają wartości: `0010` to `2`.
* Spróbuj obejść się bez `int(b, 2)`: przechodząc po cyfrach od lewej, mnóż dotychczasowy wynik przez 2 i dodawaj kolejną cyfrę.

---

## ZAD-02 — Operatory bitowe AND, OR i XOR

**Poziom:** ★☆☆
**Tagi:** `bitwise`, `AND`, `OR`, `XOR`

### Treść

Operatory bitowe działają na zapisie binarnym liczb — osobno na każdej pozycji (bicie). Liczby zapisujemy jedna pod drugą, wyrównane do prawej, a brakujące bity z lewej uzupełniamy zerami:

* `a & b` (AND) — bit wyniku jest `1` tylko wtedy, gdy **oba** bity są równe `1`,
* `a | b` (OR) — bit wyniku jest `1`, gdy **co najmniej jeden** z bitów jest równy `1`,
* `a ^ b` (XOR) — bit wyniku jest `1`, gdy bity są **różne**.

Wczytaj dwie liczby naturalne `a` i `b` i wypisz wyniki tych trzech operacji.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Trzy linie — w systemie dziesiętnym:

* 1. linia: `a & b`
* 2. linia: `a | b`
* 3. linia: `a ^ b`

### Ograniczenia

* $0 \le a, b \le 10^9$

### Przykład

**Wejście:**

```
12
10
```

**Wyjście:**

```
8
14
6
```

$12 = 1100_2$ i $10 = 1010_2$. Bit po bicie: AND daje $1000_2 = 8$, OR — $1110_2 = 14$, a XOR — $0110_2 = 6$.

### Uwagi

* Rachunek z przykładu zapisany w słupkach:

  ```
      1100      1100      1100
    & 1010    | 1010    ^ 1010
    ------    ------    ------
      1000      1110      0110
  ```

* Zwróć uwagę na zależności: `a ^ a` to zawsze `0`, `a & 0` to `0`, a `a | 0` i `a ^ 0` to `a`. Zachodzi też równość `(a & b) + (a | b) == a + b` — możesz tak sprawdzić swój wynik.

---

## ZAD-03A — Dodawanie bitowe

**Poziom:** ★★☆
**Tagi:** `bitwise`, `XOR`, `AND`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`. Oblicz $a + b$, używając wyłącznie operatorów bitowych i przesunięć.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba naturalna: $a + b$.

### Ograniczenia

* $0 \le a, b \le 10^9$ (liczby ujemne nie występują)

### Przykład

**Wejście:**

```
2
3
```

**Wyjście:**

```
5
```

### Uwagi

* Do obliczenia wyniku nie używaj `+`, `-`, `*`, `/`, `//`, `%` — tylko `&`, `|`, `^`, `~`, `<<`, `>>` i porównań.
* `a ^ b` to suma bez przeniesień, a `(a & b) << 1` to przeniesienia. Powtarzaj, dopóki przeniesienia są niezerowe.

---

## ZAD-03B — Odejmowanie bitowe

**Poziom:** ★★☆
**Tagi:** `bitwise`, `pożyczki`, `XOR`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`. Oblicz $a - b$, używając wyłącznie operatorów bitowych i przesunięć.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba naturalna: $a - b$.

### Ograniczenia

* $0 \le b \le a \le 10^9$ — wynik nigdy nie jest ujemny

### Przykład

**Wejście:**

```
7
5
```

**Wyjście:**

```
2
```

### Uwagi

* Do obliczenia wyniku nie używaj `+`, `-`, `*`, `/`, `//`, `%` — tylko `&`, `|`, `^`, `~`, `<<`, `>>` i porównań.
* `a ^ b` to różnica bez pożyczek, a `(~a & b) << 1` to pożyczki. Powtarzaj, dopóki pożyczki są niezerowe.

---

## ZAD-03C — Mnożenie bitowe

**Poziom:** ★★☆
**Tagi:** `bitwise`, `shift`, `pętle`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`. Oblicz $a \cdot b$, używając wyłącznie operatorów bitowych i przesunięć (metoda „przesuń i dodaj”).

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba naturalna: $a \cdot b$.

### Ograniczenia

* $0 \le a, b \le 10^6$ (liczby ujemne nie występują)

### Przykład

**Wejście:**

```
4
4
```

**Wyjście:**

```
16
```

### Uwagi

* Do obliczenia wyniku nie używaj `+`, `-`, `*`, `/`, `//`, `%` — tylko `&`, `|`, `^`, `~`, `<<`, `>>` i porównań.
* Dla każdego ustawionego bitu `k` liczby `b` dodaj do wyniku `a << k`. Dodawanie wykonaj bitowo, tak jak w ZAD-03A.

---

## ZAD-03D — Dzielenie całkowite bitowe

**Poziom:** ★★★
**Tagi:** `bitwise`, `dzielenie`, `shift`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`. Oblicz iloraz całkowity $\lfloor a / b \rfloor$ (w Pythonie `a // b`), używając wyłącznie operatorów bitowych i przesunięć.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba naturalna: iloraz całkowity `a` przez `b`.

### Ograniczenia

* $0 \le a \le 10^9$
* $1 \le b \le 10^9$ (dzielenie przez zero nie występuje)

### Przykład

**Wejście:**

```
9
3
```

**Wyjście:**

```
3
```

### Uwagi

* Do obliczenia wyniku nie używaj `+`, `-`, `*`, `/`, `//`, `%` — tylko `&`, `|`, `^`, `~`, `<<`, `>>` i porównań.
* Postępuj jak w dzieleniu pisemnym: znajdź największe `b << k` nie większe od `a`, a potem dla kolejnych `k` (malejąco) odejmuj `b << k` od `a`, jeśli się mieści, i ustawiaj bit `k` ilorazu. Odejmowanie wykonaj bitowo, tak jak w ZAD-03B.

---

## ZAD-04A — Liczba zer w zapisie binarnym

**Poziom:** ★☆☆
**Tagi:** `binarne`, `zliczanie`

### Treść

Wczytaj liczbę naturalną `n`. Policz, ile cyfr `0` ma jej zapis binarny (bez zer wiodących).

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: liczba zer w zapisie binarnym `n`.

### Ograniczenia

* $0 \le n \le 10^9$

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
0
```

### Uwagi

* Zapis binarny `0` to `0`, więc dla `n = 0` wynik to `1`.

---

## ZAD-04B — Liczba jedynek w zapisie binarnym

**Poziom:** ★☆☆
**Tagi:** `popcount`, `binarne`

### Treść

Wczytaj liczbę naturalną `n`. Policz, ile bitów równych `1` ma jej zapis binarny.

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: liczba jedynek w zapisie binarnym `n`.

### Ograniczenia

* $0 \le n \le 10^9$

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
2
```

### Uwagi

* Najmłodszy bit to `n & 1`, a `n >> 1` usuwa go z liczby. Dla `n = 0` wynik to `0`.

---

## ZAD-05A — Minimum bez instrukcji warunkowych

**Poziom:** ★★☆
**Tagi:** `bit-trick`, `min/max`, `bez if`

### Treść

Wczytaj dwie liczby całkowite `a` i `b`. Wypisz mniejszą z nich **bez użycia instrukcji warunkowych** (`if`, wyrażenia `x if warunek else y`) i bez funkcji `min`, `max`, `abs`, `sorted`.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba całkowita: mniejsza z liczb `a` i `b` (gdy są równe — ich wspólna wartość).

### Ograniczenia

* $-10^9 \le a, b \le 10^9$ — w tym zadaniu liczby **mogą być ujemne**

### Przykład

**Wejście:**

```
3
2
```

**Wyjście:**

```
2
```

### Uwagi

* Dopuszczalne są operacje arytmetyczne i bitowe.
* Wskazówka: dla `d = a - b` wyrażenie `d >> 63` daje `-1` (same jedynki w zapisie binarnym), gdy `d < 0`, oraz `0`, gdy `d ≥ 0`. Wtedy `d & (d >> 63)` jest równe `d` albo `0`.
* Tą samą sztuczką otrzymasz maksimum: `a - (d & (d >> 63))`.

---

## ZAD-05B — Wartość bezwzględna bez instrukcji warunkowych

**Poziom:** ★★☆
**Tagi:** `bit-trick`, `maski`, `bez if`

### Treść

Wczytaj liczbę całkowitą `x` i wypisz jej wartość bezwzględną $|x|$ **bez użycia instrukcji warunkowych** (`if`, wyrażenia `x if warunek else y`) i bez funkcji `abs`, `min`, `max`, `sorted`.

### Wejście

* 1. linia: `x`

### Wyjście

Jedna liczba naturalna: $|x|$.

### Ograniczenia

* $-10^9 \le x \le 10^9$ — liczba **może być ujemna**

### Przykład

**Wejście:**

```
-12
```

**Wyjście:**

```
12
```

### Uwagi

* Dopuszczalne są operacje arytmetyczne i bitowe; porównania (`<`, `>`) nie są potrzebne.
* Tak jak w ZAD-05A, **maska znaku** `m = x >> 63` jest równa `-1` (same jedynki), gdy `x < 0`, oraz `0`, gdy `x ≥ 0`.
* XOR z maską `0` nic nie zmienia, a XOR z maską `-1` odwraca wszystkie bity, czyli daje $-x - 1$ (tak liczby ujemne zapisuje kod uzupełnień do dwóch). Wystarczy więc obliczyć `(x ^ m) - m`.

---

## ZAD-06 — Konwersja między dowolnymi systemami (2..36)

**Poziom:** ★★☆
**Tagi:** `konwersja`, `base`, `string`

### Treść

Wczytaj zapis liczby naturalnej `X` w systemie o podstawie `p` oraz podstawę docelową `q`. Wypisz zapis tej samej liczby w systemie o podstawie `q`.

### Wejście

* 1. linia: `X` — zapis liczby w systemie o podstawie `p` (cyfry `0–9` i wielkie litery `A–Z`, gdzie `A` = 10, `B` = 11, …, `Z` = 35)
* 2. linia: `p` — podstawa systemu, w którym zapisano `X`
* 3. linia: `q` — podstawa systemu docelowego

### Wyjście

Jedna linia: zapis liczby w systemie o podstawie `q`, bez zer wiodących (cyfry `0–9` i wielkie litery `A–Z`).

### Ograniczenia

* `2 ≤ p, q ≤ 36`
* `X` ma od 1 do 20 znaków, każda cyfra jest mniejsza od `p`; `X` może zaczynać się od zer

### Przykład

**Wejście:**

```
4301
10
4
```

**Wyjście:**

```
1003031
```

### Uwagi

* Najpierw zamień `X` na liczbę (przechodząc po cyfrach od lewej: wynik = wynik · `p` + cyfra), a potem zamień ją na system `q` (reszty z dzielenia przez `q`).
* Spróbuj obejść się bez `int(X, p)` — zaimplementuj obie zamiany samodzielnie.
* Liczba `0` w każdym systemie to `0`.

---

## ZAD-07 — Zamiana sąsiadujących bitów

**Poziom:** ★☆☆
**Tagi:** `bitwise`, `maski`, `swap bits`

### Treść

Wczytaj liczbę naturalną `n`. Zamień miejscami każdą parę sąsiadujących bitów jej zapisu binarnego (bity numerujemy od `0` — najmłodszy, czyli skrajnie prawy):

* bit 0 z bitem 1,
* bit 2 z bitem 3,
* bit 4 z bitem 5,
* itd.

Wypisz otrzymaną liczbę w systemie dziesiętnym.

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: wynik po zamianie bitów.

### Ograniczenia

* $0 \le n \le 10^9$

### Przykład

**Wejście:**

```
9131
```

**Wyjście:**

```
4951
```

`9131` to binarnie `10001110101011`, a po zamianie par bitów otrzymujemy `01001101010111`, czyli `4951`.

### Uwagi

* Brakujące bity na początku zapisu traktujemy jak zera. Na przykład `4` to `100`: bit 2 (jedynka) zamienia się z bitem 3 (zerem), więc wynik to `1000`, czyli `8`.
* Maska `0x55555555` (`…0101`) wybiera bity o numerach parzystych, a `0xAAAAAAAA` (`…1010`) — o numerach nieparzystych.

---

## ZAD-08 — Najbliższa potęga dwójki (>= n)

**Poziom:** ★☆☆
**Tagi:** `potęgi 2`, `bitwise`, `pętle`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz najmniejszą potęgę liczby 2, która jest **większa lub równa** `n`, czyli najmniejsze $2^k \ge n$ dla całkowitego $k \ge 0$.

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: najmniejsza potęga dwójki nie mniejsza od `n`.

### Ograniczenia

* $0 \le n \le 10^9$

### Przykład

**Wejście:**

```
111
```

**Wyjście:**

```
128
```

### Uwagi

* $2^0 = 1$, więc dla `n = 0` i `n = 1` wynik to `1`.
* Jeśli `n` jest potęgą dwójki, wynikiem jest samo `n`.
* Kolejne potęgi dwójki otrzymasz przesunięciem `potega << 1`.

---

## ZAD-09A — Wielkie → małe (bitowo)

**Poziom:** ★★☆
**Tagi:** `ASCII`, `bitwise`, `string`

### Treść

Wczytaj napis. Zamień wszystkie wielkie litery alfabetu łacińskiego (`A–Z`) na małe, używając operacji bitowych na kodach ASCII. Pozostałe znaki pozostaw bez zmian.

### Wejście

* 1. linia: napis (może zawierać spacje, cyfry i znaki interpunkcyjne)

### Wyjście

Jedna linia: napis po zamianie.

### Ograniczenia

* napis ma od 1 do 100 znaków i składa się wyłącznie ze znaków ASCII (bez polskich liter)

### Przykład

**Wejście:**

```
Test
```

**Wyjście:**

```
test
```

### Uwagi

* Kody wielkiej i małej litery różnią się tylko bitem o wartości 32 (`0b100000`): `ord("A")` to `65`, a `ord("a")` to `97`. Ustawienie tego bitu: `ord(znak) | 32`.
* Zmieniaj tylko litery `A–Z` — np. `@` i `[` sąsiadują w tablicy ASCII z literami, ale mają pozostać bez zmian.
* Odwrotną zamianę (małe → wielkie) daje wyzerowanie tego bitu: `ord(znak) & ~32`.

---

## ZAD-09B — Numer litery w alfabecie (bitowo)

**Poziom:** ★★☆
**Tagi:** `ASCII`, `bitwise`, `maski`

### Treść

Wczytaj słowo złożone z liter alfabetu łacińskiego. Dla każdej litery wyznacz jej numer w alfabecie — `a` i `A` mają numer `1`, `b` i `B` numer `2`, …, `z` i `Z` numer `26` — używając operacji bitowej na kodzie ASCII zamiast porównań i odejmowania.

### Wejście

* 1. linia: słowo

### Wyjście

Jedna linia: numery kolejnych liter słowa oddzielone pojedynczymi spacjami.

### Ograniczenia

* słowo ma od 1 do 100 znaków i składa się wyłącznie z liter `a–z` i `A–Z`

### Przykład

**Wejście:**

```
Bit
```

**Wyjście:**

```
2 9 20
```

### Uwagi

* Zapisz kody binarnie: `ord("A")` to $65 = 1000001_2$, a `ord("a")` to $97 = 1100001_2$. Pięć najniższych bitów kodu każdej litery to właśnie jej numer w alfabecie — i to niezależnie od wielkości litery.
* Pięć najniższych bitów wydobędziesz **maską** $31 = 11111_2$: `ord(znak) & 31`. Operacja `&` z maską zeruje wszystkie bity poza tymi, które w masce są jedynkami.

---

## ZAD-09C — Odwróć wielkość liter (bitowo)

**Poziom:** ★★☆
**Tagi:** `ASCII`, `bitwise`, `toggle case`

### Treść

Wczytaj napis. Zamień wielkość każdej litery alfabetu łacińskiego na przeciwną (mała ↔ wielka), używając operacji bitowych na kodach ASCII. Pozostałe znaki pozostaw bez zmian.

### Wejście

* 1. linia: napis (może zawierać spacje, cyfry i znaki interpunkcyjne)

### Wyjście

Jedna linia: napis po zmianie.

### Ograniczenia

* napis ma od 1 do 100 znaków i składa się wyłącznie ze znaków ASCII (bez polskich liter)

### Przykład

**Wejście:**

```
Test
```

**Wyjście:**

```
tEST
```

### Uwagi

* Odwrócenie bitu o wartości 32: `ord(znak) ^ 32`. Stosuj je tylko do liter `a–z` i `A–Z`.

---

## ZAD-10 — Ile bitów trzeba odwrócić (A → B)

**Poziom:** ★★☆
**Tagi:** `XOR`, `popcount`, `bitwise`

### Treść

Wczytaj dwie liczby naturalne `A` i `B`. Oblicz, ile bitów trzeba odwrócić w liczbie `A`, aby otrzymać `B`, czyli na ilu pozycjach ich zapisy binarne się różnią.

### Wejście

* 1. linia: `A`
* 2. linia: `B`

### Wyjście

Jedna liczba naturalna: liczba różniących się bitów.

### Ograniczenia

* $0 \le A, B \le 10^9$

### Przykład

**Wejście:**

```
34
73
```

**Wyjście:**

```
5
```

`34` = `0100010`, `73` = `1001001` — różnią się na 5 pozycjach.

### Uwagi

* Krótszy zapis uzupełniamy zerami z lewej strony.
* `A ^ B` ma jedynki dokładnie na pozycjach, na których bity `A` i `B` są różne.

---

## ZAD-11 — Palindrom w systemie binarnym

**Poziom:** ★★☆
**Tagi:** `binarne`, `palindrom`, `string`

### Treść

Wczytaj liczbę naturalną `n`. Sprawdź, czy jej zapis binarny (bez zer wiodących) jest palindromem, czyli czy czytany od końca jest taki sam.

### Wejście

* 1. linia: `n`

### Wyjście

Jedno słowo: `Prawda`, jeśli zapis binarny `n` jest palindromem, w przeciwnym razie `Fałsz`.

### Ograniczenia

* $0 \le n \le 10^9$

### Przykład

**Wejście:**

```
26
```

**Wyjście:**

```
Fałsz
```

`26` ma zapis binarny `11010`, który czytany od końca daje `01011` — to nie jest palindrom.

### Uwagi

* Zapis binarny `0` to `0`, a `1` to `1` — oba są palindromami.

---

## ZAD-12 — Najdłuższy ciąg zer otoczony jedynkami

**Poziom:** ★★★
**Tagi:** `binarne`, `binary gap`, `pętle`

### Treść

Wczytaj liczbę naturalną `n`. W jej zapisie binarnym znajdź długość najdłuższego ciągu kolejnych zer, który jest **z obu stron otoczony jedynkami** (tzw. *binary gap*). Jeśli takiego ciągu nie ma, wypisz `0`.

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: długość najdłuższego takiego ciągu zer.

### Ograniczenia

* $0 \le n \le 10^9$

### Przykład

**Wejście:**

```
14
```

**Wyjście:**

```
0
```

`14` ma zapis `1110` — zero na końcu nie ma jedynki po prawej stronie, więc wynik to `0`.

### Przykład 2

**Wejście:**

```
20
```

**Wyjście:**

```
1
```

`20` ma zapis `10100` — zero między jedynkami tworzy ciąg długości `1`, a końcowe `00` się nie liczy.

### Uwagi

* Dla `n = 0` (zapis `0`) wynik to `0`.
