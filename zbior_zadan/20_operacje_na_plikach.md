# Rozdział: Operacje na plikach (stdin/stdout)

Poniższe zadania polegają na wczytywaniu danych ze **standardowego wejścia** (stdin) i wypisywaniu wyniku na **standardowe wyjście** (stdout).
**Każde zadanie (oraz każdy podpunkt w zadaniach wieloczęściowych) jest osobnym, niezależnym programem.**

**Konwencje wspólne:**

* Ścieżki wczytuj jako całe linie (mogą zawierać spacje).
* Rozszerzenia podawane są **z kropką**, np. `.txt`.
* Jeśli zadanie wymaga wypisania listy lub słownika — wypisz je w formacie jak w przykładach (np. `['a', 'b']`, `{ 'a': 1 }`).
* W zadaniach „modyfikujących pliki” w **wyjściu może nie być nic** — liczy się wykonana operacja (jeśli środowisko testujące to sprawdza).

---

## ZAD-01 — Czy ścieżka istnieje?

**Poziom:** ★☆☆
**Tagi:** `files`, `path`, `os`, `pathlib`

### Treść

Otrzymujesz ścieżkę w systemie plików. Sprawdź, czy odnosi się do istniejącego **pliku lub folderu**.

### Wejście

* 1 linia: `path` (napis — ścieżka)

### Wyjście

* 1 linia: `Prawda` jeśli ścieżka istnieje, w przeciwnym razie `Fałsz`

### Przykład

**Wejście:**

```
C:\Users\Username\Documents\plik.txt
```

**Wyjście:**

```
Prawda
```

---

## ZAD-02 — Pliki o danym rozszerzeniu w folderze (bez podfolderów)

**Poziom:** ★★☆
**Tagi:** `files`, `dir`, `listdir`, `pathlib`

### Treść

Otrzymujesz ścieżkę do folderu i rozszerzenie (np. `.txt`). Znajdź wszystkie pliki o tym rozszerzeniu znajdujące się **bezpośrednio** w tym folderze (bez przeszukiwania podfolderów). Zwróć listę nazw plików.

### Wejście

* 1 linia: `folder_path`
* 2 linia: `ext` (np. `.txt`)

### Wyjście

* 1 linia: lista nazw plików w formacie `['a.txt', 'b.txt']`

### Przykład

**Wejście:**

```
C:\Users\Username\Documents
.txt
```

**Wyjście:**

```
['dokument1.txt', 'notatki.txt', 'lista_zakupów.txt']
```

### Uwagi o formatowaniu

* Porównuj rozszerzenia **bez względu na wielkość liter** (np. `.TXT` też pasuje do `.txt`).

---

## ZAD-03 — Znajdź wszystkie ścieżki plików o danej nazwie (rekurencyjnie)

**Poziom:** ★★☆
**Tagi:** `files`, `walk`, `recursive`, `pathlib`

### Treść

Otrzymujesz nazwę pliku (np. `raport.docx`). Przeszukaj cały system plików i znajdź wszystkie pliki o tej nazwie. Wypisz listę pełnych ścieżek do znalezionych plików.

### Wejście

* 1 linia: `filename` (np. `raport.docx`)

### Wyjście

* 1 linia: lista pełnych ścieżek (napisy)

### Przykład

**Wejście:**

```
raport.docx
```

**Wyjście:**

```
[
  'C:\Users\Username\Documents\raport.docx',
  'D:\Projekty\Raporty\raport.docx',
  'E:\Backup\raport.docx'
]
```

### Uwagi

* W środowisku testowym możesz nie mieć uprawnień do wszystkich katalogów — program powinien to bezpiecznie obsłużyć (np. pomijać niedostępne miejsca).

---

## ZAD-04 — Wczytaj i wypisz treść pliku

**Poziom:** ★☆☆
**Tagi:** `files`, `read`, `encoding`

### Treść

Otrzymujesz ścieżkę do pliku tekstowego. Wczytaj zawartość pliku i wypisz ją.

### Wejście

* 1 linia: `file_path`

### Wyjście

* treść pliku (dokładnie taka jak w pliku)

### Przykład

**Wejście:**

```
C:\Users\Username\Documents\wiadomość.txt
```

**Wyjście:**

```
Witaj! To jest przykładowa treść pliku tekstowego.
```

---

## ZAD-05 — Posortuj adresy IP z pliku

**Poziom:** ★☆☆
**Tagi:** `files`, `sort`, `list`

### Treść

Otrzymujesz ścieżkę do pliku tekstowego, w którym w każdej linii znajduje się jeden adres IP. Wczytaj wszystkie adresy, posortuj je **alfabetycznie** i wypisz jako listę.

### Wejście

* 1 linia: `file_path`

### Wyjście

* 1 linia: lista adresów IP jako napisy, np. `['10.0.0.1', ...]`

### Przykład

**Wejście:**

```
C:\Users\Username\Documents\adresy_ip.txt
```

**Wyjście:**

```
['10.0.0.1', '172.16.0.5', '192.168.1.10', '192.168.1.2']
```

---

## ZAD-06 — Statystyki pliku tekstowego

**Poziom:** ★★☆
**Tagi:** `files`, `stats`, `dict`, `regex`

### Treść

Otrzymujesz ścieżkę do pliku tekstowego. Oblicz:

