/*
Tytuł: Czy osoba jest pełnoletnia?

Treść: Dla pobranych sześciu liczb: dnia urodzenia osoby, miesiąca urodzenia osoby, roku urodzenia osoby oraz aktualnego dnia, aktualnego miesiąca i aktualnego roku, sprawdź czy dana osoba jest pełnoletnia.

Dane wejściowe: 6 liczb.

Dane wyjściowe: Komunikat.

Przykład:

Dla pobranych liczb: 5, 12, 1999, 20, 11, 2020, powinna zostać wypisana informacja o pełnoletności osoby.
*/

// Pobieranie danych od użytkownika
const dzien_urodzenia = parseInt(prompt("Podaj dzień urodzenia:"));
const miesiac_urodzenia = parseInt(prompt("Podaj miesiąc urodzenia:"));
const rok_urodzenia = parseInt(prompt("Podaj rok urodzenia:"));
const dzien_obecny = parseInt(prompt("Podaj aktualny dzień:"));
const miesiac_obecny = parseInt(prompt("Podaj aktualny miesiąc:"));
const rok_obecny = parseInt(prompt("Podaj aktualny rok:"));

// Warunek pełnoletności
if (rok_obecny - rok_urodzenia > 18) {
  console.log("Osoba jest pełnoletnia.");
} else if (rok_obecny - rok_urodzenia == 18) {
  if (miesiac_obecny > miesiac_urodzenia) {
    console.log("Osoba jest pełnoletnia.");
  } else if (miesiac_obecny == miesiac_urodzenia) {
    if (dzien_obecny >= dzien_urodzenia) {
      console.log("Osoba jest pełnoletnia.");
    } else {
      console.log("Osoba nie jest pełnoletnia.");
    }
  } else {
    console.log("Osoba nie jest pełnoletnia.");
  }
} else {
  console.log("Osoba nie jest pełnoletnia.");
}
