{-
Tytuł: Obliczanie wyników operacji arytmetycznych.

Treść zadania: Napisz program, który pobierze od użytkownika dwie liczby naturalne i wypisze wyniki następujących operacji arytmetycznych:

a) suma tych liczb

b) różnica pierwszej i drugiej liczby

c) iloczyn tych liczb

d) iloraz pierwszej liczby przez drugą

e) reszta z dzielenia pierwszej liczby przez drugą

f) pierwsza liczba podniesiona do potęgi równej drugiej liczbie

Dane wejściowe: Dwie liczby naturalne dla wszystkich podpunktów.

Dane wyjściowe: Liczba naturalna dla wszystkich podpunktów.

Przykład:

    Jeśli użytkownik poda liczby 9 oraz 1, program powinien wypisać liczby: 10, 1, 9, 9, 0, 9.
    Jeśli użytkownik poda liczby 3 oraz 2, program powinien wypisać liczby: 5, 1, 6, 1, 1, 9.
-}

main :: IO ()
main = do
  putStrLn "Podaj pierwsza liczbe:"
  a <- readLn :: IO Int
  putStrLn "Podaj druga liczbe:"
  b <- readLn :: IO Int
  let wyniki = (a + b, a - b, a * b, a `div` b, a `mod` b, a ^ b)
  putStrLn $ "Wyniki operacji arytmetycznych: " ++ show wyniki
