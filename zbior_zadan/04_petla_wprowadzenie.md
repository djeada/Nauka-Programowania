## Zadanie 1 - Warunek kończący pętlę

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz program, który prosi użytkownika o podanie liczby naturalnej. Program powinien kontynuować pobieranie liczb od użytkownika, dopóki użytkownik nie wprowadzi liczby **7**. Po wprowadzeniu liczby 7 program powinien zakończyć działanie bez wyświetlania dodatkowych komunikatów.

### Dane wejściowe

- Dowolna liczba liczb naturalnych (całkowitych nieujemnych), wprowadzanych pojedynczo przez użytkownika.

### Dane wyjściowe

- Brak (program nie wyświetla żadnych danych wyjściowych).

### Przykład

- **Dane wejściowe**:
  ```
  3
  10
  5
  7
  ```
- **Oczekiwane wyjście**:
  ```
  ```
  *(brak danych wyjściowych)*

### Wskazówki

- Użyj pętli `while` lub `do...while`, która będzie trwała, dopóki wprowadzona liczba nie będzie równa 7.
- Nie musisz wyświetlać żadnych komunikatów podczas działania programu.
- Upewnij się, że liczba 7 kończy pętlę i nie jest dalej przetwarzana.

---

## Zadanie 2 - Wypisywanie liczb mniejszych od podanej

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz program, który pobiera od użytkownika jedną liczbę naturalną \( n \) (większą od 0) i wypisuje wszystkie liczby naturalne mniejsze od \( n \), zaczynając od \( n - 1 \) i kończąc na 1.

### Dane wejściowe

- Jedna liczba naturalna \( n \) (\( n > 0 \)).

### Dane wyjściowe

- Kolejne liczby naturalne mniejsze od \( n \), każda w nowej linii, w kolejności malejącej.

### Przykład

- **Dane wejściowe**:
  ```
  3
  ```
- **Oczekiwane wyjście**:
  ```
  2
  1
  ```

### Wskazówki

- Użyj pętli `for` lub `while` do iteracji od \( n - 1 \) do 1.
- Upewnij się, że program poprawnie obsługuje przypadek, gdy \( n = 1 \) (wtedy nie wypisuje nic).

---

## Zadanie 3 - Wypisywanie liczby Pi z określoną dokładnością

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz program, który:

1. Pobiera od użytkownika jedną liczbę naturalną \( n \) (\( n > 0 \)).
2. Wypisuje liczbę \( \pi \) dokładnie \( n \) razy.
3. Każda wypisana wartość liczby \( \pi \) powinna mieć dokładnie \( n \) miejsc po przecinku.

### Dane wejściowe

- Jedna liczba naturalna \( n \) (\( n > 0 \)).

### Dane wyjściowe

- \( n \) wierszy, w każdym liczba \( \pi \) z dokładnością do \( n \) miejsc po przecinku.

### Przykład

- **Dane wejściowe**:
  ```
  2
  ```
- **Oczekiwane wyjście**:
  ```
  3.14
  3.14
  ```

### Wskazówki

- Użyj biblioteki matematycznej (np. `math` w Pythonie) do pobrania wartości \( \pi \).
- Do formatowania liczby \( \pi \) z określoną liczbą miejsc po przecinku możesz użyć funkcji formatowania ciągów znaków, np. `"{:.nf}".format(math.pi)`, gdzie `n` to liczba miejsc po przecinku.
- Upewnij się, że liczba miejsc po przecinku jest zgodna z wartością \( n \).

---

## Zadanie 4 - Sumowanie liczb mniejszych od podanej

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz program, który:

1. Pobiera od użytkownika jedną liczbę naturalną \( n \) (\( n \geq 1 \)).
2. Oblicza sumę wszystkich liczb naturalnych mniejszych od \( n \) (czyli od 1 do \( n - 1 \)).
3. Wypisuje obliczoną sumę.

### Dane wejściowe

- Jedna liczba naturalna \( n \) (\( n \geq 1 \)).

### Dane wyjściowe

- Jedna liczba naturalna – suma liczb od 1 do \( n - 1 \).

### Przykład

- **Dane wejściowe**:
  ```
  5
  ```
- **Oczekiwane wyjście**:
  ```
  10
  ```
  *(Ponieważ \( 1 + 2 + 3 + 4 = 10 \).)*

### Wskazówki

- Możesz użyć wzoru na sumę ciągu arytmetycznego:
  \[ S = \frac{(n - 1) \times n}{2} \]
- Upewnij się, że program poprawnie obsługuje przypadek, gdy \( n = 1 \) (wtedy suma wynosi 0).

---

## Zadanie 5 - Liczby z przedziału

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz program, który:

1. Pobiera od użytkownika dwie liczby naturalne \( a \) i \( b \).
2. Określa, która z liczb \( a \) i \( b \) jest mniejsza, a która większa.
3. Wykonuje następujące operacje:
   - **a)** Wypisuje wszystkie liczby naturalne większe od mniejszej liczby i mniejsze od większej liczby.
   - **b)** Wypisuje wszystkie liczby naturalne podzielne przez 3, które są większe od mniejszej liczby i mniejsze od większej liczby.

### Dane wejściowe

- Dwie liczby naturalne \( a \) i \( b \), każda w oddzielnej linii.

### Dane wyjściowe

- **Podpunkt a):** Wypisz liczby spełniające warunek, każda w nowej linii.
- **Podpunkt b):** Wypisz liczby podzielne przez 3 spełniające warunek, każda w nowej linii.

### Przykład

- **Dane wejściowe**:
  ```
  9
  5
  ```
- **Oczekiwane wyjście**:

  **Podpunkt a):**
  ```
  6
  7
  8
  ```

  **Podpunkt b):**
  ```
  6
  ```

### Wskazówki

