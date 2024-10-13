## Zadanie 1 - Zwracanie stałej wartości

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz funkcje, które zwracają określone stałe wartości:

a) Funkcja zwraca liczbę całkowitą **3**.

b) Funkcja zwraca napis **"Tak"**.

c) Funkcja zwraca wartość logiczną **True** (Prawda).

### Dane wejściowe

Brak. Funkcje nie przyjmują żadnych argumentów.

### Dane wyjściowe

- **Podpunkt a):** Liczba całkowita `3`.
- **Podpunkt b):** Napis `"Tak"`.
- **Podpunkt c):** Wartość logiczna `True`.

### Przykład

**Podpunkt a):**

- **Wywołanie funkcji**:
  ```python
  wynik = zwroc_liczbe()
  ```
- **Oczekiwane wyjście**:
  ```
  3
  ```

**Podpunkt b):**

- **Wywołanie funkcji**:
  ```python
  wynik = zwroc_napis()
  ```
- **Oczekiwane wyjście**:
  ```
  Tak
  ```

**Podpunkt c):**

- **Wywołanie funkcji**:
  ```python
  wynik = zwroc_prawda()
  ```
- **Oczekiwane wyjście**:
  ```
  True
  ```

### Wskazówki

- Każdą funkcję zdefiniuj osobno.
- Funkcje nie przyjmują argumentów i zwracają jedynie określoną wartość.
- Upewnij się, że zwracany typ danych jest zgodny z oczekiwaniami (liczba całkowita, napis, wartość logiczna).

---

## Zadanie 2 - Podstawowe operacje arytmetyczne w funkcji

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz funkcję, która dla podanych dwóch liczb całkowitych wykona następujące operacje:

a) Zwróci **sumę** tych liczb.

b) Zwróci **różnicę**: druga liczba minus pierwsza liczba.

c) Zwróci **iloczyn** tych liczb.

d) Zwróci **iloraz całkowity** z dzielenia pierwszej liczby przez drugą.

e) Zwróci **resztę z dzielenia** pierwszej liczby przez drugą.

### Dane wejściowe

- Dwie liczby całkowite (mogą być dodatnie lub ujemne), przekazywane jako argumenty funkcji.

### Dane wyjściowe

- W każdym podpunkcie: jedna liczba całkowita będąca wynikiem odpowiedniej operacji.

### Przykład

Dla liczb **3** i **5**:

**Podpunkt a):**

- **Wywołanie funkcji**:
  ```python
  wynik = suma(3, 5)
  ```
- **Oczekiwane wyjście**:
  ```
  8
  ```

**Podpunkt b):**

- **Wywołanie funkcji**:
  ```python
  wynik = roznica(3, 5)
  ```
- **Oczekiwane wyjście**:
  ```
  2
  ```

**Podpunkt c):**

- **Wywołanie funkcji**:
  ```python
  wynik = iloczyn(3, 5)
  ```
- **Oczekiwane wyjście**:
  ```
  15
  ```

**Podpunkt d):**

- **Wywołanie funkcji**:
  ```python
  wynik = iloraz(3, 5)
  ```
- **Oczekiwane wyjście**:
  ```
  0
  ```

**Podpunkt e):**

- **Wywołanie funkcji**:
  ```python
  wynik = reszta(3, 5)
  ```
- **Oczekiwane wyjście**:
  ```
  3
  ```

### Wskazówki

- Przy dzieleniu upewnij się, że druga liczba nie jest zerem, aby uniknąć błędu dzielenia przez zero.
- Do obliczenia ilorazu całkowitego użyj operatora `//`, a do reszty z dzielenia operatora `%`.
- Upewnij się, że funkcje zwracają wynik odpowiedniego typu (liczba całkowita).

---

## Zadanie 3 - Sprawdzanie warunków logicznych

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz funkcję, która dla podanych dwóch liczb naturalnych sprawdza następujące warunki i zwraca odpowiednie wartości logiczne:

a) Czy pierwsza liczba jest **większa** od drugiej liczby?

