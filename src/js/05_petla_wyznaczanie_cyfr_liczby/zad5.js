/*
Czy liczba jest palindromem?

Tresc: Dla otrzymanej liczby naturalnej sprawdz, czy jest ona palindromem, tj. czy nie zmienia sie po zapisaniu cyfr w odwrotnej kolejnosci.

Dane wejsciowe: Liczba naturalna.

Dane wyjsciowe: Komunikat.

Przyklad:

Dla otrzymanej liczby 13231, powinna zostac wypisana informacja o tym, ze liczba jest palindromem.
*/

// Pobieranie danych od uzytkownika
const liczba = parseInt(prompt("Podaj liczbe:"));

// Petla
let palindrom = true;
for (let i = liczba, j = 0; i > 0; i = Math.floor(i / 10), j++) {
  if (Math.floor(liczba / 10 ** j) % 10 !== i % 10) {
    palindrom = false;
    break;
  }
}

// Wypisanie wyniku
if (palindrom) {
  console.log("Liczba jest palindromem.");
} else {
  console.log("Liczba nie jest palindromem.");
}

