/*
Tytul: Kalkulator kredytowy

Tresc: Pobierz roczna stope procentowa, liczbe lat na splacenie kredytu oraz wysokosc udzielonego kredytu. Oblicz miesieczna rate oraz calkowity koszt kredytu.

Dane wejsciowe: Trzy liczby naturalne.

Dane wyjsciowe: Dwie liczby naturalne.

Przyklad:

Dla pobranych liczb: 3.5 (roczna stopa procentowa), 8 (liczba lat) oraz 12000 (wysokosc kredytu), powinny zostac wypisane liczby 143.5 (miesieczna rata) oraz 13776 (calkowity koszt kredytu). Waluta jest umowna.
*/

// Pobieranie danych od uzytkownika
const roczna_stopa_procentowa = parseFloat(
  prompt("Podaj roczna stope procentowa:")
);
const liczba_lat = parseInt(prompt("Podaj liczbe lat na splacenie kredytu:"));
const wysokosc_kredytu = parseInt(
  prompt("Podaj wysokosc udzielonego kredytu:")
);

// Obliczanie miesiecznej raty
const miesieczna_rata =
  (wysokosc_kredytu * (roczna_stopa_procentowa / 100)) / 12;

// Obliczanie calkowitego kosztu kredytu
const calkowity_koszt_kredytu = miesieczna_rata * liczba_lat * 12;

// Wypisanie wyniku
console.log(miesieczna_rata.toFixed(2));
console.log(calkowity_koszt_kredytu.toFixed(2));

