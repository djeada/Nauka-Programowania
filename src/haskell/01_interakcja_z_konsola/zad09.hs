{-
Tytul: Kalkulator kredytowy

Tresc: Pobierz roczna stope procentowa, liczbe lat na splacenie kredytu oraz wysokosc udzielonego kredytu. Oblicz miesieczna rate oraz calkowity koszt kredytu.

Dane wejsciowe: Trzy liczby naturalne.

Dane wyjsciowe: Dwie liczby naturalne.

Przyklad:

Dla pobranych liczb: 3.5 (roczna stopa procentowa), 8 (liczba lat) oraz 12000 (wysokosc kredytu), powinny zostac wypisane liczby 143.5 (miesieczna rata) oraz 13776 (calkowity koszt kredytu). Waluta jest umowna.
-}

main :: IO ()
main = do
  putStrLn "Podaj roczna stope procentowa:"
  annualInterestRate <- readLn :: IO Double
  putStrLn "Podaj liczbe lat na splacenie kredytu:"
  numberOfYears <- readLn :: IO Int
  putStrLn "Podaj wysokosc udzielonego kredytu:"
  loanAmount <- readLn :: IO Double

  let monthlyInterestRate = annualInterestRate / 100 / 12
  let numberOfPayments = fromIntegral (numberOfYears * 12)
  let ratePlusOne = 1 + monthlyInterestRate
  let monthlyPayment = loanAmount * (monthlyInterestRate * (ratePlusOne ** numberOfPayments)) / ((ratePlusOne ** numberOfPayments) - 1)
  let totalCost = monthlyPayment * numberOfPayments

  putStrLn $ "Miesieczna rata: " ++ show monthlyPayment
  putStrLn $ "Calkowity koszt kredytu: " ++ show totalCost

