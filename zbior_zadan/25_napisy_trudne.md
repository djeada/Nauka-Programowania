# Napisy — trudne

## Zadanie 1 - Podmiana słowa w zdaniu

**Poziom trudności**: ★★☆

### Treść zadania

Masz trzy napisy:

1. **Zdanie** — tekst, w którym dokonasz zamiany.
2. **Słowo A** — słowo do znalezienia w zdaniu.
3. **Słowo B** — słowo, na które zamienisz każde wystąpienie słowa A.

Twoim zadaniem jest zamienić wszystkie wystąpienia słowa **A** na słowo **B** w podanym zdaniu.

### Dane wejściowe

- Trzy napisy:
  1. Zdanie.
  2. Słowo A.
  3. Słowo B.

### Dane wyjściowe

- Jeden napis — zdanie po dokonaniu zamian.

### Przykład

- **Dane wejściowe**:
  ```
  Lezy jezy na wiezy
  zy
  rzy
  ```
- **Oczekiwane wyjście**:
  ```
  Lerzy jerzy na wierzy
  ```

### Wskazówki

- Upewnij się, że zamieniasz wszystkie wystąpienia słowa **A** w zdaniu.
- Możesz wykorzystać funkcje do zastępowania tekstu w napisie.
- Pamiętaj, że słowo może być częścią innego słowa.

---

## Zadanie 2 - Usuń podnapis

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz dwa napisy:

1. **Napis główny** — tekst, z którego usuniesz podnapis.
2. **Podnapis do usunięcia** — ciąg znaków, który należy usunąć z napisu głównego.

Twoim zadaniem jest znaleźć i usunąć wszystkie wystąpienia podanego podnapisu w napisie głównym.

### Dane wejściowe

- Dwa napisy:
  1. Napis główny.
  2. Podnapis do usunięcia.

### Dane wyjściowe

- Jeden napis — wynik po usunięciu wszystkich wystąpień podnapisu.

### Przykład

- **Dane wejściowe**:
  ```
  Lezy jezy na wiezy
  zy
  ```
- **Oczekiwane wyjście**:
  ```
  Le je na wie
  ```

### Wskazówki

- Upewnij się, że usuwasz wszystkie wystąpienia podnapisu, niezależnie od ich pozycji.
- Możesz użyć funkcji do zastępowania podnapisu pustym ciągiem znaków.

---

## Zadanie 3 - Czy napis A jest początkiem napisu B?

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz dwa napisy:

1. **Napis A** — potencjalny przedrostek.
2. **Napis B** — napis, który sprawdzasz pod kątem przedrostka.

Twoim zadaniem jest sprawdzić, czy napis **B** zaczyna się od napisu **A**.

### Dane wejściowe

- Dwa napisy:
  1. Napis A.
  2. Napis B.

### Dane wyjściowe

- Wartość logiczna:
  - **Prawda**, jeśli napis **B** zaczyna się od napisu **A**.
  - **Fałsz**, w przeciwnym razie.

### Przykład

- **Dane wejściowe**:
  ```
  Dino
  Dinozaur jest zly
  ```
- **Oczekiwane wyjście**:
  ```
  Prawda
  ```

### Wskazówki

- Porównaj początkowy fragment napisu **B** z napisem **A**.
- Upewnij się, że uwzględniasz całość napisu **A**.

---

## Zadanie 4 - Usuń powtórzenia znaków

**Poziom trudności**: ★★★

### Treść zadania

Otrzymujesz napis. Twoim zadaniem jest usunięcie wszystkich powtórzeń znaków w tym napisie, tak aby każdy znak wystąpił tylko raz.

### Dane wejściowe

- Jeden napis.

### Dane wyjściowe

- Jeden napis — zawierający unikalne znaki z napisu wejściowego.

### Przykład

- **Dane wejściowe**:
  ```
  AAAAAAAAAABBBBBBBBA
  ```
- **Oczekiwane wyjście**:
  ```
  AB
  ```

### Wskazówki

- Przechowuj już napotkane znaki i pomijaj te, które się powtarzają.
- Zachowaj kolejność pierwszych wystąpień znaków.

---

## Zadanie 5 - Usuń powtórzenia sąsiadujących znaków

