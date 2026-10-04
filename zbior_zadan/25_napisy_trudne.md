# Rozdział 25: Napisy — zadania dodatkowe

Trudniejsze zadania na napisach: samodzielna zamiana i usuwanie fragmentów, przedrostki, kodowanie RLE, rotacje, szukanie najdłuższych powtórzeń i wspólnych fragmentów (programowanie dynamiczne) oraz sprawdzanie nawiasów za pomocą stosu. Spróbuj rozwiązywać je własnymi pętlami, bez gotowych metod w rodzaju `replace` czy `startswith` — właśnie o to w nich chodzi.

**Konwencje wspólne:**

* Każde zadanie to osobny program: czyta **standardowe wejście** i wypisuje wynik na **standardowe wyjście**.
* Program nie wypisuje komunikatów typu „Podaj napis:”. Tekst podany w `input("…")` jest ignorowany przez sprawdzarkę.
* Każdy napis zajmuje jedną całą linię wejścia, razem ze spacjami — wczytuj go przez `input()`, bez `strip()` i `split()`.
* Wielkość liter ma znaczenie (`A` i `a` to różne znaki), a spacja też jest znakiem.
* **Podnapis** to ciągły fragment napisu, np. `kot` jest podnapisem `kotlet`, a `ket` — nie.
* Pozycje znaków (indeksy) liczymy od `0`, tak jak w Pythonie.
* Odpowiedzi logiczne wypisuj jako `Prawda` albo `Fałsz` (o ile zadanie nie mówi inaczej).

---

## ZAD-01 — Podmiana słowa w zdaniu

**Poziom:** ★★☆
**Tagi:** `string`, `replace`, `substring`

### Treść

Otrzymujesz zdanie `S` oraz dwa napisy `A` i `B`. Zamień **wszystkie wystąpienia** napisu `A` w zdaniu na napis `B`. `A` może być częścią dłuższych słów — zamieniamy każde wystąpienie podnapisu.

Wystąpienia szukamy od lewej do prawej. Po każdej zamianie szukanie trwa dalej **za zamienionym fragmentem**, więc wystąpienia nie nakładają się na siebie, a wstawiony napis `B` nie jest ponownie przeszukiwany. Na przykład w `aaa` zamiana `aa` na `b` daje `ba`, a w `ab` zamiana `a` na `aa` daje `aab`.

### Wejście

* 1. linia: zdanie `S`
* 2. linia: napis `A` (szukany)
* 3. linia: napis `B` (wstawiany)

### Wyjście

Jedna linia: zdanie po zamianie.

### Ograniczenia

* `1 ≤ |S| ≤ 1000`
* `1 ≤ |A|, |B| ≤ 100` (żaden z napisów nie jest pusty)

### Przykład

**Wejście:**

```
Lezy jezy na wiezy
zy
rzy
```

**Wyjście:**

```
Lerzy jerzy na wierzy
```

### Uwagi

* Spróbuj nie używać metody `replace`: przechodź po zdaniu indeksem `i` i sprawdzaj, czy w tym miejscu zaczyna się `A` (np. porównując wycinek `S[i:i + len(A)]` z `A`). Jeśli tak — dopisz do wyniku `B` i przeskocz o `len(A)` znaków; jeśli nie — dopisz bieżący znak i przejdź o jeden dalej.

---

## ZAD-02 — Usuń podnapis

**Poziom:** ★★☆
**Tagi:** `string`, `replace`, `substring`

### Treść

Otrzymujesz napis `S` i napis `T`. Usuń z `S` **wszystkie wystąpienia** podnapisu `T`.

Wystąpienia szukamy od lewej do prawej, a usuwanie wykonujemy **jednokrotnie** (jednym przejściem): fragmenty, które dopiero po usunięciu „skleją się” w nowe wystąpienie `T`, zostają. Na przykład usunięcie `ab` z `aabb` daje `ab`, a usunięcie `aa` z `aaa` daje `a`.

### Wejście

* 1. linia: napis `S`
* 2. linia: napis `T` (do usunięcia)

### Wyjście

Jedna linia: napis po usunięciu wszystkich wystąpień `T`. Jeśli nic nie zostało, wypisz pustą linię.

### Ograniczenia

* `1 ≤ |S| ≤ 1000`
* `1 ≤ |T| ≤ 100`

### Przykład

**Wejście:**

