/*
Tytul: Jaki mamy dzien tygodnia?	

Tresc: Napisz program, ktory dla trzech pobranych liczb naturalnych (reprezentujacych date) bedzie wypisywal odpowiadajacy im dzien tygodnia. Pierwsza liczba jest dniem, druga miesiacem, trzecia rokiem.

Podpowiedz: Mozna uzyc wzoru Gaussa:
Niech data bedzie dana w formacie DD/MM/CCYY :

* DD - dzien
* MM - miesiac
* CC - stulecie
* YY - rok

$$A = CC/4 - 2CC - 1$$

$$B = 5YY/4$$

$$C = 26*(MM + 1)/10$$

$$Dzien = (A + B + C + DD) mod 7$$

Dane wejsciowe: Trzy liczby naturalne.

Dane wyjsciowe: Komunikat o dniu tygodnia.

Przyklad:

Dla pobranych liczb 9, 10 i 2020, program powinien zwrocic napis "Czwartek".
*/

// Pobieranie danych od uzytkownika
const dzien = parseInt(prompt("Podaj dzien:"));
const miesiac = parseInt(prompt("Podaj miesiac:"));
const rok = parseInt(prompt("Podaj rok:"));

const A = rok; // 4 - 2 * rok - 1
const B = 5 * rok; // 4
const C = 26 * (miesiac + 1); // 10

const dzien_tygodnia = (A + B + C + dzien) % 7;

if (dzien_tygodnia === 0) {
  console.log("Niedziela");
} else if (dzien_tygodnia === 1) {
  console.log("Poniedzialek");
} else if (dzien_tygodnia === 2) {
  console.log("Wtorek");
} else if (dzien_tygodnia === 3) {
  console.log("Sroda");
} else if (dzien_tygodnia === 4) {
  console.log("Czwartek");
} else if (dzien_tygodnia === 5) {
  console.log("Piatek");
} else {
  console.log("Sobota");
}

