/*
Tytuł: Liczba kur i owiec na farmie.

Treść: Na farmie jest a głów i b nóg. Znajdź liczbę kur i liczbę owiec.

Dane wejściowe: Dwie liczby naturalne.

Dane wyjściowe: Dwie liczby naturalne.

Przykład:

Dla otrzymanych liczb 40 i 100, powinny zostać wypisane liczby 30 i 10.
*/

// Pobieranie danych od użytkownika
const a = parseInt(prompt("Podaj liczbę głów:"));
const b = parseInt(prompt("Podaj liczbę nóg:"));

// Pętla
for (let i = 0; i <= a; i++) {
  if (i * 2 + (a - i) * 4 === b) {
    console.log(i);
    console.log(a - i);
  }
}
