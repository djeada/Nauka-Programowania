{-
ZAD-11 — Sortowanie „słownika” po kluczach i po wartościach

\**Poziom:** ★☆☆
\**Tagi:** `sort`, `dict`

### Treść

Wczytaj `n` par `klucz wartość`.
a) Wypisz listę par posortowaną rosnąco po kluczach.
b) Wypisz listę par posortowaną rosnąco po wartościach.

### Wejście

\* 1 linia: `n`
\* następnie `n` linii: `klucz wartość`

### Wyjście

\* 1 linia: lista par dla a)
\* 2 linia: lista par dla b)

### Przykład

\**Wejście:**

```
4
c 3
x 5
a -2
b 4
```

\**Wyjście:**

```
[('a', -2), ('b', 4), ('c', 3), ('x', 5)]
[('a', -2), ('c', 3), ('b', 4), ('x', 5)]
```

-}

import Data.Map (Map)
import qualified Data.Map as Map

-- Transpozycja słownika list
-- Złożoność czasowa: O(n * m)
-- Złożoność pamięciowa: O(n * m)
main :: IO ()
main = do
  putStrLn "Placeholder - transpozycja słownika list"
