{-
Tytuł: Rysowanie kształtów za pomocą znaków.

Treść zadania: Napisz program, który wypisze na standardowe wyjście ciągi znaków tworzące kwadrat, trójkąt oraz romb z jedynek. Pamiętaj o dodawaniu odpowiednich spacji i przejściach do nowej linii.

Przykłady:

Kwadrat:

xx
xx

Trójkąt:

1
22
333

Romb z jedynek:

1
111
11111
111
1

Dane wejściowe: Brak.

Dane wyjściowe: Komunikat.
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
