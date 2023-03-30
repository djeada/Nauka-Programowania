/*
Tytul: Dziedziczenie wielopoziomowe

Tresc: Napisz klase Czlowiek oraz klasy pochodne Student i StudentFizyki. Czlowiek powinien zawierac informacje o imieniu, nazwisku, miejscu urodzenia i zawodzie. Student powinien dodawac pola numeru albumu oraz kierunku studiow. StudentFizyki powinien dodawac pola sredniej z laboratoriow oraz sredniej z wykladow. Napisz program testujacy te klasy.
*/

class Czlowiek {
  constructor(imie, nazwisko, miejsceUrodzenia, zawod) {
    this.imie = imie;
    this.nazwisko = nazwisko;
    this.miejsceUrodzenia = miejsceUrodzenia;
    this.zawod = zawod;
  }
}

class Student extends Czlowiek {
  constructor(
    imie,
    nazwisko,
    miejsceUrodzenia,
    zawod,
    numerAlbumu,
    kierunekStudiow
  ) {
    super(imie, nazwisko, miejsceUrodzenia, zawod);
    this.numerAlbumu = numerAlbumu;
    this.kierunekStudiow = kierunekStudiow;
  }
}

class StudentFizyki extends Student {
  constructor(
    imie,
    nazwisko,
    miejsceUrodzenia,
    zawod,
    numerAlbumu,
    kierunekStudiow,
    sredniaZLaboratoriow,
    sredniaZWykladow
  ) {
    super(
      imie,
      nazwisko,
      miejsceUrodzenia,
      zawod,
      numerAlbumu,
      kierunekStudiow
    );
    this.sredniaZLaboratoriow = sredniaZLaboratoriow;
    this.sredniaZWykladow = sredniaZWykladow;
  }
}

const main = function () {
  let czlowiek = new Czlowiek("Jan", "Kowalski", "Warszawa", "programista");
  let student = new Student(
    "Jan",
    "Kowalski",
    "Warszawa",
    "programista",
    "12345",
    "Informatyka"
  );
  let studentFizyki = new StudentFizyki(
    "Jan",
    "Kowalski",
    "Warszawa",
    "programista",
    "12345",
    "Informatyka",
    4.5,
    4.5
  );
  console.log(czlowiek);
  console.log(student);
  console.log(studentFizyki);
};

main();

