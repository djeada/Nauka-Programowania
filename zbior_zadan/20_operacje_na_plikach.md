## Operacje na plikach

### Zad 1. (★☆☆)

Tytuł: Sprawdzenie, czy ścieżka należy do pliku/folderu

Treść: Otrzymujesz napis reprezentujący ścieżkę. Sprawdź, czy jest to ścieżka do pliku lub folderu.

Dane wejściowe: Napis

Dane wyjściowe: Wartość logiczna

### Zad 2. (★★☆)

Tytuł: Znalezienie w folderze wszystkich plików z danym rozszerzeniem

Treść: Otrzymujesz dwa napisy. Pierwszy napis to ścieżka folderu, a drugi to rozszerzenie szukanych plików. Znajdź w folderze wszystkie pliki o podanym rozszerzeniu i zapisz ich nazwy w liście.

Dane wejściowe: Dwa napisy

Dane wyjściowe: Lista napisów

### Zad 3. (★★☆)

Tytuł: Znalezienie ścieżki pliku o danej nazwie

Treść: Otrzymujesz napis reprezentujący nazwę pliku. Przeszukaj cały system i zapisz w liście wszystkie ścieżki plików o podanej nazwie.

Dane wejściowe: Napis

Dane wyjściowe: Lista napisów

### Zad 4. (★☆☆)

Tytuł: Wczytaj i wypisz treść pliku.

Treść zadania: Otrzymujesz napis reprezentujący ścieżkę do pliku tekstowego. Wczytaj plik i wypisz jego treść.

Dane wejściowe: Napis reprezentujący ścieżkę do pliku.

Dane wyjściowe: Napis zawierający treść pliku.

### Zad 5. (★☆☆)

Tytuł: Plik z listą adresów IP.

Treść zadania: Otrzymujesz napis reprezentujący ścieżkę do pliku tekstowego. Każdy wiersz pliku reprezentuje adres IP. Posortuj adresy IP i zapisz je w liście.

Dane wejściowe: Napis reprezentujący ścieżkę do pliku.

Dane wyjściowe: Lista adresów IP posortowanych alfabetycznie.

### Zad 6. (★★☆)

Tytuł: Statystyki dla pliku tekstowego.

Treść zadania: Otrzymujesz napis reprezentujący ścieżkę do pliku tekstowego. Oblicz:

a) Liczbę wierszy w pliku.

b) Liczbę słów w pliku (słowa oddzielone są spacjami i mogą składać się wyłącznie z liter).

c) Średnią długość wiersza.

d) Średnią liczbę słów na wiersz.

e) Częstość występowania każdego ze słów w pliku.

Dane wejściowe: Napis reprezentujący ścieżkę do pliku.

Dane wyjściowe:

a) Liczba naturalna reprezentująca liczbę wierszy.

b) Liczba naturalna reprezentująca liczbę słów.

c) Liczba zmiennoprzecinkowa reprezentująca średnią długość wiersza.

d) Liczba zmiennoprzecinkowa reprezentująca średnią liczbę słów na wiersz.

e) Słownik par: napis (słowo), liczba naturalna (częstotliwość występowania słowa). 

Przykład:

Dla otrzymanego napisu: "C:\Users\Username\Documents\text_file.txt" powinno zostać zwrócone:

a) Liczba naturalna reprezentująca liczbę wierszy, np. 6

b) Liczba naturalna reprezentująca liczbę słów, np. 25

c) Liczba zmiennoprzecinkowa reprezentująca średnią długość wiersza, np. 41.5

d) Liczba zmiennoprzecinkowa reprezentująca średnią liczbę słów na wiersz, np. 4.2

e) Słownik par: napis (słowo), liczba naturalna (częstotliwość występowania słowa): {'The': 2, 'quick': 2, 'brown': 2, 'fox': 2, 'jumped': 1, 'over': 1, 'the': 1, 'lazy': 1, 'dog.': 1, 'cat': 1, 'sat': 1, 'on': 1, 'mat.': 1, 'Foxes': 1, 'are': 1, 'known': 1, 'for': 1, 'their': 2, 'cunning': 1, 'and': 1, 'intelligence.': 1, 'Dogs': 1, 'loyalty': 1, 'kindness.': 1, 'Cats': 1, 'independent': 1, 'animals': 1, 'but': 1, 'can': 1, 'be': 1, 'affectionate.': 1, 'This': 1, 'text': 1, 'file': 1, 'contains': 1, 'ten': 1, 'lines': 1, 'and': 1, 'words.': 1}

Tekst pliku:

The quick brown fox jumped over the lazy dog.
The quick brown cat sat on the mat.
Foxes are known for their cunning and intelligence.
Dogs are known for their loyalty and kindness.
Cats are independent animals but can be affectionate.
This text file contains six lines and 25 words.

### Zad 7. (★☆☆)

Tytuł: Dodaj wiersz do pliku.

Treść zadania: Otrzymujesz dwa napisy. Pierwszy napis reprezentuje ścieżkę do pliku tekstowego, a drugi napis reprezentuje wiersz tekstu. Dodaj otrzymany wiersz na początek pliku tekstowego.

Dane wejściowe: Dwa napisy - ścieżka do pliku oraz wiersz tekstu.

Dane wyjściowe: Brak.

### Zad 8. (★★☆)

Tytuł: Znajdź i zmodyfikuj pliki spełniające warunek.

Treść zadania: Otrzymujesz napis reprezentujący ścieżkę do folderu.

a) Dodaj swoje inicjały na końcu wszystkich plików tekstowych znajdujących się w podanym folderze i jego podfolderach.

b) Usuń środkowy wiersz z każdego pliku CSV znajdującego się w podanym folderze i jego podfolderach.

Dane wejściowe: Napis reprezentujący ścieżkę do folderu.

Dane wyjściowe: Brak.

### Zad 9. (★★☆)

Tytuł: Usuń pliki spełniające warunek.

Treść zadania: Otrzymujesz napis reprezentujący ścieżkę do folderu. Usuń wszystkie pliki o rozmiarze większym niż 10 kB znajdujące się w podanym folderze i jego podfolderach.

Dane wejściowe: Napis reprezentujący ścieżkę do folderu.

Dane wyjściowe: Brak.

### Zad 10. (★☆☆)

Tytuł: Skopiuj pliki.

Treść zadania: Otrzymujesz dwa napisy reprezentujące ścieżki do folderów. Skopiuj wszystkie pliki PNG z pierwszego folderu do drugiego folderu.

Dane wejściowe: Dwa napisy reprezentujące ścieżki do folderów.

Dane wyjściowe: Brak.

### Zad 11.  (★★☆)

Tytuł: Podmień treści plików.

Treść zadania: Otrzymujesz dwa napisy reprezentujące ścieżki do plików. Podmień treści obu plików.

Dane wejściowe: Dwa napisy reprezentujące ścieżki do plików.

Dane wyjściowe: Brak.

### Zad 12. (★★☆)

Tytuł: Przesuń wszystkie pliki CSV do jednego folderu.

Treść zadania: Otrzymujesz dwa napisy reprezentujące ścieżki do folderów. Przenieś wszystkie pliki CSV z pierwszego folderu (oraz jego podfolderów) do drugiego folderu.

Dane wejściowe: Dwa napisy reprezentujące ścieżki do folderów.

Dane wyjściowe: Brak.
