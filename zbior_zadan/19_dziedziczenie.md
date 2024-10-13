# Dziedziczenie

## Zadanie 1 - Wywołanie metody klasy bazowej w klasie potomnej

**Poziom trudności**: ★☆☆

### Treść zadania

Zaplanować i zaimplementować dwie klasy:

1. **Klasa bazowa** – posiadająca metodę o określonej funkcjonalności.

2. **Klasa potomna** – dziedzicząca po klasie bazowej i nadpisująca tę samą metodę.

Twoim zadaniem jest w metodzie klasy potomnej, która nadpisuje metodę z klasy bazowej, wywołać tę metodę z klasy bazowej. 

Napisz program testujący te klasy, który:

- Tworzy obiekt klasy potomnej.
- Wywołuje nadpisaną metodę.
- Demonstruje wywołanie metody klasy bazowej z poziomu klasy potomnej.

### Dane wejściowe

- Brak danych wejściowych. Zadanie dotyczy implementacji klas i ich metod.

### Dane wyjściowe

- Komunikaty pokazujące działanie metod, w tym wywołanie metody klasy bazowej z poziomu klasy potomnej.

### Przykład

- **Oczekiwane zachowanie**:

  - **Klasa Bazowa** posiada metodę `przedstaw_się()`, która wypisuje komunikat, np. "Jestem klasą bazową."
  - **Klasa Potomna** nadpisuje metodę `przedstaw_się()`, w której najpierw wywołuje metodę z klasy bazowej, a następnie wypisuje dodatkowy komunikat, np. "A ja jestem klasą potomną."
  - W programie testowym tworzymy obiekt klasy potomnej i wywołujemy metodę `przedstaw_się()`. Oczekujemy następującego wyjścia:
    ```
    Jestem klasą bazową.
    A ja jestem klasą potomną.
    ```

### Wskazówki

- W metodzie klasy potomnej możesz odwołać się do metody klasy bazowej, używając odpowiedniej konstrukcji (np. poprzez specjalne słowo kluczowe lub nazwę klasy bazowej).
- Pamiętaj, że nadpisywanie metod pozwala na rozszerzenie lub modyfikację zachowania metod z klasy bazowej w klasie potomnej.

---

## Zadanie 2 - Klasa Kształt oraz klasy Koło i Kwadrat

**Poziom trudności**: ★★☆

### Treść zadania

Zaprojektuj hierarchię klas składającą się z:

1. **Klasy Kształt** – ogólnej klasy bazowej reprezentującej dowolny kształt.

2. **Klasy Koło** – klasy potomnej dziedziczącej po klasie Kształt, reprezentującej koło.

3. **Klasy Kwadrat** – klasy potomnej dziedziczącej po klasie Kształt, reprezentującej kwadrat.

Każda z klas powinna zawierać:

- **Metodę** obliczającą pole powierzchni kształtu.
- **Metodę** wyświetlającą informacje o kształcie, takie jak jego typ, parametry i obliczone pole.

Napisz program testujący te klasy, który:

- Tworzy obiekty klasy **Koło** i **Kwadrat** z odpowiednimi parametrami.
- Wywołuje metody obliczające pole i wyświetlające informacje o kształtach.

### Dane wejściowe

- Parametry potrzebne do utworzenia kształtów:
  - Dla koła: promień (liczba rzeczywista).
  - Dla kwadratu: długość boku (liczba rzeczywista).

### Dane wyjściowe

- Informacje o utworzonych kształtach, w tym:
  - Typ kształtu.
  - Parametry kształtu.
  - Obliczone pole powierzchni.

### Przykład

- **Dane wejściowe**:
  - Koło o promieniu 5.
  - Kwadrat o boku 4.

- **Oczekiwane wyjście**:
  ```
  Kształt: Koło
  Promień: 5
  Pole powierzchni: 78.5398

  Kształt: Kwadrat
  Długość boku: 4
  Pole powierzchni: 16
  ```
  *(Przyjmując, że π ≈ 3.1416)*

