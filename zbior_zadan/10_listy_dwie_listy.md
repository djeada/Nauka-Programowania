## Zadanie 1 - Wypisanie elementów dwóch list na przemian

**Poziom trudności**: ★☆☆

### Treść zadania

Dla otrzymanych dwóch list liczb całkowitych, wypisz na przemian elementy z obu list. Jeśli listy nie są tej samej długości, po wyczerpaniu elementów krótszej listy kontynuuj wypisywanie pozostałych elementów dłuższej listy.

### Dane wejściowe

- **Lista 1**: lista liczb całkowitych.
- **Lista 2**: lista liczb całkowitych.
- Listy mogą mieć dowolną długość i zawierać dowolne liczby całkowite.

### Dane wyjściowe

- Jedna linia zawierająca elementy obu list wypisane na przemian, oddzielone przecinkami (bez spacji).
- Po wyczerpaniu elementów krótszej listy, wypisz pozostałe elementy dłuższej listy w tej samej kolejności.

### Przykład

- **Dane wejściowe**:
  ```
  Lista 1: [5, 3, 7, 2]
  Lista 2: [1, -2, 3]
  ```
- **Oczekiwane wyjście**:
  ```
  5,1,3,-2,7,3,2
  ```

### Wskazówki

- Możesz użyć funkcji `zip()` do iteracji przez elementy obu list jednocześnie.
- Aby uwzględnić różne długości list, możesz użyć modułu `itertools` i funkcji `zip_longest()`.
- Alternatywnie, iteruj po indeksach do długości dłuższej listy, sprawdzając przy każdym kroku, czy indeks nie przekracza długości którejś z list.

---

## Zadanie 2 - Połączenie dwóch list

**Poziom trudności**: ★☆☆

### Treść zadania

Dla otrzymanych dwóch list liczb całkowitych, wykonaj następujące operacje:

- **a)** Połącz listy, dostawiając drugą listę na koniec pierwszej.
- **b)** Wstaw elementy o parzystych indeksach z drugiej listy na odpowiadające im indeksy pierwszej listy, zastępując istniejące elementy.

### Dane wejściowe

- **Lista 1**: lista liczb całkowitych.
- **Lista 2**: lista liczb całkowitych.
- Obie listy mogą mieć różną długość.

### Dane wyjściowe

- **Podpunkt a)**: Jedna lista zawierająca elementy pierwszej listy, a następnie elementy drugiej listy, w oryginalnej kolejności.
- **Podpunkt b)**: Jedna lista, w której elementy o parzystych indeksach zostały zastąpione elementami z drugiej listy o tych samych indeksach (jeśli istnieją).

### Przykład

- **Dane wejściowe**:
  ```
  Lista 1: [1, 2, 3]
  Lista 2: [4, 5, 6]
  ```
- **Oczekiwane wyjście**:

  **Podpunkt a)**:
  ```
  [1, 2, 3, 4, 5, 6]
  ```

  **Podpunkt b)**:
  ```
  [4, 2, 6, 3]
  ```

### Wskazówki

- **Podpunkt a)**: Możesz użyć operatora `+` do łączenia list.
- **Podpunkt b)**:
  - Iteruj po indeksach parzystych do długości krótszej z dwóch list.
  - W pierwszej liście podmień elementy o parzystych indeksach elementami z drugiej listy.
  - Jeśli druga lista jest krótsza, podmienisz tylko te elementy, które istnieją w obu listach.

---

## Zadanie 3 - Suma elementów dwóch list

**Poziom trudności**: ★☆☆

### Treść zadania

Dla otrzymanych dwóch list liczb całkowitych, zwróć listę, której elementy są sumą odpowiadających sobie elementów obu list. Jeśli listy nie są tej samej długości, brakujące elementy krótszej listy traktuj jako zera.

### Dane wejściowe

- **Lista 1**: lista liczb całkowitych.
- **Lista 2**: lista liczb całkowitych.
- Listy mogą mieć różne długości.

### Dane wyjściowe

- Jedna lista liczb całkowitych, gdzie każdy element jest sumą elementów o tym samym indeksie z obu list.
- Jeśli jedna z list jest krótsza, do sumy dodawane jest zero za brakujący element.

### Przykład

- **Dane wejściowe**:
  ```
  Lista 1: [3, 1, 2, 5]
  Lista 2: [2, 8, 6, 5]
  ```
- **Oczekiwane wyjście**:
  ```
  [5, 9, 8, 10]
  ```

