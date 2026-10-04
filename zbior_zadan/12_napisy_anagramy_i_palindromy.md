# Rozdział 12: Napisy — anagramy i palindromy

Zadania w tym rozdziale dotyczą palindromów (napisów czytanych tak samo od przodu i od tyłu), anagramów (napisów złożonych z tych samych liter w innej kolejności) oraz permutacji liter słowa.

**Konwencje wspólne:**

* Każde zadanie jest osobnym programem: czyta **standardowe wejście** i wypisuje wynik na **standardowe wyjście**.
* Program nie wypisuje komunikatów typu „Podaj słowo:”.
* Napis wczytuj jako całą linię. Spacje mogą w nim wystąpić tylko tam, gdzie treść mówi o zdaniu.
* **Słowo** w zdaniu to fragment oddzielony od innych spacjami. Znaki interpunkcyjne (np. `.` `,` `!` `?` `;` `:` `-`) stojące na początku lub końcu fragmentu nie należą do słowa (`kara.` → `kara`), a fragment złożony wyłącznie z interpunkcji nie jest słowem. W Pythonie: `fragment.strip(string.punctuation)` dla każdego fragmentu z `zdanie.split()`.
* Gdy zadanie każe ignorować wielkość liter, porównuj napisy np. po zamianie na małe litery (`lower()`), ale słowa wypisuj **w postaci z wejścia** (bez interpunkcji z brzegów).
* Gdy wynikiem jest kilka napisów, wypisz każdy w osobnej linii. Jeśli nie ma żadnego — program nic nie wypisuje.

---

## ZAD-01 — Czy słowo jest palindromem?

**Poziom:** ★☆☆
**Tagi:** `napisy`, `palindrom`

### Treść

Wczytaj jedno słowo i sprawdź, czy jest palindromem, czyli czy czytane od lewej do prawej i od prawej do lewej jest takie samo.
Wielkość liter nie ma znaczenia — `Kajak` też jest palindromem.

### Wejście

* 1. linia: słowo (same litery, bez spacji)

### Wyjście

Jedna linia:

* `Prawda` — jeśli słowo jest palindromem,
* `Fałsz` — w przeciwnym razie.

### Przykład 1

**Wejście:**

```
kajak
```

**Wyjście:**

```
Prawda
```

### Przykład 2

**Wejście:**

```
Kotek
```

**Wyjście:**

```
Fałsz
```

---

## ZAD-02 — Wszystkie permutacje słowa

**Poziom:** ★★☆
**Tagi:** `napisy`, `permutacje`, `itertools`

### Treść

Wczytaj słowo złożone z **niepowtarzających się** liter i wypisz wszystkie jego permutacje (wszystkie słowa, które można ułożyć z jego liter, używając każdej dokładnie raz) — każdą w osobnej linii, w **kolejności alfabetycznej**.

### Wejście

* 1. linia: słowo złożone z małych liter alfabetu angielskiego (`a`–`z`), litery nie powtarzają się

### Wyjście

Wszystkie permutacje słowa w kolejności alfabetycznej, każda w osobnej linii. Słowo o długości $n$ ma $n!$ permutacji.

### Ograniczenia

* Długość słowa: od 1 do 6.

### Przykład 1

**Wejście:**

```
abc
```

**Wyjście:**

```
abc
acb
bac
bca
cab
cba
```

### Przykład 2

**Wejście:**

```
on
```

**Wyjście:**

```
no
on
```

### Uwagi

* Permutacje wygeneruje za Ciebie funkcja `permutations` z modułu `itertools` (biblioteka standardowa Pythona). Zwraca ona kolejne permutacje jako **krotki** liter — krotka to niezmienna lista zapisywana w nawiasach okrągłych:

  ```python
  from itertools import permutations

  for krotka in permutations("ab"):
      print(krotka)            # ('a', 'b'), a potem ('b', 'a')
      print("".join(krotka))   # ab, a potem ba
  ```

* `permutations` zachowuje kolejność liter z podanego ciągu, więc jeśli podasz mu litery posortowane alfabetycznie (`sorted(slowo)`), permutacje powstaną od razu w kolejności alfabetycznej. Możesz też posortować gotową listę wyników.
* Samodzielne generowanie permutacji (rekurencją) przećwiczysz w rozdziale o rekurencji.

---

## ZAD-03 — Czy dwa słowa są anagramami?

**Poziom:** ★☆☆
**Tagi:** `napisy`, `anagram`, `sortowanie`

### Treść

Wczytaj dwa słowa i sprawdź, czy są anagramami, czyli czy jedno da się utworzyć przez przestawienie liter drugiego (każda litera musi wystąpić w obu słowach tyle samo razy).
Wielkość liter nie ma znaczenia. Słowo jest też anagramem samego siebie.

### Wejście

* 1. linia: słowo `s1`
* 2. linia: słowo `s2`

### Wyjście

Jedna linia:

* `Prawda` — jeśli słowa są anagramami,
* `Fałsz` — w przeciwnym razie.

### Przykład

**Wejście:**

```
ula
lua
```

**Wyjście:**

```
Prawda
```

### Uwagi

* Najprościej porównać posortowane litery obu słów (np. `sorted(s1.lower())`) albo liczbę wystąpień każdej litery.

---

## ZAD-04 — Palindromy w zdaniu

**Poziom:** ★★☆
**Tagi:** `napisy`, `palindrom`, `słowa`

