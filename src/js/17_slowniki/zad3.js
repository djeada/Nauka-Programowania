/*

Tytul: Klucz to imie, wartosc lista wypozyczonych ksiazek.

Tresc: Zbuduj prosta baze danych dla biblioteki oparta o slownik, w ktorym kluczami sa imiona czytelnikow, a wartosciami listy wypozyczonych ksiazek. Baza danych powinna umozliwiac:

1. Dodanie wypozyczonej ksiazki do danego czytelnika.
2. Zwrocenie wypozyczonej ksiazki przez czytelnika.
3. Wypisanie aktualnej listy wypozyczonych ksiazek dla danego czytelnika.

*/

const bazaDanych = {};

function dodajKsiazke(imie, tytul) {
  if (!bazaDanych[imie]) {
    bazaDanych[imie] = [tytul];
  } else {
    bazaDanych[imie].push(tytul);
  }
}

function zwrocKsiazke(imie, tytul) {
  if (!bazaDanych[imie]) {
    return;
  }
  const indeks = bazaDanych[imie].indexOf(tytul);
  if (indeks !== -1) {
    bazaDanych[imie].splice(indeks, 1);
  }
}

function wypiszKsiazki(imie) {
  if (!bazaDanych[imie]) {
    console.log("Brak wypozyczonych ksiazek dla czytelnika o imieniu " + imie);
    return;
  }
  console.log(
    "Wypozyczone ksiazki dla czytelnika " +
      imie +
      ": " +
      bazaDanych[imie].join(", ")
  );
}

function testBazaDanych() {
  dodajKsiazke("Adam", "Pan Tadeusz");
  dodajKsiazke("Adam", "Lalka");
  dodajKsiazke("Ewa", "Zbrodnia i kara");
  console.assert(bazaDanych["Adam"].length === 2, "Test 1 nie powiodl sie");
  console.assert(bazaDanych["Ewa"].length === 1, "Test 2 nie powiodl sie");

  zwrocKsiazke("Adam", "Pan Tadeusz");
  console.assert(bazaDanych["Adam"].length === 1, "Test 3 nie powiodl sie");

  wypiszKsiazki("Adam");
  wypiszKsiazki("Ewa");
  wypiszKsiazki("Ola");
}

testBazaDanych();

