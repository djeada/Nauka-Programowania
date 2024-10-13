## Zadanie 1 - Odwróć napis

**Poziom trudności**: ★☆☆

### Treść zadania

Zmień otrzymany napis tak, aby został zapisany od tyłu.

### Dane wejściowe

- Jeden napis (ciąg znaków), który może zawierać litery, cyfry i inne znaki.

### Dane wyjściowe

- Jeden napis — odwrócony ciąg wejściowy.

### Przykład

- **Dane wejściowe**:
  ```
  barszcz
  ```
- **Oczekiwane wyjście**:
  ```
  zczsrab
  ```

### Wskazówki

- Możesz użyć indeksowania z krokiem ujemnym lub funkcji do odwracania ciągów znaków.

---

## Zadanie 2 - Policz wystąpienia znaku

**Poziom trudności**: ★☆☆

### Treść zadania

Dla podanego napisu oraz znaku, znajdź liczbę wystąpień tego znaku w napisie.

### Dane wejściowe

- Jeden napis (ciąg znaków).
- Jeden znak (pojedynczy znak), którego wystąpienia mają być policzone.

### Dane wyjściowe

- Jedna liczba naturalna — liczba wystąpień podanego znaku w napisie.

### Przykład

- **Dane wejściowe**:
  ```
  klamra
  a
  ```
- **Oczekiwane wyjście**:
  ```
  2
  ```

### Wskazówki

- Użyj metody `count()` dostępnej dla ciągów znaków.

---

## Zadanie 3 - Z ilu słów składa się zdanie?

**Poziom trudności**: ★☆☆

### Treść zadania

Zlicz, ile słów składa się na podane zdanie. Znaki interpunkcyjne nie są traktowane jako słowa.

### Dane wejściowe

- Jeden napis reprezentujący zdanie, może zawierać litery, cyfry, spacje oraz znaki interpunkcyjne.

### Dane wyjściowe

- Jedna liczba naturalna — liczba słów w zdaniu.

### Przykład

- **Dane wejściowe**:
  ```
  gram na pianinie.
  ```
- **Oczekiwane wyjście**:
  ```
  3
  ```

### Wskazówki

- Użyj metody `split()`, aby podzielić zdanie na słowa.
- Możesz potrzebować usunąć znaki interpunkcyjne z końców słów.

---

## Zadanie 4 - Zamień wszystkie małe litery na duże

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymasz napis. Zamień wszystkie małe litery w tym napisie na duże.

### Dane wejściowe

- Jeden napis (ciąg znaków), zawierający małe i duże litery.

### Dane wyjściowe

- Jeden napis — oryginalny napis z zamienionymi małymi literami na duże.

### Przykład

- **Dane wejściowe**:
  ```
  Rumcajs
  ```
- **Oczekiwane wyjście**:
  ```
  RUMCAJS
  ```

### Wskazówki

- Skorzystaj z metody `upper()` dostępnej dla ciągów znaków.

---

## Zadanie 5 - Wypisz co k-ty znak napisu poziomo i pionowo

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymasz napis oraz liczbę \( k \).

- **a)** Wypisz co \( k \)-ty znak napisu poziomo, oddzielając znaki spacjami.
- **b)** Wypisz co \( k \)-ty znak napisu pionowo, wypisując każdy znak w osobnej linii.

### Dane wejściowe

- Jeden napis (ciąg znaków).
- Jedna liczba naturalna \( k \) (\( k \geq 1 \)).

### Dane wyjściowe

- **a)** Jeden napis — co \( k \)-ty znak napisu, oddzielony spacjami.
- **b)** Kilka linii — każdy \( k \)-ty znak napisu w osobnej linii.

### Przykład

- **Dane wejściowe**:
  ```
  Grzechotnik
  3
  ```
- **Oczekiwane wyjście**:

  **a)**

  ```
  z h n
  ```

  **b)**

  ```
  z
  h
  n
  ```

### Wskazówki

- Użyj indeksowania z odpowiednim krokiem (slicing) dla wybrania co \( k \)-tego znaku.

---

## Zadanie 6 - Zamień litery "a" na znaki zapytania

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymasz napis. Zamień w nim wszystkie litery "a" na znaki zapytania `?`.

### Dane wejściowe

