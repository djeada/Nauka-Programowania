{-
ZAD-03 — Znajdź wszystkie ścieżki plików o danej nazwie (rekurencyjnie)

\**Poziom:** ★★☆
\**Tagi:** `files`, `walk`, `recursive`, `pathlib`

### Treść

Otrzymujesz nazwę pliku (np. `raport.docx`). Przeszukaj cały system plików i znajdź wszystkie pliki o tej nazwie. Wypisz listę pełnych ścieżek do znalezionych plików.

### Wejście

\* 1 linia: `filename` (np. `raport.docx`)

### Wyjście

\* 1 linia: lista pełnych ścieżek (napisy)

### Przykład

\**Wejście:**

```
raport.docx
```

\**Wyjście:**

```
[
  'C:\Users\Username\Documents\raport.docx',
  'D:\Projekty\Raporty\raport.docx',
  'E:\Backup\raport.docx'
]
```

### Uwagi

\* W środowisku testowym możesz nie mieć uprawnień do wszystkich katalogów — program powinien to bezpiecznie obsłużyć (np. pomijać niedostępne miejsca).

-}
main :: IO ()
main = pure ()
