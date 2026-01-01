{-
ZAD-04 — Usuń pary ze słownika na podstawie wartości

\**Poziom:** ★☆☆
\**Tagi:** `dict`, `filtrowanie`

### Treść

Wczytaj słownik (`n` par: klucz-napis, wartość-liczba) oraz liczbę `k`. Usuń wszystkie pary, gdzie wartość == `k`. Wypisz wynikowy słownik.

### Wejście

\* 1 linia: `n`
\* następnie `n` linii: `klucz wartość`
\* ostatnia linia: `k`

### Wyjście

\* Słownik po usunięciu par

### Przykład

\**Wejście:**

```
4
aaa 5
abc 1
xxx 5
cba 3
5
```

\**Wyjście:**

```
{'abc': 1, 'cba': 3}
```

-}

import Data.Map (Map)
import qualified Data.Map as Map

-- Filtrowanie słownika
-- Złożoność czasowa: O(n)
-- Złożoność pamięciowa: O(n)
main :: IO ()
main = do
    putStrLn "Placeholder - filtrowanie słownika"
