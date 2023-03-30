/*
Tytul: Czy osoba jest pelnoletnia?

Tresc: Dla pobranych szesciu liczb: dnia urodzenia osoby, miesiaca urodzenia osoby, roku urodzenia osoby oraz aktualnego dnia, aktualnego miesiaca i aktualnego roku, sprawdz czy dana osoba jest pelnoletnia.

Dane wejsciowe: 6 liczb.

Dane wyjsciowe: Komunikat.

Przyklad:

Dla pobranych liczb: 5, 12, 1999, 20, 11, 2020, powinna zostac wypisana informacja o pelnoletnosci osoby.
*/

// Pobieranie danych od uzytkownika
const dzien_urodzenia = parseInt(prompt("Podaj dzien urodzenia:"));
const miesiac_urodzenia = parseInt(prompt("Podaj miesiac urodzenia:"));
const rok_urodzenia = parseInt(prompt("Podaj rok urodzenia:"));
const dzien_obecny = parseInt(prompt("Podaj aktualny dzien:"));
const miesiac_obecny = parseInt(prompt("Podaj aktualny miesiac:"));
const rok_obecny = parseInt(prompt("Podaj aktualny rok:"));

// Warunek pelnoletnosci
if (rok_obecny - rok_urodzenia > 18) {
  console.log("Osoba jest pelnoletnia.");
} else if (rok_obecny - rok_urodzenia == 18) {
  if (miesiac_obecny > miesiac_urodzenia) {
    console.log("Osoba jest pelnoletnia.");
  } else if (miesiac_obecny == miesiac_urodzenia) {
    if (dzien_obecny >= dzien_urodzenia) {
      console.log("Osoba jest pelnoletnia.");
    } else {
      console.log("Osoba nie jest pelnoletnia.");
    }
  } else {
    console.log("Osoba nie jest pelnoletnia.");
  }
} else {
  console.log("Osoba nie jest pelnoletnia.");
}

