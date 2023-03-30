/*
Tytul: Porownanie ze zmienna.

Tresc: Pobierz od uzytkownika dwie liczby naturalne i sprawdz, czy sa one identyczne. Wypisz odpowiedni komunikat.

Dane wejsciowe: Dwie liczby naturalne.

Dane wyjsciowe: Komunikat.

Przyklad:

Dla pobranych liczb: 7 i 4, powinien zostac wypisany komunikat, ze liczby sa rozne.
*/

// Pobieranie danych od uzytkownika
const liczba_a = parseInt(prompt("Podaj pierwsza liczbe:"));
const liczba_b = parseInt(prompt("Podaj druga liczbe:"));

// Porownanie ze zmienna
if (liczba_a === liczba_b) {
  console.log("Liczby sa identyczne");
} else {
  console.log("Liczby sa rozne");
}

