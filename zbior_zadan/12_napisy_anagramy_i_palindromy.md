# Rozdział: Napisy — palindromy, anagramy, permutacje (stdin/stdout)

Poniższe zadania polegają na wczytywaniu danych ze **standardowego wejścia** (stdin) i wypisywaniu wyniku na **standardowe wyjście** (stdout).
**Każde zadanie (oraz każdy podpunkt) jest osobnym, niezależnym programem.**

**Konwencje wspólne:**

* Napis wczytuj jako całą linię (może zawierać spacje tylko tam, gdzie jest to powiedziane).
* Jeśli w wyjściu jest „każde słowo w osobnej linii” — wypisuj dokładnie po jednej pozycji na linię.
* W zadaniach „ignoruj wielkość liter” — porównuj w wersji np. `lower()`, ale wypisuj słowa **w oryginalnej postaci z wejścia**, chyba że treść mówi inaczej.
* Jeśli wynikiem ma być „lista” i nic nie znaleziono — nie wypisuj nic (puste wyjście), o ile nie ma wprost formatu `[]`.

---

## ZAD-01 — Czy słowo jest palindromem?

**Poziom:** ★☆☆
**Tagi:** `string`, `palindrom`, `I/O`

### Treść

Wczytaj jedno słowo i sprawdź, czy jest palindromem (czytane od lewej do prawej i od prawej do lewej jest takie samo).

### Wejście

* 1. linia: słowo (same litery, bez spacji)

### Wyjście

Jedna linia:

* `Prawda` — jeśli słowo jest palindromem
* `Fałsz` — w przeciwnym razie

### Przykład

**Wejście:**

```
kajak
```

**Wyjście:**

```
Prawda
```

### Uwagi o formatowaniu

* Jeśli chcesz ignorować wielkość liter, porównuj wersje `lower()`.

---

## ZAD-02 — Wszystkie permutacje słowa

**Poziom:** ★★☆
**Tagi:** `rekurencja`, `permutacje`, `backtracking`

### Treść

Wczytaj słowo z **unikalnych liter** i wypisz wszystkie jego permutacje — każdą w osobnej linii.

### Wejście

* 1. linia: słowo (litery nie powtarzają się)

### Wyjście

Wiele linii — wszystkie permutacje słowa, każda w osobnej linii.

### Przykład

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

### Uwagi o formatowaniu

* Kolejność wypisywania permutacji nie musi być dokładnie taka jak w przykładzie, o ile są wszystkie i bez powtórzeń.

---

## ZAD-03 — Czy dwa słowa są anagramami?

**Poziom:** ★☆☆
**Tagi:** `anagram`, `sortowanie`, `zliczanie`

### Treść

Wczytaj dwa słowa i sprawdź, czy są anagramami (czy da się utworzyć jedno przez przestawienie liter drugiego).

### Wejście

* 1. linia: słowo `s1`
* 2. linia: słowo `s2`

### Wyjście

Jedna linia:

* `Prawda` — jeśli anagramy
* `Fałsz` — jeśli nie

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

* Najprościej: porównaj posortowane litery albo słowniki zliczeń znaków.

---

## ZAD-04 — Palindromy w zdaniu

**Poziom:** ★★☆
**Tagi:** `string`, `tokenizacja`, `palindrom`

### Treść

Wczytaj zdanie i wypisz wszystkie słowa, które są palindromami.
Ignoruj wielkość liter przy sprawdzaniu.

### Wejście

* 1. linia: zdanie (może zawierać spacje i znaki interpunkcyjne)

### Wyjście

Każdy znaleziony palindrom w osobnej linii, w kolejności występowania w zdaniu.

### Przykład

**Wejście:**

```
Tata zabrał kajak na wycieczkę i uderzył się w oko
```

**Wyjście:**

```
Tata
kajak
i
w
oko
```

### Uwagi o formatowaniu

* Traktuj „słowo” jako ciąg liter/cyfr po usunięciu interpunkcji z brzegów (np. `kara.` → `kara`).
* Porównuj w wersji `lower()`, ale wypisz w oryginalnym brzmieniu z wejścia (tak jak w przykładzie).

