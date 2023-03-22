/*
Tytuł: Jaki mamy dzień tygodnia?	

Treść: Napisz program, który dla trzech pobranych liczb naturalnych (reprezentujących datę) będzie wypisywał odpowiadający im dzień tygodnia. Pierwsza liczba jest dniem, druga miesiącem, trzecia rokiem.

Podpowiedź: Można użyć wzoru Gaussa:
Niech data będzie dana w formacie DD/MM/CCYY :

* DD - dzień
* MM - miesiąc
* CC - stulecie
* YY - rok

$$A = CC/4 - 2CC - 1$$

$$B = 5YY/4$$

$$C = 26*(MM + 1)/10$$

$$Dzien = (A + B + C + DD) mod 7$$

Dane wejściowe: Trzy liczby naturalne.

Dane wyjściowe: Komunikat o dniu tygodnia.

Przykład:

Dla pobranych liczb 9, 10 i 2020, program powinien zwrócić napis "Czwartek".
*/

// Pobieranie danych od użytkownika
const dzien = parseInt(prompt("Podaj dzień:"));
const miesiac = parseInt(prompt("Podaj miesiąc:"));
const rok = parseInt(prompt("Podaj rok:"));

const A = rok; // 4 - 2 * rok - 1
const B = 5 * rok; // 4
const C = 26 * (miesiac + 1); // 10

const dzien_tygodnia = (A + B + C + dzien) % 7;

if (dzien_tygodnia === 0) {
  console.log("Niedziela");
} else if (dzien_tygodnia === 1) {
  console.log("Poniedziałek");
} else if (dzien_tygodnia === 2) {
  console.log("Wtorek");
} else if (dzien_tygodnia === 3) {
  console.log("Środa");
} else if (dzien_tygodnia === 4) {
  console.log("Czwartek");
} else if (dzien_tygodnia === 5) {
  console.log("Piątek");
} else {
  console.log("Sobota");
}
