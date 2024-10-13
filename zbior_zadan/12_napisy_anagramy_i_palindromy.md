## Zadanie 1 - Sprawdzenie, czy słowo jest palindromem

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz program, który sprawdzi, czy podane słowo jest palindromem. Palindrom to słowo, które brzmi tak samo czytane od lewej do prawej i od prawej do lewej.

### Dane wejściowe

- Jeden napis składający się z liter alfabetu (bez spacji i znaków interpunkcyjnych).

### Dane wyjściowe

- Jeden napis: **"Prawda"**, jeśli słowo jest palindromem, lub **"Fałsz"**, jeśli nie jest.

### Przykład

- **Dane wejściowe**:
  ```
  kajak
  ```
- **Oczekiwane wyjście**:
  ```
  Prawda
  ```

### Wskazówki

- Porównaj napis z jego odwróconą wersją.
- Możesz zignorować wielkość liter, stosując odpowiednie funkcje do zmiany wielkości.

---

## Zadanie 2 - Znalezienie wszystkich permutacji słowa

**Poziom trudności**: ★★☆

### Treść zadania

Napisz program, który dla podanego słowa wygeneruje wszystkie jego permutacje, czyli wszystkie możliwe układy liter tego słowa.

### Dane wejściowe

- Jeden napis składający się z unikalnych liter (bez powtarzających się znaków).

### Dane wyjściowe

- Lista napisów zawierająca wszystkie możliwe permutacje słowa, każda permutacja w osobnej linii.

### Przykład

- **Dane wejściowe**:
  ```
  abc
  ```
- **Oczekiwane wyjście**:
  ```
  abc
  acb
  bac
  bca
  cab
  cba
  ```

### Wskazówki

- Rozważ użycie rekurencji lub algorytmów generujących permutacje.
- Upewnij się, że wszystkie permutacje są unikalne i że żadne nie zostały pominięte.

---

## Zadanie 3 - Sprawdzenie, czy dwa słowa są anagramami

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz program, który sprawdzi, czy podane dwa słowa są anagramami. Dwa słowa są anagramami, jeśli jedno można utworzyć poprzez przestawienie liter drugiego.

### Dane wejściowe

- Dwa napisy składające się z liter alfabetu (bez spacji i znaków interpunkcyjnych), każdy w osobnej linii.

### Dane wyjściowe

- Jeden napis: **"Prawda"**, jeśli słowa są anagramami, lub **"Fałsz"**, jeśli nie są.

### Przykład

- **Dane wejściowe**:
  ```
  ula
  lua
  ```
- **Oczekiwane wyjście**:
  ```
  Prawda
  ```

### Wskazówki

- Porównaj liczby wystąpień poszczególnych liter w obu słowach.
- Możesz użyć sortowania liter w słowach i porównania wyników.

---

## Zadanie 4 - Wyszukanie wszystkich palindromów w zdaniu

**Poziom trudności**: ★★☆

### Treść zadania

Napisz program, który dla podanego zdania znajdzie wszystkie słowa będące palindromami. Wielkość liter nie ma znaczenia (ignoruj różnice między małymi i wielkimi literami).

### Dane wejściowe

- Jeden napis reprezentujący zdanie, który może zawierać litery, cyfry, spacje oraz znaki interpunkcyjne.

### Dane wyjściowe

- Lista słów będących palindromami, każde słowo w osobnej linii, w kolejności ich występowania w zdaniu.

### Przykład

- **Dane wejściowe**:
  ```
  Tata zabrał kajak na wycieczkę i uderzył się w oko
  ```
- **Oczekiwane wyjście**:
  ```
  Tata
  kajak
  i
  w
  oko
  ```

### Wskazówki

- Podziel zdanie na słowa, usuwając znaki interpunkcyjne.
- Dla każdego słowa sprawdź, czy jest palindromem, ignorując wielkość liter.

---

## Zadanie 5 - Znalezienie anagramów słowa w zdaniu

