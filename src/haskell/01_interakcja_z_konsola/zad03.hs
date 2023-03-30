{-
Tytul: Rysowanie ksztaltow za pomoca znakow.

Tresc zadania: Napisz program, ktory wypisze na standardowe wyjscie ciagi znakow tworzace kwadrat, trojkat oraz romb z jedynek. Pamietaj o dodawaniu odpowiednich spacji i przejsciach do nowej linii.

Przyklady:

Kwadrat:

xx
xx

Trojkat:

1
22
333

Romb z jedynek:

1
111
11111
111
1

Dane wejsciowe: Brak.

Dane wyjsciowe: Komunikat.
-}

main :: IO ()
main = do
  putStrLn "Kwadrat:"
  putStrLn "xx"
  putStrLn "xx"

  putStrLn "\nTrojkat:"
  putStrLn " 1"
  putStrLn "22"
  putStrLn "333"

  putStrLn "\nRomb z jedynek:"
  putStrLn "  1"
  putStrLn " 111"
  putStrLn "11111"
  putStrLn " 111"
  putStrLn "  1"

