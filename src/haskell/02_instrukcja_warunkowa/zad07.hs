{-
ZAD-07 — Prawa logiki (p i q)

\**Poziom:** ★★☆
\**Tagi:** `bool`, `logika`, `tabele prawdy`, `formatowanie`

### Treść

Dla wszystkich kombinacji wartości logicznych `p` i `q` (True/False) sprawdź poprawność praw:

1. Wyłączony środek: `p OR (NOT p)`
2. Niesprzeczność: `NOT (p AND (NOT p))`
3. Przemienność AND: `p AND q` vs `q AND p`
4. Przemienność OR: `p OR q` vs `q OR p`
5. De Morgana 1: `NOT (p AND q)` vs `(NOT p) OR (NOT q)`
6. De Morgana 2: `NOT (p OR q)` vs `(NOT p) AND (NOT q)`

### Wejście

Brak.

### Wyjście

Żeby wynik był **jednoznaczny i łatwy do sprawdzenia**, zastosuj dokładnie ten format:

Dla każdego z 6 praw wypisz:

\* nazwę prawa w jednej linii,
\* następnie w osobnych liniach wynik dla każdej kombinacji `p, q` w kolejności:

  1. `p=False, q=False`
  2. `p=False, q=True`
  3. `p=True, q=False`
  4. `p=True, q=True`

Każda linia kombinacji ma mieć format:
`p=<...> q=<...> L=<...> R=<...> EQ=<...>`

Gdzie `<...>` to dosłownie `True` albo `False`.

### Przykład fragmentu (dla jednego prawa)

```
Przemienność alternatywy:
p=False q=False L=False R=False EQ=True
p=False q=True L=True R=True EQ=True
p=True q=False L=True R=True EQ=True
p=True q=True L=True R=True EQ=True
```

### Uwagi o formatowaniu

\* Dokładne nazwy praw (nagłówki) użyj jak poniżej:

  1. `Prawo wyłączonego środka:`
  2. `Prawo niesprzeczności:`
  3. `Przemienność koniunkcji:`
  4. `Przemienność alternatywy:`
  5. `Pierwsze prawo de Morgana:`
  6. `Drugie prawo de Morgana:`
\* Między blokami praw możesz wstawić **jedną pustą linię** (zalecane), ale nie więcej.

-}
main :: IO ()
main = do
  -- Law 1: Excluded Middle - p OR (NOT p)
  putStrLn "Prawo wyłączonego środka:"
  printLaw1 False False
  printLaw1 False True
  printLaw1 True False
  printLaw1 True True
  putStrLn ""

  -- Law 2: Non-contradiction - NOT (p AND (NOT p))
  putStrLn "Prawo niesprzeczności:"
  printLaw2 False False
  printLaw2 False True
  printLaw2 True False
  printLaw2 True True
  putStrLn ""

  -- Law 3: Commutativity of AND - p AND q vs q AND p
  putStrLn "Przemienność koniunkcji:"
  printLaw3 False False
  printLaw3 False True
  printLaw3 True False
  printLaw3 True True
  putStrLn ""

  -- Law 4: Commutativity of OR - p OR q vs q OR p
  putStrLn "Przemienność alternatywy:"
  printLaw4 False False
  printLaw4 False True
  printLaw4 True False
  printLaw4 True True
  putStrLn ""

  -- Law 5: De Morgan's 1 - NOT (p AND q) vs (NOT p) OR (NOT q)
  putStrLn "Pierwsze prawo de Morgana:"
  printLaw5 False False
  printLaw5 False True
  printLaw5 True False
  printLaw5 True True
  putStrLn ""

  -- Law 6: De Morgan's 2 - NOT (p OR q) vs (NOT p) AND (NOT q)
  putStrLn "Drugie prawo de Morgana:"
  printLaw6 False False
  printLaw6 False True
  printLaw6 True False
  printLaw6 True True

printLaw1 :: Bool -> Bool -> IO ()
printLaw1 p q = do
  let l = p || not p
  let r = True -- This law doesn't compare two sides, just evaluates one
  putStrLn $ "p=" ++ show p ++ " q=" ++ show q ++ " L=" ++ show l ++ " R=" ++ show r ++ " EQ=" ++ show (l == r)

printLaw2 :: Bool -> Bool -> IO ()
printLaw2 p q = do
  let l = not (p && not p)
  let r = True -- This law doesn't compare two sides, just evaluates one
  putStrLn $ "p=" ++ show p ++ " q=" ++ show q ++ " L=" ++ show l ++ " R=" ++ show r ++ " EQ=" ++ show (l == r)

printLaw3 :: Bool -> Bool -> IO ()
printLaw3 p q = do
  let l = p && q
  let r = q && p
  putStrLn $ "p=" ++ show p ++ " q=" ++ show q ++ " L=" ++ show l ++ " R=" ++ show r ++ " EQ=" ++ show (l == r)

printLaw4 :: Bool -> Bool -> IO ()
printLaw4 p q = do
  let l = p || q
  let r = q || p
  putStrLn $ "p=" ++ show p ++ " q=" ++ show q ++ " L=" ++ show l ++ " R=" ++ show r ++ " EQ=" ++ show (l == r)

printLaw5 :: Bool -> Bool -> IO ()
printLaw5 p q = do
  let l = not (p && q)
  let r = not p || not q
  putStrLn $ "p=" ++ show p ++ " q=" ++ show q ++ " L=" ++ show l ++ " R=" ++ show r ++ " EQ=" ++ show (l == r)

printLaw6 :: Bool -> Bool -> IO ()
printLaw6 p q = do
  let l = not (p || q)
  let r = not p && not q
  putStrLn $ "p=" ++ show p ++ " q=" ++ show q ++ " L=" ++ show l ++ " R=" ++ show r ++ " EQ=" ++ show (l == r)