a) liczbę wierszy,
b) łączną liczbę słów (słowa = ciągi liter),
c) średnią długość wiersza (w znakach),
d) średnią liczbę słów na wiersz,
e) częstość występowania słów (słownik).

### Wejście

* 1 linia: `file_path`

### Wyjście

5 elementów w tej kolejności:

1. liczba wierszy
2. liczba słów
3. średnia długość wiersza
4. średnia liczba słów na wiersz
5. słownik częstości słów

Każdy element wypisz w osobnej linii.

### Przykład

**Wejście:**

```
C:\Users\Username\Documents\tekst.txt
```

**Wyjście:**

```
4
12
17.75
3.0
{'ala': 2, 'ma': 2, 'kota': 1, 'kot': 1, 'na': 1, 'imię': 1, 'filemon': 1, 'filemona': 1, 'lubi': 2, 'mleko': 1}
```

### Uwagi o formatowaniu

* Jeżeli ujednolicisz wielkość liter — w słowniku używaj małych liter (jak w przykładzie).
* Interpunkcję traktuj jako separator (usuń ją przy wyznaczaniu słów).

---

## ZAD-07 — Dodaj wiersz na początku pliku

**Poziom:** ★☆☆
**Tagi:** `files`, `write`, `prepend`

### Treść

Otrzymujesz ścieżkę do pliku tekstowego i wiersz tekstu. Dodaj ten wiersz na **początku** pliku.

### Wejście

* 1 linia: `file_path`
* 2 linia: `line_to_add` (może zawierać spacje)

### Wyjście

Brak.

### Przykład

**Wejście:**

```
C:\Users\Username\Documents\notatki.txt
To jest nowy wiersz dodany na początku pliku.
```

**Wyjście:**
*(brak)*

---

## ZAD-08 — Modyfikacja plików spełniających warunek (rekurencyjnie)

**Poziom:** ★★☆
**Tagi:** `files`, `recursive`, `txt`, `csv`

### Treść

Otrzymujesz ścieżkę do folderu. Wykonaj:

a) dopisz swoje inicjały na końcu każdego pliku `.txt` w folderze i podfolderach,
b) usuń **środkowy wiersz** z każdego pliku `.csv` w folderze i podfolderach
(jeśli liczba wierszy jest parzysta — usuń **dolny z dwóch środkowych**).

### Wejście

* 1 linia: `folder_path`

### Wyjście

Brak.

### Przykład

**Wejście:**

```
C:\Users\Username\Documents\Projekt
```

**Wyjście:**
*(brak)*

---

## ZAD-09 — Usuń pliki większe niż 10 kB (rekurencyjnie)

**Poziom:** ★★☆
**Tagi:** `files`, `delete`, `size`, `recursive`

### Treść

Otrzymujesz ścieżkę do folderu. Usuń wszystkie pliki o rozmiarze **> 10240 bajtów** w tym folderze i jego podfolderach.

### Wejście

* 1 linia: `folder_path`

### Wyjście

Brak.

### Przykład

**Wejście:**

```
C:\Users\Username\Documents\DoUsunięcia
```

**Wyjście:**
*(brak)*

---

## ZAD-10 — Skopiuj pliki PNG do innego folderu (bez podfolderów)

**Poziom:** ★☆☆
**Tagi:** `files`, `copy`, `png`, `shutil`

### Treść

Otrzymujesz ścieżkę folderu źródłowego i docelowego. Skopiuj wszystkie pliki `.png` znajdujące się **bezpośrednio** w folderze źródłowym do folderu docelowego.

### Wejście

* 1 linia: `src_folder`
* 2 linia: `dst_folder`

### Wyjście

Brak.

### Przykład

**Wejście:**

```
C:\Users\Username\Obrazy
D:\Backup\Obrazy
```

**Wyjście:**
*(brak)*

---

## ZAD-11 — Zamień miejscami treści dwóch plików

**Poziom:** ★★☆
**Tagi:** `files`, `swap`, `read/write`

### Treść

Otrzymujesz ścieżki do dwóch plików. Zamień ich treści miejscami:

* plik A ma mieć dawną treść pliku B,
* plik B ma mieć dawną treść pliku A.

### Wejście

* 1 linia: `file_A`
* 2 linia: `file_B`

### Wyjście

Brak.

### Przykład

**Wejście:**

```
C:\Users\Username\Documents\plik1.txt
C:\Users\Username\Documents\plik2.txt
```

**Wyjście:**
*(brak)*

---

## ZAD-12 — Przenieś wszystkie pliki CSV do jednego folderu (rekurencyjnie)

**Poziom:** ★★☆
**Tagi:** `files`, `move`, `csv`, `recursive`

### Treść

Otrzymujesz ścieżkę folderu źródłowego i docelowego. Przenieś wszystkie pliki `.csv` z folderu źródłowego **i wszystkich jego podfolderów** do folderu docelowego.

### Wejście

* 1 linia: `src_folder`
* 2 linia: `dst_folder`

### Wyjście

Brak.

### Przykład

**Wejście:**

```
C:\Users\Username\Projekty
D:\Dane\CSV
```

**Wyjście:**
*(brak)*

### Uwagi

* Jeśli w folderze docelowym istnieje już plik o tej samej nazwie, zadanie wymaga zdefiniowania zachowania (np. zmiana nazwy / pominięcie) — jeśli sprawdzarka tego nie doprecyzowuje, przyjmij jedną spójną strategię w całym rozwiązaniu.
