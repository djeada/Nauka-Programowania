# Pętla - Algorytmy Matematyczne

## Zadanie 1 - Obliczanie średniej z n liczb

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz funkcję, która dla podanej liczby \( n \) poprosi użytkownika o podanie \( n \) liczb i zwróci ich średnią arytmetyczną.

### Dane wejściowe

- Jedna liczba naturalna \( n \) (\( n \geq 1 \)).
- Następnie \( n \) liczb (mogą być całkowite lub zmiennoprzecinkowe), wprowadzonych przez użytkownika.

### Dane wyjściowe

- Jedna liczba zmiennoprzecinkowa – średnia arytmetyczna podanych \( n \) liczb.

### Przykład

- **Dane wejściowe**:
  ```
  2
  4
  6
  ```
- **Wywołanie funkcji**:
  ```python
  wynik = oblicz_srednia()
  ```
- **Oczekiwane wyjście**:
  ```
  5.0
  ```
  *(Ponieważ \( \frac{4 + 6}{2} = 5.0 \).)*

### Wskazówki

- Upewnij się, że \( n \) jest liczbą naturalną większą od zera.
- Możesz użyć pętli do wczytywania \( n \) liczb od użytkownika.
- Sumuj podane liczby i na końcu podziel sumę przez \( n \), aby uzyskać średnią.
- Zwróć uwagę, że średnia może nie być liczbą całkowitą, więc wynik powinien być typu zmiennoprzecinkowego.

---

## Zadanie 2 - Potęgowanie liczby przy pomocy pętli

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz funkcję, która dla podanych dwóch liczb naturalnych \( a \) i \( b \) obliczy wartość \( a^b \) (czyli \( a \) podniesione do potęgi \( b \)) przy użyciu pętli.

### Dane wejściowe

- Dwie liczby naturalne:
  - \( a \) – podstawa potęgi.
  - \( b \) – wykładnik potęgi (\( b \geq 0 \)).

### Dane wyjściowe

- Jedna liczba naturalna – wynik potęgowania \( a^b \).

### Przykład

- **Wywołanie funkcji**:
  ```python
  wynik = potega(3, 5)
  ```
- **Oczekiwane wyjście**:
  ```
  243
  ```
  *(Ponieważ \( 3^5 = 243 \).)*

### Wskazówki

- Upewnij się, że wykładnik \( b \) jest liczbą naturalną (może być zero).
- Rozpocznij z wynikiem równym 1 i w pętli pomnóż go \( b \) razy przez \( a \).
- Jeśli \( b = 0 \), wynik powinien być równy 1 (każda liczba do potęgi zerowej wynosi 1).

---

## Zadanie 3 - Mnożenie i dzielenie przy pomocy pętli

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz funkcję, która dla podanych dwóch liczb naturalnych \( a \) i \( b \) obliczy:

a) **Iloczyn** tych liczb przy użyciu jedynie dodawania oraz pętli.

b) **Iloraz całkowity** liczby \( a \) przez liczbę \( b \) przy użyciu jedynie odejmowania oraz pętli.

### Dane wejściowe

- Dwie liczby naturalne \( a \) i \( b \), przy czym dla podpunktu b) \( b \neq 0 \).

### Dane wyjściowe

- **Podpunkt a):** Jedna liczba naturalna – iloczyn \( a \times b \).
- **Podpunkt b):** Jedna liczba naturalna – iloraz całkowity \( a // b \).

### Przykład

**Dla liczb \( a = 3 \) i \( b = 2 \):**

- **Podpunkt a):**

  - **Wywołanie funkcji**:
    ```python
    wynik = iloczyn(3, 2)
    ```
  - **Oczekiwane wyjście**:
    ```
    6
    ```

- **Podpunkt b):**

  - **Wywołanie funkcji**:
    ```python
    wynik = iloraz(3, 2)
    ```
  - **Oczekiwane wyjście**:
    ```
    1
    ```

