/*
Tytuł: Konwersja jednostek.

Treść zadania: Napisz program, który będzie konwertować jednostki zgodnie z następującymi instrukcjami:

a) Pobierz wielkość w kilogramach i wypisz, ile gramów odpowiada.

b) Pobierz wielkość w calach i wypisz, ile centymetrów odpowiada.

c) Pobierz liczbę sekund i przelicz na godziny.

d) Pobierz liczbę w euro i wypisz, ile złotówek odpowiada.
 
e) Pobierz miarę kąta w stopniach i wypisz, ile radianów odpowiada.

f) Pobierz temperaturę w stopniach Fahrenheita i wypisz ile stopni Celsjusza oraz ile stopni Kelvina odpowiada.

Dane wejściowe: Liczba naturalna we wszystkich podpunktach.

Dane wyjściowe:

* Liczba naturalna dla podpunktów 1 i 3.
* Liczba zmiennoprzecinkowa dla pozostałych podpunktów.

Przykład:

a) Dla pobranej liczby: 2, powinna zostać wypisana liczba: 2000.

b) Dla pobranej liczby: 12, powinna zostać wypisana liczba: 4.724.

c) Dla pobranej liczby: 3600, powinna zostać wypisana liczba: 1.

d) Dla pobranej liczby: 4, powinna zostać wypisana liczba: 17.6.

e) Dla pobranej liczby: 120, powinna zostać wypisana liczba:  2.094.

f) Dla pobranej liczby: 100, powinny zostać wypisane liczby: 37.777 i -235.222.
*/

// a) Pobierz wielkość w kilogramach i wypisz, ile gramów odpowiada.
const kg = parseInt(prompt("Podaj liczbę w kilogramach:"));
console.log(kg * 1000);

// b) Pobierz wielkość w calach i wypisz, ile centymetrów odpowiada.
const inch = parseInt(prompt("Podaj liczbę w calach:"));
console.log(inch * 2.54);

// c) Pobierz liczbę sekund i przelicz na godziny.
const sec = parseInt(prompt("Podaj liczbę w sekundach:"));
console.log(sec / 3600);

// d) Pobierz liczbę w euro i wypisz, ile złotówek odpowiada.
const euro = parseInt(prompt("Podaj liczbę w euro:"));
console.log(euro * 4.56);

// e) Pobierz miarę kąta w stopniach i wypisz, ile radianów odpowiada.
const deg = parseInt(prompt("Podaj liczbę w stopniach:"));
console.log(deg * 0.0174533);

// f) Pobierz temperaturę w stopniach Fahrenheita i wypisz ile stopni Celsjusza oraz ile stopni Kelvina odpowiada.
const temp = parseInt(prompt("Podaj liczbę w stopniach Fahrenheita:"));
console.log(((temp - 32) * 5) / 9);
console.log(((temp - 32) * 5) / 9 + 273.15);
