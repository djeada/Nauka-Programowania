{-
ZAD-07 — Weryfikacja nazwy użytkownika i hasła

\**Poziom:** ★★☆
\**Tagi:** `funkcje`, `while`, `string`, `porównania`

### Treść

Napisz dwie funkcje:

1. `pobierz_dane()` — pobiera od użytkownika nazwę użytkownika i hasło i zwraca je (np. jako parę).
2. `sprawdz_dane(poprawny_login, poprawne_haslo)` — w pętli wczytuje login i hasło aż będą identyczne z przekazanymi. Po poprawnym wczytaniu wypisuje:
   `Dane poprawne. Dostęp przyznany.`

### Wejście

\* `pobierz_dane()` wczytuje dwie linie:

  1. login
  2. hasło
\* `sprawdz_dane(...)` wczytuje kolejne pary (login, hasło), po dwie linie na próbę.

### Wyjście

Jedna linia (tylko raz, po poprawnym dopasowaniu):

\* `Dane poprawne. Dostęp przyznany.`

### Ograniczenia / gwarancje

\* W pewnym momencie użytkownik poda poprawne dane.

### Uwagi o formatowaniu

\* **Nie wypisuj promptów** typu „Podaj nazwę użytkownika:”.
\* Porównanie jest czułe na wielkość liter.

-}
pobierzDane :: IO (String, String)
pobierzDane = do
  login <- getLine
  haslo <- getLine
  return (login, haslo)

sprawdzDane :: String -> String -> IO ()
sprawdzDane poprawnyLogin poprawneHaslo = do
  let loop = do
        (login, haslo) <- pobierzDane
        if login == poprawnyLogin && haslo == poprawneHaslo
          then putStrLn "Dane poprawne. Dostęp przyznany."
          else loop
  loop

main :: IO ()
main = do
  (poprawnyLogin, poprawneHaslo) <- pobierzDane
  sprawdzDane poprawnyLogin poprawneHaslo
