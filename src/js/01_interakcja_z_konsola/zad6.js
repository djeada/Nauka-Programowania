/*
Tytul: Konwersja jednostek.

Tresc zadania: Napisz program, ktory bedzie konwertowac jednostki zgodnie z nastepujacymi instrukcjami:

a) Pobierz wielkosc w kilogramach i wypisz, ile gramow odpowiada.

b) Pobierz wielkosc w calach i wypisz, ile centymetrow odpowiada.

c) Pobierz liczbe sekund i przelicz na godziny.

d) Pobierz liczbe w euro i wypisz, ile zlotowek odpowiada.
 
e) Pobierz miare kata w stopniach i wypisz, ile radianow odpowiada.

f) Pobierz temperature w stopniach Fahrenheita i wypisz ile stopni Celsjusza oraz ile stopni Kelvina odpowiada.

Dane wejsciowe: Liczba naturalna we wszystkich podpunktach.

Dane wyjsciowe:

* Liczba naturalna dla podpunktow 1 i 3.
* Liczba zmiennoprzecinkowa dla pozostalych podpunktow.

Przyklad:

a) Dla pobranej liczby: 2, powinna zostac wypisana liczba: 2000.

b) Dla pobranej liczby: 12, powinna zostac wypisana liczba: 4.724.

c) Dla pobranej liczby: 3600, powinna zostac wypisana liczba: 1.

d) Dla pobranej liczby: 4, powinna zostac wypisana liczba: 17.6.

e) Dla pobranej liczby: 120, powinna zostac wypisana liczba:  2.094.

f) Dla pobranej liczby: 100, powinny zostac wypisane liczby: 37.777 i -235.222.
*/

// a) Pobierz wielkosc w kilogramach i wypisz, ile gramow odpowiada.
const kg = parseInt(prompt("Podaj liczbe w kilogramach:"));
console.log(kg * 1000);

// b) Pobierz wielkosc w calach i wypisz, ile centymetrow odpowiada.
const inch = parseInt(prompt("Podaj liczbe w calach:"));
console.log(inch * 2.54);

// c) Pobierz liczbe sekund i przelicz na godziny.
const sec = parseInt(prompt("Podaj liczbe w sekundach:"));
console.log(sec / 3600);

// d) Pobierz liczbe w euro i wypisz, ile zlotowek odpowiada.
const euro = parseInt(prompt("Podaj liczbe w euro:"));
console.log(euro * 4.56);

// e) Pobierz miare kata w stopniach i wypisz, ile radianow odpowiada.
const deg = parseInt(prompt("Podaj liczbe w stopniach:"));
console.log(deg * 0.0174533);

// f) Pobierz temperature w stopniach Fahrenheita i wypisz ile stopni Celsjusza oraz ile stopni Kelvina odpowiada.
const temp = parseInt(prompt("Podaj liczbe w stopniach Fahrenheita:"));
console.log(((temp - 32) * 5) / 9);
console.log(((temp - 32) * 5) / 9 + 273.15);