```
Lezy jezy na wiezy
zy
```

**Wyjście:**

```
Le je na wie
```

### Uwagi

* To samo przejście co w poprzednim zadaniu, tylko zamiast wstawiać nowy napis — po prostu przeskakujesz znalezione wystąpienie.

---

## ZAD-03 — Czy napis A jest początkiem napisu B?

**Poziom:** ★☆☆
**Tagi:** `string`, `prefix`

### Treść

Otrzymujesz napisy `A` i `B`. Sprawdź, czy `B` **zaczyna się** od `A`, czyli czy `A` jest przedrostkiem `B`. Każdy napis jest swoim własnym przedrostkiem, a napis dłuższy od `B` nie może być jego przedrostkiem.

### Wejście

* 1. linia: napis `A`
* 2. linia: napis `B`

### Wyjście

`Prawda`, jeśli `B` zaczyna się od `A`, w przeciwnym razie `Fałsz`.

### Ograniczenia

* `1 ≤ |A|, |B| ≤ 1000`

### Przykład

**Wejście:**

```
Dino
Dinozaur jest zly
```

**Wyjście:**

```
Prawda
```

### Uwagi

* Spróbuj porównywać znaki w pętli, bez metody `startswith`. Pamiętaj, żeby najpierw sprawdzić długości — inaczej przy `A` dłuższym od `B` wyjdziesz poza zakres napisu.

---

## ZAD-05 — Kodowanie długości serii (RLE)

**Poziom:** ★★☆
**Tagi:** `string`, `compress`, `run-length`

### Treść

**Kodowanie długości serii** (ang. *run-length encoding*, RLE) to prosta metoda kompresji. Każdą **serię** jednakowych znaków stojących bezpośrednio obok siebie zapisujemy jako ten znak, a zaraz po nim liczbę jego powtórzeń (w zapisie dziesiętnym, więc może mieć kilka cyfr). Na przykład `aaabcc` koduje się jako `a3b1c2`, a dwanaście liter `x` pod rząd — jako `x12`.

Zakoduj podany napis metodą RLE. Ten sam znak może tworzyć kilka oddzielnych serii — każdą kodujemy osobno.

### Wejście

Jedna linia: napis `S` złożony wyłącznie z liter alfabetu angielskiego (wielkość liter ma znaczenie).

### Wyjście

Jedna linia: zakodowany napis.

### Ograniczenia

* `1 ≤ |S| ≤ 1000`

### Przykład

**Wejście:**

```
AAAAAAAAAABBBBBBBBA
```

**Wyjście:**

```
A10B8A1
```

Napis składa się z trzech serii: dziesięciu liter `A`, ośmiu liter `B` i jednej litery `A`.

### Uwagi

* Przechodź po napisie i licz, ile razy z rzędu powtarza się bieżący znak. Gdy seria się kończy (następny znak jest inny albo napis się skończył), dopisz do wyniku znak i licznik zamieniony na napis (`str(licznik)`).

---

## ZAD-06 — Rotacje napisów

**Poziom:** ★★☆
**Tagi:** `string`, `rotation`, `substring`

### Treść

Otrzymujesz dwa napisy `A` i `B`. Sprawdź, czy `B` jest **rotacją** (przesunięciem cyklicznym) napisu `A`, czyli czy da się go otrzymać, przenosząc pewną liczbę początkowych znaków `A` (być może zero) na koniec. Na przykład rotacjami napisu `abcd` są `abcd`, `bcda`, `cdab` i `dabc`.

Napisy różnej długości nigdy nie są swoimi rotacjami, a każdy napis jest rotacją samego siebie.

### Wejście

* 1. linia: napis `A`
* 2. linia: napis `B`

### Wyjście

`Prawda`, jeśli `B` jest rotacją `A`, w przeciwnym razie `Fałsz`.

### Ograniczenia

* `1 ≤ |A|, |B| ≤ 1000`

### Przykład

**Wejście:**

```
malpka
pkamal
```

**Wyjście:**

```
Prawda
```

`pkamal` powstaje z `malpka` przez przeniesienie początkowych `mal` na koniec.

### Uwagi

* Każda rotacja `A` jest podnapisem napisu `A + A`. Wystarczy więc porównać długości i sprawdzić, czy `B` występuje w `A + A`.

---

## ZAD-07 — Najdłuższy powtarzający się podnapis