### Wskazówki

- **Podpunkt a):**
  - Zainicjuj zmienną wynikową na 0.
  - Wykonaj pętlę \( b \) razy, w każdej iteracji dodając \( a \) do wyniku.
- **Podpunkt b):**
  - Zainicjuj licznik na 0.
  - W pętli odejmuj od \( a \) wartość \( b \), zwiększając licznik o 1 za każdym razem, aż \( a \) będzie mniejsze od \( b \).
  - Wynikiem jest wartość licznika.
- Pamiętaj o obsłudze przypadku dzielenia przez zero – jeśli \( b = 0 \), funkcja powinna zwrócić komunikat o błędzie lub obsłużyć wyjątek.

---

## Zadanie 4 - Obliczanie silni liczby

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz funkcję, która oblicza **silnię** podanej liczby naturalnej \( n \) przy użyciu pętli.

Silnia liczby \( n \) (oznaczana jako \( n! \)) jest iloczynem wszystkich liczb naturalnych od 1 do \( n \):

\[
n! = 1 \times 2 \times 3 \times \ldots \times n
\]

Przyjmij, że \( 0! = 1 \).

### Dane wejściowe

- Jedna liczba naturalna \( n \) (\( n \geq 0 \)).

### Dane wyjściowe

- Jedna liczba naturalna – wartość \( n! \).

### Przykład

- **Wywołanie funkcji**:
  ```python
  wynik = silnia(3)
  ```
- **Oczekiwane wyjście**:
  ```
  6
  ```
  *(Ponieważ \( 3! = 1 \times 2 \times 3 = 6 \).)*

### Wskazówki

- Zainicjuj zmienną wynikową na 1.
- Użyj pętli do mnożenia kolejnych liczb od 1 do \( n \).
- Upewnij się, że funkcja poprawnie obsługuje przypadek \( n = 0 \).

---

## Zadanie 5 - Obliczanie największego wspólnego dzielnika (NWD)

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz funkcję, która dla podanych dwóch liczb naturalnych \( a \) i \( b \) zwraca ich **największy wspólny dzielnik (NWD)**.

### Dane wejściowe

- Dwie liczby naturalne \( a \) i \( b \), przy czym \( a > 0 \) i \( b > 0 \).

### Dane wyjściowe

- Jedna liczba naturalna – NWD liczb \( a \) i \( b \).

### Przykład

- **Wywołanie funkcji**:
  ```python
  wynik = nwd(60, 45)
  ```
- **Oczekiwane wyjście**:
  ```
  15
  ```
  *(Ponieważ największy wspólny dzielnik 60 i 45 to 15.)*

### Wskazówki

- Możesz użyć **Algorytmu Euklidesa**:
  - Dopóki \( b \neq 0 \), wykonuj operacje:
    - \( c = a \mod b \)
    - \( a = b \)
    - \( b = c \)
  - Gdy \( b = 0 \), NWD jest równe \( a \).
- Upewnij się, że funkcja działa poprawnie niezależnie od tego, która liczba jest większa.

---

## Zadanie 6 - Obliczanie najmniejszej wspólnej wielokrotności (NWW)

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz funkcję, która dla podanych dwóch liczb naturalnych \( a \) i \( b \) zwraca ich **najmniejszą wspólną wielokrotność (NWW)**.

### Dane wejściowe

- Dwie liczby naturalne \( a \) i \( b \), przy czym \( a > 0 \) i \( b > 0 \).

### Dane wyjściowe

- Jedna liczba naturalna – NWW liczb \( a \) i \( b \).

### Przykład

- **Wywołanie funkcji**:
  ```python
  wynik = nww(7, 9)
  ```
- **Oczekiwane wyjście**:
  ```
  63
  ```
  *(Ponieważ najmniejsza wspólna wielokrotność 7 i 9 to 63.)*

### Wskazówki

