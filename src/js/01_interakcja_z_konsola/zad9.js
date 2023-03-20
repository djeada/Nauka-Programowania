/*
Tytuł: Kalkulator kredytowy

Treść: Pobierz roczną stopę procentową, liczbę lat na spłacenie kredytu oraz wysokość udzielonego kredytu. Oblicz miesięczną ratę oraz całkowity koszt kredytu.

Dane wejściowe: Trzy liczby naturalne.

Dane wyjściowe: Dwie liczby naturalne.

Przykład:

Dla pobranych liczb: 3.5 (roczna stopa procentowa), 8 (liczba lat) oraz 12000 (wysokość kredytu), powinny zostać wypisane liczby 143.5 (miesięczna rata) oraz 13776 (całkowity koszt kredytu). Waluta jest umowna.
*/

// Pobieranie danych od użytkownika
const roczna_stopa_procentowa = parseFloat(prompt("Podaj roczną stopę procentową:"));
const liczba_lat = parseInt(prompt("Podaj liczbę lat na spłacenie kredytu:"));
const wysokosc_kredytu = parseInt(prompt("Podaj wysokość udzielonego kredytu:"));

// Obliczanie miesięcznej raty
const miesieczna_rata = (wysokosc_kredytu * (roczna_stopa_procentowa / 100)) / 12;

// Obliczanie całkowitego kosztu kredytu
const calkowity_koszt_kredytu = miesieczna_rata * liczba_lat * 12;

// Wypisanie wyniku
console.log(miesieczna_rata);