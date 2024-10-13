---

## Zadanie 1 - Obliczenie wartości wielomianu w punkcie

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz listę współczynników wielomianu w postaci \( a_nx^n + a_{n-1}x^{n-1} + \dots + a_0 \) oraz liczbę \( x \). Oblicz wartość tego wielomianu w podanym punkcie \( x \).

### Dane wejściowe

- **Liczba naturalna \( n \geq 0 \)** — stopień wielomianu.
- **Lista \( n+1 \) liczb całkowitych** — współczynniki wielomianu w kolejności od najwyższej potęgi:
  \[ [a_n, a_{n-1}, \dots, a_0] \]
- **Liczba całkowita \( x \)** — punkt, w którym należy obliczyć wartość wielomianu.

### Dane wyjściowe

- **Jedna liczba całkowita** — wartość wielomianu w punkcie \( x \).

### Przykład

- **Dane wejściowe**:
  ```
  2
  3 2 1
  1
  ```
- **Oczekiwane wyjście**:
  ```
  6
  ```

**Objaśnienie**:

Wielomian: \( 3x^2 + 2x + 1 \). Dla \( x = 1 \) wartość wynosi \( 3 \times 1^2 + 2 \times 1 + 1 = 6 \).

### Wskazówki

- Użyj schematu Hornera lub sumuj iloczyny współczynników i odpowiednich potęg \( x \).

---

## Zadanie 2 - Obliczenie iloczynu wielomianu przez skalar

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz listę współczynników wielomianu \( a_nx^n + a_{n-1}x^{n-1} + \dots + a_0 \) oraz liczbę \( k \). Oblicz współczynniki wielomianu powstałego w wyniku pomnożenia oryginalnego wielomianu przez skalar \( k \).

### Dane wejściowe

- **Liczba naturalna \( n \geq 0 \)** — stopień wielomianu.
- **Lista \( n+1 \) liczb całkowitych** — współczynniki oryginalnego wielomianu:
  \[ [a_n, a_{n-1}, \dots, a_0] \]
- **Liczba całkowita \( k \)** — skalar, przez który należy pomnożyć wielomian.

### Dane wyjściowe

- **Lista \( n+1 \) liczb całkowitych** — współczynniki nowego wielomianu po mnożeniu przez \( k \).

### Przykład

- **Dane wejściowe**:
  ```
  2
  4 -3 2
  -2
  ```
- **Oczekiwane wyjście**:
  ```
  -8 6 -4
  ```

**Objaśnienie**:

Oryginalny wielomian: \( 4x^2 - 3x + 2 \).

Po pomnożeniu przez \( -2 \) otrzymujemy: \( -8x^2 + 6x - 4 \).

### Wskazówki

- Pomnóż każdy współczynnik wielomianu przez liczbę \( k \).

---

## Zadanie 3 - Obliczenie sumy wielomianów

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz dwie listy współczynników dwóch wielomianów \( a(x) \) i \( b(x) \). Oblicz współczynniki wielomianu będącego sumą tych dwóch wielomianów.

### Dane wejściowe

- **Liczba naturalna \( n \geq 0 \)** — stopień pierwszego wielomianu.
- **Lista \( n+1 \) liczb całkowitych** — współczynniki pierwszego wielomianu:
  \[ [a_n, a_{n-1}, \dots, a_0] \]
- **Liczba naturalna \( m \geq 0 \)** — stopień drugiego wielomianu.
- **Lista \( m+1 \) liczb całkowitych** — współczynniki drugiego wielomianu:
  \[ [b_m, b_{m-1}, \dots, b_0] \]

### Dane wyjściowe

- **Lista liczb całkowitych** — współczynniki sumy wielomianów, zaczynając od najwyższej potęgi.

### Przykład

- **Dane wejściowe**:
  ```
  2
  3 5 2
  2
  2 -8 1
  ```
- **Oczekiwane wyjście**:
  ```
  5 -3 3
  ```

**Objaśnienie**:

Pierwszy wielomian: \( 3x^2 + 5x + 2 \).

Drugi wielomian: \( 2x^2 - 8x + 1 \).

Suma: \( (3+2)x^2 + (5+(-8))x + (2+1) = 5x^2 - 3x + 3 \).

### Wskazówki

- Dostosuj długości list współczynników, dodając zera tam, gdzie to konieczne.

---

