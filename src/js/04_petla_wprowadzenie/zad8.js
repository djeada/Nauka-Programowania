/*
Tytul: Liczba kur i owiec na farmie.

Tresc: Na farmie jest a glow i b nog. Znajdz liczbe kur i liczbe owiec.

Dane wejsciowe: Dwie liczby naturalne.

Dane wyjsciowe: Dwie liczby naturalne.

Przyklad:

Dla otrzymanych liczb 40 i 100, powinny zostac wypisane liczby 30 i 10.
*/

// Pobieranie danych od uzytkownika
const a = parseInt(prompt("Podaj liczbe glow:"));
const b = parseInt(prompt("Podaj liczbe nog:"));

// Petla
for (let i = 0; i <= a; i++) {
  if (i * 2 + (a - i) * 4 === b) {
    console.log(i);
    console.log(a - i);
  }
}

