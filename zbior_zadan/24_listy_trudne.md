# Listy — trudne

## Zadanie 1 - Najdłuższy ciąg jedynek

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz listę składającą się wyłącznie z zer i jedynek. Twoim zadaniem jest znaleźć indeks zera, które po zamianie na jedynkę spowoduje uzyskanie najdłuższego ciągu jedynek w tej liście. Jeśli lista składa się wyłącznie z zer lub wyłącznie z jedynek, zwróć `-1`.

### Dane wejściowe

- **Lista liczb naturalnych** — lista składająca się z zer i jedynek.

### Dane wyjściowe

- **Jedna liczba całkowita** — indeks zera, którego zamiana na jedynkę da najdłuższy ciąg jedynek.
- Jeśli lista składa się wyłącznie z zer lub jedynek, zwróć `-1`.

### Przykład

- **Dane wejściowe**:
  ```
  [0, 0, 1, 0, 1, 1, 1, 0, 1, 1]
  ```
- **Oczekiwane wyjście**:
  ```
  7
  ```

**Wyjaśnienie**:

Zmiana zera na indeksie `7` (ósmy element listy) na jedynkę tworzy najdłuższy ciąg jedynek o długości `6`.

### Wskazówki

- Przeanalizuj listę, identyfikując ciągi jedynek otoczone zerami.
- Dla każdego zera oblicz sumę długości ciągów jedynek sąsiadujących z tym zerem.
- Wybierz zero, które po zamianie maksymalizuje długość ciągu jedynek.

---

## Zadanie 2 - Przesuń zera na koniec listy

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz listę liczb całkowitych. Przenieś wszystkie zera na koniec listy, zachowując kolejność pozostałych elementów.

### Dane wejściowe

- **Lista liczb całkowitych**.

### Dane wyjściowe

- **Lista liczb całkowitych** — lista z zerami przeniesionymi na koniec.

### Przykład

- **Dane wejściowe**:
  ```
  [0, 1, 3, 0, 8, 12, 0, 4, 0, 7, 0]
  ```
- **Oczekiwane wyjście**:
  ```
  [1, 3, 8, 12, 4, 7, 0, 0, 0, 0, 0]
  ```

### Wskazówki

- Przejdź przez listę i zbierz wszystkie elementy różne od zera.
- Policz liczbę zer i dodaj je na końcu listy.

---

## Zadanie 3 - Minimalny iloczyn trzech liczb

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz listę liczb całkowitych. Znajdź najmniejszy możliwy iloczyn trzech liczb wybranych z tej listy. Jeśli lista zawiera mniej niż trzy liczby, oblicz iloczyn wszystkich jej elementów.

### Dane wejściowe

- **Lista liczb całkowitych**.

### Dane wyjściowe

- **Jedna liczba całkowita** — najmniejszy iloczyn trzech liczb lub iloczyn wszystkich elementów, jeśli lista ma mniej niż trzy elementy.

### Przykład

- **Dane wejściowe**:
  ```
  [3, -1, -3, 2, 9, 4]
  ```
- **Oczekiwane wyjście**:
  ```
  -108
  ```

**Wyjaśnienie**:

Najmniejszy iloczyn to \(-3 \times 9 \times 4 = -108\).

### Wskazówki

- Rozważ kombinacje najmniejszych i największych liczb, ponieważ iloczyn dwóch ujemnych liczb jest dodatni.
- Możesz posortować listę i sprawdzić możliwe kombinacje skrajnych wartości.

---

## Zadanie 4 - Wspólny podciąg o największej sumie

**Poziom trudności**: ★★★

### Treść zadania

Otrzymujesz dwie listy binarne \( A \) i \( B \) (składające się z zer i jedynek) o tej samej długości. Znajdź maksymalną długość podciągu (ciągłych elementów), dla którego suma elementów w podciągu z listy \( A \) jest równa sumie elementów w odpowiadającym podciągu z listy \( B \). Podciągi muszą zaczynać się i kończyć na tych samych indeksach w obu listach.

### Dane wejściowe

- **Dwie listy liczb binarnych** — listy \( A \) i \( B \) tej samej długości.

### Dane wyjściowe

- **Jedna liczba naturalna** — maksymalna długość podciągu spełniającego warunek.

### Przykład

- **Dane wejściowe**:
  ```
  A = [0, 0, 1, 1, 1, 1]
  B = [0, 1, 1, 0, 1, 0]
  ```
- **Oczekiwane wyjście**:
  ```
  5
  ```

**Wyjaśnienie**:

Podciąg od indeksu 0 do 4 (pięć elementów) ma sumę równą 3 w obu listach.

### Wskazówki

- Oblicz różnicę sum skumulowanych list \( A \) i \( B \).
- Poszukaj najdłuższego podciągu, w którym różnica sum skumulowanych jest taka sama.

---

## Zadanie 5 - Zbiór potęgowy listy

**Poziom trudności**: ★★★

### Treść zadania

Otrzymujesz listę liczb naturalnych (mogą występować powtórzenia). Wygeneruj zbiór wszystkich możliwych podzbiorów tej listy, uwzględniając powtórzenia i kolejność elementów.

### Dane wejściowe

- **Lista liczb naturalnych**.

### Dane wyjściowe