## Zadanie 4 - Mnożenie wielomianów

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz dwie listy współczynników dwóch wielomianów \( a(x) \) i \( b(x) \). Oblicz współczynniki wielomianu będącego iloczynem tych dwóch wielomianów.

### Dane wejściowe

- **Liczba naturalna \( n \geq 0 \)** — stopień pierwszego wielomianu.
- **Lista \( n+1 \) liczb całkowitych** — współczynniki pierwszego wielomianu:
  \[ [a_n, a_{n-1}, \dots, a_0] \]
- **Liczba naturalna \( m \geq 0 \)** — stopień drugiego wielomianu.
- **Lista \( m+1 \) liczb całkowitych** — współczynniki drugiego wielomianu:
  \[ [b_m, b_{m-1}, \dots, b_0] \]

### Dane wyjściowe

- **Lista liczb całkowitych** — współczynniki iloczynu wielomianów, zaczynając od najwyższej potęgi.

### Przykład

- **Dane wejściowe**:
  ```
  3
  5 0 10 6
  2
  1 2 4
  ```
- **Oczekiwane wyjście**:
  ```
  5 10 30 26 52 24
  ```

**Objaśnienie**:

Pierwszy wielomian: \( 5x^3 + 0x^2 + 10x + 6 \).

Drugi wielomian: \( x^2 + 2x + 4 \).

Iloczyn wielomianów daje wielomian stopnia \( 5 \).

### Wskazówki

- Mnożenie wielomianów polega na sumowaniu iloczynów współczynników, przy dodawaniu potęg \( x \).

---

## Zadanie 5 - Obliczenie \( n \)-tej pochodnej wielomianu

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz listę współczynników wielomianu \( a(x) = a_nx^n + a_{n-1}x^{n-1} + \dots + a_0 \) oraz liczbę naturalną \( k \). Oblicz współczynniki wielomianu będącego \( k \)-tą pochodną funkcji \( a(x) \).

### Dane wejściowe

- **Liczba naturalna \( n \geq 0 \)** — stopień wielomianu.
- **Lista \( n+1 \) liczb całkowitych** — współczynniki wielomianu:
  \[ [a_n, a_{n-1}, \dots, a_0] \]
- **Liczba naturalna \( k \geq 1 \)** — rząd pochodnej do obliczenia.

### Dane wyjściowe

- **Lista liczb całkowitych** — współczynniki \( k \)-tej pochodnej wielomianu, zaczynając od najwyższej potęgi.
- Jeśli po \( k \)-tym różniczkowaniu wielomian zniknie (wszystkie współczynniki będą zero), wypisz pustą listę.

### Przykład

- **Dane wejściowe**:
  ```
  2
  4 -3 2
  1
  ```
- **Oczekiwane wyjście**:
  ```
  8 -3
  ```

**Objaśnienie**:

Oryginalny wielomian: \( 4x^2 - 3x + 2 \).

Pierwsza pochodna: \( (2 \times 4)x^{2-1} - 3 = 8x - 3 \).

### Wskazówki

- Stosuj wzór na pochodną jednomianu: \( \frac{d}{dx} (a_nx^n) = n \times a_n x^{n-1} \).
- Powtórz proces różniczkowania \( k \) razy.

---

## Zadanie 6 - Obliczenie miejsc zerowych równania kwadratowego

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz współczynniki równania kwadratowego \( ax^2 + bx + c = 0 \). Znajdź rzeczywiste miejsca zerowe tego równania.

### Dane wejściowe

- **Trzy liczby całkowite** — współczynniki \( a \), \( b \) i \( c \), podane w jednej linii, oddzielone spacjami.

### Dane wyjściowe

- **Lista liczb zmiennoprzecinkowych** — rzeczywiste pierwiastki równania, posortowane rosnąco.
- Jeśli równanie ma jeden pierwiastek podwójny, wypisz go raz.
- Jeśli brak rzeczywistych pierwiastków, wypisz pustą listę `[]`.

### Przykład

- **Dane wejściowe**:
  ```
  1 2 1
  ```
- **Oczekiwane wyjście**:
  ```
  [-1.0]
  ```

**Objaśnienie**:

Równanie: \( x^2 + 2x + 1 = 0 \).

Delta: \( \Delta = 2^2 - 4 \times 1 \times 1 = 0 \).

Pierwiastek: \( x = \frac{-2}{2 \times 1} = -1.0 \).

### Wskazówki

- Oblicz deltę \( \Delta = b^2 - 4ac \).
- Zastosuj wzory na pierwiastki w zależności od wartości delty.

---
