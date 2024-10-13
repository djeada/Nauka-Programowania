# Interakcja z Konsolą

## Zadanie 1 - Wypisywanie tekstu na ekran

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz program, który wypisuje na standardowe wyjście określony ciąg znaków. Program powinien wyświetlić komunikat **"Witaj, świecie!"** (bez cudzysłowów).

### Dane wejściowe

Brak.

### Dane wyjściowe

- Tekst: `Witaj, świecie!` (dokładnie tak, jak podano).
- Typ wyniku: tekst.

### Przykład

- **Dane wejściowe**:
  ```
  ```
  *(brak danych wejściowych)*

- **Oczekiwane wyjście**:
  ```
  Witaj, świecie!
  ```

### Wskazówki

- Możesz użyć funkcji lub instrukcji do wyświetlania tekstu, takiej jak `print` w języku Python.
- Upewnij się, że tekst jest wypisany dokładnie w podanej formie, łącznie ze znakami interpunkcyjnymi i spacjami.

---

## Zadanie 2 - Zamiana kolejności liczb

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz program, który pobiera od użytkownika dwie liczby całkowite i wypisuje je w odwrotnej kolejności. Program powinien najpierw pobrać pierwszą liczbę, potem drugą, a następnie wyświetlić najpierw drugą liczbę, a potem pierwszą.

### Dane wejściowe

- Dwie liczby całkowite, każda w oddzielnej linii.
- Liczby mogą być dodatnie, ujemne lub zerowe.

### Dane wyjściowe

- Dwie liczby całkowite wypisane w odwrotnej kolejności niż zostały wprowadzone, każda w oddzielnej linii.

### Przykład

- **Dane wejściowe**:
  ```
  -7
  4
  ```
- **Oczekiwane wyjście**:
  ```
  4
  -7
  ```

### Wskazówki

- Przechowaj liczby w zmiennych i wypisz je w odwrotnej kolejności.
- Upewnij się, że każda liczba jest wypisana w oddzielnej linii.

---

## Zadanie 3 - Rysowanie kształtów za pomocą znaków

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz program, który wypisze na standardowe wyjście następujące kształty zbudowane z określonych znaków:

a) **Kwadrat** zbudowany z liter `x` o wymiarach 2x2.

b) **Trójkąt liczbowy** składający się z 3 linii, gdzie w każdej linii liczba znaków odpowiada numerowi linii, a znak to numer linii.

c) **Romb** zbudowany z jedynek, o maksymalnej szerokości 5 znaków.

### Dane wejściowe

Brak.

### Dane wyjściowe

Program powinien wypisać trzy kształty, każdy oddzielony pustą linią.

### Przykład

- **Oczekiwane wyjście**:
  ```
  xx
  xx

  1
  22
  333

    1
   111
  11111
   111
    1
  ```

### Wskazówki

- Użyj pętli do generowania kolejnych linii każdego kształtu.
- Zwróć uwagę na odpowiednie rozmieszczenie spacji, aby kształty były prawidłowo sformatowane.
- Możesz wykorzystać operacje na ciągach znaków, takie jak powielanie znaków.

---

## Zadanie 4 - Podstawowe operacje arytmetyczne

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz program, który pobiera od użytkownika dwie liczby naturalne i oblicza oraz wypisuje wyniki następujących operacji:

a) **Suma** tych liczb.

b) **Różnica** pierwszej liczby i drugiej liczby.

c) **Iloczyn** tych liczb.

d) **Iloraz całkowity** pierwszej liczby przez drugą (dzielenie całkowitoliczbowe).

e) **Reszta z dzielenia** pierwszej liczby przez drugą.

f) **Potęga**, gdzie pierwsza liczba jest podstawą, a druga wykładnikiem.

### Dane wejściowe

- Dwie liczby naturalne (całkowite dodatnie), każda w oddzielnej linii.

### Dane wyjściowe

- Sześć liczb całkowitych, każda w oddzielnej linii, będących wynikami operacji a)–f) w podanej kolejności.

### Przykład

**Przykład 1:**

- **Dane wejściowe**:
  ```
  9
  1
  ```
- **Oczekiwane wyjście**:
  ```
  10
  8
  9
  9
  0
  9
  ```

**Przykład 2:**

