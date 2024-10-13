## Zadanie 1 - Wczytaj i wypisz

**Poziom trudności**: ★☆☆

### Treść zadania

Dla podanej liczby naturalnej \( N \), wczytaj \( N \) liczb całkowitych do listy, a następnie:

- **a)** Wypisz elementy listy od początku do końca, każdy w osobnym wierszu.
- **b)** Wypisz elementy listy od końca do początku, wypisując je w jednym wierszu, oddzielone przecinkami (bez spacji).

### Dane wejściowe

- Jedna liczba naturalna \( N \) (\( N \geq 1 \)).
- Następnie \( N \) liczb całkowitych, każda w nowej linii.

### Dane wyjściowe

- **Podpunkt a):** \( N \) liczb całkowitych, każda w osobnym wierszu, w kolejności wprowadzenia.
- **Podpunkt b):** Jedna linia zawierająca \( N \) liczb całkowitych w odwrotnej kolejności niż wprowadzono, oddzielonych przecinkami.

### Przykład

- **Dane wejściowe**:
  ```
  3
  8
  12
  7
  ```
- **Oczekiwane wyjście**:

  **Podpunkt a):**
  ```
  8
  12
  7
  ```

  **Podpunkt b):**
  ```
  7,12,8
  ```

### Wskazówki

- Użyj listy do przechowywania wczytanych liczb.
- Do wypisania listy w odwrotnej kolejności możesz użyć odwracania listy lub indeksowania od końca.
- Przy wypisywaniu elementów oddzielonych przecinkami, upewnij się, że nie dodajesz przecinka na końcu.

---

## Zadanie 2 - Wczytaj, zmodyfikuj i wypisz

**Poziom trudności**: ★☆☆

### Treść zadania

Wczytaj liczbę naturalną \( N \) oraz \( N \) liczb całkowitych i umieść je w liście. Następnie wykonaj poniższe operacje:

- **a)** Dodaj 1 do każdego elementu listy.
- **b)** Pomnóż każdy element przez jego indeks w liście (indeksy zaczynają się od 0).
- **c)** Zastąp wszystkie elementy listy wartością pierwszego elementu.

Dla każdego podpunktu wypisz zmodyfikowaną listę w jednym wierszu, oddzielając elementy przecinkami.

### Dane wejściowe

- Jedna liczba naturalna \( N \) (\( N \geq 1 \)).
- Następnie \( N \) liczb całkowitych, każda w nowej linii.

### Dane wyjściowe

- Dla każdego podpunktu: jedna linia zawierająca \( N \) liczb całkowitych, oddzielonych przecinkami, reprezentujących zmodyfikowaną listę.

### Przykład

- **Dane wejściowe**:
  ```
  3
  3
  9
  7
  ```
- **Oczekiwane wyjście**:

  **Podpunkt a):**
  ```
  4,10,8
  ```

  **Podpunkt b):**
  ```
  0,9,14
  ```

  **Podpunkt c):**
  ```
  3,3,3
  ```

### Wskazówki

- W podpunkcie a) zwiększ każdy element o 1.
- W podpunkcie b) pomnóż każdy element przez jego indeks.
- W podpunkcie c) ustaw wszystkie elementy na wartość pierwszego elementu.

---

## Zadanie 3 - Pierwsze wystąpienie klucza

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz listę liczb całkowitych oraz liczbę całkowitą jako klucz. Znajdź indeks pierwszego wystąpienia klucza w liście. Jeśli klucz nie występuje w liście, zwróć **-1**.

### Dane wejściowe

- Jedna liczba naturalna \( N \) (\( N \geq 1 \)).
- Następnie \( N \) liczb całkowitych, każda w nowej linii.
- Na końcu jedna liczba całkowita — klucz do wyszukania.

### Dane wyjściowe

- Jedna liczba całkowita — indeks pierwszego wystąpienia klucza (indeksy zaczynają się od 0) lub **-1**, jeśli klucz nie występuje w liście.

### Przykład

- **Dane wejściowe**:
  ```
  5
  2
  9
  -1
  3
  8
  -1
  ```
- **Oczekiwane wyjście**:
  ```
  2
  ```

### Wskazówki

