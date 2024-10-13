---

## Zadanie 1 - Konwersja pomiędzy systemami binarnym i dziesiętnym

**Poziom trudności**: ★☆☆

### Treść zadania

**a)** Otrzymujesz reprezentację dziesiętną liczby naturalnej. Zwróć jej reprezentację binarną.

**b)** Otrzymujesz reprezentację binarną liczby naturalnej. Zwróć jej reprezentację dziesiętną.

### Dane wejściowe

- **Podpunkt a):** Jedna liczba naturalna w systemie dziesiętnym.
- **Podpunkt b):** Jedna liczba naturalna w systemie binarnym (ciąg cyfr 0 i 1).

### Dane wyjściowe

- **Podpunkt a):** Reprezentacja binarna podanej liczby naturalnej (ciąg cyfr 0 i 1).
- **Podpunkt b):** Reprezentacja dziesiętna podanej liczby binarnej (liczba naturalna).

### Przykład

**Podpunkt a):**

- **Dane wejściowe**:
  ```
  3
  ```
- **Oczekiwane wyjście**:
  ```
  11
  ```

**Podpunkt b):**

- **Dane wejściowe**:
  ```
  101
  ```
- **Oczekiwane wyjście**:
  ```
  5
  ```

### Wskazówki

- **Podpunkt a):** Aby przekonwertować liczbę dziesiętną na binarną, dziel liczbę przez 2 i zapisuj reszty z dzielenia.
- **Podpunkt b):** Aby przekonwertować liczbę binarną na dziesiętną, pomnóż każdą cyfrę przez odpowiednią potęgę liczby 2 i zsumuj wyniki.

---

## Zadanie 2 - Konwersja warunkowa

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz liczbę naturalną. Zwróć jej reprezentację binarną tylko wtedy, gdy:

**a)** Liczba jest parzysta.

**b)** Liczba jest liczbą pierwszą.

### Dane wejściowe

- Jedna liczba naturalna.

### Dane wyjściowe

- Reprezentacja binarna podanej liczby naturalnej (ciąg cyfr 0 i 1), jeśli spełnia warunek.
- Jeśli liczba nie spełnia warunku, nie wypisuj nic.

### Przykład

**Podpunkt a):**

- **Dane wejściowe**:
  ```
  7
  ```
- **Oczekiwane wyjście**:
  ```
  ```
  *(Brak wyjścia, ponieważ 7 nie jest liczbą parzystą.)*

**Podpunkt b):**

- **Dane wejściowe**:
  ```
  7
  ```
- **Oczekiwane wyjście**:
  ```
  111
  ```

### Wskazówki

- **Podpunkt a):** Sprawdź, czy liczba jest podzielna przez 2.
- **Podpunkt b):** Sprawdź, czy liczba jest liczbą pierwszą, dzieląc ją przez wszystkie liczby naturalne mniejsze od niej i większe od 1.

---

## Zadanie 3 - Operacje arytmetyczne z użyciem operatorów bitowych

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz dwie liczby naturalne. Używając wyłącznie operatorów bitowych, zaimplementuj następujące operacje:

**a)** Dodawanie dwóch liczb.

**b)** Odejmowanie drugiej liczby od pierwszej.

**c)** Mnożenie dwóch liczb.

**d)** Dzielenie pierwszej liczby przez drugą (całkowite).

### Dane wejściowe

- Dwie liczby naturalne, każda w osobnej linii.

### Dane wyjściowe

- Jedna liczba naturalna — wynik odpowiedniej operacji arytmetycznej.

### Przykład

**Podpunkt a):**

- **Dane wejściowe**:
  ```
  2
  3
  ```
- **Oczekiwane wyjście**:
  ```
  5
  ```

**Podpunkt b):**

- **Dane wejściowe**:
  ```
  7
  5
  ```
- **Oczekiwane wyjście**:
  ```
  2
  ```

**Podpunkt c):**

- **Dane wejściowe**:
  ```
  4
  4
  ```
- **Oczekiwane wyjście**:
  ```
  16
  ```

**Podpunkt d):**

- **Dane wejściowe**:
  ```
  9
  3
  ```
- **Oczekiwane wyjście**:
  ```
  3
  ```

### Wskazówki

- **Operatorzy bitowi**: AND (&), OR (|), XOR (^), NOT (~), przesunięcia bitowe (<<, >>).
- **Dodawanie i odejmowanie** można zrealizować przy użyciu operatorów XOR i AND.
- **Mnożenie** można zrealizować poprzez wielokrotne dodawanie.
- **Dzielenie** można zrealizować poprzez wielokrotne odejmowanie lub przesunięcia bitowe.

