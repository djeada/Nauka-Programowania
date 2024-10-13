## Zadanie 1 - Sprawdzenie liczby większej od 5

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz program, który pobiera od użytkownika jedną liczbę naturalną (całkowitą nieujemną). Jeżeli podana liczba jest **większa niż 5**, program powinien ją wypisać na standardowe wyjście. W przeciwnym razie program nie powinien wypisywać nic.

### Dane wejściowe

- Jedna liczba naturalna \( n \) (całkowita nieujemna), wprowadzona przez użytkownika.

### Dane wyjściowe

- Jeśli \( n > 5 \), wypisz liczbę \( n \).
- Jeśli \( n \leq 5 \), nie wypisuj nic.

### Przykład

**Przykład 1:**

- **Dane wejściowe**:
  ```
  10
  ```
- **Oczekiwane wyjście**:
  ```
  10
  ```

**Przykład 2:**

- **Dane wejściowe**:
  ```
  3
  ```
- **Oczekiwane wyjście**:
  ```
  ```
  *(brak danych wyjściowych)*

### Wskazówki

- Pamiętaj, że liczba naturalna to liczba całkowita nieujemna (0, 1, 2, ...).
- Użyj instrukcji warunkowej, aby sprawdzić, czy liczba jest większa niż 5.

---

## Zadanie 2 - Porównanie dwóch liczb

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz program, który pobiera od użytkownika dwie liczby naturalne (całkowite nieujemne) i sprawdza, czy są one identyczne. Program powinien wypisać odpowiedni komunikat:

- Jeśli liczby są identyczne, wypisz: **"Liczby są identyczne."**
- Jeśli liczby są różne, wypisz: **"Liczby są różne."**

### Dane wejściowe

- Dwie liczby naturalne, każda w oddzielnej linii.

### Dane wyjściowe

- Jeden komunikat tekstowy, zgodnie z powyższym opisem.

### Przykład

**Przykład 1:**

- **Dane wejściowe**:
  ```
  7
  4
  ```
- **Oczekiwane wyjście**:
  ```
  Liczby są różne.
  ```

**Przykład 2:**

- **Dane wejściowe**:
  ```
  5
  5
  ```
- **Oczekiwane wyjście**:
  ```
  Liczby są identyczne.
  ```

### Wskazówki

- Upewnij się, że komunikat jest wypisany dokładnie tak, jak podano.
- Do porównania liczb użyj operatora porównania.

---

## Zadanie 3 - Określanie znaku liczby

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz program, który pobiera od użytkownika jedną liczbę całkowitą (może być ujemna, dodatnia lub zero) i określa jej znak. Program powinien wypisać odpowiedni komunikat:

- Jeśli liczba jest ujemna, wypisz: **"Liczba jest ujemna."**
- Jeśli liczba jest dodatnia, wypisz: **"Liczba jest dodatnia."**
- Jeśli liczba jest zerem, wypisz: **"Liczba jest zerem."**

### Dane wejściowe

- Jedna liczba całkowita (ujemna, dodatnia lub zero).

### Dane wyjściowe

- Jeden komunikat tekstowy, zgodnie z powyższym opisem.

### Przykład

**Przykład 1:**

- **Dane wejściowe**:
  ```
  -5
  ```
- **Oczekiwane wyjście**:
  ```
  Liczba jest ujemna.
  ```

**Przykład 2:**

- **Dane wejściowe**:
  ```
  0
  ```
- **Oczekiwane wyjście**:
  ```
  Liczba jest zerem.
  ```

**Przykład 3:**

- **Dane wejściowe**:
  ```
  2
  ```
- **Oczekiwane wyjście**:
  ```
  Liczba jest dodatnia.
  ```

### Wskazówki

- Zero nie jest ani dodatnie, ani ujemne.
- Użyj instrukcji warunkowych, aby sprawdzić warunki.

---

## Zadanie 4 - Maksimum i minimum z dwóch liczb

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz program, który pobiera od użytkownika dwie liczby naturalne (całkowite nieujemne) i wypisuje je w taki sposób, że najpierw wypisana zostanie liczba większa (maksimum), a następnie mniejsza (minimum).

Jeśli liczby są identyczne, wypisz je w tej samej kolejności.

### Dane wejściowe

- Dwie liczby naturalne, każda w oddzielnej linii.

### Dane wyjściowe

- Dwie liczby naturalne wypisane w jednej linii, oddzielone spacją:
  - Najpierw liczba większa (lub dowolna, jeśli są równe),
  - Następnie liczba mniejsza (lub druga taka sama).

### Przykład

**Przykład 1:**

- **Dane wejściowe**:
  ```
  1
  4
  ```
- **Oczekiwane wyjście**:
  ```
  4 1
  ```

**Przykład 2:**

- **Dane wejściowe**:
  ```
  7
  3
  ```
- **Oczekiwane wyjście**:
  ```
  7 3
  ```

**Przykład 3:**

- **Dane wejściowe**:
  ```
  5
  5
  ```
- **Oczekiwane wyjście**:
  ```
  5 5
  ```

### Wskazówki

- Możesz użyć funkcji maksymalnej i minimalnej lub instrukcji warunkowych.
- Upewnij się, że liczby są wypisane w jednej linii, oddzielone spacją.

---

## Zadanie 5 - Sortowanie trzech liczb

**Poziom trudności**: ★★☆

### Treść zadania

Napisz program, który pobiera od użytkownika trzy liczby naturalne (całkowite nieujemne) i wypisuje je w kolejności rosnącej, od najmniejszej do największej.

