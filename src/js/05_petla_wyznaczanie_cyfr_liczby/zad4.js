/*
Tytuł: Cyfry liczby spełniające określone warunki.

Treść: Dla otrzymanej liczby naturalnej wypisz cyfry tej liczby, które są:

a) liczbami parzystymi,

b) mniejsze niż 5,

c) różne od 0.

Dane wejściowe: Liczba naturalna dla wszystkich podpunktów.

Dane wyjściowe: Kilka liczb.

Przykład:

a) Dla otrzymanej liczby 932, powinna zostać wypisana liczba 2.

b) Dla otrzymanej liczby 101, powinny zostać wypisane liczby 1, 0 i 1.

c) Dla otrzymanej liczby 650, powinny zostać wypisane liczby 6 i 5.
*/

// Pobieranie danych od użytkownika
const liczba = parseInt(prompt("Podaj liczbę:"));

// a) Pętla dla liczb parzystych
for (let i = liczba; i > 0; i = Math.floor(i / 10)) {
    if (i % 2 == 0) {
        console.log(i % 10);
    }
}

// b) Pętla dla liczb mniejszych od 5
for (let i = liczba; i > 0; i = Math.floor(i / 10)) {
    if (i % 10 < 5) {
        console.log(i % 10);
    }
}

// c) Pętla dla liczb różnych od 0
for (let i = liczba; i > 0; i = Math.floor(i / 10)) {
    if (i % 10 != 0) {
        console.log(i % 10);
    }
}