- Możesz użyć metody `index()` listy, ale pamiętaj o obsłudze wyjątku, gdy klucza nie ma w liście.
- Alternatywnie, przejdź przez listę za pomocą pętli i sprawdź, czy element jest równy kluczowi.

---

## Zadanie 4 - Minimum oraz maksimum

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz listę liczb całkowitych. Znajdź największy i najmniejszy element tej listy i wypisz je jako dwie osobne liczby całkowite.

### Dane wejściowe

- Jedna liczba naturalna \( N \) (\( N \geq 1 \)).
- Następnie \( N \) liczb całkowitych, każda w nowej linii.

### Dane wyjściowe

- Dwie liczby całkowite, oddzielone spacją:
  - Największy element listy.
  - Najmniejszy element listy.

### Przykład

- **Dane wejściowe**:
  ```
  9
  4
  -7
  8
  5
  6
  -9
  10
  2
  -8
  ```
- **Oczekiwane wyjście**:
  ```
  10 -9
  ```

### Wskazówki

- Możesz użyć funkcji `max()` i `min()` na liście.
- Upewnij się, że wypisujesz liczby w odpowiedniej kolejności.

---

## Zadanie 5 - Zmodyfikuj elementy spełniające warunek

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz listę liczb całkowitych. Wykonaj poniższe operacje, tworząc za każdym razem nową listę:

- **a)** Zwiększ o 1 wszystkie elementy o parzystych indeksach (indeksy zaczynają się od 0).
- **b)** Wyzeruj wszystkie elementy będące wielokrotnościami liczby 3.
- **c)** Podnieś do kwadratu wszystkie elementy mniejsze niż 10.
- **d)** Wstaw sumę wszystkich elementów listy na indeksy będące liczbami pierwszymi.
- **e)** Zamień każdy element na iloczyn wszystkich pozostałych elementów listy.

Dla każdego podpunktu wypisz zmodyfikowaną listę w jednym wierszu, oddzielając elementy przecinkami.

### Dane wejściowe

- Jedna liczba naturalna \( N \) (\( N \geq 1 \)).
- Następnie \( N \) liczb całkowitych, każda w nowej linii.

### Dane wyjściowe

- Dla każdego podpunktu: jedna linia zawierająca zmodyfikowaną listę, elementy oddzielone przecinkami.

### Przykład

- **Dane wejściowe**:
  ```
  5
  5
  7
  9
  4
  2
  ```
- **Oczekiwane wyjście**:

  **Podpunkt a):**
  ```
  6,7,10,4,3
  ```

  **Podpunkt b):**
  ```
  6,7,0,4,3
  ```

  **Podpunkt c):**
  ```
  36,49,0,16,9
  ```

  **Podpunkt d):**
  ```
  37,49,0,37,9
  ```

  **Podpunkt e):**
  ```
  2592,0,0,36,1080
  ```

### Wskazówki

- **Podpunkt a):** Iteruj po indeksach listy i zwiększ elementy o parzystych indeksach.
- **Podpunkt b):** Sprawdź, czy element jest podzielny przez 3.
- **Podpunkt c):** Podnieś do kwadratu elementy mniejsze niż 10.
- **Podpunkt d):** Oblicz sumę wszystkich elementów i wstaw na indeksy pierwsze (2, 3, 5, 7, ...).
- **Podpunkt e):** Oblicz iloczyn wszystkich elementów i dla każdego indeksu ustaw wartość iloczynu podzielonego przez wartość elementu na tym indeksie.

---

## Zadanie 6 - Czy średnia elementów znajduje się w liście?

**Poziom trudności**: ★☆☆

### Treść zadania

Dla otrzymanej listy liczb całkowitych sprawdź, czy średnia arytmetyczna jej elementów znajduje się w tej liście. Wypisz **"Tak"**, jeśli średnia jest elementem listy, lub **"Nie"** w przeciwnym razie.

### Dane wejściowe

- Jedna liczba naturalna \( N \) (\( N \geq 1 \)).
- Następnie \( N \) liczb całkowitych, każda w nowej linii.

### Dane wyjściowe

- Jeden napis: **"Tak"** lub **"Nie"**.

### Przykład

- **Dane wejściowe**:
  ```
  5
  6
  2
  1
  4
  27
  ```