- Jeden napis (ciąg znaków).

### Dane wyjściowe

- Jeden napis — oryginalny napis z zamienionymi literami "a" na `?`.

### Przykład

- **Dane wejściowe**:
  ```
  Latarnik
  ```
- **Oczekiwane wyjście**:
  ```
  L?t?rnik
  ```

### Wskazówki

- Użyj metody `replace('a', '?')`.

---

## Zadanie 7 - Zamień znaki na kody ASCII

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymasz napis. Zamień wszystkie znaki w tym napisie na odpowiadające im kody ASCII. Zastąp oryginalny napis ciągiem tych kodów, oddzielonych przecinkami i spacjami.

### Dane wejściowe

- Jeden napis (ciąg znaków).

### Dane wyjściowe

- Jeden napis — ciąg kodów ASCII znaków z oryginalnego napisu, oddzielonych przecinkami i spacjami.

### Przykład

- **Dane wejściowe**:
  ```
  Robot
  ```
- **Oczekiwane wyjście**:
  ```
  82, 111, 98, 111, 116
  ```

### Wskazówki

- Iteruj przez znaki w napisie i użyj funkcji `ord()` dla każdego z nich.

---

## Zadanie 8 - Wypisz pionowo słowa, z których składa się zdanie

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymasz napis reprezentujący zdanie. Podziel zdanie na słowa i wypisz każde słowo w osobnej linii. Znaki interpunkcyjne nie są uwzględniane jako słowa.

### Dane wejściowe

- Jeden napis (ciąg znaków).

### Dane wyjściowe

- Kilka linii — każde słowo zdania w osobnej linii.

### Przykład

- **Dane wejściowe**:
  ```
  Ala ma kota
  ```
- **Oczekiwane wyjście**:
  ```
  Ala
  ma
  kota
  ```

### Wskazówki

- Użyj metody `split()` do podziału zdania na słowa.

---

## Zadanie 9 - Wczytaj i rozdziel informacje o pracowniku

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymasz napis zawierający informacje o pracowniku, oddzielone średnikami:

- Imię
- Nazwisko
- Miejsce urodzenia
- Stanowisko
- Zarobki

Zapisz te informacje w osobnych zmiennych i wypisz je z odpowiednimi komunikatami.

### Dane wejściowe

- Jeden napis — informacje o pracowniku, dane oddzielone średnikami `;`.

### Dane wyjściowe

- Kilka linii — każda zawierająca jeden element informacji z odpowiednim opisem.

### Przykład

- **Dane wejściowe**:
  ```
  Jan; Kowalski; Warszawa; Programista; 1000;
  ```
- **Oczekiwane wyjście**:
  ```
  Imię: Jan
  Nazwisko: Kowalski
  Miejsce urodzenia: Warszawa
  Zawód: Programista
  Zarobki: 1000
  ```

### Wskazówki

- Użyj metody `split(';')` do podziału napisu na części.

---

## Zadanie 10 - Znajdź najdłuższe/najkrótsze słowo w zdaniu

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymasz zdanie. Znajdź:

- **a)** Najdłuższe słowo w zdaniu.
- **b)** Najkrótsze słowo w zdaniu.

Jeśli jest kilka słów o takiej samej długości, wybierz to, które występuje jako pierwsze.

### Dane wejściowe

- Jeden napis reprezentujący zdanie.

### Dane wyjściowe

- **a)** Jeden napis — najdłuższe słowo.
- **b)** Jeden napis — najkrótsze słowo.

### Przykład

- **Dane wejściowe**:
  ```
  Kaczka lubi wiosnę.
  ```
- **Oczekiwane wyjście**:

  **a)**

  ```
  Kaczka
  ```

  **b)**

  ```
  lubi
  ```

### Wskazówki

- Użyj metody `split()` i funkcji `len()`.

---

## Zadanie 11 - Średnia długość słów w zdaniu

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymasz zdanie. Oblicz średnią długość słów w tym zdaniu. Wynik powinien być liczbą całkowitą.

### Dane wejściowe

- Jeden napis reprezentujący zdanie.

### Dane wyjściowe

- Jedna liczba naturalna — średnia długość słów.

### Przykład

- **Dane wejściowe**:
  ```
  Zepsuty rower.
  ```
