# Słowniki

## Zadanie 1 - Słownik z kluczami będącymi liczbami naturalnymi i wartościami ich kwadratów

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz liczbę naturalną. Stwórz słownik, w którym kluczami będą kolejne liczby naturalne mniejsze od otrzymanej liczby, a wartościami będą ich kwadraty.

### Dane wejściowe

- Jedna liczba naturalna \( n \geq 1 \).

### Dane wyjściowe

- Słownik, gdzie kluczami są liczby od 1 do \( n-1 \), a wartościami są kwadraty tych liczb.

### Przykład

- **Dane wejściowe**:
  ```
  5
  ```
- **Oczekiwane wyjście**:
  ```
  {1: 1, 2: 4, 3: 9, 4: 16}
  ```

### Wskazówki

- Użyj pętli, aby iterować przez liczby od 1 do \( n-1 \).
- Oblicz kwadrat każdej liczby i dodaj parę klucz-wartość do słownika.

---

## Zadanie 2 - Słownik z kluczami z jednej listy i wartościami z drugiej listy

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz dwie listy liczb całkowitych. Utwórz słownik, w którym kluczami są elementy pierwszej listy, a wartościami są odpowiadające im elementy drugiej listy. Jeśli listy są różnej długości, zwróć pusty słownik.

### Dane wejściowe

- Dwie liczby naturalne \( n \) i \( m \) — długości list, każda w osobnej linii.
- Następnie \( n \) liczb całkowitych — elementy pierwszej listy.
- Następnie \( m \) liczb całkowitych — elementy drugiej listy.

### Dane wyjściowe

- Słownik z kluczami z pierwszej listy i wartościami z drugiej listy.
- Jeśli \( n \ne m \), wypisz pusty słownik `{}`.

### Przykład

- **Dane wejściowe**:
  ```
  3
  3
  3 5 8
  1 2 -1
  ```
- **Oczekiwane wyjście**:
  ```
  {3: 1, 5: 2, 8: -1}
  ```

### Wskazówki

- Sprawdź, czy długości obu list są takie same.
- Jeśli tak, iteruj równocześnie przez obie listy, tworząc pary klucz-wartość.

---

## Zadanie 3 - Biblioteka: baza danych wypożyczonych książek

**Poziom trudności**: ★☆☆

### Treść zadania

Stwórz prostą bazę danych dla biblioteki, używając słownika, w którym kluczami są imiona czytelników, a wartościami są listy wypożyczonych przez nich książek. Program powinien umożliwiać:

1. Dodanie wypożyczonej książki do listy danego czytelnika.
2. Usunięcie książki z listy czytelnika (zwrot książki).
3. Wyświetlenie aktualnej listy wypożyczonych książek dla danego czytelnika.

### Dane wejściowe

- Operacje wykonywane przez użytkownika, każda w osobnej linii:
  - **Dodanie książki**: `dodaj [imię] [tytuł_książki]`
  - **Zwrot książki**: `zwróć [imię] [tytuł_książki]`
  - **Wyświetlenie listy**: `lista [imię]`
- Program kończy działanie po wpisaniu słowa `koniec`.

### Dane wyjściowe

- Po operacji `lista [imię]` wypisz: `Książki wypożyczone przez [imię]: [lista książek]`
- Jeśli czytelnik nie ma wypożyczonych książek, wypisz odpowiedni komunikat.

### Przykład

- **Dane wejściowe**:
  ```
  dodaj Jan Hobbit
  dodaj Anna "Duma i uprzedzenie"
  dodaj Jan "Władca Pierścieni"
  lista Jan
  zwróć Jan Hobbit
  lista Jan
  lista Anna
  koniec
  ```
- **Oczekiwane wyjście**:
  ```
  Książki wypożyczone przez Jan: Hobbit, Władca Pierścieni
  Książki wypożyczone przez Jan: Władca Pierścieni
  Książki wypożyczone przez Anna: Duma i uprzedzenie
  ```

### Wskazówki

- Użyj słownika z imionami jako kluczami i listami książek jako wartościami.
- Pamiętaj o obsłudze sytuacji, gdy czytelnik lub książka nie istnieje.

---