- Najpierw ustal, która z liczb \( a \) i \( b \) jest mniejsza.
- Użyj pętli do iteracji od mniejszej liczby + 1 do większej liczby - 1.
- W podpunkcie b) dodatkowo sprawdzaj, czy liczba jest podzielna przez 3 (operator modulo `%`).

---

## Zadanie 6 - Sumowanie elementów ciągu

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz program, który dla podanej liczby naturalnej \( n \) oblicza i wypisuje sumę pierwszych \( n \) wyrazów ciągu \( a_n \) według poniższych wzorów:

- **a)** \( a_n = n^2 + n + 1 \)
- **b)** \( a_n = n^2 + 5n \)
- **c)** \( a_n = n + 2n \)

Wynik w każdym przypadku powinien być zaokrąglony do najbliższej liczby naturalnej (choć w tym zadaniu wyniki będą liczbami całkowitymi).

### Dane wejściowe

- Jedna liczba naturalna \( n \) (\( n \geq 1 \)).

### Dane wyjściowe

- Trzy liczby naturalne – suma \( n \) pierwszych wyrazów ciągu dla każdego podpunktu (a, b, c), każda w oddzielnej linii.

### Przykład

- **Dane wejściowe**:
  ```
  2
  ```
- **Oczekiwane wyjście**:

  **Podpunkt a):**
  ```
  10
  ```
  *(Ponieważ \( a_1 = 3 \), \( a_2 = 7 \); suma: \( 3 + 7 = 10 \).)*

  **Podpunkt b):**
  ```
  16
  ```
  *(Ponieważ \( a_1 = 6 \), \( a_2 = 10 \); suma: \( 6 + 10 = 16 \).)*

  **Podpunkt c):**
  ```
  9
  ```
  *(Ponieważ \( a_n = n + 2n = 3n \), więc \( a_1 = 3 \), \( a_2 = 6 \); suma: \( 3 + 6 = 9 \).)*

### Wskazówki

- Dla każdego podpunktu użyj pętli do sumowania wartości \( a_n \) od \( n = 1 \) do podanego \( n \).
- Upewnij się, że obliczenia są wykonywane poprawnie zgodnie z podanymi wzorami.
- Możesz użyć funkcji `round()`, jeśli zajdzie potrzeba zaokrąglenia.

---

## Zadanie 7 - Potęgowanie liczby Pi

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz program, który:

1. Pobiera od użytkownika jedną liczbę naturalną \( n \) (\( n \geq 0 \)).
2. Oblicza wartość \( \pi^n \) (liczba Pi podniesiona do potęgi \( n \)).
3. Wypisuje wynik z dokładnością do dwóch miejsc po przecinku.

### Dane wejściowe

- Jedna liczba naturalna \( n \) (\( n \geq 0 \)).

### Dane wyjściowe

- Jedna liczba zmiennoprzecinkowa – wynik \( \pi^n \) zaokrąglony do dwóch miejsc po przecinku.

### Przykład

- **Dane wejściowe**:
  ```
  1
  ```
- **Oczekiwane wyjście**:
  ```
  3.14
  ```
  *(Ponieważ \( \pi^1 = \pi \approx 3.14 \).)*

- **Dane wejściowe**:
  ```
  2
  ```
- **Oczekiwane wyjście**:
  ```
  9.87
  ```
  *(Ponieważ \( \pi^2 \approx 9.8696 \).)*

### Wskazówki

- Użyj funkcji potęgowania (np. `math.pow()` lub operatora `**`).
- Skorzystaj z biblioteki matematycznej do uzyskania wartości \( \pi \).
- Do zaokrąglenia wyniku do dwóch miejsc po przecinku użyj funkcji formatowania, np. `"{:.2f}".format(wynik)`.

---

## Zadanie 8 - Obliczanie liczby kur i owiec na farmie

**Poziom trudności**: ★★☆

### Treść zadania

Na farmie znajdują się kury i owce. Wiadomo, że:

- Łączna liczba **głów** wynosi \( a \).
- Łączna liczba **nóg** wynosi \( b \).

Napisz program, który obliczy:

- Liczbę **kur** na farmie.
- Liczbę **owiec** na farmie.

Przyjmij następujące założenia:

- Każda kura ma 1 głowę i 2 nogi.
- Każda owca ma 1 głowę i 4 nogi.
- Liczba kur i owiec jest liczbą naturalną nieujemną.
- Zakładamy, że dane wejściowe są takie, że istnieje rozwiązanie w liczbach naturalnych.

### Dane wejściowe

- Dwie liczby naturalne:
  1. \( a \) – liczba głów (całkowita nieujemna).
  2. \( b \) – liczba nóg (całkowita nieujemna).

### Dane wyjściowe

- Dwie liczby naturalne:
  1. Liczba kur na farmie.
  2. Liczba owiec na farmie.

### Przykład

- **Dane wejściowe**:
  ```
  40
  100
  ```
- **Oczekiwane wyjście**:
  ```
  30
  10
  ```
  *(Oznacza to, że na farmie jest 30 kur i 10 owiec.)*

### Wskazówki

- Utwórz układ równań:
  1. \( c + s = a \) (gdzie \( c \) – liczba kur, \( s \) – liczba owiec).
  2. \( 2c + 4s = b \) (ponieważ kura ma 2 nogi, a owca 4).
- Rozwiąż układ równań metodą podstawiania lub eliminacji:
  - Możesz wyliczyć \( c = a - s \) z pierwszego równania i podstawić do drugiego.
  - Otrzymasz równanie z jedną niewiadomą \( s \).
- Po obliczeniu liczby owiec \( s \), wylicz liczbę kur \( c \) korzystając z pierwszego równania.
- Upewnij się, że wyniki są liczbami naturalnymi nieujemnymi.

---
