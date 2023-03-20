/*
Tytuł: Liczba pi.

Treść: Dla otrzymanej liczby naturalnej wypisz liczbę Pi tyle razy, ile wynosi ta liczba, z dokładnością do tylu miejsc po przecinku, ile wynosi otrzymana liczba.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla otrzymanej liczby 2, powinno zostać wypisane:

    3,14
    3,14
*/

// Pobieranie danych od użytkownika
const liczba = parseInt(prompt("Podaj liczbę:"));

// Pętla
for (let i = 0; i < liczba; i++) {
    console.log(Math.PI.toFixed(liczba));
}