**Poziom trudności**: ★★☆

### Treść zadania

Napisz program, który w podanym zdaniu znajdzie wszystkie słowa będące anagramami podanego słowa. Wielkość liter nie ma znaczenia.

### Dane wejściowe

- Jeden napis reprezentujący zdanie.
- Jeden napis reprezentujący słowo do sprawdzenia, oba napisy w osobnych liniach.

### Dane wyjściowe

- Lista słów z zdania, które są anagramami podanego słowa, każde słowo w osobnej linii.

### Przykład

- **Dane wejściowe**:
  ```
  Sroga kara.
  arak
  ```
- **Oczekiwane wyjście**:
  ```
  kara
  ```

### Wskazówki

- Podziel zdanie na słowa i usuń znaki interpunkcyjne.
- Porównaj uporządkowane litery słowa z literami każdego słowa w zdaniu.

---

## Zadanie 6 - Permutacje słowa, które są palindromami

**Poziom trudności**: ★★☆

### Treść zadania

Napisz program, który znajdzie wszystkie permutacje podanego słowa, które są palindromami.

### Dane wejściowe

- Jeden napis składający się z liter alfabetu.

### Dane wyjściowe

- Lista unikalnych palindromów będących permutacjami podanego słowa, każde w osobnej linii.

### Przykład

- **Dane wejściowe**:
  ```
  aabb
  ```
- **Oczekiwane wyjście**:
  ```
  abba
  baab
  ```

### Wskazówki

- Sprawdź, czy możliwe jest ułożenie palindromu z podanych liter.
- Generuj permutacje i sprawdzaj, czy są palindromami, eliminując duplikaty.

---

## Zadanie 7 - Minimalna liczba usuniętych znaków, aby uzyskać anagramy

**Poziom trudności**: ★★★

### Treść zadania

Napisz program, który dla dwóch podanych słów zwróci minimalną liczbę znaków, które trzeba usunąć z obu słów, aby otrzymać z nich anagramy. Jeśli słowa są różnej długości, zwróć **-1**.

### Dane wejściowe

- Dwa napisy składające się z liter alfabetu, każdy w osobnej linii.

### Dane wyjściowe

- Jedna liczba naturalna — minimalna liczba znaków do usunięcia z obu słów, aby otrzymać anagramy, lub **-1**, jeśli słowa są różnej długości.

### Przykład

- **Dane wejściowe**:
  ```
  grazyna
  razynax
  ```
- **Oczekiwane wyjście**:
  ```
  2
  ```

### Wskazówki

- Porównaj liczby wystąpień każdej litery w obu słowach.
- Suma różnic w liczbie wystąpień poszczególnych liter da minimalną liczbę znaków do usunięcia.

---

## Zadanie 8 - Wyjątkowe palindromy

**Poziom trudności**: ★★★

### Treść zadania

Napisz program, który znajdzie wszystkie unikalne, wyjątkowe palindromy, jakie można utworzyć z podanego słowa, bez zmiany kolejności występowania znaków. Nie uwzględniaj duplikatów w wyniku.

Wyjątkowy palindrom musi spełniać jeden z dwóch warunków:

1. Wszystkie znaki są identyczne, np. "aaa".
2. Wszystkie znaki poza środkowym są identyczne, np. "cbc".

Pojedynczy znak jest również uznawany za wyjątkowy palindrom.

### Dane wejściowe

- Jeden napis składający się z liter alfabetu.

### Dane wyjściowe

- Lista unikalnych palindromów spełniających powyższe warunki, każde w osobnej linii.

### Przykład

- **Dane wejściowe**:
  ```
  xxyxx
  ```
- **Oczekiwane wyjście**:
  ```
  x
  xx
  xxx
  xxyxx
  y
  yxy
  ```

### Wskazówki

- Przejdź przez wszystkie podciągi słowa i sprawdź, czy spełniają warunki wyjątkowego palindromu.
- Upewnij się, że nie uwzględniasz duplikatów w wyniku.

---