---

## Zadanie 4 - Liczba zer i jedynek w reprezentacji binarnej

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz liczbę naturalną w systemie dziesiętnym.

**a)** Oblicz, ile zer zawiera jej binarna reprezentacja.

**b)** Oblicz, ile jedynek zawiera jej binarna reprezentacja.

### Dane wejściowe

- Jedna liczba naturalna.

### Dane wyjściowe

- Jedna liczba naturalna — liczba zer (podpunkt a) lub jedynek (podpunkt b) w reprezentacji binarnej.

### Przykład

**Podpunkt a):**

- **Dane wejściowe**:
  ```
  3
  ```
- **Oczekiwane wyjście**:
  ```
  0
  ```
  *(Reprezentacja binarna liczby 3 to '11', która nie zawiera zer.)*

**Podpunkt b):**

- **Dane wejściowe**:
  ```
  3
  ```
- **Oczekiwane wyjście**:
  ```
  2
  ```
  *(Reprezentacja binarna liczby 3 to '11', która zawiera dwie jedynki.)*

### Wskazówki

- Przekonwertuj liczbę na system binarny i zlicz wystąpienia '0' lub '1'.
- Możesz też iterować przez bity liczby, używając operacji bitowych.

---

## Zadanie 5 - Wybieranie minimum i maksimum bez instrukcji warunkowych

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz dwie liczby naturalne.

**a)** Zwróć mniejszą z nich, nie używając instrukcji warunkowych ani zewnętrznych bibliotek.

**b)** Zwróć większą z nich, nie używając instrukcji warunkowych ani zewnętrznych bibliotek.

### Dane wejściowe

- Dwie liczby naturalne, każda w osobnej linii.

### Dane wyjściowe

- Jedna liczba naturalna — mniejsza (podpunkt a) lub większa (podpunkt b) z podanych liczb.

### Przykład

**Podpunkt a):**

- **Dane wejściowe**:
  ```
  3
  2
  ```
- **Oczekiwane wyjście**:
  ```
  2
  ```

**Podpunkt b):**

- **Dane wejściowe**:
  ```
  3
  2
  ```
- **Oczekiwane wyjście**:
  ```
  3
  ```

### Wskazówki

- Możesz użyć operacji arytmetycznych i bitowych, takich jak dodawanie, odejmowanie, mnożenie, dzielenie oraz przesunięcia bitowe.
- Rozważ wykorzystanie różnicy liczb oraz właściwości znaku wyniku.

---

## Zadanie 6 - Konwersja między dowolnymi systemami liczbowymi

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz liczbę naturalną, podstawę systemu liczbowego, w którym jest zapisana ta liczba, oraz podstawę systemu docelowego. Przekonwertuj tę liczbę na nowy system liczbowy.

### Dane wejściowe

- Trzy liczby naturalne, każda w osobnej linii:
  1. Liczba do konwersji.
  2. Podstawa systemu liczbowego tej liczby (od 2 do 36).
  3. Podstawa systemu liczbowego docelowego (od 2 do 36).

### Dane wyjściowe

- Liczba naturalna — reprezentacja podanej liczby w nowym systemie liczbowym.

### Przykład

- **Dane wejściowe**:
  ```
  4301
  10
  4
  ```
- **Oczekiwane wyjście**:
  ```
  1003031
  ```

### Wskazówki

- Najpierw przekonwertuj liczbę do systemu dziesiętnego, jeśli nie jest w nim podana.
- Następnie przekonwertuj liczbę z systemu dziesiętnego na system docelowy.
- Dla podstaw większych niż 10 użyj odpowiednich symboli (np. A dla 10, B dla 11, ..., Z dla 35).

---

## Zadanie 7 - Odwrócenie sąsiadujących bitów

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz liczbę naturalną w systemie dziesiętnym. Zamień miejscami każdą parę sąsiadujących bitów w jej reprezentacji binarnej i zwróć wynik w systemie dziesiętnym.

### Dane wejściowe

- Jedna liczba naturalna.

### Dane wyjściowe

- Jedna liczba naturalna — wynik po zamianie miejscami sąsiadujących bitów.

### Przykład

- **Dane wejściowe**:
  ```
  9131
  ```
- **Oczekiwane wyjście**:
  ```
  4951
  ```

### Wskazówki

- Podziel bity liczby na pary i zamień w każdej parze bity miejscami.
- Jeśli liczba bitów jest nieparzysta, ostatni bit pozostaje bez zmian.

---

## Zadanie 8 - Najbliższa potęga dwójki

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz liczbę naturalną w systemie dziesiętnym. Znajdź najmniejszą potęgę liczby 2, która jest większa lub równa podanej liczbie.