## Zadanie 4 - Usuwanie par z słownika na podstawie wartości

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz słownik zawierający pary klucz-wartość, gdzie kluczami są napisy, a wartościami liczby całkowite. Otrzymujesz również liczbę całkowitą. Usuń z słownika wszystkie pary, dla których wartość jest równa podanej liczbie.

### Dane wejściowe

- Liczba naturalna \( n \) — liczba par w słowniku.
- Następnie \( n \) linii z parą: `[klucz] [wartość]`.
- Jedna liczba całkowita \( k \) — wartość do usunięcia.

### Dane wyjściowe

- Słownik po usunięciu odpowiednich par.

### Przykład

- **Dane wejściowe**:
  ```
  4
  aaa 5
  abc 1
  xxx 5
  cba 3
  5
  ```
- **Oczekiwane wyjście**:
  ```
  {'abc': 1, 'cba': 3}
  ```

### Wskazówki

- Możesz użyć kopii słownika lub zbudować nowy słownik z filtrowanymi elementami.

---

## Zadanie 5 - Pracownik z największym sumarycznym zyskiem

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz listę par, gdzie każda para zawiera imię i nazwisko pracownika oraz liczbę naturalną reprezentującą zysk z transakcji przeprowadzonej przez tego pracownika. Znajdź pracownika, który łącznie przyniósł firmie największy zysk.

### Dane wejściowe

- Liczba naturalna \( n \) — liczba wpisów.
- Następnie \( n \) linii z parą: `[imię_i_nazwisko] [zysk]`.

### Dane wyjściowe

- Imię i nazwisko pracownika z największym sumarycznym zyskiem.

### Przykład

- **Dane wejściowe**:
  ```
  5
  Barnaba_Barabash 120
  Jon_Snow 100
  Kira_Summer 300
  Barnaba_Barabash 200
  Bob_Marley 110
  ```
- **Oczekiwane wyjście**:
  ```
  Barnaba_Barabash
  ```

### Wskazówki

- Sumuj zyski dla każdego pracownika w słowniku.
- Znajdź klucz z największą sumaryczną wartością.

---

## Zadanie 6 - Histogram wystąpień znaków w słowie

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz napis. Znajdź częstość występowania każdego znaku w tym napisie.

### Dane wejściowe

- Jeden napis.

### Dane wyjściowe

- Słownik z kluczami będącymi znakami i wartościami będącymi liczbą ich wystąpień.

### Przykład

- **Dane wejściowe**:
  ```
  klasa
  ```
- **Oczekiwane wyjście**:
  ```
  {'k': 1, 'l': 1, 'a': 2, 's': 1}
  ```

### Wskazówki

- Iteruj przez znaki w napisie i zliczaj ich wystąpienia.

---

## Zadanie 7 - Histogram słów w tekście

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz tekst w postaci napisu. Znajdź częstość występowania każdego słowa w tym tekście, ignorując wielkość liter. Słowa składają się wyłącznie z liter.

### Dane wejściowe

- Jeden napis reprezentujący tekst.

### Dane wyjściowe

- Słownik z kluczami będącymi słowami (małymi literami) i wartościami będącymi liczbą ich wystąpień.

### Przykład

- **Dane wejściowe**:
  ```
  Ala ma kota. Ala lubi koty.
  ```
- **Oczekiwane wyjście**:
  ```
  {'ala': 2, 'ma': 1, 'kota': 1, 'lubi': 1, 'koty': 1}
  ```

### Wskazówki

- Usuń znaki interpunkcyjne i zamień tekst na małe litery.
- Podziel tekst na słowa i zliczaj ich wystąpienia.

---

## Zadanie 8 - Najczęściej występująca litera w zdaniu

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz zdanie. Znajdź literę, która występuje w nim najczęściej. Jeśli jest kilka takich liter, wybierz tę, która pojawia się jako pierwsza.

### Dane wejściowe

- Jeden napis reprezentujący zdanie.

### Dane wyjściowe

- Jeden znak — najczęściej występująca litera.

### Przykład

- **Dane wejściowe**:
  ```
  lezy jerzy na wiezy
  ```
- **Oczekiwane wyjście**:
  ```
  e
  ```

### Wskazówki