- **Dane wejściowe**:
  ```
  3
  2
  ```
- **Oczekiwane wyjście**:
  ```
  5
  1
  6
  1
  1
  9
  ```

### Wskazówki

- Przy dzieleniu upewnij się, że wykonujesz dzielenie całkowitoliczbowe (bez części ułamkowej).
- Do obliczenia potęgi możesz użyć operatora potęgowania lub funkcji matematycznej.
- Zachowaj kolejność wypisywanych wyników zgodnie z poleceniem.

---

## Zadanie 5 - Obliczanie wartości funkcji w danym punkcie

**Poziom trudności**: ★★☆

### Treść zadania

Napisz program, który oblicza wartość funkcji w danym punkcie, zgodnie z poniższymi instrukcjami:

a) Otrzymujesz wartość \( x \). Oblicz wartość funkcji \( y = 3x + 10 \).

b) Pobierz wartości współczynników \( a \), \( b \) oraz wartość \( x \). Oblicz wartość funkcji \( y = ax + b \).

c) Otrzymujesz wartość \( x \). Oblicz wartość funkcji \( y = x^3 + 22 - 20 \).

d) Pobierz wartości \( a \), \( b \), \( c \), \( m \), \( n \) oraz \( x \). Oblicz wartość funkcji \( y = ax^m + bx^n + c - a \).

e) Otrzymujesz wartość \( x \) (w radianach). Oblicz wartość funkcji:
\[ y = \sin^3(x) \cdot \cos^2(x) + e^{x^2} + \ln(x^3 + 2x^2 - x - 3) \]

### Dane wejściowe

- **Podpunkt a):** Jedna liczba (całkowita lub zmiennoprzecinkowa) – wartość \( x \).
- **Podpunkt b):** Trzy liczby (całkowite lub zmiennoprzecinkowe): \( a \), \( b \), \( x \).
- **Podpunkt c):** Jedna liczba (całkowita lub zmiennoprzecinkowa) – wartość \( x \).
- **Podpunkt d):** Sześć liczb (całkowitych lub zmiennoprzecinkowych): \( a \), \( b \), \( c \), \( m \), \( n \), \( x \).
- **Podpunkt e):** Jedna liczba zmiennoprzecinkowa – wartość \( x \) w radianach.

### Dane wyjściowe

- W każdym podpunkcie: jedna liczba zmiennoprzecinkowa z dokładnością do trzech miejsc po przecinku – wynik \( y \).

### Przykład

**Podpunkt a):**

- **Dane wejściowe**:
  ```
  3
  ```
- **Oczekiwane wyjście**:
  ```
  19.000
  ```

**Podpunkt b):**

- **Dane wejściowe**:
  ```
  1
  2
  3
  ```
- **Oczekiwane wyjście**:
  ```
  5.000
  ```

**Podpunkt c):**

- **Dane wejściowe**:
  ```
  5
  ```
- **Oczekiwane wyjście**:
  ```
  127.000
  ```

**Podpunkt d):**

- **Dane wejściowe**:
  ```
  1
  1
  1
  1
  1
  1
  ```
- **Oczekiwane wyjście**:
  ```
  2.000
  ```

**Podpunkt e):**

- **Dane wejściowe**:
  ```
  2
  ```
- **Oczekiwane wyjście**:
  ```
  57.179
  ```

### Wskazówki

- W podpunkcie e) korzystaj z funkcji trygonometrycznych w radianach.
- Funkcja \( \ln \) oznacza logarytm naturalny.
- Upewnij się, że argumenty funkcji logarytmicznej są dodatnie.
- Do obliczeń możesz użyć biblioteki matematycznej, np. `math` w Pythonie.

---

## Zadanie 6 - Konwersja jednostek

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz program, który dokonuje konwersji jednostek zgodnie z poniższymi poleceniami:

a) Pobierz masę w **kilogramach** i oblicz, ile to **gramów**.

b) Pobierz długość w **calach** i oblicz, ile to **centymetrów**.

c) Pobierz czas w **sekundach** i przelicz na **pełne godziny**.

d) Pobierz kwotę w **euro** i oblicz, ile to **złotych**, przy kursie 1 euro = 4.4 zł.

e) Pobierz kąt w **stopniach** i oblicz, ile to **radianów**.

