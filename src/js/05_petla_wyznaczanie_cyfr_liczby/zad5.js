/*
Czy liczba jest palindromem?

Treść: Dla otrzymanej liczby naturalnej sprawdź, czy jest ona palindromem, tj. czy nie zmienia się po zapisaniu cyfr w odwrotnej kolejności.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Komunikat.

Przykład:

Dla otrzymanej liczby 13231, powinna zostać wypisana informacja o tym, że liczba jest palindromem.
*/

// Pobieranie danych od użytkownika
const liczba = parseInt(prompt("Podaj liczbę:"));

// Pętla
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