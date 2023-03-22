{-
Tytuł: Kalkulator kredytowy

Treść: Pobierz roczną stopę procentową, liczbę lat na spłacenie kredytu oraz wysokość udzielonego kredytu. Oblicz miesięczną ratę oraz całkowity koszt kredytu.

Dane wejściowe: Trzy liczby naturalne.

Dane wyjściowe: Dwie liczby naturalne.

Przykład:

Dla pobranych liczb: 3.5 (roczna stopa procentowa), 8 (liczba lat) oraz 12000 (wysokość kredytu), powinny zostać wypisane liczby 143.5 (miesięczna rata) oraz 13776 (całkowity koszt kredytu). Waluta jest umowna.
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
