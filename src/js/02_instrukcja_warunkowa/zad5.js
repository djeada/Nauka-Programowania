/*
Tytul: Posortowanie trzech liczb.

Tresc: Pobierz od uzytkownika trzy liczby naturalne i wypisz je w kolejnosci rosnacej.

Dane wejsciowe: Trzy liczby naturalne.

Dane wyjsciowe: Trzy liczby naturalne.

Przyklad:

Dla pobranych liczb: 2, 1 oraz 4, powinny zostac wypisane liczby: 1, 2 i 4.
*/

// Pobieranie danych od uzytkownika
const liczba_a = parseInt(prompt("Podaj pierwsza liczbe:"));
const liczba_b = parseInt(prompt("Podaj druga liczbe:"));
const liczba_c = parseInt(prompt("Podaj trzecia liczbe:"));

// Porownanie ze zmienna
if (liczba_a > liczba_b && liczba_a > liczba_c) {
  if (liczba_b > liczba_c) {
    console.log(liczba_c);
    console.log(liczba_b);
    console.log(liczba_a);
  } else {
    console.log(liczba_b);
    console.log(liczba_c);
    console.log(liczba_a);
  }
} else if (liczba_b > liczba_a && liczba_b > liczba_c) {
  if (liczba_a > liczba_c) {
    console.log(liczba_c);
    console.log(liczba_a);
    console.log(liczba_b);
  } else {
    console.log(liczba_a);
    console.log(liczba_c);
    console.log(liczba_b);
  }
} else {
  if (liczba_a > liczba_b) {
    console.log(liczba_b);
    console.log(liczba_a);
    console.log(liczba_c);
  } else {
    console.log(liczba_a);
    console.log(liczba_b);
    console.log(liczba_c);
  }
}