### Wskazówki

- Ustal długość najdłuższej listy.
- Iteruj po indeksach od 0 do maksymalnej długości.
- Przy pobieraniu elementów z list sprawdzaj, czy indeks nie przekracza ich długości; jeśli tak, użyj zera.

---

## Zadanie 4 - Mnożenie wektorowe

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz dwie listy liczb całkowitych reprezentujące dwa wektory w trójwymiarowej przestrzeni euklidesowej. Zaimplementuj iloczyn skalarny tych wektorów.

### Dane wejściowe

- **Wektor A**: lista 3 liczb całkowitych.
- **Wektor B**: lista 3 liczb całkowitych.

### Dane wyjściowe

- Jedna liczba całkowita — wynik iloczynu skalarnego dwóch wektorów.

### Przykład

- **Dane wejściowe**:
  ```
  Wektor A: [1, 2, 3]
  Wektor B: [3, 1, 2]
  ```
- **Oczekiwane wyjście**:
  ```
  11
  ```
  *(Obliczenie: \( 1 \times 3 + 2 \times 1 + 3 \times 2 = 3 + 2 + 6 = 11 \))*

### Wskazówki

- Iloczyn skalarny dwóch wektorów \( \vec{A} \) i \( \vec{B} \) to suma iloczynów odpowiadających sobie współrzędnych: \( A_x B_x + A_y B_y + A_z B_z \).
- Upewnij się, że obie listy mają dokładnie 3 elementy.

---

## Zadanie 5 - Obliczenie średniej ważonej

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz dwie listy liczb zmiennoprzecinkowych:

- Pierwsza lista zawiera **wartości**.
- Druga lista zawiera odpowiadające im **wagi**.

Oblicz średnią ważoną tych wartości.

### Dane wejściowe

- **Lista wartości**: lista liczb zmiennoprzecinkowych.
- **Lista wag**: lista liczb zmiennoprzecinkowych.
- Obie listy mają tę samą długość.

### Dane wyjściowe

- Jedna liczba zmiennoprzecinkowa — średnia ważona wartości, obliczona jako suma iloczynów wartości i ich wag, podzielona przez sumę wag.

### Przykład

- **Dane wejściowe**:
  ```
  Wartości: [0.2, 0.4, 0.1, 0.2, 0.1]
  Wagi: [2.0, 5.0, 0.0, 2.0, 1.0]
  ```
- **Oczekiwane wyjście**:
  ```
  0.29
  ```
  *(Obliczenie: \( \frac{0.2 \times 2.0 + 0.4 \times 5.0 + 0.1 \times 0.0 + 0.2 \times 2.0 + 0.1 \times 1.0}{2.0 + 5.0 + 0.0 + 2.0 + 1.0} = \frac{0.4 + 2.0 + 0 + 0.4 + 0.1}{10.0} = \frac{2.9}{10.0} = 0.29 \))*

### Wskazówki

- Oblicz sumę iloczynów wartości i wag.
- Oblicz sumę wag.
- Podziel sumę iloczynów przez sumę wag.

---

## Zadanie 6 - Znalezienie elementów wspólnych dwóch list

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz dwie listy liczb całkowitych. Znajdź i wypisz elementy, które występują w obu listach.

### Dane wejściowe

- **Lista 1**: lista liczb całkowitych.
- **Lista 2**: lista liczb całkowitych.

### Dane wyjściowe

- Lista liczb całkowitych będących elementami wspólnymi obu list.
- Elementy wypisz w kolejności występowania w pierwszej liście.
- Jeśli nie ma elementów wspólnych, wypisz pustą listę `[]`.

### Przykład

- **Dane wejściowe**:
  ```
  Lista 1: [9, 2, 5, 4]
  Lista 2: [4, 2, 1]
  ```
- **Oczekiwane wyjście**:
  ```
  [2, 4]
  ```

### Wskazówki

- Możesz użyć zbiorów (`set`) do znalezienia przecięcia, ale pamiętaj o kolejności elementów.
- Iteruj przez pierwszą listę i dodawaj do wyniku elementy, które są również w drugiej liście.

---

## Zadanie 7 - Różnica między dwoma listami

**Poziom trudności**: ★☆☆

### Treść zadania

Dla otrzymanych dwóch list liczb całkowitych, znajdź elementy, które nie są wspólne dla obu list. Innymi słowy, wypisz elementy, które występują tylko w jednej z list.