- **Oczekiwane wyjście**:
  ```
  Nie
  ```

### Wskazówki

- Oblicz średnią arytmetyczną elementów listy.
- Sprawdź, czy średnia (lub jej całkowita część) znajduje się w liście.

---

## Zadanie 7 - Średnia dwóch największych liczb

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz listę liczb naturalnych. Znajdź największą i drugą co do wielkości liczbę w liście, a następnie oblicz ich średnią arytmetyczną i wypisz jako liczbę zmiennoprzecinkową.

### Dane wejściowe

- Jedna liczba naturalna \( N \) (\( N \geq 2 \)).
- Następnie \( N \) liczb naturalnych, każda w nowej linii.

### Dane wyjściowe

- Jedna liczba zmiennoprzecinkowa — średnia arytmetyczna dwóch największych liczb z dokładnością do jednego miejsca po przecinku.

### Przykład

- **Dane wejściowe**:
  ```
  6
  9
  2
  3
  2
  1
  7
  ```
- **Oczekiwane wyjście**:
  ```
  8.0
  ```

### Wskazówki

- Posortuj listę lub znajdź największą i drugą największą liczbę.
- Oblicz średnią tych dwóch liczb.

---

## Zadanie 8 - Usuń klucz

**Poziom trudności**: ★☆☆

### Treść zadania

Dla otrzymanej listy liczb całkowitych oraz liczby całkowitej jako klucza, usuń pierwsze wystąpienie klucza w liście.

### Dane wejściowe

- Jedna liczba naturalna \( N \) (\( N \geq 1 \)).
- Następnie \( N \) liczb całkowitych, każda w nowej linii.
- Na końcu jedna liczba całkowita — klucz do usunięcia.

### Dane wyjściowe

- Lista liczb całkowitych po usunięciu pierwszego wystąpienia klucza, elementy oddzielone przecinkami.

### Przykład

- **Dane wejściowe**:
  ```
  5
  6
  2
  1
  4
  27
  4
  ```
- **Oczekiwane wyjście**:
  ```
  6,2,1,27
  ```

### Wskazówki

- Użyj metody `remove()` do usunięcia pierwszego wystąpienia klucza.
- Jeśli klucz nie występuje w liście, lista pozostaje bez zmian.

---

## Zadanie 9 - Usuń duplikaty

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz listę liczb naturalnych. Usuń z niej wszystkie duplikaty, tak aby każda liczba występowała tylko raz.

### Dane wejściowe

- Jedna liczba naturalna \( N \) (\( N \geq 1 \)).
- Następnie \( N \) liczb naturalnych, każda w nowej linii.

### Dane wyjściowe

- Lista liczb naturalnych bez duplikatów, elementy oddzielone przecinkami, w kolejności ich pierwszego wystąpienia.

### Przykład

- **Dane wejściowe**:
  ```
  6
  3
  2
  1
  3
  2
  2
  ```
- **Oczekiwane wyjście**:
  ```
  3,2,1
  ```

### Wskazówki

- Możesz użyć zbioru `set` do identyfikacji unikalnych elementów, ale pamiętaj o zachowaniu kolejności — użyj więc struktury `OrderedDict` lub iteruj ręcznie i dodawaj elementy, jeśli nie zostały wcześniej dodane.

---

## Zadanie 10 - Czy punkty mogą stanowić wierzchołki trójkąta?

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz współrzędne trzech punktów \( A(x_A, y_A) \), \( B(x_B, y_B) \) i \( C(x_C, y_C) \). Sprawdź, czy te punkty mogą stanowić wierzchołki trójkąta (czy nie leżą na jednej prostej).

### Dane wejściowe

- Sześć liczb całkowitych, każda w nowej linii:
  - \( x_A \), \( y_A \)
  - \( x_B \), \( y_B \)
  - \( x_C \), \( y_C \)

### Dane wyjściowe

- Jeden napis: **"Tak"** jeśli punkty mogą stanowić wierzchołki trójkąta, lub **"Nie"** w przeciwnym razie.

### Przykład

- **Dane wejściowe**:
  ```
  -3
  -2
  -3
  1
  -3
  0
  ```
- **Oczekiwane wyjście**:
  ```
  Nie
  ```

