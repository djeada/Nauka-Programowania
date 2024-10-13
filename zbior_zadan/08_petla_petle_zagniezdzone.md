# Pętla - Pętle Zagnieżdżone

## Zadanie 1 - Kwadrat

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz program, który dla podanej liczby naturalnej \( n \) wypisze kwadrat o boku długości \( n \), zbudowany z gwiazdek (\( * \)).

### Dane wejściowe

- Jedna liczba naturalna \( n \) (\( n \geq 1 \)).

### Dane wyjściowe

- Kwadrat o boku \( n \), złożony z gwiazdek. Każdy wiersz powinien zawierać \( n \) gwiazdek bez odstępów.
- Każdy wiersz kwadratu powinien być wypisany w osobnej linii.

### Przykład

- **Dane wejściowe**:
  ```
  2
  ```
- **Oczekiwane wyjście**:
  ```
  **
  **
  ```

### Wskazówki

- Użyj dwóch zagnieżdżonych pętli: zewnętrznej dla wierszy i wewnętrznej dla kolumn.
- W każdej iteracji pętli zewnętrznej wypisz jeden wiersz gwiazdek.

---

## Zadanie 2 - Trójkąt prostokątny równoboczny

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz program, który dla podanej liczby naturalnej \( n \) wypisze trójkąt prostokątny równoramienny o wysokości \( n \), zbudowany z gwiazdek (\( * \)).

### Dane wejściowe

- Jedna liczba naturalna \( n \) (\( n \geq 1 \)).

### Dane wyjściowe

- Trójkąt, w którym w pierwszym wierszu jest jedna gwiazdka, w drugim dwie, aż do \( n \) gwiazdek w ostatnim wierszu.
- Każdy wiersz trójkąta powinien być wypisany w osobnej linii.

### Przykład

- **Dane wejściowe**:
  ```
  3
  ```
- **Oczekiwane wyjście**:
  ```
  *
  **
  ***
  ```

### Wskazówki

- Użyj pętli, w której numer wiersza odpowiada liczbie gwiazdek do wypisania w tym wierszu.

---

## Zadanie 3 - Odwrócony trójkąt prostokątny równoboczny

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz program, który dla podanej liczby naturalnej \( n \) wypisze odwrócony trójkąt prostokątny równoramienny o wysokości \( n \), zaczynając od podstawy.

### Dane wejściowe

- Jedna liczba naturalna \( n \) (\( n \geq 1 \)).

### Dane wyjściowe

- Trójkąt, w którym w pierwszym wierszu jest \( n \) gwiazdek, w drugim \( n - 1 \), aż do jednej gwiazdki w ostatnim wierszu.
- Każdy wiersz trójkąta powinien być wypisany w osobnej linii.

### Przykład

- **Dane wejściowe**:
  ```
  4
  ```
- **Oczekiwane wyjście**:
  ```
  ****
  ***
  **
  *
  ```

### Wskazówki

- Użyj pętli, która w każdej iteracji zmniejsza liczbę gwiazdek o jeden.

---

## Zadanie 4 - Tabliczka mnożenia

**Poziom trudności**: ★★☆

### Treść zadania

Napisz program, który dla podanej liczby naturalnej \( N \) wypisze tabliczkę mnożenia o wymiarach \( N \times N \).

### Dane wejściowe

- Jedna liczba naturalna \( N \) (\( N \geq 1 \)).

### Dane wyjściowe

- Tabliczka mnożenia składająca się z \( N \) wierszy i \( N \) kolumn.
- Wartości w tabliczce powinny być liczbami całkowitymi, a liczby w wierszu powinny być oddzielone spacjami.
- Każdy wiersz powinien być wypisany w osobnej linii.

### Przykład

- **Dane wejściowe**:
  ```
  3
  ```
- **Oczekiwane wyjście**:
  ```
  1 2 3
  2 4 6
  3 6 9
  ```

### Wskazówki

- Użyj zagnieżdżonych pętli: zewnętrznej dla wierszy i wewnętrznej dla kolumn.
- Wartość w komórce to iloczyn numeru wiersza i kolumny.
- Zadbaj o formatowanie wyjścia, aby tabliczka była czytelna.

---

## Zadanie 5 - Litera X

**Poziom trudności**: ★★☆

### Treść zadania

Napisz program, który dla podanej liczby naturalnej \( n \) wypisze literę "X" o wysokości \( n \), zbudowaną z gwiazdek (\( * \)).

### Dane wejściowe

- Jedna liczba naturalna \( n \) (\( n \geq 3 \)).

### Dane wyjściowe

- Litera "X" o wysokości \( n \), gdzie gwiazdki są umieszczone na przekątnych.
- Każdy wiersz powinien być wypisany w osobnej linii.

### Przykład

- **Dane wejściowe**:
  ```
  5
  ```
