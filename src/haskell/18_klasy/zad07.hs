{-
ZAD-07 — Zliczanie instancji klasy

\**Poziom:** ★☆☆
\**Tagi:** `class`, `static`

### Treść

Zaprojektuj klasę **MojaKlasa**, która zlicza ile instancji utworzono:

\* prywatne pole statyczne licznik,
\* konstruktor zwiększa licznik,
\* metoda statyczna zwraca licznik.

Program tworzy np. 3 obiekty i wypisuje liczbę instancji.

### Wejście

Brak.

### Wyjście

Jedna linia.

### Przykład

\**Wyjście:**

```
Liczba utworzonych instancji: 3
```

-}

import Data.IORef

-- W Haskell używamy IORef do zliczania instancji
-- Złożoność pamięciowa: O(1)
data MojaKlasa = MojaKlasa {id :: Int}

main :: IO ()
main = do
  -- Symulacja zliczania instancji
  licznik <- newIORef 0

  -- Tworzenie instancji
  modifyIORef licznik (+ 1)
  let obj1 = MojaKlasa 1

  modifyIORef licznik (+ 1)
  let obj2 = MojaKlasa 2

  modifyIORef licznik (+ 1)
  let obj3 = MojaKlasa 3

  count <- readIORef licznik
  putStrLn $ "Liczba utworzonych instancji: " ++ show count
