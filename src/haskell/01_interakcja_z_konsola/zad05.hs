{-
  Tytul: Obliczanie wartosci funkcji w danym punkcie.

  Tresc zadania: Napisz program, ktory bedzie obliczac wartosc funkcji w danym punkcie zgodnie z nastepujacymi instrukcjami:

  a) Otrzymujesz wspolrzedna $x$. Wyznacz wartosc funkcji $y = 3x + 10$ w tym punkcie.

  b) Pobierz wspolczynniki $a$, $b$ oraz punkt $x$. Wyznacz wartosc funkcji $y = ax + b$ w tym punkcie.

  c) Otrzymujesz wspolrzedna $x$. Wyznacz wartosc funkcji $y = x^3 + 22 - 20$ w tym punkcie.

  d) Pobierz wspolczynniki $a$, $b$, $c$, $d$, $m$, $n$ oraz punkt $x$. Wyznacz wartosc funkcji $y = ax^m + bx^n + c - a$ w tym punkcie.

  e) Otrzymujesz wspolrzedna $x$. Wyznacz wartosc funkcji $y = sin^3(x) \cdot cos^2(x) + e^(x^2) + log(x^3 + 2x^2 - x - 3)$ w tym punkcie.

  Dane wejsciowe:

  * Liczba naturalna dla punktow 1, 3 i 5.
  * Trzy liczby naturalne dla punktu 2.
  * Szesc liczb naturalnych dla punktu 4.

  Dane wyjsciowe:

  * Liczba naturalna dla punktow 1, 2, 3 i 4.
  * Liczba zmiennoprzecinkowa dla punktu 5.

  Przyklad:

  a) Jesli otrzymasz wspolrzedna $x = 3$, program powinien wypisac liczbe 19.

  b) Jesli pobierzesz liczby 1, 2 i 3, program powinien wypisac liczbe 5.

  c) Jesli otrzymasz wspolrzedna $x = 5$, program powinien wypisac liczbe 155.

  d) Jesli pobierzesz liczby 1, 1, 1, 1, 1 i 1, program powinien wypisac liczbe 2.

  e) Jesli otrzymasz wspolrzedna $x = 2$, program powinien wypisac liczbe 57.179.
-}

import Data.Fixed (mod')
import Prelude

pow :: Double -> Int -> Double
pow x y = x Prelude.^ y

main :: IO ()
main = do
  putStrLn "Podaj wspolrzedne x:"
  x <- readLn :: IO Double
  putStrLn $ "Wartosc funkcji y = 3x + 10: " ++ show (3 * x + 10)
  putStrLn "Podaj wspolczynniki a, b:"
  a <- readLn :: IO Double
  b <- readLn :: IO Double
  putStrLn $ "Wartosc funkcji y = ax + b: " ++ show (a * x + b)
  putStrLn $ "Wartosc funkcji y = x^3 + 22 - 20: " ++ show (x * x * x + 22 - 20)
  putStrLn "Podaj wspolczynniki a, b, c, d, m, n:"
  a <- readLn :: IO Double
  b <- readLn :: IO Double
  c <- readLn :: IO Double
  d <- readLn :: IO Double
  m <- readLn :: IO Int
  n <- readLn :: IO Int
  putStrLn $ "Wartosc funkcji y = ax^m + bx^n + c - a: " ++ show (a * (x `pow` m) + b * (x `pow` n) + c - a)
  putStrLn $ "Wartosc funkcji y = sin^3(x) * cos^2(x) + e^(x^2) + log(x^3 + 2x^2 - x - 3): " ++ show ((sin x Prelude.^ 3) * (cos x Prelude.^ 2) + exp (x * x) + log (x * x * x + 2 * x * x - x - 3))

