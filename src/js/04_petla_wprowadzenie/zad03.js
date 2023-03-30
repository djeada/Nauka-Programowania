/*
Tytul: Liczba pi.

Tresc: Dla otrzymanej liczby naturalnej wypisz liczbe Pi tyle razy, ile wynosi ta liczba, z dokladnoscia do tylu miejsc po przecinku, ile wynosi otrzymana liczba.

Dane wejsciowe: Liczba naturalna.

Dane wyjsciowe: Liczba naturalna.

Przyklad:

Dla otrzymanej liczby 2, powinno zostac wypisane:

    3,14
    3,14
*/

// Pobieranie danych od uzytkownika
const liczba = parseInt(prompt("Podaj liczbe:"));

// Petla
for (let i = 0; i < liczba; i++) {
  console.log(Math.PI.toFixed(liczba));
}

