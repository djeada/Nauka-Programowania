---

## Zadanie 1 - Macierz z identycznymi wierszami, składającymi się z liczb od 0 do \( b \)

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz dwie liczby naturalne \( a \) i \( b \). Utwórz macierz składającą się z \( a \) identycznych wierszy, gdzie każdy wiersz zawiera liczby od 0 do \( b \) włącznie.

### Dane wejściowe

- Dwie liczby naturalne \( a \) i \( b \), każda podana w osobnej linii.

### Dane wyjściowe

- Macierz składająca się z \( a \) wierszy.
- Każdy wiersz zawiera liczby od 0 do \( b \) włącznie, oddzielone spacjami.
- Każdy wiersz wypisz w osobnej linii.

### Przykład

- **Dane wejściowe**:
  ```
  3
  2
  ```
- **Oczekiwane wyjście**:
  ```
  0 1 2
  0 1 2
  0 1 2
  ```

### Wskazówki

- Wygeneruj listę liczb od 0 do \( b \).
- Powtórz ten wiersz \( a \) razy, tworząc macierz.

---

## Zadanie 2 - Macierz kwadratowa z iloczynem współrzędnych

**Poziom trudności**: ★☆☆

### Treść zadania

Dla podanej liczby naturalnej \( n \), utwórz macierz kwadratową o wymiarach \( n \times n \), w której każdy element jest iloczynem jego indeksów wiersza i kolumny.

### Dane wejściowe

- Jedna liczba naturalna \( n \) (\( n \geq 1 \)).

### Dane wyjściowe

- Macierz składająca się z \( n \) wierszy i \( n \) kolumn.
- Element na pozycji \( [i][j] \) (przy indeksowaniu od 0) jest równy \( i \times j \).
- Każdy wiersz wypisz w osobnej linii, a elementy w wierszu oddziel spacjami.

### Przykład

- **Dane wejściowe**:
  ```
  3
  ```
- **Oczekiwane wyjście**:
  ```
  0 0 0
  0 1 2
  0 2 4
  ```

### Wskazówki

- Użyj zagnieżdżonych pętli, aby wypełnić macierz.

---

## Zadanie 3 - Macierz z parami elementów odpowiadających sobie z dwóch list

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz dwie listy liczb naturalnych. Utwórz macierz dwukolumnową, w której:

- Pierwsza kolumna zawiera elementy pierwszej listy.
- Druga kolumna zawiera elementy drugiej listy.

Jeśli listy nie są tej samej długości, zwróć pustą macierz.

### Dane wejściowe

- Dwie liczby naturalne \( n \) i \( m \) — długości list, każda w osobnej linii.
- Następnie \( n \) liczb naturalnych — elementy pierwszej listy.
- Następnie \( m \) liczb naturalnych — elementy drugiej listy.

### Dane wyjściowe

- Jeśli \( n = m \), wypisz macierz o \( n \) wierszach i 2 kolumnach.
  - Każdy wiersz wypisz w osobnej linii, elementy w wierszu oddziel spacjami.
- Jeśli \( n \ne m \), wypisz komunikat **"Pusta macierz"**.

### Przykład

- **Dane wejściowe**:
  ```
  3
  3
  3
  5
  2
  2
  8
  1
  ```
- **Oczekiwane wyjście**:
  ```
  3 2
  5 8
  2 1
  ```

### Wskazówki

- Sprawdź, czy długości list są równe.
- Jeśli nie, wypisz odpowiedni komunikat.

---

## Zadanie 4 - Dodawanie i odejmowanie macierzy

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz dwie macierze o tych samych wymiarach. Wykonaj następujące operacje:

- **a)** Dodaj do siebie elementy obu macierzy, tworząc nową macierz.
- **b)** Odejmij od pierwszej macierzy drugą macierz, tworząc nową macierz.

### Dane wejściowe

- Dwie liczby naturalne \( n \) i \( m \) — liczba wierszy i kolumn macierzy, każda w osobnej linii.
- Następnie \( n \) wierszy pierwszej macierzy, każdy wiersz zawiera \( m \) liczb całkowitych oddzielonych spacjami.
- Następnie \( n \) wierszy drugiej macierzy, każdy wiersz zawiera \( m \) liczb całkowitych oddzielonych spacjami.

### Dane wyjściowe

- **Podpunkt a):** macierz będąca sumą obu macierzy.
- **Podpunkt b):** macierz będąca różnicą pierwszej i drugiej macierzy.
- Każdy wiersz macierzy wypisz w osobnej linii, elementy w wierszu oddziel spacjami.

### Przykład

- **Dane wejściowe**:
  ```
  2
  2
  1 2
  -2 0
  5 -3
  1 7
  ```
- **Oczekiwane wyjście**:

  **Podpunkt a):**
  ```
  6 -1
  -1 7
  ```

  **Podpunkt b):**
  ```
  -4 5
  -3 -7
  ```

### Wskazówki