---

## ZAD-05 — Anagramy słowa w zdaniu

**Poziom:** ★★☆
**Tagi:** `anagram`, `string`, `zliczanie`

### Treść

Wczytaj zdanie oraz słowo-klucz. Wypisz wszystkie słowa ze zdania, które są anagramami słowa-klucza (ignoruj wielkość liter).

### Wejście

* 1. linia: zdanie
* 2. linia: słowo-klucz `k`

### Wyjście

Każde słowo ze zdania będące anagramem `k` — w osobnej linii (w kolejności występowania).

### Przykład

**Wejście:**

```
Sroga kara.
arak
```

**Wyjście:**

```
kara
```

### Uwagi

* Tak jak wyżej: usuń interpunkcję z brzegów słów.
* Porównuj np. posortowane litery w `lower()`.

---

## ZAD-06 — Permutacje słowa, które są palindromami

**Poziom:** ★★☆
**Tagi:** `palindrom`, `permutacje`, `multiset`

### Treść

Wczytaj słowo i wypisz wszystkie **unikalne** palindromy, które są jego permutacjami.

### Wejście

* 1. linia: słowo (litery mogą się powtarzać)

### Wyjście

Każdy unikalny palindrom w osobnej linii. Jeśli nie istnieje żaden — puste wyjście.

### Przykład

**Wejście:**

```
aabb
```

**Wyjście:**

```
abba
baab
```

### Uwagi

* Najpierw sprawdź warunek istnienia palindromu z liter: co najwyżej jeden znak może mieć nieparzystą liczbę wystąpień.
* Generuj palindromy z połówek (bez wypisywania duplikatów).

---

## ZAD-07 — Minimalna liczba usunięć, aby uzyskać anagramy

**Poziom:** ★★★
**Tagi:** `anagram`, `zliczanie`, `greedy`

### Treść

Wczytaj dwa słowa. Jeśli mają różne długości, wypisz `-1`.
W przeciwnym razie oblicz minimalną liczbę znaków, które trzeba usunąć (łącznie z obu słów), aby pozostałe napisy były anagramami.

### Wejście

* 1. linia: słowo `s1`
* 2. linia: słowo `s2`

### Wyjście

* jedna liczba całkowita: minimalna liczba usunięć lub `-1`

### Przykład

**Wejście:**

```
grazyna
razynax
```

**Wyjście:**

```
2
```

### Uwagi

* Dla tej samej długości: policz zliczenia liter i zsumuj wartości `abs(c1[lit] - c2[lit])`, a wynik wypisz jako tę sumę. (To jest łączna liczba usunięć.)

---

## ZAD-08 — Wyjątkowe palindromy (podciągi bez zmiany kolejności)

**Poziom:** ★★★
**Tagi:** `substring`, `palindrom`, `unikalność`

### Treść

Wczytaj słowo i znajdź wszystkie **unikalne** palindromy, które można z niego utworzyć jako **spójne podciągi** (substringi), bez zmiany kolejności znaków, spełniające warunek „wyjątkowości”:

1. wszystkie znaki są identyczne (np. `aaa`), **albo**
2. wszystkie znaki poza środkowym są identyczne (np. `cbc`).

Pojedynczy znak też jest wyjątkowym palindromem.

### Wejście

* 1. linia: słowo (litery)

### Wyjście

Każdy unikalny wyjątkowy palindrom w osobnej linii.
Jeśli nic poza pojedynczymi znakami nie pasuje, wypisz tylko te unikalne znaki (po jednej linii na znak).

### Przykład

**Wejście:**

```
xxyxx
```

**Wyjście:**

```
x
xx
xxx
xxyxx
y
yxy
```

### Uwagi o formatowaniu

* Usuń duplikaty w wyniku (np. ten sam palindrom znaleziony w kilku miejscach wypisz raz).
* Kolejność wypisywania może być zgodna z pierwszym pojawieniem się w tekście (łatwe i czytelne): wypisuj przy pierwszym znalezieniu danego palindromu.