**Poziom:** ★★★
**Tagi:** `string`, `substrings`, `dp`

### Treść

Otrzymujesz napis. Znajdź **najdłuższy podnapis, który występuje w nim co najmniej dwa razy**. Wystąpienia mogą na siebie nachodzić — na przykład w napisie `aaaa` podnapis `aaa` występuje dwa razy (od indeksu 0 i od indeksu 1).

* Jeśli kilka różnych podnapisów ma tę samą, maksymalną długość — wypisz ten, którego **pierwsze wystąpienie zaczyna się najwcześniej**.
* Jeśli żaden znak się nie powtarza (nie ma powtarzającego się podnapisu) — wypisz pustą linię.

### Wejście

Jedna linia: napis `S`.

### Wyjście

Jedna linia: najdłuższy powtarzający się podnapis albo pusta linia.

### Ograniczenia

* `1 ≤ |S| ≤ 1000`

### Przykład

**Wejście:**

```
pythonpython
```

**Wyjście:**

```
python
```

### Przykład 2

**Wejście:**

```
cdabxabycd
```

**Wyjście:**

```
cd
```

Podnapisy `cd` i `ab` powtarzają się i oba mają długość 2, ale `cd` występuje po raz pierwszy wcześniej (od indeksu 0), a `ab` — dopiero od indeksu 2.

### Uwagi

* Programowanie dynamiczne: niech `w[i][j]` (dla `i < j`) oznacza długość najdłuższego wspólnego początku fragmentów `S[i:]` i `S[j:]`. Jeśli `S[i] == S[j]`, to `w[i][j] = w[i + 1][j + 1] + 1`, w przeciwnym razie `0`. Wynikiem jest największa wartość w tablicy. Jeśli przeglądasz pary `(i, j)` w kolejności rosnącego `i` i zmieniasz wynik tylko na ściśle dłuższy, remisy rozstrzygną się same. Czas $O(n^2)$.
* Sprawdzanie każdego podnapisu (jest ich około $n^2/2$) z osobnym wyszukiwaniem w całym napisie daje czas $O(n^3)$ — przy długich napisach to za dużo.

---

## ZAD-08 — Najdłuższy wspólny przedrostek

**Poziom:** ★★★
**Tagi:** `string`, `prefix`, `list`

### Treść

Otrzymujesz `n` napisów. Znajdź ich **najdłuższy wspólny przedrostek**, czyli najdłuższy napis, od którego zaczynają się wszystkie podane napisy. Jeśli napisy nie mają wspólnego przedrostka (np. zaczynają się od różnych liter), wynikiem jest napis pusty — wypisz wtedy pustą linię.

### Wejście

* 1. linia: `n` — liczba napisów
* kolejne `n` linii: napisy (każdy w osobnej linii)

### Wyjście

Jedna linia: najdłuższy wspólny przedrostek (albo pusta linia).

### Ograniczenia

* `1 ≤ n ≤ 100`
* każdy napis ma od 1 do 100 znaków

### Przykład

**Wejście:**

```
3
Remolada
Remux
Remmy
```

**Wyjście:**

```
Rem
```

### Uwagi

* Przy jednym napisie wynikiem jest cały ten napis.
* Wygodnie jest zacząć od pierwszego napisu jako kandydata i skracać go, porównując po kolei z każdym kolejnym napisem.

---

## ZAD-09 — Najdłuższy wspólny podnapis

**Poziom:** ★★★
**Tagi:** `string`, `dp`, `substring`

### Treść

Otrzymujesz dwa napisy `A` i `B`. Znajdź ich **najdłuższy wspólny podnapis**, czyli najdłuższy ciągły fragment, który występuje zarówno w `A`, jak i w `B`.

* Jeśli kilka różnych podnapisów ma tę samą, maksymalną długość — wypisz ten, który w napisie `A` **zaczyna się najwcześniej**.
* Jeśli napisy nie mają ani jednego wspólnego znaku — wypisz pustą linię.

### Wejście

* 1. linia: napis `A`
* 2. linia: napis `B`

### Wyjście

Jedna linia: najdłuższy wspólny podnapis albo pusta linia.

### Ograniczenia

* `1 ≤ |A|, |B| ≤ 1000`

### Przykład

**Wejście:**

```
ijkabcdl
xxxxabcd
```

**Wyjście:**

```
abcd
```

