/*
Tytul: Zaokraglanie w dol.

Tresc: Napisz funkcje, ktora zaokragli iloraz dwoch liczb naturalnych do najblizszej liczby calkowitej w dol, bez uzycia operatorow '/' i '%'.

Dane wejsciowe: dwie liczby naturalne

Dane wyjsciowe: liczba naturalna

Przyklad:

Dla otrzymanych liczb 7 i 2, funkcja powinna zwrocic liczbe 3.
*/

// Funkcja zaokraglajaca iloraz dwoch liczb naturalnych do najblizszej liczby calkowitej w dol
const podziel = (liczba1, liczba2) => {
  if (liczba2 === 0) return NaN;

  let iloraz = 0;
  let suma = 0;
  let kierunek = liczba1 < 0 === liczba2 < 0 ? 1 : -1;
  let liczba1Abs = Math.abs(liczba1);
  let liczba2Abs = Math.abs(liczba2);

  while (suma + liczba2Abs <= liczba1Abs) {
    suma += liczba2Abs;
    iloraz++;
  }

  return iloraz * kierunek;
};

// Pobieranie danych od uzytkownika
const liczba1 = parseInt(prompt("Podaj pierwsza liczbe:"));
const liczba2 = parseInt(prompt("Podaj druga liczbe:"));

// Wypisanie wyniku
console.log(podziel(liczba1, liczba2));

