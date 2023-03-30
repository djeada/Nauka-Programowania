/*

Tytuł: Klucz to imię, wartość lista wypożyczonych książek.

Treść: Zbuduj prostą bazę danych dla biblioteki opartą o słownik, w którym kluczami są imiona czytelników, a wartościami listy wypożyczonych książek. Baza danych powinna umożliwiać:

1. Dodanie wypożyczonej książki do danego czytelnika.
2. Zwrócenie wypożyczonej książki przez czytelnika.
3. Wypisanie aktualnej listy wypożyczonych książek dla danego czytelnika.

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
    console.log("Brak wypożyczonych książek dla czytelnika o imieniu " + imie);
    return;
  }
  console.log(
    "Wypożyczone książki dla czytelnika " +
      imie +
      ": " +
      bazaDanych[imie].join(", ")
  );
}

function testBazaDanych() {
  dodajKsiazke("Adam", "Pan Tadeusz");
  dodajKsiazke("Adam", "Lalka");
  dodajKsiazke("Ewa", "Zbrodnia i kara");
  console.assert(bazaDanych["Adam"].length === 2, "Test 1 nie powiódł się");
  console.assert(bazaDanych["Ewa"].length === 1, "Test 2 nie powiódł się");

  zwrocKsiazke("Adam", "Pan Tadeusz");
  console.assert(bazaDanych["Adam"].length === 1, "Test 3 nie powiódł się");

  wypiszKsiazki("Adam");
  wypiszKsiazki("Ewa");
  wypiszKsiazki("Ola");
}

testBazaDanych();