- Upewnij się, że macierze mają takie same wymiary.
- Dodawaj i odejmuj odpowiadające sobie elementy macierzy.

---

## Zadanie 5 - Sprawdzanie czy macierz jest "magiczna"

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz macierz kwadratową z dodatnimi liczbami naturalnymi. Sprawdź, czy jest to kwadrat magiczny, czyli czy suma liczb w każdym wierszu, każdej kolumnie oraz obu przekątnych jest taka sama.

### Dane wejściowe

- Jedna liczba naturalna \( n \) — wymiar macierzy (\( n \geq 1 \)).
- Następnie \( n \) wierszy macierzy, każdy wiersz zawiera \( n \) liczb naturalnych oddzielonych spacjami.

### Dane wyjściowe

- Jeden napis: **"Prawda"**, jeśli macierz jest kwadratem magicznym, lub **"Fałsz"**, jeśli nie jest.

### Przykład

- **Dane wejściowe**:
  ```
  3
  6 7 2
  1 5 9
  8 3 4
  ```
- **Oczekiwane wyjście**:
  ```
  Prawda
  ```

### Wskazówki

- Oblicz sumę pierwszego wiersza jako sumę oczekiwaną.
- Sprawdź sumy wszystkich wierszy, kolumn i obu przekątnych.

---

## Zadanie 6 - Scalanie przedziałów w liście przedziałów

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz listę przedziałów, gdzie każdy przedział jest parą liczb naturalnych \([a_i, b_i]\), przy czym \( a_i \leq b_i \). Niektóre przedziały mogą się nakładać na siebie. Połącz nakładające się przedziały i zwróć listę przedziałów, które się nie pokrywają.

### Dane wejściowe

- Jedna liczba naturalna \( n \) — liczba przedziałów (\( n \geq 1 \)).
- Następnie \( n \) wierszy, każdy zawiera dwa liczby naturalne \( a_i \) i \( b_i \), oddzielone spacją.

### Dane wyjściowe

- Lista przedziałów po scaleniu, każdy przedział wypisz w osobnej linii w formacie \( a_j \) i \( b_j \), oddzielone spacją.
- Przedziały wypisz w kolejności rosnącej po ich początkach.

### Przykład

- **Dane wejściowe**:
  ```
  7
  23 67
  23 53
  45 88
  77 88
  10 22
  11 12
  42 45
  ```
- **Oczekiwane wyjście**:
  ```
  10 22
  23 88
  ```

### Wskazówki

- Posortuj przedziały według początków.
- Iteruj przez przedziały i scalaj je, jeśli się nakładają.

---

## Zadanie 7 - Zerowanie macierzy

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz macierz (listę list) liczb naturalnych. Jeśli którykolwiek element macierzy jest równy zero, zamień wszystkie elementy w jego wierszu i kolumnie na zera.

### Dane wejściowe

- Dwie liczby naturalne \( n \) i \( m \) — liczba wierszy i kolumn macierzy (\( n \geq 1, m \geq 1 \)).
- Następnie \( n \) wierszy macierzy, każdy zawiera \( m \) liczb naturalnych oddzielonych spacjami.

### Dane wyjściowe

- Macierz po przekształceniu, wypisz w takiej samej formie jak dane wejściowe.
- Każdy wiersz wypisz w osobnej linii, elementy w wierszu oddziel spacjami.

### Przykład

- **Dane wejściowe**:
  ```
  3 3
  1 2 3
  4 0 6
  7 8 9
  ```
- **Oczekiwane wyjście**:
  ```
  1 0 3
  0 0 0
  7 0 9
  ```

### Wskazówki

- Najpierw znajdź wszystkie pozycje zer w macierzy.
- Następnie ustaw odpowiednie wiersze i kolumny na zera.

---

## Zadanie 8 - Wypisanie elementów macierzy spiralnie

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz macierz (listę list) liczb naturalnych. Wypisz elementy macierzy w kolejności spiralnej, zaczynając od elementu w lewym górnym rogu i poruszając się zgodnie z ruchem wskazówek zegara.

### Dane wejściowe

- Dwie liczby naturalne \( n \) i \( m \) — liczba wierszy i kolumn macierzy (\( n \geq 1, m \geq 1 \)).
- Następnie \( n \) wierszy macierzy, każdy zawiera \( m \) liczb naturalnych oddzielonych spacjami.

### Dane wyjściowe

- Jedna linia zawierająca elementy macierzy w kolejności spiralnej, oddzielone spacjami.

### Przykład

- **Dane wejściowe**:
  ```
  3 3
  1 2 3
  4 5 6
  7 8 9
  ```
- **Oczekiwane wyjście**:
  ```
  1 2 3 6 9 8 7 4 5
  ```

### Wskazówki

- Użyj zmiennych do śledzenia granic macierzy podczas iteracji spiralnej.

---

