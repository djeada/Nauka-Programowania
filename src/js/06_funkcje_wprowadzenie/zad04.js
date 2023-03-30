/*

Tytul: Maks i min

Napisz funkcje, ktora:

a) Dla otrzymanych dwoch liczb zwroci mniejsza.

b) Dla otrzymanych dwoch liczb zwroci wieksza.

c) Dla otrzymanych trzech liczb zwroci najmniejsza.

d) Dla otrzymanych trzech liczb zwroci najwieksza.

Dane wejsciowe:

a) Dwie liczby naturalne.

b) Dwie liczby naturalne.

c) Trzy liczby naturalne.

d) Trzy liczby naturalne.

Dane wyjsciowe: Liczba naturalna dla wszystkich podpunktow.

Przyklad:

a) Dla otrzymanych liczb 3 i 1, funkcja powinna zwrocic liczbe 1.

b) Dla otrzymanych liczb 3 i 1, funkcja powinna zwrocic liczbe 3.

c) Dla otrzymanych liczb 3, 2 i 1, funkcja powinna zwrocic liczbe 1.

d) Dla otrzymanych liczb 3, 2 i 1, funkcja powinna zwrocic liczbe 3.
*/

// Funkcja zwracajaca mniejsza liczbe
function zwracajMniejszaLiczbe(liczba_a, liczba_b) {
  if (liczba_a < liczba_b) {
    return liczba_a;
  } else {
    return liczba_b;
  }
}

// Funkcja zwracajaca wieksza liczbe
function zwracajWiekszaLiczbe(liczba_a, liczba_b) {
  if (liczba_a > liczba_b) {
    return liczba_a;
  } else {
    return liczba_b;
  }
}

// Funkcja zwracajaca najmniejsza liczbe
function zwracajNajmniejszaLiczbe(liczba_a, liczba_b, liczba_c) {
  if (liczba_a < liczba_b && liczba_a < liczba_c) {
    return liczba_a;
  } else if (liczba_b < liczba_a && liczba_b < liczba_c) {
    return liczba_b;
  } else {
    return liczba_c;
  }
}

// Funkcja zwracajaca najwieksza liczbe
function zwracajNajwiekszaLiczbe(liczba_a, liczba_b, liczba_c) {
  if (liczba_a > liczba_b && liczba_a > liczba_c) {
    return liczba_a;
  } else if (liczba_b > liczba_a && liczba_b > liczba_c) {
    return liczba_b;
  } else {
    return liczba_c;
  }
}

// Pobieranie danych od uzytkownika
var liczba_a = prompt("Podaj pierwsza liczbe: ");
var liczba_b = prompt("Podaj druga liczbe: ");
var liczba_c = prompt("Podaj trzecia liczbe: ");

// Wyswietlanie wynikow
console.log("Mniejsza liczba to: " + zwracajMniejszaLiczbe(liczba_a, liczba_b));
console.log("Wieksza liczba to: " + zwracajWiekszaLiczbe(liczba_a, liczba_b));
console.log(
  "Najmniejsza liczba to: " +
    zwracajNajmniejszaLiczbe(liczba_a, liczba_b, liczba_c)
);
console.log(
  "Najwieksza liczba to: " +
    zwracajNajwiekszaLiczbe(liczba_a, liczba_b, liczba_c)
);