- **Lista list** — wszystkie możliwe podzbiory elementów z listy wejściowej, włącznie z pustą listą.

### Przykład

- **Dane wejściowe**:
  ```
  [1, 2, 1]
  ```
- **Oczekiwane wyjście**:
  ```
  [[], [1], [2], [1, 2], [1, 1], [2, 1], [1, 1, 2], [1, 2, 1], [1, 1, 2, 1]]
  ```

**Uwaga**:

Kolejność elementów i powtórzenia są istotne.

### Wskazówki

- Możesz użyć algorytmu generującego kombinacje na podstawie binarnej reprezentacji liczb od \( 0 \) do \( 2^n - 1 \).
- Dla każdej pozycji w liście zdecyduj, czy element jest w podzbiorze.

---

## Zadanie 6 - Połączenie posortowanych list

**Poziom trudności**: ★★★

### Treść zadania

Otrzymujesz listę zawierającą \( M \) posortowanych list liczb naturalnych. Połącz te listy w jedną posortowaną listę zawierającą wszystkie elementy bez powtórzeń.

### Dane wejściowe

- **Lista posortowanych list liczb naturalnych**.

### Dane wyjściowe

- **Jedna posortowana lista liczb naturalnych** — zawierająca unikalne elementy ze wszystkich list wejściowych.

### Przykład

- **Dane wejściowe**:
  ```
  [
    [-6, 23, 29, 33],
    [6, 22, 35, 71],
    [5, 19, 21, 37],
    [-12, -7, -3, 28]
  ]
  ```
- **Oczekiwane wyjście**:
  ```
  [-12, -7, -6, -3, 5, 6, 19, 21, 22, 23, 28, 29, 33, 35, 37, 71]
  ```

### Wskazówki

- Użyj algorytmu scalania wielu list, np. z wykorzystaniem kopca (kolejki priorytetowej).
- Pamiętaj o usunięciu duplikatów podczas scalania.

---

## Zadanie 7 - Obliczanie pojemności wody między słupkami

**Poziom trudności**: ★★★

### Treść zadania

Otrzymujesz listę liczb naturalnych reprezentujących wysokości słupków ustawionych obok siebie. Twoim zadaniem jest obliczyć, ile jednostek wody może zostać zatrzymanych pomiędzy słupkami po opadach deszczu.

### Dane wejściowe

- **Lista liczb naturalnych** — wysokości słupków.

### Dane wyjściowe

- **Jedna liczba naturalna** — maksymalna ilość wody, jaka może zostać zatrzymana.

### Przykład

- **Dane wejściowe**:
  ```
  [3, 0, 1, 0, 2]
  ```
- **Oczekiwane wyjście**:
  ```
  5
  ```

**Wyjaśnienie**:

Łączna ilość wody zatrzymanej między słupkami wynosi 5 jednostek.

### Wskazówki

- Dla każdego słupka oblicz maksymalną wysokość słupka po lewej i prawej stronie.
- Ilość wody nad danym słupkiem to minimalna z tych dwóch wartości minus wysokość bieżącego słupka.

---

## Zadanie 8 - Maksymalny zysk ze sprzedaży sznurka

**Poziom trudności**: ★★★

### Treść zadania

Masz sznurek o długości \( n \) jednostek i cennik określający ceny sznurków o długościach od 1 do \( n \). Możesz pociąć sznurek na kawałki o całkowitych długościach. Znajdź maksymalny zysk, jaki można uzyskać ze sprzedaży sznurka.

### Dane wejściowe

- **Lista \( n \) liczb całkowitych** — ceny sznurków o długościach od 1 do \( n \).
- **Liczba naturalna \( n \)** — długość sznurka do sprzedania.

### Dane wyjściowe

- **Jedna liczba całkowita** — maksymalny zysk ze sprzedaży.

### Przykład

- **Dane wejściowe**:
  - Ceny: `[1, 5, 8, 9, 10, 17, 17, 20]`
  - Długość sznurka: `4`
- **Oczekiwane wyjście**:
  ```
  10
  ```

**Wyjaśnienie**:

Największy zysk uzyskamy, sprzedając sznurek o długości 4 w całości.

### Wskazówki

- Zastosuj podejście dynamiczne, rozważając wszystkie możliwe podziały sznurka.
- Użyj pamięci podręcznej do przechowywania wyników dla mniejszych długości.

---

## Zadanie 9 - Najdłuższy naprzemienny podciąg

**Poziom trudności**: ★★★

### Treść zadania

Otrzymujesz listę liczb całkowitych. Znajdź najdłuższy podciąg naprzemienny, w którym różnice między kolejnymi elementami zmieniają znak na przeciwny.

### Dane wejściowe

- **Lista liczb całkowitych**.

### Dane wyjściowe

- **Lista liczb całkowitych** — najdłuższy naprzemienny podciąg.

### Przykład

- **Dane wejściowe**:
  ```
  [1, -2, 6, 4, -3, 2, -4, -3]
  ```
- **Oczekiwane wyjście**:
  ```
  [1, -2, 6, -3, 2, -4]
  ```

### Wskazówki

- Przechowuj dwa stany dla każdego elementu: rosnący i malejący.
- Dla każdego elementu aktualizuj maksymalną długość naprzemiennego podciągu.
