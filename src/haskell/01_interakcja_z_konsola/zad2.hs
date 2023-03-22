{-
Tytuł: Zamiana kolejności liczb.

Treść zadania: Napisz program, który pobierze od użytkownika dwie liczby naturalne i wypisze je w odwróconej kolejności.

Dane wejściowe: Dwie liczby naturalne.

Dane wyjściowe: Dwie liczby naturalne.

Przykład:

Jeśli użytkownik poda liczby -7 oraz 4, program powinien wypisać liczby: 4 i -7.
-}

main :: IO ()
main = do
  putStrLn "Podaj pierwsza liczbe:"
  a <- readLn :: IO Int
  putStrLn "Podaj druga liczbe:"
  b <- readLn :: IO Int
  putStrLn $ "Liczby w odwrotnej kolejnosci: " ++ show b ++ " " ++ show a
