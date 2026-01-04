{-
ZAD-01 — Sprawdź poprawność adresu e-mail

\**Poziom:** ★★☆
\**Tagi:** `regex`, `string`, `walidacja`

### Treść

Otrzymujesz napis reprezentujący adres e-mail. Sprawdź, czy jest poprawny zgodnie z regułami:

\* Adres e-mail składa się z identyfikatora użytkownika, znaku `@` oraz nazwy domeny.
\* **Identyfikator użytkownika** może zawierać wyłącznie:

  * litery `a–z`, `A–Z`,
  * cyfry `0–9`,
  * znaki specjalne: `!`, `#`, `$`, `%`, `&`, `'`, `*`, `+`, `-`, `/`, `=`, `?`, `^`, `_`, `` ` ``, `{`, `|`, `}`, `~`,
  * kropki `.`, ale:

    * nie może być pierwszym ani ostatnim znakiem,
    * nie może wystąpić dwukrotnie po sobie.
\* **Nazwa domeny** może zawierać wyłącznie:

  * litery `a–z`, `A–Z`,
  * cyfry `0–9`,
  * kropki `.` oraz myślniki `-`, ale:

    * nie mogą być pierwszym ani ostatnim znakiem,
    * nie mogą wystąpić dwukrotnie po sobie.

### Wejście

Jedna linia:

\* `email`

### Wyjście

Jedna linia:

\* `Prawda` — jeśli e-mail jest poprawny
\* `Fałsz` — w przeciwnym razie

### Przykład

\**Wejście:**

```
adam@gmail.com
```

\**Wyjście:**

```
Prawda
```

-}

import Data.Char (isAlphaNum)
import Data.List (isInfixOf)

-- Walidacja adresu email (uproszczona bez regex)
-- Złożoność czasowa: O(n), gdzie n to długość adresu
-- Złożoność pamięciowa: O(1)
validateEmail :: String -> Bool
validateEmail email =
  case break (== '@') email of
    ([], _) -> False
    (_, []) -> False
    (username, '@' : domain) ->
      validUsername username && validDomain domain
    _ -> False
  where
    validUsername [] = False
    validUsername u =
      not (head u == '.' || last u == '.')
        && not (".." `isInfixOf` u)
        && all validUserChar u

    validUserChar c = isAlphaNum c || c `elem` "!#$%&'*+-/=?^_`{|}~."

    validDomain [] = False
    validDomain d =
      not (head d == '.' || last d == '.' || head d == '-' || last d == '-')
        && not (".." `isInfixOf` d)
        && not ("--" `isInfixOf` d)
        && all validDomainChar d
        && '.' `elem` d

    validDomainChar c = isAlphaNum c || c `elem` ".-"

main :: IO ()
main = do
  email <- getLine
  putStrLn $ if validateEmail email then "Prawda" else "Fałsz"