### Dane wejściowe

- Trzy liczby naturalne, każda w oddzielnej linii.

### Dane wyjściowe

- Trzy liczby naturalne wypisane w jednej linii, oddzielone spacjami, w kolejności rosnącej.

### Przykład

**Przykład 1:**

- **Dane wejściowe**:
  ```
  2
  1
  4
  ```
- **Oczekiwane wyjście**:
  ```
  1 2 4
  ```

**Przykład 2:**

- **Dane wejściowe**:
  ```
  5
  3
  5
  ```
- **Oczekiwane wyjście**:
  ```
  3 5 5
  ```

**Przykład 3:**

- **Dane wejściowe**:
  ```
  7
  7
  7
  ```
- **Oczekiwane wyjście**:
  ```
  7 7 7
  ```

### Wskazówki

- Możesz użyć wbudowanych funkcji sortujących, jeśli są dostępne.
- Upewnij się, że liczby są wypisane w jednej linii, oddzielone spacjami.

---

## Zadanie 6 - Maksimum z czterech liczb

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz program, który pobiera od użytkownika cztery liczby naturalne (całkowite nieujemne) i wypisuje największą z nich.

### Dane wejściowe

- Cztery liczby naturalne, każda w oddzielnej linii.

### Dane wyjściowe

- Jedna liczba naturalna – największa spośród podanych.

### Przykład

**Przykład 1:**

- **Dane wejściowe**:
  ```
  2
  5
  1
  4
  ```
- **Oczekiwane wyjście**:
  ```
  5
  ```

**Przykład 2:**

- **Dane wejściowe**:
  ```
  7
  7
  3
  7
  ```
- **Oczekiwane wyjście**:
  ```
  7
  ```

### Wskazówki

- Możesz użyć funkcji maksymalnej dla listy liczb.
- Upewnij się, że program działa poprawnie, nawet gdy największa liczba występuje kilka razy.

---

## Zadanie 7 - Weryfikacja praw logiki

**Poziom trudności**: ★★☆

### Treść zadania

Napisz program, który dla wszystkich możliwych kombinacji wartości logicznych zmiennych \( p \) i \( q \) (True i False) sprawdza poprawność następujących praw logiki:

a) **Prawo wyłączonego środka**:
   \[ p \lor \lnot p = \text{True} \]

b) **Prawo niesprzeczności**:
   \[ \lnot (p \land \lnot p) = \text{True} \]

c) **Przemienność koniunkcji**:
   \[ p \land q = q \land p \]

d) **Przemienność alternatywy**:
   \[ p \lor q = q \lor p \]

e) **Pierwsze prawo de Morgana**:
   \[ \lnot (p \land q) = \lnot p \lor \lnot q \]

f) **Drugie prawo de Morgana**:
   \[ \lnot (p \lor q) = \lnot p \land \lnot q \]

### Dane wejściowe

- Brak. Program powinien automatycznie przetestować wszystkie możliwe kombinacje wartości \( p \) i \( q \).

### Dane wyjściowe

Dla każdego prawa wypisz:

- Kombinację wartości \( p \) i \( q \).
- Wartości wyrażenia po lewej i prawej stronie.
- Informację, czy wartości są równe.

### Przykład

**Prawo niesprzeczności:**

- **Wynik programu**:
  ```
  Prawo niesprzeczności:
  p = True
  Left side: True
  Right side: True
  Equal: True

  p = False
  Left side: True
  Right side: True
  Equal: True
  ```

**Pierwsze prawo de Morgana:**

- **Wynik programu**:
  ```
  Pierwsze prawo de Morgana:
  p = True, q = True
  Left side: False
  Right side: False
  Equal: True

  p = True, q = False
  Left side: True
  Right side: True
  Equal: True

  p = False, q = True
  Left side: True
  Right side: True
  Equal: True

  p = False, q = False
  Left side: True
  Right side: True
  Equal: True
  ```

### Wskazówki

- Użyj operatorów logicznych dostępnych w języku programowania.
- Upewnij się, że dla każdej kombinacji wartości \( p \) i \( q \) wyniki po obu stronach są porównywane.

---

## Zadanie 8 - Sprawdzanie możliwości zbudowania trójkąta

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz program, który pobiera od użytkownika trzy liczby naturalne (większe od zera) reprezentujące długości boków i sprawdza, czy z odcinków o takich długościach można zbudować trójkąt.

Program powinien wypisać odpowiedni komunikat:

- Jeśli można zbudować trójkąt, wypisz: **"Trójkąt można zbudować z podanych boków."**
- Jeśli nie można zbudować trójkąta, wypisz: **"Trójkąta nie można zbudować z podanych boków."**

### Dane wejściowe

- Trzy liczby naturalne (większe od zera), każda w oddzielnej linii.

### Dane wyjściowe

- Jeden komunikat tekstowy, zgodnie z powyższym opisem.

### Przykład

**Przykład 1:**

- **Dane wejściowe**:
  ```
  3
  4
  5
  ```
- **Oczekiwane wyjście**:
  ```
  Trójkąt można zbudować z podanych boków.
  ```

**Przykład 2:**

- **Dane wejściowe**:
  ```
  1
  2
  3
  ```
- **Oczekiwane wyjście**:
  ```
  Trójkąta nie można zbudować z podanych boków.
  ```

### Wskazówki

- Warunek istnienia trójkąta: suma długości dowolnych dwóch boków musi być większa od długości trzeciego boku.
- Sprawdź wszystkie trzy kombinacje.
