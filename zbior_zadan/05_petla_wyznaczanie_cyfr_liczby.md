## Zadanie 1 - Liczenie cyfr w liczbie

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz program, który pobiera od użytkownika liczbę naturalną i wypisuje, z ilu cyfr składa się ta liczba.

### Dane wejściowe

- Jedna liczba naturalna (całkowita nieujemna).

### Dane wyjściowe

- Jedna liczba naturalna – liczba cyfr w podanej liczbie.

### Przykład

- **Dane wejściowe**:
  ```
  342
  ```
- **Oczekiwane wyjście**:
  ```
  3
  ```

### Wskazówki

- Możesz zamienić liczbę na ciąg znaków i policzyć długość tego ciągu.
- Alternatywnie, możesz użyć pętli i dzielić liczbę przez 10, zwiększając licznik przy każdej iteracji.

---

## Zadanie 2 - Wypisywanie cyfr liczby w odwrotnej kolejności

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz program, który pobiera od użytkownika liczbę naturalną i wypisuje cyfry, z których się składa, zaczynając od cyfry jedności (czyli w odwrotnej kolejności niż w zapisie liczby).

### Dane wejściowe

- Jedna liczba naturalna.

### Dane wyjściowe

- Kolejne cyfry liczby, każda w nowej linii, zaczynając od cyfry jedności.

### Przykład

- **Dane wejściowe**:
  ```
  8214
  ```
- **Oczekiwane wyjście**:
  ```
  4
  1
  2
  8
  ```

### Wskazówki

- Możesz użyć operatora modulo (`%`) oraz dzielenia całkowitego (`//`) do wyodrębnienia kolejnych cyfr.
- Pętla powinna trwać, dopóki liczba jest większa od zera.

---

## Zadanie 3 - Sumowanie cyfr liczby

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz program, który pobiera od użytkownika liczbę naturalną i oblicza sumę cyfr tej liczby.

### Dane wejściowe

- Jedna liczba naturalna.

### Dane wyjściowe

- Jedna liczba naturalna – suma cyfr podanej liczby.

### Przykład

- **Dane wejściowe**:
  ```
  129
  ```
- **Oczekiwane wyjście**:
  ```
  12
  ```

### Wskazówki

- Użyj operatora modulo (`%`) i dzielenia całkowitego (`//`) do wyodrębnienia cyfr.
- Suma cyfr to suma wszystkich wyodrębnionych cyfr z liczby.

---

## Zadanie 4 - Wypisywanie cyfr spełniających określone warunki

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz program, który pobiera od użytkownika liczbę naturalną i wypisuje cyfry tej liczby, które spełniają poniższe warunki:

a) Są liczbami **parzystymi**.

b) Są **mniejsze niż 5**.

c) Są **różne od zera**.

### Dane wejściowe

- Jedna liczba naturalna dla wszystkich podpunktów.

### Dane wyjściowe

- Dla każdego podpunktu wypisz odpowiednie cyfry, każda w nowej linii.

### Przykład

**Podpunkt a):**

- **Dane wejściowe**:
  ```
  932
  ```
- **Oczekiwane wyjście**:
  ```
  2
  ```

**Podpunkt b):**

- **Dane wejściowe**:
  ```
  101
  ```
- **Oczekiwane wyjście**:
  ```
  1
  0
  1
  ```

**Podpunkt c):**

- **Dane wejściowe**:
  ```
  650
  ```
- **Oczekiwane wyjście**:
  ```
  6
  5
  ```

### Wskazówki

- Dla każdego podpunktu przeanalizuj cyfry liczby i sprawdź, czy spełniają dany warunek.
- Możesz użyć pętli i operatorów logicznych do filtrowania cyfr.

---

## Zadanie 5 - Sprawdzanie, czy liczba jest palindromem

**Poziom trudności**: ★★☆

### Treść zadania

Napisz program, który sprawdza, czy podana przez użytkownika liczba naturalna jest **palindromem**, czyli czy pozostaje taka sama po odwróceniu kolejności jej cyfr.

### Dane wejściowe

- Jedna liczba naturalna.

### Dane wyjściowe

- Jeden komunikat tekstowy:
  - Jeśli liczba jest palindromem, wypisz: **"Liczba jest palindromem."**
  - Jeśli liczba nie jest palindromem, wypisz: **"Liczba nie jest palindromem."**

### Przykład

- **Dane wejściowe**:
  ```
  13231
  ```
- **Oczekiwane wyjście**:
  ```
  Liczba jest palindromem.
  ```

### Wskazówki

- Możesz zamienić liczbę na ciąg znaków i sprawdzić, czy jest równy swojemu odbiciu.
- Alternatywnie, możesz odwrócić liczbę matematycznie i porównać z oryginałem.

---

## Zadanie 6 - Wypisywanie liczb spełniających określone warunki

**Poziom trudności**: ★★☆

### Treść zadania

Napisz program, który pobiera od użytkownika liczbę naturalną i wypisuje liczby spełniające poniższe warunki:

a) Wszystkie liczby naturalne **mniejsze** od podanej liczby, których **suma cyfr jest równa 10**.

b) Wszystkie liczby naturalne **dwucyfrowe** **większe** od podanej liczby.

c) Wszystkie liczby naturalne **trzycyfrowe**, których **suma cyfr jest równa** podanej liczbie.

d) Wszystkie liczby naturalne **trzycyfrowe**, które są **podzielne przez sumę cyfr** podanej liczby.

e) Wszystkie liczby naturalne **mniejsze** od podanej liczby, składające się wyłącznie z **parzystych cyfr**.

### Dane wejściowe

- Jedna liczba naturalna dla wszystkich podpunktów.

### Dane wyjściowe

- Dla każdego podpunktu wypisz odpowiednie liczby, każda w nowej linii.

### Przykład

**Dla podanej liczby: 95**

**Podpunkt a):**

- **Oczekiwane wyjście**:
  ```
  (brak)
  ```

**Podpunkt b):**

- **Oczekiwane wyjście**:
  ```
  96
  97
  98
  99
  ```

**Podpunkt c):**

- **Oczekiwane wyjście**:
  ```
  (brak)
  ```

**Podpunkt d):**

- **Oczekiwane wyjście**:
  ```
  (brak)
  ```

**Podpunkt e):**

- **Oczekiwane wyjście**:
  ```
  2
  4
  6
  8
  22
  24
  26
  28
  42
  44
  46
  48
  62
  64
  66
  68
  82
  84
  86
  88
  ```

### Wskazówki

- **Podpunkt a):** Iteruj po liczbach mniejszych od podanej i sprawdzaj, czy suma ich cyfr wynosi 10.
- **Podpunkt b):** Wypisz liczby dwucyfrowe większe od podanej liczby (od 10 do 99).
- **Podpunkt c):** Iteruj po liczbach trzycyfrowych (od 100 do 999) i sprawdzaj, czy suma ich cyfr jest równa podanej liczbie.
- **Podpunkt d):** Oblicz sumę cyfr podanej liczby, a następnie wypisz liczby trzycyfrowe podzielne przez tę sumę.
- **Podpunkt e):** Wypisz liczby mniejsze od podanej, których wszystkie cyfry są parzyste (np. 2, 4, 6, 8, 22, 24, itd.).