- Zignoruj spacje i znaki interpunkcyjne.
- Użyj słownika do zliczenia wystąpień liter.

---

## Zadanie 9 - Znaki występujące co najmniej dwa razy

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz napis. Znajdź wszystkie znaki, które występują w nim co najmniej dwa razy, i wypisz je bez powtórzeń.

### Dane wejściowe

- Jeden napis.

### Dane wyjściowe

- Napis składający się z unikalnych znaków występujących co najmniej dwa razy.

### Przykład

- **Dane wejściowe**:
  ```
  aaabbbccc
  ```
- **Oczekiwane wyjście**:
  ```
  abc
  ```

### Wskazówki

- Zlicz wystąpienia znaków i wybierz te z liczbą większą lub równą 2.

---

## Zadanie 10 - Znalezienie anagramów w tekście

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz tekst. Znajdź wszystkie grupy słów będących anagramami (słowa zawierające te same litery w tej samej liczbie). Ignoruj wielkość liter. Słowa składają się wyłącznie z liter.

### Dane wejściowe

- Jeden napis.

### Dane wyjściowe

- Lista list słów będących anagramami.

### Przykład

- **Dane wejściowe**:
  ```
  To absurd, że tyran Brudas, ten straszliwy bandzior sprawuje rządy w tym kraju. Burza nad galerią i alergia na narty to żadna zbrodnia jak bandzior i jego arbuz.
  ```
- **Oczekiwane wyjście**:
  ```
  [["absurd", "brudas"], ["tyran", "narty"], ["bandzior", "zbrodnia"], ["burza", "arbuz"], ["galeria", "alergia"]]
  ```

### Wskazówki

- Posortuj litery w każdym słowie i użyj ich jako klucza do grupowania.

---

## Zadanie 11 - Sortowanie słownika według kluczy i wartości

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz słownik z parami napisów i liczb całkowitych. Wypisz listę par:

**a)** Posortowaną według kluczy (napisów) w porządku alfabetycznym.

**b)** Posortowaną według wartości (liczb) w porządku rosnącym.

### Dane wejściowe

- Liczba naturalna \( n \) — liczba par w słowniku.
- Następnie \( n \) linii z parą: `[klucz] [wartość]`.

### Dane wyjściowe

- **Podpunkt a):** Lista par posortowanych według kluczy.
- **Podpunkt b):** Lista par posortowanych według wartości.

### Przykład

- **Dane wejściowe**:
  ```
  4
  c 3
  x 5
  a -2
  b 4
  ```
- **Oczekiwane wyjście**:

  **a)**
  ```
  [('a', -2), ('b', 4), ('c', 3), ('x', 5)]
  ```

  **b)**
  ```
  [('a', -2), ('c', 3), ('b', 4), ('x', 5)]
  ```

### Wskazówki

- Użyj odpowiednich funkcji sortowania z kluczem.

---

## Zadanie 12 - Porównanie dwóch słowników

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz dwa słowniki, gdzie kluczami są napisy, a wartościami listy liczb całkowitych. Listy mogą być w różnej kolejności. Sprawdź, czy słowniki zawierają te same pary klucz-wartość, przy czym kolejność elementów w listach nie ma znaczenia.

### Dane wejściowe

- Dwa słowniki:
  - Liczba naturalna \( n \), a następnie \( n \) par `[klucz] [lista_wartości]`.
  - Liczba naturalna \( m \), a następnie \( m \) par `[klucz] [lista_wartości]`.

### Dane wyjściowe

- Wartość logiczna: **"Prawda"**, jeśli słowniki są identyczne, lub **"Fałsz"**, jeśli nie są.

### Przykład

- **Dane wejściowe**:
  ```
  2
  a 1 2 3
  b 4 5
  2
  a 3 2 1
  b 5 4
  ```
- **Oczekiwane wyjście**:
  ```
  Prawda
  ```

- **Dane wejściowe**:
  ```
  2
  a 1 2 3
  b 4 5
  3
  a 3 2 1
  b 5 4
  c 6 7
  ```
- **Oczekiwane wyjście**:
  ```
  Fałsz
  ```

### Wskazówki

- Porównaj klucze obu słowników.
- Dla każdego klucza porównaj zestawy wartości (nie kolejność).

---
