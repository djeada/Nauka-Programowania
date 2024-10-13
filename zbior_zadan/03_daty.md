# Daty

## Zadanie 1 - Sprawdzanie poprawności numeru dnia tygodnia lub miesiąca

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz program, który pobiera od użytkownika liczbę naturalną i wypisuje ją na standardowe wyjście **tylko wtedy**, gdy jest ona poprawnym numerem dnia tygodnia lub miesiąca.

- **Dzień tygodnia** jest numerowany od 1 (poniedziałek) do 7 (niedziela).
- **Miesiąc** jest numerowany od 1 (styczeń) do 12 (grudzień).

Jeśli podana liczba nie mieści się w żadnym z tych zakresów, program nie powinien wypisywać nic.

### Dane wejściowe

- Jedna liczba naturalna (całkowita nieujemna) wprowadzona przez użytkownika.

### Dane wyjściowe

- Jeśli podana liczba jest w zakresie od 1 do 12 (włącznie), wypisz tę liczbę.
- W przeciwnym razie nie wypisuj nic.

### Przykład

**Przykład 1:**

- **Dane wejściowe**:
  ```
  5
  ```
- **Oczekiwane wyjście**:
  ```
  5
  ```

**Przykład 2:**

- **Dane wejściowe**:
  ```
  10
  ```
- **Oczekiwane wyjście**:
  ```
  10
  ```

**Przykład 3:**

- **Dane wejściowe**:
  ```
  15
  ```
- **Oczekiwane wyjście**:
  ```
  ```
  *(brak danych wyjściowych)*

### Wskazówki

- Użyj instrukcji warunkowej, aby sprawdzić, czy liczba mieści się w zakresie od 1 do 12.
- Pamiętaj, że liczby od 1 do 12 obejmują zarówno numery dni tygodnia (1–7), jak i miesiące (1–12).

---

## Zadanie 2 - Sprawdzanie pełnoletności na podstawie daty urodzenia

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz program, który pobiera od użytkownika datę urodzenia oraz aktualną datę i sprawdza, czy osoba urodzona w podanym dniu jest **pełnoletnia** (ma ukończone 18 lat) w podanym dniu aktualnym.

Program powinien wypisać odpowiedni komunikat:

- Jeśli osoba jest pełnoletnia, wypisz: **"Osoba jest pełnoletnia."**
- Jeśli osoba nie jest pełnoletnia, wypisz: **"Osoba nie jest pełnoletnia."**

**Założenia:**

- Data urodzenia i data aktualna są poprawnymi datami.
- Uwzględnij, że pełnoletność osiąga się dokładnie w dniu 18. urodzin.

### Dane wejściowe

Sześć liczb całkowitych, każda w oddzielnej linii:

1. Dzień urodzenia (1–31)
2. Miesiąc urodzenia (1–12)
3. Rok urodzenia (np. 2002)
4. Aktualny dzień (1–31)
5. Aktualny miesiąc (1–12)
6. Aktualny rok (np. 2020)

### Dane wyjściowe

- Jeden komunikat tekstowy:
  - **"Osoba jest pełnoletnia."** lub
  - **"Osoba nie jest pełnoletnia."**

### Przykład

**Przykład 1:**

- **Dane wejściowe**:
  ```
  5
  12
  1999
  20
  11
  2020
  ```
- **Oczekiwane wyjście**:
  ```
  Osoba jest pełnoletnia.
  ```

**Przykład 2:**

- **Dane wejściowe**:
  ```
  15
  6
  2005
  20
  11
  2020
  ```
- **Oczekiwane wyjście**:
  ```
  Osoba nie jest pełnoletnia.
  ```

### Wskazówki

- Porównaj daty, zaczynając od roku, następnie miesiąca, a na końcu dnia.
- Jeśli aktualny rok minus rok urodzenia jest większy niż 18, osoba jest pełnoletnia.
- Jeśli różnica lat wynosi dokładnie 18, porównaj miesiące i dni, aby ustalić pełnoletność.

---

## Zadanie 3 - Sprawdzanie, czy rok jest przestępny

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz program, który pobiera od użytkownika rok (liczbę naturalną) i sprawdza, czy jest to **rok przestępny**.

Program powinien wypisać odpowiedni komunikat:

- Jeśli rok jest przestępny, wypisz: **"Rok jest przestępny."**
- Jeśli rok nie jest przestępny, wypisz: **"Rok nie jest przestępny."**

**Definicja roku przestępnego:**

