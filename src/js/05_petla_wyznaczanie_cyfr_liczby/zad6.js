/*
Tytuł: Liczby spełniające określone warunki.

Treść: Dla pobranej liczby naturalnej wypisz:

a) wszystkie liczby naturalne mniejsze od pobranej, których suma cyfr jest równa 10,

b) wszystkie liczby naturalne dwucyfrowe większe od pobranej,

c) wszystkie liczby naturalne trzycyfrowe, których suma cyfr jest równa pobranej liczbie,

d) wszystkie liczby naturalne trzycyfrowe podzielne przez sumę cyfr pobranej liczby,

e) wszystkie liczby naturalne mniejsze od pobranej, składające się wyłącznie z parzystych cyfr.

Dane wejściowe: Liczba naturalna dla wszystkich podpunktów.

Dane wyjściowe: Kilka liczb naturalnych.

Przykłady

Dla pobranej liczby: 95:

a) wszystkie liczby naturalne mniejsze od pobranej, których suma cyfr jest równa 10: brak

b) wszystkie liczby naturalne dwucyfrowe większe od pobranej: 96, 97, 98, 99

c) wszystkie liczby naturalne trzycyfrowe, których suma cyfr jest równa pobranej liczbie: brak

d) wszystkie liczby naturalne trzycyfrowe podzielne przez sumę cyfr pobranej liczby: brak

e) wszystkie liczby naturalne mniejsze od pobranej, składające się wyłącznie z parzystych cyfr: 2, 4
*/

// Pobieranie danych od użytkownika
const liczba = parseInt(prompt("Podaj liczbę:"));

// a) Pętla dla liczb mniejszych od pobranej, których suma cyfr jest równa 10
for (let i = liczba - 1; i > 0; i--) {
    let sumaCyfr = 0;
    for (let j = i; j > 0; j = Math.floor(j / 10)) {
        sumaCyfr += j % 10;
    }
    if (sumaCyfr == 10) {
        console.log(i);
    }
}

// b) Pętla dla liczb dwucyfrowych większych od pobranej
for (let i = liczba + 1; i < 100; i++) {
    console.log(i);
}

// c) Pętla dla liczb trzycyfrowych, których suma cyfr jest równa pobranej liczbie
for (let i = 100; i < 1000; i++) {
    let sumaCyfr = 0;
    for (let j = i; j > 0; j = Math.floor(j / 10)) {
        sumaCyfr += j % 10;
    }
    if (sumaCyfr == liczba) {
        console.log(i);
    }
}

// d) Pętla dla liczb trzycyfrowych podzielnych przez sumę cyfr pobranej liczby
for (let i = 100; i < 1000; i++) {
    let sumaCyfr = 0;
    for (let j = i; j > 0; j = Math.floor(j / 10)) {
        sumaCyfr += j % 10;
    }
    if (i % sumaCyfr == 0) {
        console.log(i);
    }
}

// e) Pętla dla liczb mniejszych od pobranej, składające się wyłącznie z parzystych cyfr
for (let i = liczba - 1; i > 0; i--) {
    let parzysta = true;
    for (let j = i; j > 0; j = Math.floor(j / 10)) {
        if (j % 2 != 0) {
            parzysta = false;
            break;
        }
    }
    if (parzysta) {
        console.log(i);
    }
}