### Dane wejściowe

- **Lista 1**: lista liczb całkowitych.
- **Lista 2**: lista liczb całkowitych.

### Dane wyjściowe

- Lista liczb całkowitych, które występują tylko w jednej z list.
- Elementy wypisz w dowolnej kolejności.
- Jeśli wszystkie elementy są wspólne, wypisz pustą listę `[]`.

### Przykład

- **Dane wejściowe**:
  ```
  Lista 1: [9, 2, 5, 4]
  Lista 2: [4, 2, 1]
  ```
- **Oczekiwane wyjście**:
  ```
  [9, 5, 1]
  ```

### Wskazówki

- Użyj operacji różnicy symetrycznej na zbiorach (`set`), aby znaleźć elementy unikalne dla każdej listy.
- Możesz też iterować przez obie listy i sprawdzać, czy element nie występuje w drugiej liście.

---

## Zadanie 8 - Połącz posortowane listy w posortowaną listę

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz dwie posortowane rosnąco listy liczb całkowitych. Połącz je w jedną posortowaną listę, eliminując duplikaty.

### Dane wejściowe

- **Lista 1**: posortowana rosnąco lista liczb całkowitych.
- **Lista 2**: posortowana rosnąco lista liczb całkowitych.

### Dane wyjściowe

- Jedna posortowana rosnąco lista liczb całkowitych, zawierająca elementy z obu list bez duplikatów.

### Przykład

- **Dane wejściowe**:
  ```
  Lista 1: [2, 4, 7]
  Lista 2: [3, 5, 9]
  ```
- **Oczekiwane wyjście**:
  ```
  [2, 3, 4, 5, 7, 9]
  ```

### Wskazówki

- Użyj metody merge z algorytmu sortowania przez scalanie.
- Iteruj przez obie listy jednocześnie, porównując bieżące elementy i dodając mniejszy do wyniku.
- Pamiętaj o obsłudze duplikatów i dodawaniu pozostałych elementów, gdy jedna z list się skończy.

---

## Zadanie 9 - Usuń z pierwszej listy część wspólną obu list

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz dwie listy liczb całkowitych. Usuń z pierwszej listy wszystkie elementy, które występują również w drugiej liście.

### Dane wejściowe

- **Lista 1**: lista liczb całkowitych.
- **Lista 2**: lista liczb całkowitych.

### Dane wyjściowe

- Lista liczb całkowitych zawierająca elementy pierwszej listy po usunięciu elementów wspólnych z drugą listą.
- Elementy wypisz w oryginalnej kolejności z pierwszej listy.
- Jeśli wszystkie elementy zostały usunięte, wypisz pustą listę `[]`.

### Przykład

- **Dane wejściowe**:
  ```
  Lista 1: [9, 2, 5, 4]
  Lista 2: [4, 2, 1]
  ```
- **Oczekiwane wyjście**:
  ```
  [9, 5]
  ```

### Wskazówki

- Przejdź przez pierwszą listę i dodaj do wyniku te elementy, które nie są w drugiej liście.
- Możesz użyć zbioru (`set`) z elementami drugiej listy dla szybszego sprawdzania przynależności.

---

## Zadanie 10 - Znajdź medianę dwóch posortowanych list

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz dwie posortowane rosnąco listy liczb całkowitych o równej długości. Znajdź medianę zbioru wszystkich elementów obu list.

### Dane wejściowe

- **Lista 1**: posortowana rosnąco lista liczb całkowitych.
- **Lista 2**: posortowana rosnąco lista liczb całkowitych.
- Obie listy mają tę samą, niezerową długość.

### Dane wyjściowe

- Jedna liczba zmiennoprzecinkowa — mediana wszystkich elementów z obu list.

### Przykład

- **Dane wejściowe**:
  ```
  Lista 1: [2, 4, 7]
  Lista 2: [3, 5, 9]
  ```
- **Oczekiwane wyjście**:
  ```
  4.5
  ```
  *(Złączone listy: [2, 3, 4, 5, 7, 9]; mediana to średnia z dwóch środkowych wartości: \( (4 + 5) / 2 = 4.5 \))*

### Wskazówki

- Połącz obie listy i posortuj wynikową listę.
- Mediana to środkowy element (lub średnia dwóch środkowych elementów, jeśli liczba elementów jest parzysta).
- Możesz zoptymalizować rozwiązanie, unikając pełnego sortowania, korzystając z właściwości posortowanych list.

---