b) Czy **suma** tych liczb jest **mniejsza niż 10**?

c) Czy **obie liczby są nieparzyste**?

d) Czy **większa liczba** jest **mniejsza** od **kwadratu pierwszej liczby**?

### Dane wejściowe

- Dwie liczby naturalne (całkowite nieujemne), przekazywane jako argumenty funkcji.

### Dane wyjściowe

- Cztery wartości logiczne (`True` lub `False`), odpowiadające wynikom sprawdzenia warunków a)–d).

### Przykład

Dla liczb **3** i **2**:

- **Wywołanie funkcji**:
  ```python
  wynik_a, wynik_b, wynik_c, wynik_d = sprawdz_warunki(3, 2)
  ```
- **Oczekiwane wyjście**:
  ```
  True
  True
  False
  True
  ```

### Wskazówki

- Do sprawdzania parzystości liczby użyj operatora modulo `%`.
- Funkcja może zwracać wyniki jako krotkę lub listę wartości logicznych.
- Przy porównywaniu liczb zwróć uwagę na kolejność argumentów.

---

## Zadanie 4 - Znajdowanie minimum i maksimum

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz funkcje, które:

a) Dla podanych dwóch liczb zwracają **mniejszą** z nich.

b) Dla podanych dwóch liczb zwracają **większą** z nich.

c) Dla podanych trzech liczb zwracają **najmniejszą** z nich.

d) Dla podanych trzech liczb zwracają **największą** z nich.

### Dane wejściowe

- **Podpunkt a)** i **b)**: Dwie liczby naturalne.
- **Podpunkt c)** i **d)**: Trzy liczby naturalne.

### Dane wyjściowe

- W każdym podpunkcie: jedna liczba naturalna – wynik odpowiedniej funkcji.

### Przykład

**Podpunkt a):**

- **Wywołanie funkcji**:
  ```python
  wynik = min_z_dwoch(3, 1)
  ```
- **Oczekiwane wyjście**:
  ```
  1
  ```

**Podpunkt b):**

- **Wywołanie funkcji**:
  ```python
  wynik = max_z_dwoch(3, 1)
  ```
- **Oczekiwane wyjście**:
  ```
  3
  ```

**Podpunkt c):**

- **Wywołanie funkcji**:
  ```python
  wynik = min_z_trzech(3, 2, 1)
  ```
- **Oczekiwane wyjście**:
  ```
  1
  ```

**Podpunkt d):**

- **Wywołanie funkcji**:
  ```python
  wynik = max_z_trzech(3, 2, 1)
  ```
- **Oczekiwane wyjście**:
  ```
  3
  ```

### Wskazówki

- Możesz użyć wbudowanych funkcji `min()` i `max()`.
- Upewnij się, że funkcje działają poprawnie również dla liczb równych.

---

## Zadanie 5 - Zamiana wartości miejscami

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz funkcję, która zamienia miejscami wartości dwóch zmiennych. Po wykonaniu funkcji, zmienna `a` powinna przechowywać wartość zmiennej `b`, a zmienna `b` powinna przechowywać wartość zmiennej `a`.

### Dane wejściowe

- Dwie liczby naturalne, przekazywane jako argumenty funkcji.

### Dane wyjściowe

- Dwie liczby naturalne – wartości zmiennych po zamianie, zwrócone jako krotka lub lista.

### Przykład

- **Wywołanie funkcji**:
  ```python
  a, b = zamien_wartosci(8, 5)
  ```
- **Oczekiwane wyjście**:
  ```
  a = 5
  b = 8
  ```

### Wskazówki

- W niektórych językach programowania można zamienić wartości zmiennych bez użycia zmiennej pomocniczej, np. w Pythonie: `a, b = b, a`.
- Upewnij się, że funkcja zwraca wartości w odpowiedniej kolejności.

---

## Zadanie 6 - Obliczanie sumy cyfr liczby

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz funkcję, która dla podanej liczby naturalnej oblicza sumę jej cyfr.

### Dane wejściowe

- Jedna liczba naturalna.

