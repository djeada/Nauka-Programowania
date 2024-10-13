# Sortowanie — Algorytmy

## Zadanie 1 - Sortowanie bąbelkowe

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz algorytm sortowania bąbelkowego dla listy liczb całkowitych. Algorytm polega na wielokrotnym porównywaniu sąsiednich elementów listy i zamianie ich miejscami, jeśli są w niewłaściwej kolejności. Proces ten jest powtarzany, aż cała lista zostanie posortowana, czyli przejście przez listę nie spowoduje żadnych zmian.

### Dane wejściowe

- Lista liczb całkowitych.

### Dane wyjściowe

- Posortowana lista liczb całkowitych w kolejności rosnącej.

### Przykład

- **Dane wejściowe**:
  ```
  [6, 2, 1, 4, 27]
  ```
- **Oczekiwane wyjście**:
  ```
  [1, 2, 4, 6, 27]
  ```

### Wskazówki

- W każdej iteracji największy element "wypływa" na koniec nieposortowanej części listy.
- Pamiętaj o zmniejszaniu zakresu iteracji po każdej pełnej przebieżce.

---

## Zadanie 2 - Sortowanie przez wybieranie

**Poziom trudności**: ★★☆

### Treść zadania

Napisz algorytm sortowania przez wybieranie dla listy liczb całkowitych. Algorytm działa poprzez wielokrotne znajdowanie najmniejszego elementu z nieposortowanej części listy i zamianę go z pierwszym elementem tej części. Proces ten jest powtarzany, aż cała lista zostanie posortowana.

### Dane wejściowe

- Lista liczb całkowitych.

### Dane wyjściowe

- Posortowana lista liczb całkowitych w kolejności rosnącej.

### Przykład

- **Dane wejściowe**:
  ```
  [6, 2, 1, 4, 27]
  ```
- **Oczekiwane wyjście**:
  ```
  [1, 2, 4, 6, 27]
  ```

### Wskazówki

- Dla każdego indeksu znajdź najmniejszy element w nieposortowanej części i zamień go z elementem na bieżącym indeksie.
- Algorytm ma złożoność czasową O(n²).

---

## Zadanie 3 - Sortowanie przez wstawianie

**Poziom trudności**: ★★☆

### Treść zadania

Napisz algorytm sortowania przez wstawianie dla listy liczb całkowitych. Algorytm działa poprzez budowanie posortowanej listy element po elemencie. Dla każdego elementu z listy wejściowej wstaw go w odpowiednie miejsce w posortowanej części listy.

### Dane wejściowe

- Lista liczb całkowitych.

### Dane wyjściowe

- Posortowana lista liczb całkowitych w kolejności rosnącej.

### Przykład

- **Dane wejściowe**:
  ```
  [6, 2, 1, 4, 27]
  ```
- **Oczekiwane wyjście**:
  ```
  [1, 2, 4, 6, 27]
  ```

### Wskazówki

- Przechodź przez listę i dla każdego elementu przesuń go w lewo, aż znajdzie odpowiednie miejsce.
- Algorytm jest efektywny dla niemal posortowanych danych.

---

## Zadanie 4 - Sortowanie przez scalanie

**Poziom trudności**: ★★☆

### Treść zadania

Zaimplementuj algorytm sortowania przez scalanie dla danej listy liczb całkowitych. Algorytm działa rekurencyjnie, dzieląc listę na mniejsze części i łącząc je w posortowane fragmenty.

Algorytm:

1. Jeśli lista ma mniej niż dwa elementy, jest już posortowana.
2. Podziel listę na dwie (w miarę) równe części.
3. Rekurencyjnie zastosuj sortowanie przez scalanie do obu części.
4. Scal dwie posortowane części w jedną posortowaną listę.

### Dane wejściowe

- Lista liczb całkowitych.

### Dane wyjściowe

- Posortowana lista liczb całkowitych w kolejności rosnącej.

### Przykład

- **Dane wejściowe**:
  ```
  [6, 2, 1, 4, 27]
  ```
- **Oczekiwane wyjście**:
  ```
  [1, 2, 4, 6, 27]
  ```

### Wskazówki

- Funkcja scalająca powinna łączyć dwie posortowane listy w jedną.
- Algorytm ma złożoność czasową O(n log n).

---

## Zadanie 5 - Sortowanie szybkie

**Poziom trudności**: ★★☆

### Treść zadania

Zaimplementuj algorytm sortowania szybkiego (Quick Sort) dla danej listy liczb całkowitych. Algorytm działa poprzez wybór elementu zwanego pivotem i podział listy na części.

Algorytm:

1. Jeśli lista ma mniej niż dwa elementy, jest już posortowana.
2. Wybierz pivot (np. pierwszy element listy).
3. Podziel listę na trzy części:
   - Elementy mniejsze od pivota.
   - Elementy równe pivotowi.
   - Elementy większe od pivota.
4. Rekurencyjnie zastosuj sortowanie szybkie do części z elementami mniejszymi i większymi od pivota.
5. Połącz wyniki w następującej kolejności: posortowane mniejsze, pivoty, posortowane większe.

### Dane wejściowe

- Lista liczb całkowitych.

### Dane wyjściowe

- Posortowana lista liczb całkowitych w kolejności rosnącej.

### Przykład

- **Dane wejściowe**:
  ```
  [6, 2, 1, 4, 27]
  ```
- **Oczekiwane wyjście**:
  ```
  [1, 2, 4, 6, 27]
  ```

### Wskazówki

- W najgorszym przypadku algorytm ma złożoność O(n²), ale średnio O(n log n).
- Dobór pivota może wpłynąć na wydajność algorytmu.

