/*
Tytul: Ile dni minelo od poczatku roku?	

Tresc: Dla trzech pobranych liczb: reprezentujacych date wypisz, ile dni minelo od poczatku roku. Pierwsza liczba jest dniem, druga miesiacem, trzecia rokiem. 

Dane wejsciowe: Liczba naturalna.

Dane wyjsciowe: Liczba naturalna.

Przyklad: Dla pobranych liczb: 14, 2 oraz 1482, powinna zostac zwrocona liczba 45.
*/

// Pobieranie danych od uzytkownika
const dzien = parseInt(prompt("Podaj dzien:"));
const miesiac = parseInt(prompt("Podaj miesiac:"));
const rok = parseInt(prompt("Podaj rok:"));

// Sprawdzenie, czy liczby sa poprawne
if (dzien > 0 && miesiac > 0 && rok > 0) {
  // Sprawdzenie, czy miesiac to poprawny
  if (miesiac < 13) {
    // Sprawdzenie, czy rok jest przestepny
    if ((rok % 4 === 0 && rok % 100 !== 0) || rok % 400 === 0) {
      // Sprawdzenie, czy dzien jest poprawny
      if (
        dzien < 30 ||
        (dzien === 30 && miesiac !== 2) ||
        (dzien === 29 && miesiac === 2)
      ) {
        // Sprawdzenie, czy miesiac to styczen
        if (miesiac === 1) {
          console.log(dzien);
        }
        // Sprawdzenie, czy miesiac to luty
        else if (miesiac === 2) {
          console.log(dzien + 31);
        }
        // Sprawdzenie, czy miesiac to marzec
        else if (miesiac === 3) {
          console.log(dzien + 31 + 29);
        }
        // Sprawdzenie, czy miesiac to kwiecien
        else if (miesiac === 4) {
          console.log(dzien + 31 + 29 + 31);
        }
        // Sprawdzenie, czy miesiac to maj
        else if (miesiac === 5) {
          console.log(dzien + 31 + 29 + 31 + 30);
        }
        // Sprawdzenie, czy miesiac to czerwiec
        else if (miesiac === 6) {
          console.log(dzien + 31 + 29 + 31 + 30 + 31);
        }
        // Sprawdzenie, czy miesiac to lipiec
        else if (miesiac === 7) {
          console.log(dzien + 31 + 29 + 31 + 30 + 31 + 30);
        }
        // Sprawdzenie, czy miesiac to sierpien
        else if (miesiac === 8) {
          console.log(dzien + 31 + 29 + 31 + 30 + 31 + 30 + 31);
        }
        // Sprawdzenie, czy miesiac to wrzesien
        else if (miesiac === 9) {
          console.log(dzien + 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31);
        }
        // Sprawdzenie, czy miesiac to pazdziernik
        else if (miesiac === 10) {
          console.log(dzien + 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30);
        }
        // Sprawdzenie, czy miesiac to listopad
        else if (miesiac === 11) {
          console.log(dzien + 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31);
        }
        // Sprawdzenie, czy miesiac to grudzien
        else if (miesiac === 12) {
          console.log(
            dzien + 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30
          );
        }
      } else {
        console.log("Liczba jest niepoprawna");
      }
    }
    // Sprawdzenie, czy rok nie jest przestepny
    else {
      // Sprawdzenie, czy dzien jest poprawny
      if (
        dzien < 30 ||
        (dzien === 30 && miesiac !== 2) ||
        (dzien === 28 && miesiac === 2)
      ) {
        // Sprawdzenie, czy miesiac to styczen
        if (miesiac === 1) {
          console.log(dzien);
        }
        // Sprawdzenie, czy miesiac to luty
        else if (miesiac === 2) {
          console.log(dzien + 31);
        }
        // Sprawdzenie, czy miesiac to marzec
        else if (miesiac === 3) {
          console.log(dzien + 31 + 28);
        }
        // Sprawdzenie, czy miesiac to kwiecien
        else if (miesiac === 4) {
          console.log(dzien + 31 + 28 + 31);
        }
        // Sprawdzenie, czy miesiac to maj
        else if (miesiac === 5) {
          console.log(dzien + 31 + 28 + 31 + 30);
        }
        // Sprawdzenie, czy miesiac to czerwiec
        else if (miesiac === 6) {
          console.log(dzien + 31 + 28 + 31 + 30 + 31);
        }
        // Sprawdzenie, czy miesiac to lipiec
        else if (miesiac === 7) {
          console.log(dzien + 31 + 28 + 31 + 30 + 31 + 30);
        }
        // Sprawdzenie, czy miesiac to sierpien
        else if (miesiac === 8) {
          console.log(dzien + 31 + 28 + 31 + 30 + 31 + 30 + 31);
        }
        // Sprawdzenie, czy miesiac to wrzesien
        else if (miesiac === 9) {
          console.log(dzien + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31);
        }
        // Sprawdzanie, czy miesiac to pazdziernik
        else if (miesiac === 10) {
          console.log(dzien + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30);
        }
        // Sprawdzenie, czy miesiac to listopad
        else if (miesiac === 11) {
          console.log(dzien + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31);
        }
        // Sprawdzenie, czy miesiac to grudzien
        else if (miesiac === 12) {
          console.log(
            dzien + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30
          );
        }
      } else {
        console.log("Liczba jest niepoprawna");
      }
    }
  } else {
    console.log("Liczba jest niepoprawna");
  }
}