### Wskazówki

- W klasie **Kształt** możesz zdefiniować metodę abstrakcyjną lub ogólną metodę obliczającą pole, którą nadpiszesz w klasach potomnych.
- Użyj dziedziczenia, aby zorganizować wspólne elementy klas i uniknąć duplikowania kodu.

---

## Zadanie 3 - Polimorfizm z klasami Zwierz, Pies i Kot

**Poziom trudności**: ★★☆

### Treść zadania

Zaprojektuj następujące klasy:

1. **Klasa Zwierz** – klasa bazowa reprezentująca ogólne zwierzę, zawierająca metodę `odgłos()`, która definiuje dźwięk wydawany przez zwierzę.

2. **Klasa Pies** – klasa potomna dziedzicząca po klasie **Zwierz**, nadpisująca metodę `odgłos()` tak, aby zwracała odgłos psa.

3. **Klasa Kot** – klasa potomna dziedzicząca po klasie **Zwierz**, nadpisująca metodę `odgłos()` tak, aby zwracała odgłos kota.

Napisz program testujący te klasy, który:

- Tworzy obiekty klasy **Zwierz**, **Pies** i **Kot**.
- Umieszcza te obiekty w jednej kolekcji (np. liście lub tablicy).
- Iteruje przez kolekcję i dla każdego obiektu wywołuje metodę `odgłos()`, demonstrując polimorfizm.

### Dane wejściowe

- Brak danych wejściowych. Zadanie polega na implementacji klas i metod oraz ich wykorzystaniu w programie testującym.

### Dane wyjściowe

- Komunikaty wypisywane przez metodę `odgłos()` dla każdego obiektu w kolekcji.

### Przykład

- **Oczekiwane wyjście**:
  ```
  Zwierz wydaje odgłos: ...
  Pies wydaje odgłos: Hau!
  Kot wydaje odgłos: Miau!
  ```

### Wskazówki

- Polimorfizm umożliwia traktowanie obiektów różnych klas dziedziczących po tej samej klasie bazowej w jednolity sposób.
- Umieszczając obiekty różnych klas w jednej kolekcji, możesz iterować przez nią i wywoływać na obiektach metody zdefiniowane w klasie bazowej, które zostały nadpisane w klasach potomnych.

---

## Zadanie 4 - Dziedziczenie wielopoziomowe z klasą Człowiek

**Poziom trudności**: ★★☆

### Treść zadania

Zaprojektuj hierarchię klas wykorzystującą dziedziczenie wielopoziomowe:

1. **Klasa Człowiek** – zawiera pola:
   - Imię (tekst).
   - Nazwisko (tekst).
   - Miejsce urodzenia (tekst).
   - Zawód (tekst).

2. **Klasa Student** – dziedziczy po klasie **Człowiek** i dodaje pola:
   - Numer albumu (liczba całkowita).
   - Kierunek studiów (tekst).

3. **Klasa StudentFizyki** – dziedziczy po klasie **Student** i dodaje pola:
   - Średnia z laboratoriów (liczba rzeczywista).
   - Średnia z wykładów (liczba rzeczywista).

Napisz program testujący te klasy, który:

- Tworzy obiekty każdej z klas z odpowiednimi danymi.
- Wyświetla informacje o utworzonych obiektach, pokazując dziedziczenie i rozszerzanie właściwości na kolejnych poziomach.

### Dane wejściowe

- Informacje potrzebne do utworzenia obiektów:
  - Dla **Człowiek**: imię, nazwisko, miejsce urodzenia, zawód.
  - Dla **Student**: wszystkie powyższe oraz numer albumu i kierunek studiów.
  - Dla **StudentFizyki**: wszystkie powyższe oraz średnia z laboratoriów i średnia z wykładów.

### Dane wyjściowe