### Przykład 2

**Wejście:**

```
xyab
abxy
```

**Wyjście:**

```
xy
```

Oba podnapisy `xy` i `ab` mają długość 2; w `A` wcześniej zaczyna się `xy`.

### Uwagi

* Programowanie dynamiczne: niech `d[i][j]` oznacza długość najdłuższego wspólnego fragmentu **kończącego się** na znakach `A[i - 1]` i `B[j - 1]`. Jeśli te znaki są równe, `d[i][j] = d[i - 1][j - 1] + 1`, w przeciwnym razie `0`. Największa wartość w tablicy to długość wyniku. Czas $O(|A| \cdot |B|)$.

---

## ZAD-10 — Poprawność nawiasów

**Poziom:** ★★☆
**Tagi:** `string`, `stack`, `nawiasy`

### Treść

Otrzymujesz napis, który oprócz dowolnych innych znaków może zawierać nawiasy trzech rodzajów: okrągłe `()`, kwadratowe `[]` i klamrowe `{}`. Pozostałe znaki pomijamy. Nawiasy są **poprawne**, jeśli każdy nawias zamykający zamyka nawias otwierający tego samego rodzaju, który został otwarty najpóźniej i jeszcze nie jest zamknięty, a na końcu napisu żaden nawias nie zostaje otwarty. Na przykład `{[()()]}` i `a(b)[c]` są poprawne, a `([)]`, `(()` i `())` — nie.

Sprawdź napis, czytając go od lewej do prawej:

* jeśli trafisz na nawias zamykający, dla którego nie ma żadnego otwartego nawiasu albo ostatnio otwarty nawias jest innego rodzaju — **błąd jest na pozycji tego nawiasu zamykającego** (dalszej części napisu już nie sprawdzamy),
* jeśli dojdziesz do końca bez takiego błędu, ale niektóre nawiasy pozostały otwarte — **błąd jest na pozycji pierwszego (najbardziej na lewo) niezamkniętego nawiasu otwierającego**.

### Wejście

Jedna linia: napis `S`.

### Wyjście

`Tak`, jeśli nawiasy są poprawne; w przeciwnym razie pozycja (indeks liczony od `0`) pierwszego błędu.

### Ograniczenia

* `1 ≤ |S| ≤ 1000`

### Przykład

**Wejście:**

```
a(b[c]{d}e)f
```

**Wyjście:**

```
Tak
```

### Przykład 2

**Wejście:**

```
(a[b)c]
```

**Wyjście:**

```
4
```

Nawias `)` na pozycji 4 zamyka ostatnio otwarty nawias `[`, czyli nawias innego rodzaju.

### Przykład 3

**Wejście:**

```
((x)(
```

**Wyjście:**

```
0
```

Na końcu otwarte zostają nawiasy z pozycji 0 i 4 — pierwszy z nich jest na pozycji 0.

### Uwagi

* Do tego zadania służy **stos**: struktura, do której dokładamy elementy na wierzch i zdejmujemy je z wierzchu (ostatni włożony wychodzi pierwszy). W Pythonie stosem jest zwykła lista: `append` kładzie element na wierzch, `stos[-1]` podgląda wierzch, a `pop()` go zdejmuje:

  ```python
  stos = []
  stos.append(3)   # stos: [3]
  stos.append(7)   # stos: [3, 7]
  print(stos[-1])  # 7 — wierzch stosu
  stos.pop()       # zdejmuje 7, stos: [3]
  print(len(stos)) # 1
  ```

* Każdy nawias otwierający odkładaj na stos (najlepiej jego **indeks** — przyda się do zgłoszenia błędu). Przy nawiasie zamykającym sprawdź, czy stos nie jest pusty i czy na wierzchu leży nawias pasującego rodzaju; jeśli tak — zdejmij go. Pary nawiasów wygodnie trzymać w słowniku, np. `{")": "(", "]": "[", "}": "{"}`.
* Po przejściu całego napisu niezamknięte nawiasy zostają na stosie — pierwszy z nich leży na samym dole (`stos[0]`).

### Kod startowy

```python
def pierwszy_blad(napis):
    # Zwróć indeks pierwszego błędu albo -1, jeśli nawiasy są poprawne.
    return -1


napis = input()
blad = pierwszy_blad(napis)
if blad == -1:
    print("Tak")
else:
    print(blad)
```

---
