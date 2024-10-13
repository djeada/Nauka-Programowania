# Operacje na plikach

## Zadanie 1 - Sprawdzenie, czy ścieżka należy do pliku lub folderu

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz napis reprezentujący ścieżkę w systemie plików. Twoim zadaniem jest sprawdzić, czy podana ścieżka odnosi się do istniejącego pliku lub folderu.

### Dane wejściowe

- Jeden napis reprezentujący ścieżkę w systemie plików.

### Dane wyjściowe

- Wartość logiczna:
  - **Prawda**, jeśli ścieżka odnosi się do istniejącego pliku lub folderu.
  - **Fałsz**, jeśli ścieżka nie odnosi się do żadnego istniejącego pliku ani folderu.

### Przykład

- **Dane wejściowe**:
  ```
  C:\Users\Username\Documents\plik.txt
  ```
- **Oczekiwane wyjście**:
  ```
  Prawda
  ```

### Wskazówki

- Sprawdź, czy ścieżka istnieje w systemie plików.
- Upewnij się, że obsługujesz zarówno ścieżki do plików, jak i do folderów.

---

## Zadanie 2 - Znalezienie wszystkich plików z danym rozszerzeniem w folderze

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz dwa napisy:

1. Ścieżka do folderu.
2. Rozszerzenie plików do wyszukania (np. `.txt`, `.jpg`).

Twoim zadaniem jest znaleźć w podanym folderze wszystkie pliki o podanym rozszerzeniu i zwrócić ich nazwy w postaci listy.

### Dane wejściowe

- Dwa napisy:
  1. Ścieżka do folderu.
  2. Rozszerzenie plików do wyszukania (wraz z kropką, np. `.txt`).

### Dane wyjściowe

- Lista napisów zawierająca nazwy plików z podanym rozszerzeniem znajdujących się w podanym folderze.

### Przykład

- **Dane wejściowe**:
  ```
  C:\Users\Username\Documents
  .txt
  ```
- **Oczekiwane wyjście**:
  ```
  ['dokument1.txt', 'notatki.txt', 'lista_zakupów.txt']
  ```

### Wskazówki

- Przeszukaj tylko bezpośrednie zawartości podanego folderu (nie uwzględniaj podfolderów).
- Upewnij się, że porównujesz rozszerzenia plików w sposób niezależny od wielkości liter.

---

## Zadanie 3 - Znalezienie ścieżek plików o danej nazwie

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz napis reprezentujący nazwę pliku (np. `raport.docx`). Twoim zadaniem jest przeszukać cały system plików i znaleźć wszystkie pliki o podanej nazwie. Zwróć listę pełnych ścieżek do tych plików.

### Dane wejściowe

- Jeden napis reprezentujący nazwę pliku do wyszukania.

### Dane wyjściowe

- Lista napisów zawierająca pełne ścieżki do wszystkich plików o podanej nazwie.

### Przykład

- **Dane wejściowe**:
  ```
  raport.docx
  ```
- **Oczekiwane wyjście**:
  ```
  [
    'C:\Users\Username\Documents\raport.docx',
    'D:\Projekty\Raporty\raport.docx',
    'E:\Backup\raport.docx'
  ]
  ```

### Wskazówki

- Przeszukaj wszystkie dyski i foldery dostępne w systemie.
- Upewnij się, że masz odpowiednie uprawnienia do odczytu poszczególnych folderów.

---

## Zadanie 4 - Wczytaj i wypisz treść pliku

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz napis reprezentujący ścieżkę do pliku tekstowego. Twoim zadaniem jest wczytać zawartość tego pliku i wypisać jego treść.

### Dane wejściowe

- Jeden napis reprezentujący ścieżkę do pliku tekstowego.

### Dane wyjściowe

- Napis zawierający treść pliku.

### Przykład

- **Dane wejściowe**:
  ```
  C:\Users\Username\Documents\wiadomość.txt
  ```
- **Oczekiwane wyjście**:
  ```
  Witaj! To jest przykładowa treść pliku tekstowego.
  ```

### Wskazówki

- Upewnij się, że plik istnieje i masz do niego dostęp.
- Zadbaj o poprawne kodowanie znaków podczas wczytywania pliku.

---

## Zadanie 5 - Posortuj adresy IP z pliku

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz napis reprezentujący ścieżkę do pliku tekstowego. Plik zawiera w każdym wierszu jeden adres IP. Twoim zadaniem jest wczytać adresy IP z pliku, posortować je alfabetycznie i zwrócić w postaci listy.

### Dane wejściowe

- Jeden napis reprezentujący ścieżkę do pliku tekstowego.

### Dane wyjściowe

- Lista napisów zawierająca posortowane alfabetycznie adresy IP.

### Przykład

- **Dane wejściowe**:
  ```
  C:\Users\Username\Documents\adresy_ip.txt
  ```
- **Plik "adresy_ip.txt" zawiera**:
  ```
  192.168.1.10
  10.0.0.1
  172.16.0.5
  192.168.1.2
  ```