- Szczegółowe informacje o utworzonych obiektach, obejmujące wszystkie pola zdefiniowane w ich klasach i klasach bazowych.

### Przykład

- **Dane wejściowe**:
  - Człowiek: Imię: Jan, Nazwisko: Kowalski, Miejsce urodzenia: Kraków, Zawód: Inżynier.
  - Student: Imię: Anna, Nazwisko: Nowak, Miejsce urodzenia: Warszawa, Zawód: Student, Numer albumu: 12345, Kierunek studiów: Informatyka.
  - StudentFizyki: Imię: Piotr, Nazwisko: Wiśniewski, Miejsce urodzenia: Gdańsk, Zawód: Student, Numer albumu: 54321, Kierunek studiów: Fizyka, Średnia z laboratoriów: 4.5, Średnia z wykładów: 4.0.

- **Oczekiwane wyjście**:
  ```
  Człowiek:
  Imię: Jan
  Nazwisko: Kowalski
  Miejsce urodzenia: Kraków
  Zawód: Inżynier

  Student:
  Imię: Anna
  Nazwisko: Nowak
  Miejsce urodzenia: Warszawa
  Zawód: Student
  Numer albumu: 12345
  Kierunek studiów: Informatyka

  Student Fizyki:
  Imię: Piotr
  Nazwisko: Wiśniewski
  Miejsce urodzenia: Gdańsk
  Zawód: Student
  Numer albumu: 54321
  Kierunek studiów: Fizyka
  Średnia z laboratoriów: 4.5
  Średnia z wykładów: 4.0
  ```

### Wskazówki

- W dziedziczeniu wielopoziomowym każda klasa potomna dziedziczy wszystkie pola i metody swoich klas bazowych.
- Upewnij się, że konstruktory klas potomnych poprawnie inicjalizują pola zdefiniowane w klasach bazowych, przekazując odpowiednie wartości.

---

## Zadanie 5 - Dziedziczenie wielokrotne z klasą Ptak

**Poziom trudności**: ★★☆

### Treść zadania

Zaprojektuj następujące klasy:

1. **Klasa Zwierz** – zawierająca metody:
   - `jedz()` – wypisuje komunikat, np. "Zwierz je."
   - `spij()` – wypisuje komunikat, np. "Zwierz śpi."
   - `wydaj_dźwięk()` – wypisuje komunikat, np. "Zwierz wydaje dźwięk."

2. **Klasa ObiektLatający** – zawierająca metody:
   - `leć()` – wypisuje komunikat, np. "Obiekt latający leci."
   - `wyląduj()` – wypisuje komunikat, np. "Obiekt latający ląduje."

3. **Klasa Ptak** – dziedzicząca **wielokrotnie** po obu klasach: **Zwierz** i **ObiektLatający**.

Napisz program testujący klasę **Ptak**, który:

- Tworzy obiekt klasy **Ptak**.
- Wywołuje metody odziedziczone z obu klas bazowych.

### Dane wejściowe

- Brak danych wejściowych. Zadanie polega na implementacji klas i ich metod oraz wykorzystaniu ich w programie testującym.

### Dane wyjściowe

- Komunikaty wypisywane przez metody klasy **Ptak**, pochodzące z obu klas bazowych.

### Przykład

- **Oczekiwane wyjście**:
  ```
  Ptak je.
  Ptak śpi.
  Ptak wydaje dźwięk.
  Ptak leci.
  Ptak ląduje.
  ```

### Wskazówki

- W dziedziczeniu wielokrotnym klasa potomna dziedziczy po więcej niż jednej klasie bazowej.
- Upewnij się, że w klasie **Ptak** dostępne są wszystkie metody z klas **Zwierz** i **ObiektLatający**.
- Zwróć uwagę na ewentualne konflikty nazw metod lub pól i zastanów się, jak je rozwiązać, aby zachować poprawność programu.
