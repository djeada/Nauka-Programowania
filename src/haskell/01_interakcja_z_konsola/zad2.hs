{-
Tytul: Zamiana kolejnosci liczb.

Tresc zadania: Napisz program, ktory pobierze od uzytkownika dwie liczby naturalne i wypisze je w odwroconej kolejnosci.

Dane wejsciowe: Dwie liczby naturalne.

Dane wyjsciowe: Dwie liczby naturalne.

Przyklad:

Jesli uzytkownik poda liczby -7 oraz 4, program powinien wypisac liczby: 4 i -7.
-}

main :: IO ()
main = do
  putStrLn "Podaj pierwsza liczbe:"
  a <- readLn :: IO Int
  putStrLn "Podaj druga liczbe:"
  b <- readLn :: IO Int
  putStrLn $ "Liczby w odwrotnej kolejnosci: " ++ show b ++ " " ++ show a

