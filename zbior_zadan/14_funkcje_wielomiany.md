# Rozdział: Funkcje — wielomiany

Poniższe zadania dotyczą implementacji **funkcji** operujących na wielomianach zapisanych jako lista współczynników w kolejności od najwyższej potęgi do wyrazu wolnego:
`[a_n, a_{n-1}, ..., a_0]` oznacza wielomian `a_n x^n + a_{n-1} x^{n-1} + ... + a_0`.

**Konwencje wspólne:**

* Każdy podpunkt to osobna funkcja (możesz też robić osobne programy testujące – ale zadanie dotyczy funkcji).
* Współczynniki mogą być ujemne (czyli w praktyce: liczby całkowite).
* Dla wyniku jako listy: zwracaj listę współczynników w tym samym formacie (od najwyższej potęgi).
* Jeśli wynikowy wielomian ma wiodące zera, można je usuwać, ale **zostaw przynajmniej jedno zero**, jeśli cały wielomian jest zerowy (np. `[0]`).

---

## ZAD-01 — Wartość wielomianu w punkcie

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `wielomiany`, `Horner`

### Treść

Napisz funkcję, która otrzymuje listę współczynników wielomianu `a` oraz liczbę `x`, a następnie zwraca wartość wielomianu w punkcie `x`.

### Wejście (argumenty funkcji)

* `a` — lista współczynników `[a_n, ..., a_0]`
* `x` — liczba naturalna (lub całkowita)

### Wyjście (zwracana wartość)

* jedna liczba (całkowita)

### Przykład

Dla `a = [3, 2, 1]` i `x = 1` funkcja zwraca:
`6`

### Uwagi

* Najprościej użyć schematu Hornera.

---

## ZAD-02 — Iloczyn wielomianu przez skalar

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `wielomiany`, `skalar`

### Treść

Napisz funkcję, która otrzymuje listę współczynników wielomianu `a` oraz liczbę `k`, a następnie zwraca współczynniki wielomianu powstałego z pomnożenia każdego współczynnika przez `k`.

### Wejście (argumenty funkcji)

* `a` — lista współczynników `[a_n, ..., a_0]`
* `k` — liczba (całkowita)

### Wyjście (zwracana wartość)

* lista współczynników wielomianu `k * P(x)`

### Przykład

Dla `a = [4, -3, 2]` i `k = -2` funkcja zwraca:
`[-8, 6, -4]`

---

## ZAD-03 — Suma wielomianów

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `wielomiany`, `listy`

### Treść

Napisz funkcję, która otrzymuje dwie listy współczynników wielomianów `a` i `b` (mogą mieć różne stopnie) i zwraca współczynniki wielomianu będącego ich sumą.

### Wejście (argumenty funkcji)

* `a` — lista `[a_n, ..., a_0]`
* `b` — lista `[b_m, ..., b_0]`

### Wyjście (zwracana wartość)

* lista współczynników `a + b` w tej samej konwencji

### Przykład

Dla `a = [3, 5, 2]` i `b = [2, -8, 1]` funkcja zwraca:
`[5, -3, 3]`

### Uwagi

* Jeśli listy mają różne długości, wyrównaj je od końca (od wyrazu wolnego).

---

## ZAD-04 — Mnożenie wielomianów

**Poziom:** ★★☆
**Tagi:** `funkcje`, `wielomiany`, `konwolucja`

### Treść

Napisz funkcję, która otrzymuje dwie listy współczynników wielomianów `a` i `b` i zwraca listę współczynników wielomianu będącego ich iloczynem.

### Wejście (argumenty funkcji)

* `a` — lista `[a_n, ..., a_0]`
* `b` — lista `[b_m, ..., b_0]`

### Wyjście (zwracana wartość)

* lista współczynników wielomianu `a * b` (długość `len(a)+len(b)-1`)

### Przykład

Dla `a = [5, 0, 10, 6]` oraz `b = [1, 2, 4]` funkcja zwraca:
`[5, 10, 30, 26, 52, 24]`

---

## ZAD-05 — k-ta pochodna wielomianu

**Poziom:** ★★☆
**Tagi:** `funkcje`, `pochodna`, `wielomiany`

### Treść

Napisz funkcję, która otrzymuje listę współczynników wielomianu `a` oraz liczbę naturalną `k` i zwraca współczynniki wielomianu będącego **k-tą pochodną**.

### Wejście (argumenty funkcji)

* `a` — lista `[a_n, ..., a_0]`
* `k` — liczba naturalna

### Wyjście (zwracana wartość)

* lista współczynników wielomianu po zróżniczkowaniu `k` razy

### Przykład

Dla `a = [4, -3, 2]` oraz `k = 1` funkcja zwraca:
`[8, -3]`

### Uwagi

* Jeśli `k` jest większe niż stopień wielomianu, wynikiem jest wielomian zerowy: `[0]`.

---

## ZAD-06 — Miejsca zerowe równania kwadratowego (rzeczywiste)

**Poziom:** ★★☆
**Tagi:** `funkcje`, `delta`, `pierwiastki`

### Treść

Napisz funkcję, która otrzymuje listę współczynników równania kwadratowego `[a, b, c]` dla `a x^2 + b x + c` i zwraca listę **rzeczywistych** miejsc zerowych.

### Wejście (argumenty funkcji)

* `coef` — lista trzech liczb `[a, b, c]`

### Wyjście (zwracana wartość)

* lista liczb zmiennoprzecinkowych:

  * jeśli `Δ < 0` → pusta lista `[]`
  * jeśli `Δ = 0` → dwa jednakowe pierwiastki `[x, x]`
  * jeśli `Δ > 0` → dwa pierwiastki `[x1, x2]` (kolejność dowolna)

### Przykład

Dla `[1, 2, 1]` funkcja zwraca:
`[-1.0, -1.0]`

### Ograniczenia / gwarancje

* Zakładamy `a ≠ 0` (to naprawdę równanie kwadratowe).

### Uwagi

* Licz `Δ = b^2 - 4ac`.
* Pierwiastki: `(-b ± sqrt(Δ)) / (2a)`.
