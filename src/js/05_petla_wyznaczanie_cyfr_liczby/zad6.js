/*
Tytul: Liczby spelniajace okreslone warunki.

Tresc: Dla pobranej liczby naturalnej wypisz:

a) wszystkie liczby naturalne mniejsze od pobranej, ktorych suma cyfr jest rowna 10,

b) wszystkie liczby naturalne dwucyfrowe wieksze od pobranej,

c) wszystkie liczby naturalne trzycyfrowe, ktorych suma cyfr jest rowna pobranej liczbie,

d) wszystkie liczby naturalne trzycyfrowe podzielne przez sume cyfr pobranej liczby,

e) wszystkie liczby naturalne mniejsze od pobranej, skladajace sie wylacznie z parzystych cyfr.

Dane wejsciowe: Liczba naturalna dla wszystkich podpunktow.

Dane wyjsciowe: Kilka liczb naturalnych.

Przyklady

Dla pobranej liczby: 95:

a) wszystkie liczby naturalne mniejsze od pobranej, ktorych suma cyfr jest rowna 10: brak

b) wszystkie liczby naturalne dwucyfrowe wieksze od pobranej: 96, 97, 98, 99

c) wszystkie liczby naturalne trzycyfrowe, ktorych suma cyfr jest rowna pobranej liczbie: brak

d) wszystkie liczby naturalne trzycyfrowe podzielne przez sume cyfr pobranej liczby: brak

e) wszystkie liczby naturalne mniejsze od pobranej, skladajace sie wylacznie z parzystych cyfr: 2, 4
*/

// Pobieranie danych od uzytkownika
const liczba = parseInt(prompt("Podaj liczbe:"));

// a) Petla dla liczb mniejszych od pobranej, ktorych suma cyfr jest rowna 10
for (let i = liczba - 1; i > 0; i--) {
  let sumaCyfr = 0;
  for (let j = i; j > 0; j = Math.floor(j / 10)) {
    sumaCyfr += j % 10;
  }
  if (sumaCyfr == 10) {
    console.log(i);
  }
}

// b) Petla dla liczb dwucyfrowych wiekszych od pobranej
for (let i = liczba + 1; i < 100; i++) {
  console.log(i);
}

// c) Petla dla liczb trzycyfrowych, ktorych suma cyfr jest rowna pobranej liczbie
for (let i = 100; i < 1000; i++) {
  let sumaCyfr = 0;
  for (let j = i; j > 0; j = Math.floor(j / 10)) {
    sumaCyfr += j % 10;
  }
  if (sumaCyfr == liczba) {
    console.log(i);
  }
}

// d) Petla dla liczb trzycyfrowych podzielnych przez sume cyfr pobranej liczby
for (let i = 100; i < 1000; i++) {
  let sumaCyfr = 0;
  for (let j = i; j > 0; j = Math.floor(j / 10)) {
    sumaCyfr += j % 10;
  }
  if (i % sumaCyfr == 0) {
    console.log(i);
  }
}

// e) Petla dla liczb mniejszych od pobranej, skladajace sie wylacznie z parzystych cyfr
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