### Dane wejściowe

- Jedna liczba naturalna.

### Dane wyjściowe

- Jedna liczba naturalna — potęga dwójki większa lub równa podanej liczbie.

### Przykład

- **Dane wejściowe**:
  ```
  111
  ```
- **Oczekiwane wyjście**:
  ```
  128
  ```

### Wskazówki

- Możesz wykorzystać właściwości bitowe liczb potęg dwójki.
- Potęgi dwójki mają w reprezentacji binarnej jeden bit ustawiony na 1 i resztę na 0.

---

## Zadanie 9 - Zmiana wielkości liter za pomocą operatorów bitowych

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz napis składający się z liter alfabetu łacińskiego.

**a)** Zamień wszystkie wielkie litery na małe.

**b)** Zamień wszystkie małe litery na wielkie.

**c)** Zamień wielkość wszystkich liter na przeciwną (małe na wielkie, wielkie na małe).

### Dane wejściowe

- Jeden napis.

### Dane wyjściowe

- Jeden napis — wynik po odpowiedniej konwersji liter.

### Przykład

**Podpunkt a):**

- **Dane wejściowe**:
  ```
  Test
  ```
- **Oczekiwane wyjście**:
  ```
  test
  ```

**Podpunkt b):**

- **Dane wejściowe**:
  ```
  Test
  ```
- **Oczekiwane wyjście**:
  ```
  TEST
  ```

**Podpunkt c):**

- **Dane wejściowe**:
  ```
  Test
  ```
- **Oczekiwane wyjście**:
  ```
  tEST
  ```

### Wskazówki

- Litery w kodowaniu ASCII mają określone wartości bitowe.
- Możesz użyć operacji bitowych, takich jak OR, AND, XOR, aby manipulować konkretnymi bitami odpowiedzialnymi za wielkość liter.

---

## Zadanie 10 - Zamień A na B

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz dwie liczby naturalne \( A \) i \( B \). Oblicz, ile bitów należy zmienić (odwrócić) w liczbie \( A \), aby otrzymać liczbę \( B \).

### Dane wejściowe

- Dwie liczby naturalne \( A \) i \( B \), każda w osobnej linii.

### Dane wyjściowe

- Jedna liczba naturalna — liczba bitów, które należy odwrócić.

### Przykład

- **Dane wejściowe**:
  ```
  34
  73
  ```
- **Oczekiwane wyjście**:
  ```
  5
  ```

### Wskazówki

- Wykonaj operację XOR na liczbach \( A \) i \( B \), a następnie policz liczbę jedynek w wyniku.
- Każda jedynka w wyniku XOR oznacza różnicę w odpowiednim bicie.

---

## Zadanie 11 - Czy liczba jest palindromem w systemie binarnym?

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz liczbę naturalną w systemie dziesiętnym. Sprawdź, czy jej reprezentacja binarna jest palindromem (czytana od lewej do prawej i od prawej do lewej jest taka sama).

### Dane wejściowe

- Jedna liczba naturalna.

### Dane wyjściowe

- Jeden napis: **"Prawda"**, jeśli reprezentacja binarna liczby jest palindromem, lub **"Fałsz"**, jeśli nie jest.

### Przykład

- **Dane wejściowe**:
  ```
  26
  ```
- **Oczekiwane wyjście**:
  ```
  Prawda
  ```
  *(Reprezentacja binarna liczby 26 to '11010', która jest palindromem po usunięciu wiodących zer.)*

### Wskazówki

- Przekonwertuj liczbę na system binarny.
- Porównaj ciąg binarny z jego odwróconą wersją.

---

## Zadanie 12 - Najdłuższy ciąg zer w liczbie binarnej

**Poziom trudności**: ★★★

### Treść zadania

Otrzymujesz liczbę naturalną w systemie dziesiętnym. Oblicz długość najdłuższego ciągu zer otoczonego jedynkami w jej reprezentacji binarnej.

### Dane wejściowe

- Jedna liczba naturalna.

### Dane wyjściowe

- Jedna liczba naturalna — długość najdłuższego ciągu zer otoczonego jedynkami.

### Przykład

- **Dane wejściowe**:
  ```
  14
  ```
- **Oczekiwane wyjście**:
  ```
  1
  ```
  *(Reprezentacja binarna liczby 14 to '1110', najdłuższy ciąg zer otoczony jedynkami ma długość 1.)*

### Wskazówki

- Przekonwertuj liczbę na system binarny.
- Znajdź wszystkie ciągi zer pomiędzy jedynkami i określ najdłuższy z nich.

---