## Zadanie 9 - Klepsydra o największej sumie

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz macierz (listę list) liczb całkowitych o wymiarach co najmniej \( 3 \times 3 \). Znajdź klepsydrę o największej sumie. Klepsydra składa się z 7 elementów:

- Trzy kolejne elementy w jednym wierszu.
- Jeden element bezpośrednio pod środkowym elementem z poprzedniego wiersza.
- Trzy kolejne elementy w wierszu dwa poziomy niżej, w tych samych kolumnach co pierwsze trzy elementy.

### Dane wejściowe

- Dwie liczby naturalne \( n \) i \( m \) — liczba wierszy i kolumn macierzy (\( n \geq 3, m \geq 3 \)).
- Następnie \( n \) wierszy macierzy, każdy zawiera \( m \) liczb całkowitych oddzielonych spacjami.

### Dane wyjściowe

- Jedna liczba całkowita — maksymalna suma elementów klepsydry w macierzy.

### Przykład

- **Dane wejściowe**:
  ```
  4 4
  7 4 2 0
  4 8 10 8
  3 6 7 6
  3 9 19 14
  ```
- **Oczekiwane wyjście**:
  ```
  75
  ```

### Wskazówki

- Przejdź przez wszystkie możliwe pozycje klepsydr w macierzy.
- Oblicz sumę elementów dla każdej klepsydry i zachowaj największą.

---

## Zadanie 10 - Obróć macierz o 90 stopni

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz kwadratową macierz liczb naturalnych. Obróć ją o 90 stopni zgodnie z ruchem wskazówek zegara.

### Dane wejściowe

- Jedna liczba naturalna \( n \) — wymiar macierzy (\( n \geq 1 \)).
- Następnie \( n \) wierszy macierzy, każdy wiersz zawiera \( n \) liczb naturalnych oddzielonych spacjami.

### Dane wyjściowe

- Macierz po obrocie, wypisz w takiej samej formie jak dane wejściowe.

### Przykład

- **Dane wejściowe**:
  ```
  3
  1 2 3
  4 5 6
  7 8 9
  ```
- **Oczekiwane wyjście**:
  ```
  7 4 1
  8 5 2
  9 6 3
  ```

### Wskazówki

- Możesz transponować macierz, a następnie odwrócić kolejność elementów w każdym wierszu.

---

## Zadanie 11 - Gra w statki

**Poziom trudności**: ★★★

### Treść zadania

Stwórz grę w statki na planszy \( 10 \times 10 \):

1. **Przygotowanie planszy**:
   - Utwórz macierz \( 10 \times 10 \) wypełnioną znakami '.' (kropka).
   - Wylosuj położenie następujących statków:
     - 1 statek o długości 4.
     - 2 statki o długości 3.
     - 3 statki o długości 2.
     - 5 statków o długości 1.
   - Statki mogą być umieszczane poziomo lub pionowo.
   - Statki nie mogą się stykać ani nachodzić na siebie.

2. **Rozgrywka**:
   - Wyświetl planszę złożoną z 10 wierszy po 10 kropek.
   - Poproś użytkownika o podanie współrzędnych (wiersz i kolumna) do ostrzału.
   - Jeśli na podanych współrzędnych znajduje się część statku, zamień kropkę na 'o' i poinformuj o trafieniu.
   - Jeśli nie trafiono w statek, zamień kropkę na 'x' i poinformuj o pudle.
   - Wyświetl zaktualizowaną planszę po każdym ruchu.

3. **Zakończenie gry**:
   - Gra kończy się, gdy wszystkie części statków zostaną trafione (wygrana) lub gdy użytkownik wykona 10 nietrafionych strzałów (przegrana).
   - Po zakończeniu gry poinformuj użytkownika o wyniku.

### Dane wejściowe

- W trakcie gry użytkownik podaje pary liczb naturalnych \( r \) i \( c \) (\( 0 \leq r, c < 10 \)), reprezentujące wiersz i kolumnę na planszy.

### Dane wyjściowe

- W trakcie gry wyświetlaj aktualną planszę po każdym ruchu.
- Po zakończeniu gry wyświetl komunikat o wygranej lub przegranej.

### Przykład

- **Rozpoczęcie gry**:
  ```
  . . . . . . . . . .
  . . . . . . . . . .
  . . . . . . . . . .
  . . . . . . . . . .
  . . . . . . . . . .
  . . . . . . . . . .
  . . . . . . . . . .
  . . . . . . . . . .
  . . . . . . . . . .
  . . . . . . . . . .
  ```
- **Przykładowy komunikat po strzale**:
  ```
  Podaj współrzędne (wiersz i kolumna): 2 3
  Pudło!
  ```
- **Zakończenie gry**:
  ```
  Gratulacje! Zatopiłeś wszystkie statki.
  ```

### Wskazówki

- Do losowania położeń statków możesz użyć generatora liczb losowych.
- Upewnij się, że statki nie nachodzą na siebie i nie stykają się bokami ani rogami.
- Śledź liczbę trafionych i nietrafionych strzałów.

---
