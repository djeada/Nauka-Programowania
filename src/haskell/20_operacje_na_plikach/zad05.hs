{-
ZAD-05 — Posortuj adresy IP z pliku

\**Poziom:** ★☆☆
\**Tagi:** `files`, `sort`, `list`

### Treść

Otrzymujesz ścieżkę do pliku tekstowego, w którym w każdej linii znajduje się jeden adres IP. Wczytaj wszystkie adresy, posortuj je **alfabetycznie** i wypisz jako listę.

### Wejście

\* 1 linia: `file_path`

### Wyjście

\* 1 linia: lista adresów IP jako napisy, np. `['10.0.0.1', ...]`

### Przykład

\**Wejście:**

```
C:\Users\Username\Documents\adresy_ip.txt
```

\**Wyjście:**

```
['10.0.0.1', '172.16.0.5', '192.168.1.10', '192.168.1.2']
```

-}

import Control.Exception (IOException, catch)
import Data.List (sort)
import System.IO (readFile)

-- Sortuje adresy IP z pliku
-- Złożoność czasowa: O(n log n), gdzie n to liczba adresów
-- Złożoność pamięciowa: O(n)
main :: IO ()
main = do
  filePath <- getLine
  contents <-
    catch
      (readFile filePath)
      ( \e -> do
          let _ = (e :: IOException)
          return ""
      )
  let ips = lines contents
  let sorted = sort ips
  print sorted