- NWW można obliczyć za pomocą wzoru:

  \[
  \text{NWW}(a, b) = \frac{a \times b}{\text{NWD}(a, b)}
  \]

- Najpierw oblicz NWD liczb \( a \) i \( b \) (możesz użyć funkcji z **Zadania 5**).
- Następnie oblicz NWW korzystając z powyższego wzoru.

---

## Zadanie 7 - Obliczanie pierwiastka metodą Newtona

**Poziom trudności**: ★★☆

### Treść zadania

Napisz funkcję, która dla podanej liczby naturalnej \( n \) zwraca jej pierwiastek kwadratowy, obliczony przy użyciu **metody Newtona (Herona)**.

Metoda Newtona do obliczania pierwiastka kwadratowego polega na iteracyjnym stosowaniu wzoru:

\[
x_{k+1} = \frac{1}{2} \left( x_k + \frac{n}{x_k} \right)
\]

Gdzie:

- \( x_0 \) – początkowe przybliżenie (możesz przyjąć \( x_0 = n \) lub \( x_0 = n/2 \)).
- Proces iteracyjny kontynuujemy, aż do osiągnięcia zadanej dokładności (np. różnica między kolejnymi przybliżeniami jest mniejsza niż \( \epsilon = 0.0001 \)).

### Dane wejściowe

- Jedna liczba naturalna \( n \) (\( n \geq 0 \)).

### Dane wyjściowe

- Jedna liczba zmiennoprzecinkowa – przybliżona wartość pierwiastka kwadratowego z \( n \).

### Przykład

- **Wywołanie funkcji**:
  ```python
  wynik = pierwiastek(16)
  ```
- **Oczekiwane wyjście**:
  ```
  4.0
  ```
  *(Ponieważ \( \sqrt{16} = 4 \).)*

### Wskazówki

- Zainicjuj \( x_0 = n \) lub \( x_0 = n/2 \).
- Użyj pętli `while` do iteracyjnego obliczania kolejnych przybliżeń.
- Warunek zakończenia pętli może być oparty na różnicy między kolejnymi przybliżeniami (np. \( |x_{k+1} - x_k| < \epsilon \)).
- Upewnij się, że funkcja działa poprawnie dla \( n = 0 \) i \( n = 1 \).
- Wynik może być zaokrąglony do określonej liczby miejsc po przecinku, jeśli jest to wymagane.

---

## Zadanie 8 - Naiwny test pierwszości liczby

**Poziom trudności**: ★★☆

### Treść zadania

Napisz funkcję, która dla podanej liczby naturalnej \( n \) sprawdza, czy jest ona **liczbą pierwszą**.

Liczba pierwsza to liczba naturalna większa od 1, która ma dokładnie dwa dzielniki: 1 i samą siebie.

### Dane wejściowe

- Jedna liczba naturalna \( n \) (\( n \geq 2 \)).

### Dane wyjściowe

- Jedna wartość logiczna (`True` lub `False`), wskazująca, czy liczba \( n \) jest pierwsza.

### Przykład

- **Wywołanie funkcji**:
  ```python
  wynik = czy_pierwsza(7)
  ```
- **Oczekiwane wyjście**:
  ```
  True
  ```

- **Wywołanie funkcji**:
  ```python
  wynik = czy_pierwsza(4)
  ```
- **Oczekiwane wyjście**:
  ```
  False
  ```

### Wskazówki

- Możesz użyć prostego algorytmu polegającego na sprawdzaniu, czy \( n \) dzieli się bez reszty przez którąkolwiek liczbę naturalną od 2 do \( n - 1 \).
- Aby zoptymalizować algorytm, możesz sprawdzać dzielniki tylko do \( \sqrt{n} \).
- Jeśli znajdziesz choć jeden dzielnik różny od 1 i \( n \), liczba nie jest pierwsza.
- Upewnij się, że funkcja zwraca `False` dla \( n = 1 \), ponieważ 1 nie jest liczbą pierwszą.

---