### Wskazówki

- Sprawdź, czy pole trójkąta wyznaczonego przez te punkty jest różne od zera.
- Możesz użyć wzoru na pole trójkąta z wykorzystaniem współrzędnych.

---

## Zadanie 11 - Samochody jadące w przeciwnych kierunkach

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz listę znaków reprezentujących samochody jadące na wschód ('A') i zachód ('B'). Policz, ile razy samochody jadące w przeciwnych kierunkach mijają się.

### Dane wejściowe

- Jedna liczba naturalna \( N \) (\( N \geq 1 \)).
- Następnie ciąg \( N \) znaków 'A' lub 'B', bez spacji, w jednej linii.

### Dane wyjściowe

- Jedna liczba naturalna — liczba mijających się par samochodów.

### Przykład

- **Dane wejściowe**:
  ```
  5
  ABABB
  ```
- **Oczekiwane wyjście**:
  ```
  5
  ```

### Wskazówki

- Iteruj przez listę i licz, ile samochodów jedzie na wschód ('A').
- Gdy napotkasz samochód jadący na zachód ('B'), dodaj do wyniku liczbę samochodów jadących na wschód, które już minąłeś.

---

## Zadanie 12 - Rotacja w lewo/prawo

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz listę liczb całkowitych, kierunek przesunięcia oraz liczbę miejsc, o jakie elementy listy mają zostać przesunięte.

- Kierunek przesunięcia:
  - **0** — przesunięcie w lewo.
  - **1** — przesunięcie w prawo.

Przesuń elementy listy w podanym kierunku o podaną liczbę miejsc.

### Dane wejściowe

- Jedna liczba naturalna \( N \) (\( N \geq 1 \)).
- Następnie \( N \) liczb całkowitych, każda w nowej linii.
- Kolejna liczba naturalna — kierunek przesunięcia (0 lub 1).
- Ostatnia liczba naturalna — liczba miejsc do przesunięcia (\( K \geq 0 \)).

### Dane wyjściowe

- Lista liczb całkowitych po przesunięciu, elementy oddzielone przecinkami.

### Przykład

- **Dane wejściowe**:
  ```
  7
  5
  27
  6
  2
  1
  10
  8
  0
  2
  ```
- **Oczekiwane wyjście**:
  ```
  6,2,1,10,8,5,27
  ```

### Wskazówki

- Możesz użyć operacji cięcia listy (`slice`) i konkatenacji.
- Pamiętaj o obsłudze przypadku, gdy \( K \) jest większe niż długość listy (użyj operacji modulo).

---

## Zadanie 13 - Znalezienie brakującego elementu w ciągu arytmetycznym

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz listę liczb naturalnych, która jest fragmentem ciągu arytmetycznego z jednym brakującym elementem. Znajdź brakujący element.

### Dane wejściowe

- Jedna liczba naturalna \( N \) (\( N \geq 2 \)).
- Następnie \( N \) liczb naturalnych, każda w nowej linii.

### Dane wyjściowe

- Jedna liczba naturalna — brakujący element ciągu.

### Przykład

- **Dane wejściowe**:
  ```
  4
  5
  2
  1
  3
  ```
- **Oczekiwane wyjście**:
  ```
  4
  ```

### Wskazówki

- Posortuj listę.
- Oblicz różnicę ciągu (różnicę między kolejnymi elementami).
- Znajdź miejsce, gdzie różnica jest inna, i oblicz brakujący element.

---

## Zadanie 14 - Znalezienie elementu bez pary

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz listę liczb całkowitych zawierającą nieparzystą liczbę elementów. Każdy element poza jednym występuje w parze (dokładnie dwa razy). Znajdź element, który nie ma pary.

### Dane wejściowe

- Jedna liczba naturalna \( N \) (nieparzysta, \( N \geq 1 \)).
- Następnie \( N \) liczb całkowitych, każda w nowej linii.

### Dane wyjściowe

- Jedna liczba całkowita — element bez pary.

### Przykład

- **Dane wejściowe**:
  ```
  7
  1
  3
  1
  7
  3
  1
  1
  ```
- **Oczekiwane wyjście**:
  ```
  7
  ```

### Wskazówki