- **Oczekiwane wyjście**:
  ```
  *   *
   * *
    *
   * *
  *   *
  ```

### Wskazówki

- Użyj zagnieżdżonych pętli do iteracji przez wiersze i kolumny.
- Wypisz gwiazdkę, gdy indeks kolumny jest równy indeksowi wiersza lub gdy suma indeksów wiersza i kolumny wynosi \( n - 1 \).
- W pozostałych miejscach wypisz spację.

---

## Zadanie 6 - Litera Z

**Poziom trudności**: ★★☆

### Treść zadania

Napisz program, który dla podanej liczby naturalnej \( n \) wypisze literę "Z" o wysokości \( n \), zbudowaną z gwiazdek (\( * \)).

### Dane wejściowe

- Jedna liczba naturalna \( n \) (\( n \geq 3 \)).

### Dane wyjściowe

- Litera "Z" o wysokości \( n \), gdzie górna i dolna linia oraz przekątna są zbudowane z gwiazdek.
- Każdy wiersz powinien być wypisany w osobnej linii.

### Przykład

- **Dane wejściowe**:
  ```
  5
  ```
- **Oczekiwane wyjście**:
  ```
  *****
     *
    *
   *
  *****
  ```

### Wskazówki

- W pierwszym i ostatnim wierszu wypisz \( n \) gwiazdek.
- W wierszach pomiędzy wypisz gwiazdkę w odpowiednim miejscu przekątnej.
- Użyj zagnieżdżonych pętli i warunków do określenia, kiedy wypisać gwiazdkę, a kiedy spację.

---

## Zadanie 7 - Choinka

**Poziom trudności**: ★★☆

### Treść zadania

Napisz program, który dla podanej liczby naturalnej \( N \) wypisze choinkę złożoną z \( N \) trójkątów ustawionych jeden na drugim. Wysokość pierwszego trójkąta to 1, a wysokość każdego kolejnego jest o 1 większa od poprzedniego.

### Dane wejściowe

- Jedna liczba naturalna \( N \) (\( N \geq 1 \)).

### Dane wyjściowe

- Choinka złożona z \( N \) trójkątów, gdzie każdy trójkąt jest zbudowany z gwiazdek (\( * \)).
- Każdy wiersz powinien być wypisany w osobnej linii.

### Przykład

- **Dane wejściowe**:
  ```
  3
  ```
- **Oczekiwane wyjście**:
  ```
  *
  *
  **
  *
  **
  ***
  ```

### Wskazówki

- Użyj pętli do generowania kolejnych trójkątów.
- Wysokość każdego trójkąta zwiększa się o 1.
- W każdej iteracji generuj trójkąt o odpowiedniej wysokości.

---

## Zadanie 8 - Trójkąt Pascala

**Poziom trudności**: ★★☆

### Treść zadania

Napisz program, który dla podanej liczby naturalnej \( n \) wypisze trójkąt Pascala o wysokości \( n \).

### Dane wejściowe

- Jedna liczba naturalna \( n \) (\( n \geq 1 \)).

### Dane wyjściowe

- Trójkąt Pascala o wysokości \( n \), gdzie każdy wiersz zawiera odpowiednie współczynniki dwumianowe.
- Każdy wiersz powinien być wypisany w osobnej linii, a liczby w wierszu powinny być oddzielone spacjami.

### Przykład

- **Dane wejściowe**:
  ```
  3
  ```
- **Oczekiwane wyjście**:
  ```
  1
  1 1
  1 2 1
  ```

### Wskazówki

- Użyj list do przechowywania poprzedniego wiersza trójkąta.
- W każdym wierszu oblicz kolejne wartości na podstawie sumy dwóch liczb nad nim.
- Możesz korzystać ze wzoru na współczynniki dwumianowe.

---

## Zadanie 9 - N pierwszych liczb pierwszych

**Poziom trudności**: ★★☆

### Treść zadania

Napisz program, który dla podanej liczby naturalnej \( N \) wypisze pierwsze \( N \) liczb pierwszych.

### Dane wejściowe

- Jedna liczba naturalna \( N \) (\( N \geq 1 \)).

### Dane wyjściowe

- Pierwsze \( N \) liczb pierwszych, oddzielone spacjami lub przecinkami.
- Wszystkie liczby powinny być wypisane w jednej linii.

### Przykład

- **Dane wejściowe**:
  ```
  5
  ```
- **Oczekiwane wyjście**:
  ```
  2 3 5 7 11
  ```

### Wskazówki

- Użyj pętli, aby znaleźć kolejne liczby pierwsze.
- Sprawdzaj podzielność liczby przez liczby mniejsze lub równe jej pierwiastkowi kwadratowemu.
- Kontynuuj, aż znajdziesz \( N \) liczb pierwszych.

---
