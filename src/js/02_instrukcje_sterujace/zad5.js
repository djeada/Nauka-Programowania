/*
Tytuł: Posortowanie trzech liczb.

Treść: Pobierz od użytkownika trzy liczby naturalne i wypisz je w kolejności rosnącej.

Dane wejściowe: Trzy liczby naturalne.

Dane wyjściowe: Trzy liczby naturalne.

Przykład:

Dla pobranych liczb: 2, 1 oraz 4, powinny zostać wypisane liczby: 1, 2 i 4.
*/

// Pobieranie danych od użytkownika
const liczba_a = parseInt(prompt("Podaj pierwszą liczbę:"));
const liczba_b = parseInt(prompt("Podaj drugą liczbę:"));
const liczba_c = parseInt(prompt("Podaj trzecią liczbę:"));

// Porównanie ze zmienną
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