f) Pobierz temperaturę w **stopniach Fahrenheita** i oblicz odpowiadającą temperaturę w **stopniach Celsjusza** oraz w **kelwinach**.

### Dane wejściowe

- Jedna liczba (całkowita lub zmiennoprzecinkowa) dla każdego podpunktu.

### Dane wyjściowe

- **Podpunkt a)**: jedna liczba całkowita – masa w gramach.
- **Podpunkt b)**: jedna liczba zmiennoprzecinkowa z dokładnością do dwóch miejsc po przecinku – długość w centymetrach.
- **Podpunkt c)**: jedna liczba całkowita – liczba pełnych godzin.
- **Podpunkt d)**: jedna liczba zmiennoprzecinkowa z dokładnością do dwóch miejsc po przecinku – kwota w złotych.
- **Podpunkt e)**: jedna liczba zmiennoprzecinkowa z dokładnością do trzech miejsc po przecinku – kąt w radianach.
- **Podpunkt f)**: dwie liczby zmiennoprzecinkowe z dokładnością do trzech miejsc po przecinku – temperatura w stopniach Celsjusza i w kelwinach.

### Przykład

**Podpunkt a):**

- **Dane wejściowe**:
  ```
  2
  ```
- **Oczekiwane wyjście**:
  ```
  2000
  ```

**Podpunkt b):**

- **Dane wejściowe**:
  ```
  12
  ```
- **Oczekiwane wyjście**:
  ```
  30.48
  ```

**Podpunkt c):**

- **Dane wejściowe**:
  ```
  3600
  ```
- **Oczekiwane wyjście**:
  ```
  1
  ```

**Podpunkt d):**

- **Dane wejściowe**:
  ```
  4
  ```
- **Oczekiwane wyjście**:
  ```
  17.60
  ```

**Podpunkt e):**

- **Dane wejściowe**:
  ```
  120
  ```
- **Oczekiwane wyjście**:
  ```
  2.094
  ```

**Podpunkt f):**

- **Dane wejściowe**:
  ```
  100
  ```
- **Oczekiwane wyjście**:
  ```
  37.778
  310.928
  ```

### Wskazówki

- Użyj stałej \( \pi \) (pi) ≈ 3.1416.
- W konwersji temperatur zastosuj wzory:
  - \( °C = \frac{5}{9} (°F - 32) \)
  - \( K = °C + 273.15 \)
- Zaokrąglij wyniki do wymaganej liczby miejsc po przecinku.

---

## Zadanie 7 - Pola i objętości figur geometrycznych

**Poziom trudności**: ★★☆

### Treść zadania

Napisz program, który oblicza pola i objętości figur geometrycznych zgodnie z poniższymi poleceniami:

a) Oblicz **pole trójkąta** o podanej podstawie \( a \) i wysokości \( h \): \( P = \frac{1}{2} a h \).

b) Oblicz **pole prostokąta** o bokach \( a \) i \( b \): \( P = a b \).

c) Oblicz **pole rombu** o przekątnych \( d_1 \) i \( d_2 \): \( P = \frac{1}{2} d_1 d_2 \).

d) Oblicz **objętość kuli** o promieniu \( r \): \( V = \frac{4}{3} \pi r^3 \).

e) Oblicz **objętość stożka** o promieniu podstawy \( r \) i wysokości \( h \): \( V = \frac{1}{3} \pi r^2 h \).

f) Oblicz **objętość prostopadłościanu** o wymiarach \( a \), \( b \), \( c \): \( V = a b c \).

### Dane wejściowe

- **Podpunkt a)**, b), c): Dwie liczby (całkowite lub zmiennoprzecinkowe).
- **Podpunkt d)**: Jedna liczba (całkowita lub zmiennoprzecinkowa).
- **Podpunkt e)**: Dwie liczby (całkowite lub zmiennoprzecinkowe).
- **Podpunkt f)**: Trzy liczby (całkowite lub zmiennoprzecinkowe).

### Dane wyjściowe

- W każdym podpunkcie: jedna liczba zmiennoprzecinkowa z dokładnością do trzech miejsc po przecinku.

### Przykład

**Podpunkt a):**

- **Dane wejściowe**:
  ```
  5
  2
  ```
- **Oczekiwane wyjście**:
  ```
  5.000
  ```

**Podpunkt b):**

