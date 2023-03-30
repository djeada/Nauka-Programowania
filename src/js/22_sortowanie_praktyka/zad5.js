/*

Tytul: Sortowanie listy miast.

Tresc: Klasa Miasto ma dwie wlasciwosci: nazwa (napis) oraz liczba_mieszkancow (liczba naturalna). Posortuj liste miast wzgledem nazwy oraz wzgledem liczby mieszkancow.

Dane wejsciowe: Lista miast.

Dane wyjsciowe: Posortowana lista miast.

Przyklad:
Dla listy miast: [Miasto("Paris", 2150000), Miasto("Berlin", 3800000), Miasto("New York", 8400000)], powinna zostac zwrocona lista: [Miasto("Berlin", 3800000), Miasto("New York", 8400000), Miasto("Paris", 2150000)].
Dla listy miast: [Miasto("Paris", 2150000), Miasto("Berlin", 3800000), Miasto("New York", 8400000)], powinna zostac zwrocona lista: [Miasto("Berlin", 3800000), Miasto("Paris", 2150000), Miasto("New York", 8400000)].

*/

class Miasto {
  constructor(nazwa, liczba_mieszkancow) {
    this.nazwa = nazwa;
    this.liczba_mieszkancow = liczba_mieszkancow;
  }
}

const sortowanieMiastNazwa = (lista) => {
  return lista.sort((a, b) => a.nazwa.localeCompare(b.nazwa));
};

const sortowanieMiastLiczbaMieszkancow = (lista) => {
  return lista.sort((a, b) => a.liczba_mieszkancow - b.liczba_mieszkancow);
};

// Testy
const listaMiast = [
  new Miasto("Paris", 2150000),
  new Miasto("Berlin", 3800000),
  new Miasto("New York", 8400000),
];

const wynikNazwa = [
  new Miasto("Berlin", 3800000),
  new Miasto("New York", 8400000),
  new Miasto("Paris", 2150000),
];

const wynikLiczbaMieszkancow = [
  new Miasto("Paris", 2150000),
  new Miasto("Berlin", 3800000),
  new Miasto("New York", 8400000),
];

console.assert(
  JSON.stringify(sortowanieMiastNazwa(listaMiast)) ===
    JSON.stringify(wynikNazwa),
  "Test 1 nieudany"
);
console.assert(
  JSON.stringify(sortowanieMiastLiczbaMieszkancow(listaMiast)) ===
    JSON.stringify(wynikLiczbaMieszkancow),
  "Test 2 nieudany"
);