- Użyj operacji XOR na wszystkich elementach — pary się wyzerują, pozostanie element bez pary.
- Możesz też użyć słownika (`dict`) do zliczania wystąpień.

---

## Zadanie 15 - Znalezienie elementu dominującego

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz listę liczb naturalnych. Znajdź element, który występuje w liście więcej niż połowa jej długości (tzw. element dominujący). Jeśli taki element nie istnieje, wypisz **-1**.

### Dane wejściowe

- Jedna liczba naturalna \( N \) (\( N \geq 1 \)).
- Następnie \( N \) liczb naturalnych, każda w nowej linii.

### Dane wyjściowe

- Jedna liczba naturalna — element dominujący lub **-1**, jeśli taki element nie istnieje.

### Przykład

- **Dane wejściowe**:
  ```
  5
  4
  7
  4
  4
  2
  ```
- **Oczekiwane wyjście**:
  ```
  4
  ```

### Wskazówki

- Użyj słownika (`dict`) do zliczania liczby wystąpień każdego elementu.
- Sprawdź, czy któryś element występuje więcej niż \( N/2 \) razy.

---

## Zadanie 16 - Znalezienie indeksów pierwszej pary o sumie x

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz listę liczb całkowitych oraz liczbę całkowitą \( x \). Znajdź indeksy pierwszej pary elementów, których suma jest równa \( x \). Jeśli taka para nie istnieje, wypisz **-1 -1**.

### Dane wejściowe

- Jedna liczba naturalna \( N \) (\( N \geq 2 \)).
- Następnie \( N \) liczb całkowitych, każda w nowej linii.
- Na końcu liczba całkowita \( x \).

### Dane wyjściowe

- Dwie liczby całkowite — indeksy pary elementów (indeksy zaczynają się od 0), lub **-1 -1**, jeśli taka para nie istnieje.

### Przykład

- **Dane wejściowe**:
  ```
  5
  1
  3
  4
  5
  2
  5
  ```
- **Oczekiwane wyjście**:
  ```
  0 2
  ```

### Wskazówki

- Możesz użyć słownika do przechowywania wcześniej napotkanych wartości i ich indeksów.
- Iteruj przez listę i dla każdego elementu sprawdź, czy \( x - \) ten element jest w słowniku.

---

## Zadanie 17 - Znalezienie wszystkich par o sumie x

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz listę liczb całkowitych oraz liczbę całkowitą \( x \). Znajdź wszystkie pary elementów, których suma jest równa \( x \).

### Dane wejściowe

- Jedna liczba naturalna \( N \) (\( N \geq 2 \)).
- Następnie \( N \) liczb całkowitych, każda w nowej linii.
- Na końcu liczba całkowita \( x \).

### Dane wyjściowe

- Lista par liczb całkowitych — wartości elementów, nie indeksy. Każda para w osobnej linii, elementy w parze oddzielone spacją.

### Przykład

- **Dane wejściowe**:
  ```
  5
  1
  2
  4
  3
  7
  5
  ```
- **Oczekiwane wyjście**:
  ```
  1 4
  2 3
  ```

### Wskazówki

- Użyj dwóch pętli zagnieżdżonych lub słownika do efektywnego znajdowania par.
- Upewnij się, że nie wypisujesz tych samych par więcej niż raz.

---

## Zadanie 18 - Znalezienie indeksu najmniejszego elementu w przesuniętej liście

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz listę liczb całkowitych, która została posortowana rosnąco i przesunięta w prawo o nieznaną liczbę miejsc. Znajdź indeks najmniejszego elementu w tej liście.

### Dane wejściowe

- Jedna liczba naturalna \( N \) (\( N \geq 1 \)).
- Następnie \( N \) liczb całkowitych, każda w nowej linii.

### Dane wyjściowe

- Jedna liczba całkowita — indeks najmniejszego elementu (indeksy zaczynają się od 0).

### Przykład

- **Dane wejściowe**:
  ```
  5
  7
  8
  -1
  4
  5
  ```
- **Oczekiwane wyjście**:
  ```
  2
  ```

### Wskazówki

- Możesz użyć zmodyfikowanego algorytmu wyszukiwania binarnego.
- Szukaj punktu, w którym następuje przełamanie rosnącej sekwencji.

---