- **Dane wejściowe**:
  ```
  3
  3
  ```
- **Oczekiwane wyjście**:
  ```
  9.000
  ```

**Podpunkt c):**

- **Dane wejściowe**:
  ```
  2
  4
  ```
- **Oczekiwane wyjście**:
  ```
  4.000
  ```

**Podpunkt d):**

- **Dane wejściowe**:
  ```
  2
  ```
- **Oczekiwane wyjście**:
  ```
  33.510
  ```

**Podpunkt e):**

- **Dane wejściowe**:
  ```
  3
  2
  ```
- **Oczekiwane wyjście**:
  ```
  18.850
  ```

**Podpunkt f):**

- **Dane wejściowe**:
  ```
  2
  2
  2
  ```
- **Oczekiwane wyjście**:
  ```
  8.000
  ```

### Wskazówki

- Użyj stałej \( \pi \) (pi) ≈ 3.1416 w obliczeniach.
- Pamiętaj o odpowiednim zaokrągleniu wyników.

---

## Zadanie 8 - Obliczanie kosztu pokrycia podłogi płytkami

**Poziom trudności**: ★★☆

### Treść zadania

Napisz program, który obliczy całkowity koszt pokrycia podłogi płytkami. Otrzymasz:

- Cenę jednej płytki.
- Długość boku płytki (płytka jest kwadratowa).
- Długość podłogi.
- Szerokość podłogi.

Oblicz, ile płytek potrzeba, aby pokryć całą podłogę, i podaj całkowity koszt.

### Dane wejściowe

- Cztery liczby (całkowite lub zmiennoprzecinkowe):

  1. Cena jednej płytki.
  2. Długość boku płytki.
  3. Długość podłogi.
  4. Szerokość podłogi.

### Dane wyjściowe

- Jedna liczba zmiennoprzecinkowa z dokładnością do dwóch miejsc po przecinku – całkowity koszt.

### Przykład

- **Dane wejściowe**:
  ```
  2
  3
  20
  40
  ```
- **Oczekiwane wyjście**:
  ```
  196.00
  ```

### Wskazówki

- Oblicz liczbę płytek potrzebnych wzdłuż długości i szerokości podłogi, zaokrąglając w górę do najbliższej liczby całkowitej.
- Liczba płytek = liczba płytek wzdłuż długości × liczba płytek wzdłuż szerokości.
- Całkowity koszt = liczba płytek × cena jednej płytki.

---

## Zadanie 9 - Kalkulator kredytowy

**Poziom trudności**: ★★☆

### Treść zadania

Napisz program, który obliczy miesięczną ratę oraz całkowity koszt kredytu na podstawie:

- Rocznej stopy procentowej (w procentach).
- Okresu spłaty kredytu (w latach).
- Kwoty kredytu.

Użyj wzoru na ratę annuitetową (stałą):

\[ M = P \times \frac{r (1 + r)^n}{(1 + r)^n - 1} \]

gdzie:

- \( M \) – miesięczna rata,
- \( P \) – kwota kredytu,
- \( r \) – miesięczna stopa procentowa (roczna stopa procentowa podzielona przez 12 i wyrażona jako ułamek dziesiętny),
- \( n \) – łączna liczba rat (liczba miesięcy).

### Dane wejściowe

- Trzy liczby:

  1. Roczna stopa procentowa (zmiennoprzecinkowa).
  2. Okres spłaty w latach (całkowita).
  3. Kwota kredytu (zmiennoprzecinkowa).

### Dane wyjściowe

- Dwie liczby zmiennoprzecinkowe z dokładnością do dwóch miejsc po przecinku:

  1. Miesięczna rata.
  2. Całkowity koszt kredytu.

### Przykład

- **Dane wejściowe**:
  ```
  3.5
  8
  12000
  ```
- **Oczekiwane wyjście**:
  ```
  143.50
  13776.00
  ```

### Wskazówki

- Oblicz miesięczną stopę procentową: \( r = \frac{\text{roczna stopa procentowa}}{12 \times 100} \).
- Oblicz łączną liczbę rat: \( n = \text{okres spłaty w latach} \times 12 \).
- Całkowity koszt kredytu to: \( M \times n \).
- Zaokrąglij wyniki do dwóch miejsc po przecinku.
