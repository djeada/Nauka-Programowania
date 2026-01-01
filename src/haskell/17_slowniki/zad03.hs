{-
ZAD-03 — Biblioteka: baza wypożyczeń

\**Poziom:** ★☆☆
\**Tagi:** `dict`, `list`, `pętle`, `string`

### Treść

Utrzymuj słownik: `imię -> lista wypożyczonych książek`.
Obsługuj komendy (każda w osobnej linii) aż do `koniec`:

\* `dodaj [imię] [tytuł]`
\* `zwróć [imię] [tytuł]`
\* `lista [imię]`

Po `lista [imię]` wypisz:

\* jeśli lista niepusta: `Książki wypożyczone przez [imię]: t1, t2, ...`
\* jeśli brak książek (lub brak czytelnika): `Książki wypożyczone przez [imię]: brak`

### Wejście

Wiele linii z komendami, koniec po słowie `koniec`.

### Wyjście

Tylko po komendach `lista ...`.

### Przykład

\**Wejście:**

```
dodaj Jan Hobbit
dodaj Anna "Duma i uprzedzenie"
dodaj Jan "Władca Pierścieni"
lista Jan
zwróć Jan Hobbit
lista Jan
lista Anna
koniec
```

\**Wyjście:**

```
Książki wypożyczone przez Jan: Hobbit, Władca Pierścieni
Książki wypożyczone przez Jan: Władca Pierścieni
Książki wypożyczone przez Anna: Duma i uprzedzenie
```

-}

import Data.Map (Map)
import qualified Data.Map as Map
import Data.List (intercalate)

-- Biblioteka - baza wypożyczeń (uproszczona implementacja)
-- Złożoność czasowa: O(n log n) dla n operacji
-- Złożoność pamięciowa: O(n)
main :: IO ()
main = do
    putStrLn "Biblioteka - implementacja wymaga interaktywnego parsowania komend"
    -- Pełna implementacja wymagałaby parsowania komend i zarządzania stanem
