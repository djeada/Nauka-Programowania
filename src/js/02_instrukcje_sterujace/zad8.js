/*
Tytuł: Warunek trójkąta.

Treść: Dla trzech pobranych od użytkownika długości boków sprawdź, czy można z nich zbudować trójkąt. Jednostki są umowne.

Dane wejściowe: Trzy liczby naturalne oznaczające długości boków trójkąta.

Dane wyjściowe: Komunikat o możliwości lub niemożliwości zbudowania trójkąta.

Przykład:

Dla pobranych liczb: 1, 2 oraz 3, powinna zostać wypisana informacja, że nie można zbudować trójkąta z podanych boków.
*/

// Pobieranie danych od użytkownika
const bok_a = parseInt(prompt("Podaj długość boku a:"));
const bok_b = parseInt(prompt("Podaj długość boku b:"));
const bok_c = parseInt(prompt("Podaj długość boku c:"));

// Warunek trójkąta
if (bok_a + bok_b > bok_c && bok_a + bok_c > bok_b && bok_b + bok_c > bok_a) {
  console.log("Można zbudować trójkąt z podanych boków.");
} else {
  console.log("Nie można zbudować trójkąta z podanych boków.");
}
