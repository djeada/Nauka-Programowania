{-
ZAD-04 — Wszystkie wystąpienia podnapisu

\**Poziom:** ★★☆
\**Tagi:** `string`, `substring`, `find`

### Treść

Otrzymujesz napis `S` i napis `W` (wzorzec). Znajdź **wszystkie** pozycje w `S`, od których zaczyna się wystąpienie `W`, i wypisz je w kolejności rosnącej.

Wystąpienia mogą na siebie nachodzić: w napisie `aaaa` wzorzec `aa` zaczyna się na pozycjach `0`, `1` i `2`.

### Wejście

\* 1. linia: napis `S`
\* 2. linia: wzorzec `W`

### Wyjście

Jedna linia: indeksy początków wszystkich wystąpień `W` w `S`, oddzielone pojedynczymi spacjami.
Jeśli `W` nie występuje w `S`, wypisz `Brak`.

### Ograniczenia

\* `1 ≤ |S| ≤ 1000`
\* `1 ≤ |W| ≤ 100`

### Przykład

\**Wejście:**

```
abrakadabra
abra
```

\**Wyjście:**

```
0 7
```

### Uwagi

\* Spróbuj nie używać metod `find` ani `count`: dla każdej pozycji `i` od `0` do `len(S) - len(W)` sprawdź, czy od tego miejsca zaczyna się `W` — tak jak sprawdzałeś przedrostek w zadaniu ZAD-03.
\* W przeciwieństwie do zadań ZAD-01 i ZAD-02 po znalezieniu wystąpienia **nie przeskakujemy** go — kolejną sprawdzaną pozycją jest `i + 1`.

-}
import Data.List (isPrefixOf, tails)
import System.IO (hSetEncoding, stdin, stdout, utf8)

-- Indeksy wszystkich (także nachodzących) wystąpień wzorca w napisie.
-- Złożoność czasowa: O(n * m), pamięciowa: O(n)
wystapienia :: String -> String -> [Int]
wystapienia napis wzorzec =
  [i | (i, reszta) <- zip [0 ..] (tails napis), wzorzec `isPrefixOf` reszta]

main :: IO ()
main = do
  hSetEncoding stdin utf8
  hSetEncoding stdout utf8
  napis <- getLine
  wzorzec <- getLine
  let pozycje = wystapienia napis wzorzec
  putStrLn $ if null pozycje then "Brak" else unwords (map show pozycje)
