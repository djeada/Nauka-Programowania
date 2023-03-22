/*
Tytuł: Zaokrąglanie w dół.

Treść: Napisz funkcję, która zaokrągli iloraz dwóch liczb naturalnych do najbliższej liczby całkowitej w dół, bez użycia operatorów '/' i '%'.

Dane wejściowe: dwie liczby naturalne

Dane wyjściowe: liczba naturalna

Przykład:

Dla otrzymanych liczb 7 i 2, funkcja powinna zwrócić liczbę 3.
*/

// Funkcja zaokrąglająca iloraz dwóch liczb naturalnych do najbliższej liczby całkowitej w dół
const podziel = (liczba1, liczba2) => {
  if (liczba2 === 0) return NaN;

  let iloraz = 0;
  let suma = 0;
  let kierunek = liczba1 < 0 === liczba2 < 0 ? 1 : -1;
  let liczba1Abs = Math.abs(liczba1);
  let liczba2Abs = Math.abs(liczba2);

  while (suma + liczba2Abs <= liczba1Abs) {
    suma += liczba2Abs;
    iloraz++;
  }

  return iloraz * kierunek;
};

// Pobieranie danych od użytkownika
const liczba1 = parseInt(prompt("Podaj pierwszą liczbę:"));
const liczba2 = parseInt(prompt("Podaj drugą liczbę:"));

// Wypisanie wyniku
console.log(podziel(liczba1, liczba2));
