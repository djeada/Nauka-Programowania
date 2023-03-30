/*
Tytul: Cyfry liczby spelniajace okreslone warunki.

Tresc: Dla otrzymanej liczby naturalnej wypisz cyfry tej liczby, ktore sa:

a) liczbami parzystymi,

b) mniejsze niz 5,

c) rozne od 0.

Dane wejsciowe: Liczba naturalna dla wszystkich podpunktow.

Dane wyjsciowe: Kilka liczb.

Przyklad:

a) Dla otrzymanej liczby 932, powinna zostac wypisana liczba 2.

b) Dla otrzymanej liczby 101, powinny zostac wypisane liczby 1, 0 i 1.

c) Dla otrzymanej liczby 650, powinny zostac wypisane liczby 6 i 5.
*/

// Pobieranie danych od uzytkownika
const liczba = parseInt(prompt("Podaj liczbe:"));

// a) Petla dla liczb parzystych
for (let i = liczba; i > 0; i = Math.floor(i / 10)) {
  if (i % 2 == 0) {
    console.log(i % 10);
  }
}

// b) Petla dla liczb mniejszych od 5
for (let i = liczba; i > 0; i = Math.floor(i / 10)) {
  if (i % 10 < 5) {
    console.log(i % 10);
  }
}

// c) Petla dla liczb roznych od 0
for (let i = liczba; i > 0; i = Math.floor(i / 10)) {
  if (i % 10 != 0) {
    console.log(i % 10);
  }
}