**Poziom trudności**: ★★★

### Treść zadania

Otrzymujesz napis. Twoim zadaniem jest usunięcie powtórzeń tych samych znaków, które występują bezpośrednio obok siebie, pozostawiając tylko jedno wystąpienie z każdej serii takich znaków.

### Dane wejściowe

- Jeden napis.

### Dane wyjściowe

- Jeden napis — wynik po usunięciu powtórzeń sąsiadujących znaków.

### Przykład

- **Dane wejściowe**:
  ```
  AAAAAAAAAABBBBBBBBA
  ```
- **Oczekiwane wyjście**:
  ```
  ABA
  ```

### Wskazówki

- Iteruj przez napis i porównuj każdy znak z poprzednim.
- Dodaj znak do wyniku tylko jeśli różni się od poprzedniego.

---

## Zadanie 6 - Rotacje napisów

**Poziom trudności**: ★★★

### Treść zadania

Otrzymujesz dwa napisy o tej samej długości. Twoim zadaniem jest sprawdzić, czy jeden napis jest rotacją drugiego. Rotacja oznacza przesunięcie znaków w napisie tak, że część z końca trafia na początek.

### Dane wejściowe

- Dwa napisy.

### Dane wyjściowe

- Wartość logiczna:
  - **Prawda**, jeśli jeden napis jest rotacją drugiego.
  - **Fałsz**, w przeciwnym razie.

### Przykład

- **Dane wejściowe**:
  ```
  malpka
  pkamal
  ```
- **Oczekiwane wyjście**:
  ```
  Prawda
  ```

### Wskazówki

- Możesz sprawdzić, czy jeden z napisów jest podciągiem dwóch połączonych kopii drugiego napisu.
- Sprawdź, czy długości obu napisów są identyczne.

---

## Zadanie 7 - Powtarzające się podnapisy

**Poziom trudności**: ★★★

### Treść zadania

Otrzymujesz napis. Twoim zadaniem jest znaleźć wszystkie podnapisy, które występują w tym napisie więcej niż jeden raz.

### Dane wejściowe

- Jeden napis.

### Dane wyjściowe

- Lista napisów — zawierająca wszystkie powtarzające się podnapisy.

### Przykład

- **Dane wejściowe**:
  ```
  pythonpython
  ```
- **Oczekiwane wyjście**:
  ```
  ['python']
  ```

### Wskazówki

- Rozważ wszystkie możliwe długości podnapisów od 1 do połowy długości napisu.
- Użyj struktury danych do śledzenia liczby wystąpień każdego podnapisu.

---

## Zadanie 8 - Najdłuższy wspólny przedrostek

**Poziom trudności**: ★★★

### Treść zadania

Otrzymujesz listę napisów. Twoim zadaniem jest znaleźć najdłuższy przedrostek (początkowy fragment), który jest wspólny dla wszystkich napisów w liście.

### Dane wejściowe

- Lista napisów.

### Dane wyjściowe

- Jeden napis — najdłuższy wspólny przedrostek.

### Przykład

- **Dane wejściowe**:
  ```
  Remolada
  Remux
  Remmy
  ```
- **Oczekiwane wyjście**:
  ```
  Rem
  ```

### Wskazówki

- Porównuj znaki na tych samych pozycjach we wszystkich napisach.
- Przerwij porównywanie, gdy napotkasz różne znaki.

---

## Zadanie 9 - Najdłuższy wspólny podnapis

**Poziom trudności**: ★★★

### Treść zadania

Otrzymujesz dwa napisy. Twoim zadaniem jest znaleźć najdłuższy wspólny podciąg znaków (podnapis), który występuje w obu napisach.

### Dane wejściowe

- Dwa napisy.

### Dane wyjściowe

- Jeden napis — najdłuższy wspólny podnapis.

### Przykład

- **Dane wejściowe**:
  ```
  ijkabcdl
  xxxxabcd
  ```
- **Oczekiwane wyjście**:
  ```
  abcd
  ```

### Wskazówki

- Możesz użyć algorytmu dynamicznego programowania do znalezienia najdłuższego wspólnego podciągu.
- Twórz tablicę dwuwymiarową, która przechowuje długości wspólnych podciągów dla różnych indeksów.