- **Oczekiwane wyjście**:
  ```
  ['10.0.0.1', '172.16.0.5', '192.168.1.10', '192.168.1.2']
  ```

### Wskazówki

- Pamiętaj, że alfabetyczne sortowanie adresów IP może nie odpowiadać ich kolejności numerycznej.
- Jeśli chcesz sortować adresy IP według wartości numerycznych, rozważ podział adresów na oktety i porównywanie ich jako liczb.

---

## Zadanie 6 - Statystyki dla pliku tekstowego

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz napis reprezentujący ścieżkę do pliku tekstowego. Twoim zadaniem jest obliczyć następujące statystyki dla tego pliku:

a) Liczbę wierszy w pliku.

b) Łączną liczbę słów w pliku (słowa są oddzielone spacjami i składają się wyłącznie z liter).

c) Średnią długość wiersza (liczbę znaków na wiersz).

d) Średnią liczbę słów na wiersz.

e) Częstotliwość występowania każdego słowa w pliku (w formie słownika).

### Dane wejściowe

- Jeden napis reprezentujący ścieżkę do pliku tekstowego.

### Dane wyjściowe

- a) Liczba naturalna — liczba wierszy w pliku.
- b) Liczba naturalna — łączna liczba słów w pliku.
- c) Liczba zmiennoprzecinkowa — średnia długość wiersza (w znakach).
- d) Liczba zmiennoprzecinkowa — średnia liczba słów na wiersz.
- e) Słownik, w którym kluczami są słowa (napisy), a wartościami liczby naturalne reprezentujące częstotliwość występowania słów.

### Przykład

- **Dane wejściowe**:
  ```
  C:\Users\Username\Documents\tekst.txt
  ```
- **Zawartość pliku "tekst.txt"**:
  ```
  Ala ma kota.
  Kot ma na imię Filemon.
  Filemon lubi mleko.
  Ala lubi Filemona.
  ```
- **Oczekiwane wyjście**:

  a) Liczba wierszy: `4`

  b) Liczba słów: `12`

  c) Średnia długość wiersza: `17.75`

  d) Średnia liczba słów na wiersz: `3.0`

  e) Częstotliwość słów:
  ```
  {
    'Ala': 2,
    'ma': 2,
    'kota': 1,
    'Kot': 1,
    'na': 1,
    'imię': 1,
    'Filemon': 1,
    'Filemona': 1,
    'lubi': 2,
    'mleko': 1
  }
  ```

### Wskazówki

- Przy liczeniu słów usuń znaki interpunkcyjne i zamień tekst na małe litery, jeśli chcesz traktować słowa jednolicie.
- Możesz użyć funkcji do podziału tekstu na słowa, takich jak `split()`.
- Zadbaj o to, by słowa były traktowane identycznie bez względu na wielkość liter (jeśli to wymagane).

---

## Zadanie 7 - Dodaj wiersz na początku pliku

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz dwa napisy:

1. Ścieżka do pliku tekstowego.
2. Wiersz tekstu do dodania.

Twoim zadaniem jest dodać podany wiersz na początku pliku tekstowego.

### Dane wejściowe

- Dwa napisy:
  1. Ścieżka do pliku tekstowego.
  2. Wiersz tekstu do dodania.

### Dane wyjściowe

- Brak (zmodyfikuj plik zgodnie z poleceniem).

### Przykład

- **Dane wejściowe**:
  ```
  C:\Users\Username\Documents\notatki.txt
  ```
  ```
  To jest nowy wiersz dodany na początku pliku.
  ```
- **Operacja**:
  - Dodaj podany wiersz na początku pliku "notatki.txt".

### Wskazówki

- Pamiętaj, że musisz przesunąć istniejącą treść pliku, aby zrobić miejsce na nowy wiersz.
- Upewnij się, że zachowujesz formatowanie pliku, np. dodając znak nowej linii po dodanym wierszu.

---

## Zadanie 8 - Modyfikacja plików spełniających warunek

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz napis reprezentujący ścieżkę do folderu. Wykonaj następujące operacje:

a) Dodaj swoje inicjały na końcu wszystkich plików tekstowych (`.txt`) znajdujących się w podanym folderze oraz we wszystkich jego podfolderach.

b) Usuń środkowy wiersz z każdego pliku CSV (`.csv`) znajdującego się w podanym folderze oraz we wszystkich jego podfolderach.

### Dane wejściowe

- Jeden napis reprezentujący ścieżkę do folderu.

### Dane wyjściowe

- Brak (zmodyfikuj pliki zgodnie z poleceniem).

### Przykład

- **Dane wejściowe**:
  ```
  C:\Users\Username\Documents\Projekt
  ```

- **Operacje**:
  - a) Dodaj swoje inicjały (np. "AB") na końcu każdego pliku `.txt` w folderze "Projekt" i jego podfolderach.
  - b) W każdym pliku `.csv` w folderze "Projekt" i jego podfolderach usuń wiersz znajdujący się w środku pliku.

