{-
ZAD-11 — Palindrom w systemie binarnym

\**Poziom:** ★★☆
\**Tagi:** `binarne`, `palindrom`, `string`

### Treść

Wczytaj liczbę naturalną `n`. Sprawdź, czy jej reprezentacja binarna (bez wiodących zer) jest palindromem.

Wypisz:

\* `Prawda` — jeśli tak,
\* `Fałsz` — jeśli nie.

### Wejście

\* 1. linia: `n`

### Wyjście

Jedno słowo: `Prawda` lub `Fałsz`.

### Przykład

\**Wejście:**

```
26
```

\**Wyjście:**

```
Fałsz
```

### Uwagi (ważne)

\* `26` ma zapis binarny `11010`, który **nie** jest palindromem.
  (W Twoim wcześniejszym przykładzie było to opisane błędnie — tu trzymamy się definicji palindromu 1:1.)

-}

import Data.Bits (complement, xor)

-- Uzupełnienie do jedynki i dwójki
-- Złożoność czasowa: O(1)
-- Złożoność pamięciowa: O(1)
main :: IO ()
main = do
    n <- readLn :: IO Int
    let onesComplement = complement n
    let twosComplement = onesComplement + 1
    putStrLn $ "Ones complement: " ++ show onesComplement
    putStrLn $ "Twos complement: " ++ show twosComplement
