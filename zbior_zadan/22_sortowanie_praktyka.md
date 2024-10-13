# Sortowanie — praktyka

## Zadanie 1 - Sortowanie znaków w napisie

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz napis. Posortuj alfabetycznie wszystkie jego znaki i zwróć wynikowy napis.

### Dane wejściowe

- Jeden napis.

### Dane wyjściowe

- Napis z posortowanymi znakami.

### Przykład

- **Dane wejściowe**:
  ```
  Ala ma kota
  ```
- **Oczekiwane wyjście**:
  ```
   Aaaaklmot
  ```

### Wskazówki

- Możesz użyć funkcji sortującej dostępnej dla ciągów znaków lub list.

---

## Zadanie 2 - Sortowanie słów w zdaniu

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz zdanie w postaci napisu. Podziel je na słowa, a następnie posortuj te słowa alfabetycznie. Zwróć listę posortowanych słów. Pomijaj znaki interpunkcyjne; traktuj je jako separatory.

### Dane wejściowe

- Jeden napis reprezentujący zdanie.

### Dane wyjściowe

- Lista posortowanych słów.

### Przykład

- **Dane wejściowe**:
  ```
  Lemur wygina śmiało ciało
  ```
- **Oczekiwane wyjście**:
  ```
  ['Lemur', 'ciało', 'wygina', 'śmiało']
  ```

### Wskazówki

- Użyj funkcji do podziału napisu na słowa (np. `split()`).
- Przy sortowaniu uwzględnij polskie znaki.

---

## Zadanie 3 - Sortowanie listy par względem jednej z kategorii

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz listę par, gdzie każda para składa się z napisu i liczby.

**a)** Posortuj listę par względem liczb (rosnąco).

**b)** Posortuj listę par względem długości napisów (rosnąco).

### Dane wejściowe

- Lista par: `(napis, liczba)`.

### Dane wyjściowe

- Lista posortowanych par zgodnie z podanym kryterium.

### Przykład

- **Dane wejściowe**:
  ```
  [('ab', 3), ('bca', 1), ('c', 2)]
  ```
- **Oczekiwane wyjście**:

  **a)**
  ```
  [('bca', 1), ('c', 2), ('ab', 3)]
  ```

  **b)**
  ```
  [('c', 2), ('ab', 3), ('bca', 1)]
  ```

### Wskazówki

- Użyj funkcji sortującej z odpowiednim kluczem (np. `key=lambda x: x[1]` dla liczb).

---

## Zadanie 4 - Sortowanie napisów w liście względem długości

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz listę napisów. Posortuj tę listę względem długości napisów, od najkrótszego do najdłuższego.

### Dane wejściowe

- Lista napisów.

### Dane wyjściowe

- Lista napisów posortowana według długości.

### Przykład

- **Dane wejściowe**:
  ```
  ['abcd', 'ab', 'a', 'abc']
  ```
- **Oczekiwane wyjście**:
  ```
  ['a', 'ab', 'abc', 'abcd']
  ```

### Wskazówki

- Użyj funkcji sortującej z kluczem `len`.

---

## Zadanie 5 - Sortowanie listy miast

**Poziom trudności**: ★☆☆

### Treść zadania

Masz klasę `Miasto`, która posiada dwie właściwości:

- `nazwa` — napis,
- `liczba_mieszkańców` — liczba naturalna.

Otrzymujesz listę obiektów tej klasy.

**a)** Posortuj listę miast alfabetycznie według nazw.

**b)** Posortuj listę miast według liczby mieszkańców (rosnąco).

### Dane wejściowe

- Lista obiektów klasy `Miasto`.

### Dane wyjściowe

- Lista obiektów klasy `Miasto` posortowana zgodnie z podanym kryterium.

### Przykład

- **Dane wejściowe**:
  ```
  [Miasto("Paris", 2150000), Miasto("Berlin", 3800000), Miasto("New York", 8400000)]
  ```
- **Oczekiwane wyjście**:

  **a)**
  ```
  [Miasto("Berlin", 3800000), Miasto("New York", 8400000), Miasto("Paris", 2150000)]
  ```

  **b)**
  ```
  [Miasto("Paris", 2150000), Miasto("Berlin", 3800000), Miasto("New York", 8400000)]
  ```

### Wskazówki

- Przy sortowaniu możesz użyć funkcji sortującej z kluczem, który odwołuje się do odpowiedniej właściwości obiektu.

---

## Zadanie 6 - Sortowanie listy binarnej

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz listę liczb naturalnych, składającą się wyłącznie z zer i jedynek. Posortuj tę listę w kolejności rosnącej.

### Dane wejściowe

- Lista liczb naturalnych (0 lub 1).

### Dane wyjściowe

- Posortowana lista liczb naturalnych.

### Przykład

- **Dane wejściowe**:
  ```
  [1, 0, 1, 0, 1, 1]
  ```
- **Oczekiwane wyjście**:
  ```
  [0, 0, 1, 1, 1, 1]
  ```

### Wskazówki

- Możesz użyć algorytmu zliczania lub funkcji sortującej.

---

## Zadanie 7 - Sortowanie listy liczb z zakresu 0-2

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz listę liczb naturalnych, w której elementami są tylko 0, 1 lub 2. Posortuj tę listę w kolejności rosnącej.

### Dane wejściowe

- Lista liczb naturalnych (0, 1, 2).

### Dane wyjściowe

- Posortowana lista liczb naturalnych.

### Przykład

- **Dane wejściowe**:
  ```
  [1, 0, 1, 2, 2, 0, 1]
  ```
- **Oczekiwane wyjście**:
  ```
  [0, 0, 1, 1, 1, 2, 2]
  ```

### Wskazówki

- Możesz użyć algorytmu zliczania liczby wystąpień każdego z elementów.

---

## Zadanie 8 - Wyszukiwanie indeksu klucza w cyklicznie posortowanej liście

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz cyklicznie posortowaną listę liczb całkowitych oraz klucz. Lista jest posortowana rosnąco, ale została przesunięta o pewną liczbę miejsc (rotacja). Twoim zadaniem jest znaleźć indeks pierwszego wystąpienia klucza w tej liście. Jeśli klucz nie występuje w liście, zwróć -1.

### Dane wejściowe

- Lista liczb całkowitych — cyklicznie posortowana.
- Liczba całkowita — klucz do znalezienia.

### Dane wyjściowe

- Liczba całkowita — indeks pierwszego wystąpienia klucza lub -1, jeśli klucz nie występuje.

### Przykład

- **Dane wejściowe**:
  ```
  [3, 4, 5, 6, 1, 2]
  4
  ```
- **Oczekiwane wyjście**:
  ```
  1
  ```

### Wskazówki

- Użyj zmodyfikowanego algorytmu wyszukiwania binarnego, który uwzględnia rotację listy.
- Sprawdź, w której części listy (lewej czy prawej) należy kontynuować poszukiwania.

---