- **Oczekiwane wyjście**:
  ```
  6
  ```

### Wskazówki

- Oblicz sumę długości słów i podziel przez ich liczbę.

---

## Zadanie 12 - Usuń spacje ze zdania

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymasz zdanie. Usuń z niego wszystkie spacje.

### Dane wejściowe

- Jeden napis reprezentujący zdanie.

### Dane wyjściowe

- Jeden napis — zdanie bez spacji.

### Przykład

- **Dane wejściowe**:
  ```
  Ala ma kota
  ```
- **Oczekiwane wyjście**:
  ```
  Alamakota
  ```

### Wskazówki

- Użyj metody `replace(' ', '')`.

---

## Zadanie 13 - Znaki znajdujące się na pozycjach będących liczbami pierwszymi

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymasz napis. Znajdź znaki na pozycjach będących liczbami pierwszymi.

### Dane wejściowe

- Jeden napis (ciąg znaków).

### Dane wyjściowe

- Lista znaków — znaki z pozycji o indeksach będących liczbami pierwszymi.

### Przykład

- **Dane wejściowe**:
  ```
  Słoń
  ```
- **Oczekiwane wyjście**:
  ```
  ['o', 'ń']
  ```

### Wskazówki

- Indeksy w Pythonie zaczynają się od 0.
- Liczby pierwsze w zakresie indeksów to 2, 3, 5, 7, itd.

---

## Zadanie 14 - Napis składający się z liczb od 1 do n

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymasz liczbę naturalną \( n \). Zwróć napis składający się z kolejnych liczb od 1 do \( n \), bez separatorów.

### Dane wejściowe

- Jedna liczba naturalna \( n \) (\( n \geq 1 \)).

### Dane wyjściowe

- Jeden napis — ciąg liczb od 1 do \( n \).

### Przykład

- **Dane wejściowe**:
  ```
  3
  ```
- **Oczekiwane wyjście**:
  ```
  123
  ```

### Wskazówki

- Użyj pętli i konkatenacji napisów.

---

## Zadanie 15 - Słowa ze zdania jako osobne elementy listy

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymasz zdanie. Zwróć listę słów w nim zawartych.

### Dane wejściowe

- Jeden napis reprezentujący zdanie.

### Dane wyjściowe

- Lista napisów — słów ze zdania.

### Przykład

- **Dane wejściowe**:
  ```
  Ala ma kota
  ```
- **Oczekiwane wyjście**:
  ```
  ["Ala", "ma", "kota"]
  ```

### Wskazówki

- Użyj metody `split()`.

---

## Zadanie 16 - Odległość Hamminga

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymasz dwa napisy o tej samej długości. Oblicz odległość Hamminga między nimi.

### Dane wejściowe

- Dwa napisy o równej długości.

### Dane wyjściowe

- Jedna liczba naturalna — liczba pozycji, na których znaki w napisach są różne.

### Przykład

- **Dane wejściowe**:
  ```
  adam
  axam
  ```
- **Oczekiwane wyjście**:
  ```
  1
  ```

### Wskazówki

- Iteruj przez indeksy napisów i porównuj znaki.

---

## Zadanie 17 - Konwersja listy na napis

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymasz listę liczb naturalnych. Zamień ją na napis, łącząc liczby bez separatorów.

### Dane wejściowe

- Lista liczb naturalnych.

### Dane wyjściowe

- Jeden napis — liczby z listy połączone w ciąg znaków.

### Przykład

- **Dane wejściowe**:
  ```
  [2, 4, 7]
  ```
- **Oczekiwane wyjście**:
  ```
  247
  ```

### Wskazówki

- Użyj funkcji `str()` dla każdego elementu i połącz je.

---

## Zadanie 18 - Odwróć słowa w zdaniu

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymasz zdanie. Zamień każde słowo na jego lustrzane odbicie (odwróć litery w słowie).

### Dane wejściowe

- Jeden napis reprezentujący zdanie.

### Dane wyjściowe

- Jeden napis — zdanie z odwróconymi słowami.

### Przykład

- **Dane wejściowe**:
  ```
  Ala ma kota
  ```
- **Oczekiwane wyjście**:
  ```
  alA am atok
  ```

### Wskazówki

- Użyj metody `split()` i odwróć każde słowo osobno.

---