### Wskazówki

- Przeszukaj folder rekurencyjnie, aby uwzględnić wszystkie podfoldery.
- Przy usuwaniu środkowego wiersza, jeśli plik ma parzystą liczbę wierszy, usuń dolny z dwóch środkowych wierszy.
- Upewnij się, że masz uprawnienia do modyfikacji plików.

---

## Zadanie 9 - Usuń pliki większe niż 10 kB

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz napis reprezentujący ścieżkę do folderu. Twoim zadaniem jest usunąć wszystkie pliki o rozmiarze większym niż 10 kilobajtów (10 240 bajtów), znajdujące się w podanym folderze oraz we wszystkich jego podfolderach.

### Dane wejściowe

- Jeden napis reprezentujący ścieżkę do folderu.

### Dane wyjściowe

- Brak (usuń pliki zgodnie z poleceniem).

### Przykład

- **Dane wejściowe**:
  ```
  C:\Users\Username\Documents\DoUsunięcia
  ```

- **Operacja**:
  - Usuń wszystkie pliki większe niż 10 kB w folderze "DoUsunięcia" i jego podfolderach.

### Wskazówki

- Przeszukaj folder rekurencyjnie, aby uwzględnić wszystkie podfoldery.
- Upewnij się, że masz uprawnienia do usuwania plików.
- Zachowaj ostrożność, aby nie usunąć plików, których nie powinieneś usuwać.

---

## Zadanie 10 - Skopiuj pliki PNG do innego folderu

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz dwa napisy:

1. Ścieżka do folderu źródłowego.
2. Ścieżka do folderu docelowego.

Twoim zadaniem jest skopiować wszystkie pliki z rozszerzeniem `.png` z folderu źródłowego do folderu docelowego.

### Dane wejściowe

- Dwa napisy:
  1. Ścieżka do folderu źródłowego.
  2. Ścieżka do folderu docelowego.

### Dane wyjściowe

- Brak (skopiuj pliki zgodnie z poleceniem).

### Przykład

- **Dane wejściowe**:
  ```
  Źródło: C:\Users\Username\Obrazy
  Cel: D:\Backup\Obrazy
  ```

- **Operacja**:
  - Skopiuj wszystkie pliki `.png` z folderu "Obrazy" do folderu "D:\Backup\Obrazy".

### Wskazówki

- Upewnij się, że folder docelowy istnieje lub obsłuż sytuację, gdy nie istnieje.
- Skopiuj tylko pliki z rozszerzeniem `.png` znajdujące się bezpośrednio w folderze źródłowym (nie uwzględniaj podfolderów, chyba że jest to wymagane).

---

## Zadanie 11 - Podmień treści plików

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz dwa napisy reprezentujące ścieżki do dwóch plików. Twoim zadaniem jest zamienić miejscami treści tych plików, tak aby:

- Plik A zawierał pierwotną treść pliku B.
- Plik B zawierał pierwotną treść pliku A.

### Dane wejściowe

- Dwa napisy:
  1. Ścieżka do pliku A.
  2. Ścieżka do pliku B.

### Dane wyjściowe

- Brak (zmodyfikuj pliki zgodnie z poleceniem).

### Przykład

- **Dane wejściowe**:
  ```
  Plik A: C:\Users\Username\Documents\plik1.txt
  Plik B: C:\Users\Username\Documents\plik2.txt
  ```

- **Operacja**:
  - Zamień treści plików "plik1.txt" i "plik2.txt".

### Wskazówki

- Możesz użyć tymczasowego pliku lub zmiennej do przechowania treści jednego z plików podczas zamiany.
- Upewnij się, że zachowujesz uprawnienia i atrybuty plików po modyfikacji.

---

## Zadanie 12 - Przenieś wszystkie pliki CSV do jednego folderu

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz dwa napisy:

1. Ścieżka do folderu źródłowego.
2. Ścieżka do folderu docelowego.

Twoim zadaniem jest przenieść wszystkie pliki z rozszerzeniem `.csv` z folderu źródłowego oraz wszystkich jego podfolderów do folderu docelowego.

### Dane wejściowe

- Dwa napisy:
  1. Ścieżka do folderu źródłowego.
  2. Ścieżka do folderu docelowego.

### Dane wyjściowe

- Brak (przenieś pliki zgodnie z poleceniem).

### Przykład

- **Dane wejściowe**:
  ```
  Źródło: C:\Users\Username\Projekty
  Cel: D:\Dane\CSV
  ```

- **Operacja**:
  - Przenieś wszystkie pliki `.csv` z folderu "Projekty" i jego podfolderów do folderu "D:\Dane\CSV".

### Wskazówki

- Upewnij się, że podczas przenoszenia plików nie dojdzie do konfliktu nazw plików.
- Jeśli plik o tej samej nazwie już istnieje w folderze docelowym, rozważ zmianę nazwy pliku lub pomiń go.
- Pamiętaj o przenoszeniu, a nie kopiowaniu plików.
