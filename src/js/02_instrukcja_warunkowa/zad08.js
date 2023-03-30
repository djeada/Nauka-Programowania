/*
Tytul: Warunek trojkata.

Tresc: Dla trzech pobranych od uzytkownika dlugosci bokow sprawdz, czy mozna z nich zbudowac trojkat. Jednostki sa umowne.

Dane wejsciowe: Trzy liczby naturalne oznaczajace dlugosci bokow trojkata.

Dane wyjsciowe: Komunikat o mozliwosci lub niemozliwosci zbudowania trojkata.

Przyklad:

Dla pobranych liczb: 1, 2 oraz 3, powinna zostac wypisana informacja, ze nie mozna zbudowac trojkata z podanych bokow.
*/

// Pobieranie danych od uzytkownika
const bok_a = parseInt(prompt("Podaj dlugosc boku a:"));
const bok_b = parseInt(prompt("Podaj dlugosc boku b:"));
const bok_c = parseInt(prompt("Podaj dlugosc boku c:"));

// Warunek trojkata
if (bok_a + bok_b > bok_c && bok_a + bok_c > bok_b && bok_b + bok_c > bok_a) {
  console.log("Mozna zbudowac trojkat z podanych bokow.");
} else {
  console.log("Nie mozna zbudowac trojkata z podanych bokow.");
}

