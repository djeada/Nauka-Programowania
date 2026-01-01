/*
ZAD-03 — Biblioteka: baza wypożyczeń

**Poziom:** ★☆☆
**Tagi:** `dict`, `list`, `pętle`, `string`

### Treść

Utrzymuj słownik: `imię -> lista wypożyczonych książek`.
Obsługuj komendy (każda w osobnej linii) aż do `koniec`:

* `dodaj [imię] [tytuł]`
* `zwróć [imię] [tytuł]`
* `lista [imię]`

Po `lista [imię]` wypisz:

* jeśli lista niepusta: `Książki wypożyczone przez [imię]: t1, t2, ...`
* jeśli brak książek (lub brak czytelnika): `Książki wypożyczone przez [imię]: brak`

### Wejście

Wiele linii z komendami, koniec po słowie `koniec`.

### Wyjście

Tylko po komendach `lista ...`.

### Przykład

**Wejście:**

```
dodaj Jan Hobbit
dodaj Anna "Duma i uprzedzenie"
dodaj Jan "Władca Pierścieni"
lista Jan
zwróć Jan Hobbit
lista Jan
lista Anna
koniec
```

**Wyjście:**

```
Książki wypożyczone przez Jan: Hobbit, Władca Pierścieni
Książki wypożyczone przez Jan: Władca Pierścieni
Książki wypożyczone przez Anna: Duma i uprzedzenie
```

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