### Dane wyjściowe

- Jedna liczba naturalna – suma cyfr podanej liczby.

### Przykład

- **Wywołanie funkcji**:
  ```python
  wynik = suma_cyfr(13231)
  ```
- **Oczekiwane wyjście**:
  ```
  10
  ```

### Wskazówki

- Możesz zamienić liczbę na napis i sumować cyfry za pomocą pętli.
- Alternatywnie, użyj pętli z dzieleniem przez 10 i operatorem modulo `%` do wyodrębniania cyfr.

---

## Zadanie 7 - Weryfikacja nazwy użytkownika i hasła

**Poziom trudności**: ★★☆

### Treść zadania

Napisz dwie funkcje:

1. **Pierwsza funkcja** powinna poprosić użytkownika o podanie **nazwy użytkownika** i **hasła**, a następnie zwrócić te dane.

2. **Druga funkcja** powinna otrzymać dane zwrócone przez pierwszą funkcję i w pętli prosić użytkownika o ponowne podanie nazwy użytkownika i hasła. Pętla powinna trwać do momentu, gdy użytkownik poda dane **identyczne** z tymi przekazanymi przez pierwszą funkcję. Po poprawnym wprowadzeniu danych funkcja powinna wyświetlić komunikat **"Dane poprawne. Dostęp przyznany."**

### Dane wejściowe

- **Pierwsza funkcja**: nazwa użytkownika i hasło wprowadzone przez użytkownika.
- **Druga funkcja**: nazwa użytkownika i hasło wprowadzone przez użytkownika w pętli.

### Dane wyjściowe

- **Druga funkcja**: komunikat po poprawnym wprowadzeniu danych.

### Przykład

1. **Pierwsza funkcja**:

   - **Dane wejściowe**:
     ```
     Podaj nazwę użytkownika: admin
     Podaj hasło: 1234
     ```

2. **Druga funkcja**:

   - **Przykładowy przebieg pętli**:
     ```
     Podaj nazwę użytkownika: user
     Podaj hasło: 4321
     ```
     *(Dane niepoprawne, pętla trwa dalej)*
     ```
     Podaj nazwę użytkownika: admin
     Podaj hasło: 1234
     ```
     *(Dane poprawne)*

   - **Oczekiwane wyjście**:
     ```
     Dane poprawne. Dostęp przyznany.
     ```

### Wskazówki

- W drugiej funkcji użyj pętli `while` do wielokrotnego pobierania danych.
- Do porównania napisów możesz użyć operatora `==`.
- Pamiętaj o tym, że porównanie jest czułe na wielkość liter.

---

## Zadanie 8 - Zaokrąglanie ilorazu w dół bez operatorów dzielenia

**Poziom trudności**: ★★☆

### Treść zadania

Napisz funkcję, która oblicza iloraz dwóch liczb naturalnych, zaokrąglony w dół do najbliższej liczby całkowitej, **bez użycia operatorów dzielenia (`/`) i reszty z dzielenia (`%`)**.

### Dane wejściowe

- Dwie liczby naturalne:
  - **Dzielna** (liczba, którą dzielimy).
  - **Dzielnik** (liczba, przez którą dzielimy).

### Dane wyjściowe

- Jedna liczba naturalna – iloraz zaokrąglony w dół.

### Przykład

- **Dane wejściowe**:
  ```
  7
  2
  ```
- **Wywołanie funkcji**:
  ```python
  wynik = zaokraglij_w_dol(7, 2)
  ```
- **Oczekiwane wyjście**:
  ```
  3
  ```

### Wskazówki

- Możesz użyć pętli, w której będziesz odejmować dzielnik od dzielnej, aż dzielna będzie mniejsza od dzielnika. Licznik pętli będzie wynikiem ilorazu.
- Pamiętaj o obsłudze przypadku, gdy dzielnik jest równy 0 – w takiej sytuacji należy zwrócić komunikat o błędzie lub obsłużyć wyjątek.
- Upewnij się, że zwracana wartość jest liczbą całkowitą.

---
