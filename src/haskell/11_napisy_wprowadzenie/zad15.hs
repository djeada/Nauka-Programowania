{-
ZAD-15 — Akronim ze zdania

\**Poziom:** ★☆☆
\**Tagi:** `napisy`, `słowa`, `upper`

### Treść

\**Akronim** to skrót utworzony z pierwszych liter kolejnych słów, np. „Polska Akademia Nauk” → `PAN`.

Wczytaj zdanie i wypisz jego akronim: pierwsze znaki wszystkich słów (zgodnie z konwencją rozdziału — bez interpunkcji), zapisane jeden za drugim **wielkimi** literami.

### Wejście

\* 1. linia: zdanie (zawiera co najmniej jedno słowo; może zawierać polskie litery)

### Wyjście

Jedna linia: akronim.

### Przykład

\**Wejście:**

```
Polska Akademia Nauk
```

\**Wyjście:**

```
PAN
```

### Uwagi

\* Słowa mogą być rozdzielone kilkoma spacjami, a zdanie może zaczynać się lub kończyć spacjami — `split()` bez argumentu poradzi sobie z tym.
\* Interpunkcja nie należy do słowa: w zdaniu `(Unia Europejska)` słowami są `Unia` i `Europejska`, więc akronim to `UE`. Samotny myślnik `-` nie jest słowem.
\* Zamiana na wielką literę dotyczy także polskich liter: `żółta łódź` → `ŻŁ`.

-}
import Data.Char (toUpper)
import System.IO (hSetEncoding, stdin, stdout, utf8)

-- Znaki interpunkcyjne (jak string.punctuation w Pythonie)
interpunkcja :: String
interpunkcja = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

usunInterpunkcje :: String -> String
usunInterpunkcje = reverse . dropWhile (`elem` interpunkcja) . reverse . dropWhile (`elem` interpunkcja)

-- Akronim: wielkie pierwsze litery kolejnych słów
akronim :: String -> String
akronim zdanie = [toUpper znak | (znak : _) <- map usunInterpunkcje (words zdanie)]

main :: IO ()
main = do
  hSetEncoding stdin utf8
  hSetEncoding stdout utf8
  zdanie <- getLine
  putStrLn (akronim zdanie)