### Treść

Wczytaj zdanie i wypisz wszystkie jego słowa, które są palindromami. Przy sprawdzaniu ignoruj wielkość liter.
Słowa wyznaczaj zgodnie z konwencją rozdziału (bez interpunkcji z brzegów). Pojedyncza litera też jest palindromem.

### Wejście

* 1. linia: zdanie (może zawierać znaki interpunkcyjne)

### Wyjście

Każde słowo będące palindromem w osobnej linii, w kolejności występowania w zdaniu i w postaci z wejścia (bez interpunkcji z brzegów). Słowo, które powtarza się w zdaniu, wypisz tyle razy, ile razy występuje. Jeśli w zdaniu nie ma palindromów, program nic nie wypisuje.

### Przykład 1

**Wejście:**

```
Anna zabrała kajak na wycieczkę i uderzyła się w oko.
```

**Wyjście:**

```
Anna
kajak
i
w
oko
```

`Anna` jest palindromem, bo po zamianie na małe litery daje `anna`; z `oko.` usuwamy kropkę.

### Przykład 2

**Wejście:**

```
Hello world
```

**Wyjście:** *(brak)*

---

## ZAD-05 — Anagramy słowa w zdaniu

**Poziom:** ★★☆
**Tagi:** `napisy`, `anagram`, `słowa`

### Treść

Wczytaj zdanie oraz słowo-klucz `k`. Wypisz wszystkie słowa zdania, które są anagramami słowa `k` (także samo słowo `k`). Przy porównywaniu ignoruj wielkość liter.
Słowa wyznaczaj zgodnie z konwencją rozdziału (bez interpunkcji z brzegów).

### Wejście

* 1. linia: zdanie
* 2. linia: słowo-klucz `k`

### Wyjście

Każde słowo zdania będące anagramem `k` w osobnej linii, w kolejności występowania i w postaci z wejścia. Jeśli takich słów nie ma, program nic nie wypisuje.

### Przykład

**Wejście:**

```
Sroga kara, a potem raka.
arak
```

**Wyjście:**

```
kara
raka
```

### Uwagi

* Wykorzystaj rozwiązanie zadania ZAD-03: porównuj posortowane litery słów zapisanych małymi literami.

---

## ZAD-06 — Permutacje słowa, które są palindromami

**Poziom:** ★★☆
**Tagi:** `napisy`, `palindrom`, `permutacje`

### Treść

Wczytaj słowo i wypisz wszystkie **różne** palindromy, które można ułożyć z jego liter (używając każdej litery dokładnie tyle razy, ile razy występuje w słowie).

### Wejście

* 1. linia: słowo złożone z małych liter alfabetu angielskiego (`a`–`z`); litery mogą się powtarzać

### Wyjście

Każdy palindrom w osobnej linii, bez powtórzeń, w **kolejności alfabetycznej**. Jeśli z liter słowa nie da się ułożyć żadnego palindromu, program nic nie wypisuje.

### Ograniczenia

* Długość słowa: od 1 do 10.

### Przykład 1

**Wejście:**

```
aabb
```

**Wyjście:**

```
abba
baab
```

### Przykład 2

**Wejście:**

```
abc
```

**Wyjście:** *(brak)*

### Uwagi

* Palindrom da się ułożyć tylko wtedy, gdy co najwyżej jedna litera występuje nieparzystą liczbę razy (ta litera trafia na środek).
* Wystarczy wygenerować permutacje „połówki” palindromu (po połowie wystąpień każdej litery, np. funkcją `permutations` z zadania ZAD-02) i do każdej dokleić środek oraz odwróconą połówkę. Gdy litery się powtarzają, `permutations` zwraca te same układy wielokrotnie — powtórzenia usuniesz, zbierając wyniki w zbiorze (`set`).

---

## ZAD-07 — Minimalna liczba usunięć, aby uzyskać anagramy

**Poziom:** ★★☆
**Tagi:** `napisy`, `anagram`, `zliczanie`

### Treść

Wczytaj dwa słowa (mogą mieć różne długości). Oblicz, ile **łącznie** znaków trzeba co najmniej usunąć z obu słów, aby pozostałe napisy były anagramami (pozostałe napisy mogą też być puste).

### Wejście

* 1. linia: słowo `s1` (małe litery)
* 2. linia: słowo `s2` (małe litery)

### Wyjście

Jedna linia: minimalna łączna liczba usuniętych znaków.

### Przykład 1

**Wejście:**

```
grazyna
razynax
```

**Wyjście:**

```
2
```

Z pierwszego słowa usuwamy `g`, z drugiego `x` — zostają anagramy `razyna` i `razyna`.

### Przykład 2

**Wejście:**

```
kajak
ak
```

**Wyjście:**

```
3
```

Z `kajak` usuwamy `k`, `j` i `a` — zostaje `ka`, które jest anagramem `ak`. Z `ak` nic nie usuwamy.

### Uwagi

* Dla każdej litery policz, ile razy występuje w `s1` (np. `s1.count(litera)`) i ile w `s2`. Nadmiarowe wystąpienia trzeba usunąć, więc wynik to suma wartości $|c_1 - c_2|$ po wszystkich literach występujących w którymkolwiek słowie (np. po literach zbioru `set(s1 + s2)`).

---

## ZAD-08 — Wyjątkowe palindromy (podciągi bez zmiany kolejności)

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