- Rok jest przestępny, jeśli jest podzielny przez 4, ale nie jest podzielny przez 100, **chyba że** jest podzielny przez 400.

### Dane wejściowe

- Jedna liczba naturalna – rok.

### Dane wyjściowe

- Jeden komunikat tekstowy zgodny z powyższym opisem.

### Przykład

**Przykład 1:**

- **Dane wejściowe**:
  ```
  2020
  ```
- **Oczekiwane wyjście**:
  ```
  Rok jest przestępny.
  ```

**Przykład 2:**

- **Dane wejściowe**:
  ```
  2100
  ```
- **Oczekiwane wyjście**:
  ```
  Rok nie jest przestępny.
  ```

### Wskazówki

- Użyj operatora modulo `%` do sprawdzania podzielności.
- Zwróć uwagę na kolejność warunków:
  - Jeśli rok jest podzielny przez 400, jest przestępny.
  - Jeśli rok jest podzielny przez 100 (ale nie przez 400), nie jest przestępny.
  - Jeśli rok jest podzielny przez 4 (ale nie przez 100), jest przestępny.
  - W przeciwnym razie rok nie jest przestępny.

---

## Zadanie 4 - Wypisywanie dnia tygodnia na podstawie numeru

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz program, który dla podanej liczby naturalnej wypisze odpowiadający jej **dzień tygodnia**. Numeracja dni tygodnia jest następująca:

1. Poniedziałek
2. Wtorek
3. Środa
4. Czwartek
5. Piątek
6. Sobota
7. Niedziela

Jeśli podana liczba nie jest w zakresie od 1 do 7 (włącznie), program powinien wypisać komunikat: **"Niepoprawny numer dnia tygodnia."**

### Dane wejściowe

- Jedna liczba naturalna.

### Dane wyjściowe

- Nazwa dnia tygodnia lub komunikat o błędzie.

### Przykład

**Przykład 1:**

- **Dane wejściowe**:
  ```
  2
  ```
- **Oczekiwane wyjście**:
  ```
  Wtorek
  ```

**Przykład 2:**

- **Dane wejściowe**:
  ```
  8
  ```
- **Oczekiwane wyjście**:
  ```
  Niepoprawny numer dnia tygodnia.
  ```

### Wskazówki

- Możesz użyć instrukcji `if-elif-else` lub struktury danych (np. listy) do mapowania numerów na nazwy dni tygodnia.
- Upewnij się, że program obsługuje poprawnie liczby spoza zakresu 1–7.

---

## Zadanie 5 - Liczba dni w miesiącu

**Poziom trudności**: ★☆☆

### Treść zadania

Napisz program, który dla podanego numeru miesiąca (liczby naturalnej) wypisze liczbę dni w tym miesiącu.

Przyjmij, że rok **nie jest** przestępny (luty ma 28 dni).

Jeśli podana liczba nie jest poprawnym numerem miesiąca (1–12), program powinien wypisać komunikat: **"Niepoprawny numer miesiąca."**

### Dane wejściowe

- Jedna liczba naturalna – numer miesiąca.

### Dane wyjściowe

- Liczba dni w miesiącu lub komunikat o błędzie.

### Przykład

**Przykład 1:**

- **Dane wejściowe**:
  ```
  1
  ```
- **Oczekiwane wyjście**:
  ```
  31
  ```

**Przykład 2:**

- **Dane wejściowe**:
  ```
  2
  ```
- **Oczekiwane wyjście**:
  ```
  28
  ```

**Przykład 3:**

- **Dane wejściowe**:
  ```
  13
  ```
- **Oczekiwane wyjście**:
  ```
  Niepoprawny numer miesiąca.
  ```

### Wskazówki

- Miesiące i liczba ich dni:
  - Styczeń (1): 31
  - Luty (2): 28
  - Marzec (3): 31
  - Kwiecień (4): 30
  - Maj (5): 31
  - Czerwiec (6): 30
  - Lipiec (7): 31
  - Sierpień (8): 31
  - Wrzesień (9): 30
  - Październik (10): 31
  - Listopad (11): 30
  - Grudzień (12): 31
- Możesz użyć listy lub słownika do przechowywania liczby dni w poszczególnych miesiącach.

---

## Zadanie 6 - Sprawdzanie poprawności daty

**Poziom trudności**: ★★☆

### Treść zadania

Napisz program, który dla podanej daty (dzień, miesiąc, rok) sprawdza, czy jest ona **poprawną datą** w kalendarzu gregoriańskim.

Program powinien wypisać odpowiedni komunikat:

- Jeśli data jest poprawna, wypisz: **"Data jest poprawna."**
- Jeśli data jest niepoprawna, wypisz: **"Data jest niepoprawna."**

### Dane wejściowe

- Trzy liczby naturalne:
  1. Dzień (1–31)
  2. Miesiąc (1–12)
  3. Rok (np. 2020)

### Dane wyjściowe

- Jeden komunikat tekstowy.

### Przykład

**Przykład 1:**

- **Dane wejściowe**:
  ```
  29
  2
  2020
  ```
- **Oczekiwane wyjście**:
  ```
  Data jest poprawna.
  ```

**Przykład 2:**

- **Dane wejściowe**:
  ```
  31
  4
  2021
  ```
- **Oczekiwane wyjście**:
  ```
  Data jest niepoprawna.
  ```

### Wskazówki

- Sprawdź, czy miesiąc jest w zakresie 1–12.
- Ustal, ile dni ma dany miesiąc (pamiętaj o roku przestępnym dla lutego).
- Sprawdź, czy dzień mieści się w zakresie 1–maksymalna liczba dni w miesiącu.
- Rok przestępny ustal zgodnie z zasadami z **Zadania 3**.

---

## Zadanie 7 - Obliczanie liczby dni od początku roku

**Poziom trudności**: ★★☆

### Treść zadania

Napisz program, który dla podanej daty (dzień, miesiąc, rok) obliczy, ile dni minęło od początku tego roku do podanej daty **włącznie**.

### Dane wejściowe

- Trzy liczby naturalne:
  1. Dzień (1–31)
  2. Miesiąc (1–12)
  3. Rok (np. 2021)

### Dane wyjściowe

- Jedna liczba naturalna – liczba dni od początku roku.

### Przykład

**Przykład 1:**

- **Dane wejściowe**:
  ```
  14
  2
  1482
  ```
- **Oczekiwane wyjście**:
  ```
  45
  ```

**Przykład 2:**

- **Dane wejściowe**:
  ```
  1
  1
  2021
  ```
- **Oczekiwane wyjście**:
  ```
  1
  ```

### Wskazówki

- Utwórz listę z liczbą dni w poszczególnych miesiącach.
- Jeśli rok jest przestępny, luty ma 29 dni, w przeciwnym razie 28 dni.
- Zsumuj dni pełnych miesięcy, które minęły, oraz dodaj dzień z aktualnego miesiąca.
- Przykład obliczeń dla daty 14.02.1482:
  - Styczeń: 31 dni
  - Luty: 14 dni
  - Suma: 31 + 14 = 45 dni

---

## Zadanie 8 - Obliczanie dnia tygodnia dla podanej daty

**Poziom trudności**: ★★☆

### Treść zadania

Napisz program, który dla podanej daty (dzień, miesiąc, rok) wyznaczy, jaki to **dzień tygodnia**.

**Użyj wzoru** Zeller's Congruence (dla kalendarza gregoriańskiego):

1. Jeśli miesiąc jest mniejszy niż 3 (styczeń lub luty), dodaj 12 do miesiąca i odejmij 1 od roku:

   ```
   Jeśli miesiąc <= 2:
       miesiąc += 12
       rok -= 1
   ```

2. Oblicz wartości pomocnicze:

   ```
   K = rok % 100
   J = rok // 100
   h = (dzień + ((13 * (miesiąc + 1)) // 5) + K + (K // 4) + (J // 4) + (5 * J)) % 7
   ```

3. Dzień tygodnia to:

   - 0: Sobota
   - 1: Niedziela
   - 2: Poniedziałek
   - 3: Wtorek
   - 4: Środa
   - 5: Czwartek
   - 6: Piątek

### Dane wejściowe

- Trzy liczby naturalne:
  1. Dzień (1–31)
  2. Miesiąc (1–12)
  3. Rok (np. 2020)

### Dane wyjściowe

- Nazwa dnia tygodnia odpowiadającego podanej dacie.

### Przykład

**Przykład:**

- **Dane wejściowe**:
  ```
  9
  10
  2020
  ```
- **Oczekiwane wyjście**:
  ```
  Piątek
  ```

### Wskazówki

- Przy obliczeniach używaj dzielenia całkowitoliczbowego `//` i operacji modulo `%`.
- Po obliczeniu wartości `h`, zmapuj ją na nazwę dnia tygodnia według podanej tabeli.
- Upewnij się, że data jest poprawna (możesz wykorzystać rozwiązanie z **Zadania 6**).

---
